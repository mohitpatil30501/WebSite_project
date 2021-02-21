import json
import sqlite3

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import *


class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']

        # Join room group
        await self.channel_layer.group_add(
            self.id,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['process'] == 'signup-verify':
            if await self.prn_check(text_data_json['data']['prn']) != 0:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'signup-verify',
                        'status': False,
                        'error': 'PRN already exist, Try to LogIn...!'
                    }
                )
            else:
                data = await self.signup_verify(text_data_json['data'])
                status = data['status']
                if status:
                    await self.prn_session(text_data_json['data']['prn'])
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'signup-verify',
                            'status': status,
                            'data': data['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'signup-verify',
                            'status': status,
                            'error': data['error']
                        }
                    )
        elif text_data_json['process'] == 'username-availability':
            username = text_data_json['username']
            count = await self.username_check(username)
            if count != 0:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'username-availability',
                        'status': False,
                        'error': 'Username Already Exists...!'
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'username-availability',
                        'status': True,
                        'data': 'Username Available'
                    }
                )
        elif text_data_json['process'] == 'password-availability':
            password = text_data_json['password']
            username = text_data_json['username']
            data = await self.password_check(password, username)
            if not data['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'password-availability',
                        'status': False,
                        'error': data['error']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'password-availability',
                        'status': True,
                        'data': data['data']
                    }
                )

    async def send_status(self, event):
        if event['status']:
            await self.send(text_data=json.dumps({
                'process': event['process'],
                'status': event['status'],
                'data': event['data']
            }))
        else:
            await self.send(text_data=json.dumps({
                'process': event['process'],
                'status': event['status'],
                'error': event['error']
            }))

    # First step of Sign in of Student
    @database_sync_to_async
    def signup_verify(self, data):
        try:
            user = CollegeStudentData.objects.filter(prn=data['prn'], mother_name=data['mother_name'].upper()).get()
            return {
                'status': True,
                'data': {
                    'prn': user.prn,
                    'name': user.name,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'mother_name': user.mother_name,
                }
            }
        except:
            return {
                'status': False,
                'error': 'Incorrect PRN or Mother Name..!'
            }

    @database_sync_to_async
    def prn_check(self, prn):
        return Student.objects.filter(college_data__prn=prn).count()

    @database_sync_to_async
    def prn_session(self, prn):
        self.scope["session"]["prn"] = prn

    @database_sync_to_async
    def username_check(self, username):
        return User.objects.filter(username=username).count()

    @database_sync_to_async
    def password_check(self, password, username):
        if len(password) < 8:
            return {
                'status': False,
                'error': 'Password must be at least 8 characters'
            }
        if len(username) == 0:
            return {
                'status': False,
                'error': 'Please Set Username First'
            }
        capital = small = number = symbol = False
        prn = self.scope["session"]["prn"]
        try:
            data = CollegeStudentData.objects.filter(prn=prn).get()
            data = [data.prn, data.name, data.first_name, data.last_name, data.mother_name]
        except:
            data = None
        if data is not None:
            for word in data:
                if word in password.upper() or password.upper() in word:
                    return {
                        'status': False,
                        'error': 'Password must be not related to personal details'
                    }

            if username.upper() in password.upper() or password.upper() in username.upper():
                return {
                    'status': False,
                    'error': 'Password must be not related to personal details'
                }

            for c in password:
                if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    capital = True
                elif c in "abcdefghijklmnopqrstuvwxyz":
                    small = True
                elif c in "1234567890":
                    number = True
                elif c in r'''~`!@#$%^&*()_+-={}|[]\;':",./<>?''':
                    symbol = True
                elif c == ' ':
                    return {
                        'status': False,
                        'error': 'Password not contain whitespace'
                    }

            if not capital or not small or not number or not symbol:
                return {
                    'status': False,
                    'error': 'Password must be contain one Capital, Small, Number and Symbol character'
                }
            else:
                return {
                    'status': True,
                    'data': 'Password is suitable'
                }
        else:
            return {
                'status': False,
                'error': 'Problem to PRN Data..!'
            }


class UserResetPasswordConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']

        # Join room group
        await self.channel_layer.group_add(
            self.id,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['process'] == 'password-availability':
            password = text_data_json['password']
            id = text_data_json['id']
            data = await self.password_check(password, id)
            if not data['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'password-availability',
                        'status': False,
                        'error': data['error']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'password-availability',
                        'status': True,
                        'data': data['data']
                    }
                )

    async def send_status(self, event):
        if event['status']:
            await self.send(text_data=json.dumps({
                'process': event['process'],
                'status': event['status'],
                'data': event['data']
            }))
        else:
            await self.send(text_data=json.dumps({
                'process': event['process'],
                'status': event['status'],
                'error': event['error']
            }))

    @database_sync_to_async
    def password_check(self, password, id):
        if len(password) < 8:
            return {
                'status': False,
                'error': 'Password must be at least 8 characters'
            }
        if len(id) == 0:
            return {
                'status': False,
                'error': 'Something Went Wrong'
            }
        capital = small = number = symbol = False
        try:
            data = Student.objects.filter(id=id).get()
            data = [data.college_data.prn, data.college_data.name, data.student.first_name, data.student.last_name, data.college_data.mother_name]
        except:
            data = None
        if data is not None:
            for word in data:
                if word in password.upper() or password.upper() in word:
                    return {
                        'status': False,
                        'error': 'Password must be not related to personal details'
                    }

            for c in password:
                if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    capital = True
                elif c in "abcdefghijklmnopqrstuvwxyz":
                    small = True
                elif c in "1234567890":
                    number = True
                elif c in r'''~`!@#$%^&*()_+-={}|[]\;':",./<>?''':
                    symbol = True
                elif c == ' ':
                    return {
                        'status': False,
                        'error': 'Password not contain whitespace'
                    }

            if not capital or not small or not number or not symbol:
                return {
                    'status': False,
                    'error': 'Password must be contain one Capital, Small, Number and Symbol character'
                }
            else:
                return {
                    'status': True,
                    'data': 'Password is suitable'
                }
        else:
            return {
                'status': False,
                'error': 'Problem to PRN Data..!'
            }
