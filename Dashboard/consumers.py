import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import *
from User.models import *


class DetailsConsumer(AsyncWebsocketConsumer):
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
        if text_data_json['process'] == 'details-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.save_details(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'details-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'details-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'details-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
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
    def save_details(self, data):
        try:
            details = Details.objects.filter(id=data['id'], teacher__id=data['teacher']).get()

            details.name = data['name']
            if data['website'] == '':
                details.website = None
            else:
                details.website = data['website']

            details.email = data['email']

            if data['phone'] == '':
                details.phone = None
            else:
                details.phone = data['phone']

            if data['mobile'] == '':
                details.mobile = None
            else:
                details.mobile = data['mobile']

            if data['address'] == '':
                details.address = None
            else:
                details.address = data['address']

            if data['date_of_birth'] == '':
                details.date_of_birth = None
            else:
                details.date_of_birth = data['date_of_birth']
            details.save()

            return {
                'status': True,
                'data': {
                    'teacher': str(details.teacher.id),
                    'id': str(details.id),
                    'name': details.name,
                    'website': details.website,
                    'email': details.email,
                    'phone': details.phone,
                    'mobile': details.mobile,
                    'address': details.address,
                    'date_of_birth': details.date_of_birth,
                }
            }
        except:
            return {
                'status': False,
                'error': 'Data Not Found..!'
            }

    @database_sync_to_async
    def verify_user(self, data):
        if Details.objects.filter(id=data['id'], teacher__id=data['teacher']).count() != 0:
            return True
        return False


class DesignationConsumer(AsyncWebsocketConsumer):
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
        if text_data_json['process'] == 'designation-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.save_designation(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'designation-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'designation-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'designation-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'subject_of_interest-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_subject_of_interest(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'subject_of_interest-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'subject_of_interest-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'subject_of_interest-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'academics-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_academics(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'academics-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'academics-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'academics-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'membership-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_membership(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'membership-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'membership-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'membership-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'institute-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_institute(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'institute-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'institute-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'institute-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'administrative-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_administrative(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'administrative-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'administrative-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'administrative-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'industry-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_industry(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'industry-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'industry-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'industry-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'faculty-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_faculty(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'faculty-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'faculty-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'faculty-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'subject_of_interest-edit':
            response = await self.edit_subject_of_interest(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'subject_of_interest-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'subject_of_interest-edit',
                        'status': False,
                        'error': response['error']
                    }
                )
        elif text_data_json['process'] == 'academics-edit':
            response = await self.edit_academics(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'academics-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'academics-edit',
                        'status': False,
                        'error': response['error']
                    }
                )
        elif text_data_json['process'] == 'membership-edit':
            response = await self.edit_membership(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'membership-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'membership-edit',
                        'status': False,
                        'error': response['error']
                    }
                )
        elif text_data_json['process'] == 'institute-edit':
            response = await self.edit_institute(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'institute-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'institute-edit',
                        'status': False,
                        'error': response['error']
                    }
                )
        elif text_data_json['process'] == 'administrative-edit':
            response = await self.edit_administrative(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'administrative-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'administrative-edit',
                        'status': False,
                        'error': response['error']
                    }
                )
        elif text_data_json['process'] == 'industry-edit':
            response = await self.edit_industry(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'industry-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'industry-edit',
                        'status': False,
                        'error': response['error']
                    }
                )
        elif text_data_json['process'] == 'faculty-edit':
            response = await self.edit_faculty(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'faculty-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'faculty-edit',
                        'status': False,
                        'error': response['error']
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
    def verify_user(self, data):
        if Designation.objects.filter(id=data['id'], teacher__id=data['teacher']).count() != 0:
            return True
        return False

    @database_sync_to_async
    def save_designation(self, data):
        try:
            designation = Designation.objects.filter(id=data['id'], teacher__id=data['teacher']).get()

            designation.designation = data['designation'] if data['designation'] is not None else None
            designation.department = data['department'] if data['department'] is not None else None
            designation.institute = data['institute'] if data['institute'] is not None else None

            designation.save()

            return {
                'status': True,
                'data': {
                    'teacher': str(designation.teacher.id),
                    'id': str(designation.id),
                    'designation': designation.designation,
                    'department': designation.department,
                    'institute': designation.institute,
                }
            }
        except:
            return {
                'status': False,
                'error': 'Data Not Found..!'
            }

    @database_sync_to_async
    def add_subject_of_interest(self, data):
        if data['subject_of_interest'] is not None or data['subject_of_interest'] != '':
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                subject_of_interest = SubjectOfInterest.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                                       subject_of_interest=data['subject_of_interest'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(subject_of_interest.teacher.id),
                        'id': str(subject_of_interest.id),
                        'subject_of_interest': subject_of_interest.subject_of_interest,
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def add_academics(self, data):
        if (data['degree'] is not None or data['degree'] != '') and (
                data['specialisation'] is not None or data['specialisation'] != '') and (
                data['university'] is not None or data['university'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['remarks'] is not None or data['remarks'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                academics = Academics.objects.create(id=uuid.uuid4(), teacher=teacher, degree=data['degree'],
                                                     specialisation=data['specialisation'],
                                                     university=data['university'], year=data['year'],
                                                     remarks=data['remarks'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(academics.teacher.id),
                        'id': str(academics.id),
                        'degree': academics.degree,
                        'specialisation': academics.specialisation,
                        'university': academics.university,
                        'year': academics.year,
                        'remarks': academics.remarks,
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def add_membership(self, data):
        if (data['society'] is not None or data['society'] != '') and (
                data['ist_no'] is not None or data['ist_no'] != '') and (
                data['date_of_membership'] is not None or data['date_of_membership'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                membership = ProfessionalMembership.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                                   society=data['society'],
                                                                   ist_no=data['ist_no'],
                                                                   date_of_membership=data['date_of_membership'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(membership.teacher.id),
                        'id': str(membership.id),
                        'society': membership.society,
                        'ist_no': membership.ist_no,
                        'date_of_membership': membership.date_of_membership
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def add_institute(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_join'] is not None or data['date_of_join'] != '') and (
                data['date_of_leave'] is not None or data['date_of_leave'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                institute = TeachingExperience.objects.create(id=uuid.uuid4(), teacher=teacher, name=data['name'],
                                                              designation=data['designation'],
                                                              date_of_join=data['date_of_join'],
                                                              date_of_leave=data['date_of_leave'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(institute.teacher.id),
                        'id': str(institute.id),
                        'name': institute.name,
                        'designation': institute.designation,
                        'date_of_join': institute.date_of_join,
                        'date_of_leave': institute.date_of_leave,
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def add_administrative(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_join'] is not None or data['date_of_join'] != '') and (
                data['date_of_leave'] is not None or data['date_of_leave'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                administrative = AdministrativeExperience.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                                         name=data['name'],
                                                                         designation=data['designation'],
                                                                         date_of_join=data['date_of_join'],
                                                                         date_of_leave=data['date_of_leave'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(administrative.teacher.id),
                        'id': str(administrative.id),
                        'name': administrative.name,
                        'designation': administrative.designation,
                        'date_of_join': administrative.date_of_join,
                        'date_of_leave': administrative.date_of_leave,
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def add_industry(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_join'] is not None or data['date_of_join'] != '') and (
                data['date_of_leave'] is not None or data['date_of_leave'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                industry = IndustrialExperience.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                               name=data['name'],
                                                               designation=data['designation'],
                                                               date_of_join=data['date_of_join'],
                                                               date_of_leave=data['date_of_leave'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(industry.teacher.id),
                        'id': str(industry.id),
                        'name': industry.name,
                        'designation': industry.designation,
                        'date_of_join': industry.date_of_join,
                        'date_of_leave': industry.date_of_leave,
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def add_faculty(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_approval'] is not None or data['date_of_approval'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                faculty = FacultyDevelopment.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                            name=data['name'],
                                                            designation=data['designation'],
                                                            date_of_approval=data['date_of_approval'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(faculty.teacher.id),
                        'id': str(faculty.id),
                        'name': faculty.name,
                        'designation': faculty.designation,
                        'date_of_approval': faculty.date_of_approval,
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_subject_of_interest(self, data):
        if data['subject_of_interest'] is not None or data['subject_of_interest'] != '':
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                subject_of_interest = SubjectOfInterest.objects.filter(id=data['id'], teacher=teacher).get()
                subject_of_interest.subject_of_interest = data['subject_of_interest']
                subject_of_interest.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(subject_of_interest.teacher.id),
                        'id': str(subject_of_interest.id),
                        'subject_of_interest': subject_of_interest.subject_of_interest,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_academics(self, data):
        if (data['degree'] is not None or data['degree'] != '') and (
                data['specialisation'] is not None or data['specialisation'] != '') and (
                data['university'] is not None or data['university'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['remarks'] is not None or data['remarks'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                academics = Academics.objects.filter(id=data['id'], teacher=teacher).get()
                academics.degree = data['degree']
                academics.specialisation = data['specialisation']
                academics.university = data['university']
                academics.year = data['year']
                academics.remarks = data['remarks']
                academics.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(academics.teacher.id),
                        'id': str(academics.id),
                        'degree': academics.degree,
                        'specialisation': academics.specialisation,
                        'university': academics.university,
                        'year': academics.year,
                        'remarks': academics.remarks,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_membership(self, data):
        if (data['society'] is not None or data['society'] != '') and (
                data['ist_no'] is not None or data['ist_no'] != '') and (
                data['date_of_membership'] is not None or data['date_of_membership'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                membership = ProfessionalMembership.objects.filter(id=data['id'], teacher=teacher).get()
                membership.society = data['society']
                membership.ist_no = data['ist_no']
                membership.date_of_membership = data['date_of_membership']
                membership.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(membership.teacher.id),
                        'id': str(membership.id),
                        'society': membership.society,
                        'ist_no': membership.ist_no,
                        'date_of_membership': membership.date_of_membership,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_institute(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_join'] is not None or data['date_of_join'] != '') and (
                data['date_of_leave'] is not None or data['date_of_leave'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                institute = TeachingExperience.objects.filter(id=data['id'], teacher=teacher).get()
                institute.name = data['name']
                institute.designation = data['designation']
                institute.date_of_join = data['date_of_join']
                institute.date_of_leave = data['date_of_leave']
                institute.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(institute.teacher.id),
                        'id': str(institute.id),
                        'name': institute.name,
                        'designation': institute.designation,
                        'date_of_join': institute.date_of_join,
                        'date_of_leave': institute.date_of_leave,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_administrative(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_join'] is not None or data['date_of_join'] != '') and (
                data['date_of_leave'] is not None or data['date_of_leave'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                administrative = AdministrativeExperience.objects.filter(id=data['id'], teacher=teacher).get()
                administrative.name = data['name']
                administrative.designation = data['designation']
                administrative.date_of_join = data['date_of_join']
                administrative.date_of_leave = data['date_of_leave']
                administrative.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(administrative.teacher.id),
                        'id': str(administrative.id),
                        'name': administrative.name,
                        'designation': administrative.designation,
                        'date_of_join': administrative.date_of_join,
                        'date_of_leave': administrative.date_of_leave,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_industry(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_join'] is not None or data['date_of_join'] != '') and (
                data['date_of_leave'] is not None or data['date_of_leave'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                industry = IndustrialExperience.objects.filter(id=data['id'], teacher=teacher).get()
                industry.name = data['name']
                industry.designation = data['designation']
                industry.date_of_join = data['date_of_join']
                industry.date_of_leave = data['date_of_leave']
                industry.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(industry.teacher.id),
                        'id': str(industry.id),
                        'name': industry.name,
                        'designation': industry.designation,
                        'date_of_join': industry.date_of_join,
                        'date_of_leave': industry.date_of_leave,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }

    @database_sync_to_async
    def edit_faculty(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['designation'] is not None or data['designation'] != '') and (
                data['date_of_approval'] is not None or data['date_of_approval'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                faculty = FacultyDevelopment.objects.filter(id=data['id'], teacher=teacher).get()
                faculty.name = data['name']
                faculty.designation = data['designation']
                faculty.date_of_approval = data['date_of_approval']
                faculty.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(faculty.teacher.id),
                        'id': str(faculty.id),
                        'name': faculty.name,
                        'designation': faculty.designation,
                        'date_of_approval': faculty.date_of_approval,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!'
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!'
            }
