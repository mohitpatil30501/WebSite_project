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


class ActivityConsumer(AsyncWebsocketConsumer):
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
        if text_data_json['process'] == 'publications_book-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_publications_book(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'publications_book-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'publications_book-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_book-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'publications_journal-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_publications_journal(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'publications_journal-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'publications_journal-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_journal-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'publications_paper-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_publications_paper(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'publications_paper-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'publications_paper-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_paper-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'sttps-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_sttps(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'sttps-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'sttps-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'sttps-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'workshops-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_workshops(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'workshops-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'workshops-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'workshops-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'oiis-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_oiis(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'oiis-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'oiis-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'oiis-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'consultancys-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_consultancys(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'consultancys-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'consultancys-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'consultancys-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'awards-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_awards(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'awards-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'awards-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'awards-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'projects-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_projects(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'projects-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'projects-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'projects-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'ecas-form-submission':
            if await self.verify_user(text_data_json['data']):
                response = await self.add_ecas(text_data_json['data'])
                if response['status']:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'ecas-form-submission',
                            'status': True,
                            'data': response['data']
                        }
                    )
                else:
                    await self.channel_layer.group_send(
                        self.id,
                        {
                            'type': 'send_status',
                            'process': 'ecas-form-submission',
                            'status': False,
                            'error': response['error']
                        }
                    )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'ecas-form-submission',
                        'status': False,
                        'error': 'Not valid User..! Something Went Wrong, Please Try Again..!'
                    }
                )
        elif text_data_json['process'] == 'publications_book-edit':
            response = await self.edit_publications_book(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_book-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_book-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'publications_journal-edit':
            response = await self.edit_publications_journal(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_journal-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_journal-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'publications_paper-edit':
            response = await self.edit_publications_paper(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_paper-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'publications_paper-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'sttps-edit':
            response = await self.edit_sttps(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'sttps-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'sttps-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'workshops-edit':
            response = await self.edit_workshops(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'workshops-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'workshops-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'oiis-edit':
            response = await self.edit_oiis(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'oiis-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'oiis-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'consultancys-edit':
            response = await self.edit_consultancys(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'consultancys-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'consultancys-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'awards-edit':
            response = await self.edit_awards(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'awards-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'awards-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'projects-edit':
            response = await self.edit_projects(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'projects-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'projects-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
                    }
                )
        elif text_data_json['process'] == 'ecas-edit':
            response = await self.edit_ecas(text_data_json['data'])
            if response['status']:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'ecas-edit',
                        'status': True,
                        'data': response['data']
                    }
                )
            else:
                await self.channel_layer.group_send(
                    self.id,
                    {
                        'type': 'send_status',
                        'process': 'ecas-edit',
                        'status': False,
                        'error': response['error'],
                        'data': response['data'],
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
                'error': event['error'],
                'data': event['data'],
            }))

    @database_sync_to_async
    def verify_user(self, data):
        if Designation.objects.filter(id=data['id'], teacher__id=data['teacher']).count() != 0:
            return True
        return False

    @database_sync_to_async
    def add_publications_book(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['publication'] is not None or data['publication'] != '') and (
                data['year'] is not None or data['year'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                book = PublicationsBook.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                       name=data['name'], publication=data['publication'],
                                                       year=data['year'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(book.teacher.id),
                        'id': str(book.id),
                        'name': book.name,
                        'publication': book.publication,
                        'year': book.year,
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
    def add_publications_journal(self, data):
        if (data['name'] is not None or data['name'] != '') and (data['title'] is not None or data['title'] != '') and (
                data['publication'] is not None or data['publication'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['page'] is not None or data['page'] != '') and (data['url'] is not None or data['url'] != '') and (
                data['level'] is not None or data['level'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                journal = PublicationsJournal.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                             name=data['name'], title=data['title'],
                                                             publication=data['publication'], page=data['page'],
                                                             year=data['year'], url=data['url'],
                                                             level=data['level'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(journal.teacher.id),
                        'id': str(journal.id),
                        'name': journal.name,
                        'title': journal.title,
                        'publication': journal.publication,
                        'page': journal.page,
                        'year': journal.year,
                        'url': journal.url,
                        'level': journal.level,
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
    def add_publications_paper(self, data):
        if (data['name'] is not None or data['name'] != '') and (data['title'] is not None or data['title'] != '') and (
                data['publication'] is not None or data['publication'] != '') and (
                data['year'] is not None or data['year'] != '') and (data['url'] is not None or data['url'] != '') and (
                data['level'] is not None or data['level'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                paper = PublicationsPaper.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                         name=data['name'], title=data['title'],
                                                         publication=data['publication'],
                                                         year=data['year'], url=data['url'],
                                                         level=data['level'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(paper.teacher.id),
                        'id': str(paper.id),
                        'name': paper.name,
                        'title': paper.title,
                        'publication': paper.publication,
                        'year': paper.year,
                        'url': paper.url,
                        'level': paper.level,
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
    def add_sttps(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['date_form'] is not None or data['date_form'] != '') and (
                data['date_to'] is not None or data['date_to'] != '') and (
                data['day'] is not None or data['day'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                sttp = ShortTermsTrainingProgram.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                                name=data['name'], organization=data['organization'],
                                                                year=data['year'],
                                                                date_form=data['date_form'], date_to=data['date_to'],
                                                                day=data['day'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(sttp.teacher.id),
                        'id': str(sttp.id),
                        'name': sttp.name,
                        'organization': sttp.organization,
                        'year': sttp.year,
                        'date_form': sttp.date_form,
                        'date_to': sttp.date_to,
                        'day': sttp.day,
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
    def add_workshops(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['date_form'] is not None or data['date_form'] != '') and (
                data['date_to'] is not None or data['date_to'] != '') and (
                data['day'] is not None or data['day'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                workshop = Workshops.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                    name=data['name'], organization=data['organization'],
                                                    year=data['year'],
                                                    date_form=data['date_form'], date_to=data['date_to'],
                                                    day=data['day'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(workshop.teacher.id),
                        'id': str(workshop.id),
                        'name': workshop.name,
                        'organization': workshop.organization,
                        'year': workshop.year,
                        'date_form': workshop.date_form,
                        'date_to': workshop.date_to,
                        'day': workshop.day,
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
    def add_oiis(self, data):
        if (data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['invitee'] is not None or data['invitee'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                oii = OtherInstituteInteractions.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                                organization=data['organization'],
                                                                year=data['year'],
                                                                invitee=data['invitee'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(oii.teacher.id),
                        'id': str(oii.id),
                        'organization': oii.organization,
                        'year': oii.year,
                        'invitee': oii.invitee,
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
    def add_consultancys(self, data):
        if (data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['work_done'] is not None or data['work_done'] != '') and (
                data['cost'] is not None or data['cost'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                consultancy = Consultancy.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                         organization=data['organization'],
                                                         year=data['year'],
                                                         work_done=data['work_done'],
                                                         cost=data['cost'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(consultancy.teacher.id),
                        'id': str(consultancy.id),
                        'organization': consultancy.organization,
                        'year': consultancy.year,
                        'work_done': consultancy.work_done,
                        'cost': consultancy.cost,
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
    def add_awards(self, data):
        if (data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['title'] is not None or data['title'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                award = AwardReceived.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                     organization=data['organization'],
                                                     year=data['year'],
                                                     title=data['title'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(award.teacher.id),
                        'id': str(award.id),
                        'organization': award.organization,
                        'year': award.year,
                        'title': award.title,
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
    def add_projects(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['level'] is not None or data['level'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                project = ProjectGuided.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                       name=data['name'],
                                                       year=data['year'],
                                                       level=data['level'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(project.teacher.id),
                        'id': str(project.id),
                        'name': project.name,
                        'year': project.year,
                        'level': project.level,
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
    def add_ecas(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['year'] is not None or data['year'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                eca = ExtraCurricularActivities.objects.create(id=uuid.uuid4(), teacher=teacher,
                                                               name=data['name'],
                                                               year=data['year'])
                return {
                    'status': True,
                    'data': {
                        'teacher': str(eca.teacher.id),
                        'id': str(eca.id),
                        'name': eca.name,
                        'year': eca.year,
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
    def edit_publications_book(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['publication'] is not None or data['publication'] != '') and (
                data['year'] is not None or data['year'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                book = PublicationsBook.objects.filter(id=data['id'], teacher=teacher).get()
                book.name = data['name']
                book.publication = data['publication']
                book.year = data['year']
                book.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(book.teacher.id),
                        'id': str(book.id),
                        'name': book.name,
                        'publication': book.publication,
                        'year': book.year,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_publications_journal(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['title'] is not None or data['title'] != '') and (
                data['publication'] is not None or data['publication'] != '') and (
                data['page'] is not None or data['page'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['url'] is not None or data['url'] != '') and (
                data['level'] is not None or data['level'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                journal = PublicationsJournal.objects.filter(id=data['id'], teacher=teacher).get()
                journal.name = data['name']
                journal.title = data['title']
                journal.publication = data['publication']
                journal.page = data['page']
                journal.year = data['year']
                journal.url = data['url']
                journal.level = data['level']
                journal.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(journal.teacher.id),
                        'id': str(journal.id),
                        'name': journal.name,
                        'title': journal.title,
                        'publication': journal.publication,
                        'page': journal.page,
                        'year': journal.year,
                        'url': journal.url,
                        'level': journal.level,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_publications_paper(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['title'] is not None or data['title'] != '') and (
                data['publication'] is not None or data['publication'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['url'] is not None or data['url'] != '') and (
                data['level'] is not None or data['level'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                paper = PublicationsPaper.objects.filter(id=data['id'], teacher=teacher).get()
                paper.name = data['name']
                paper.title = data['title']
                paper.publication = data['publication']
                paper.year = data['year']
                paper.url = data['url']
                paper.level = data['level']
                paper.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(paper.teacher.id),
                        'id': str(paper.id),
                        'name': paper.name,
                        'title': paper.title,
                        'publication': paper.publication,
                        'year': paper.year,
                        'url': paper.url,
                        'level': paper.level,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_sttps(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['date_form'] is not None or data['date_form'] != '') and (
                data['date_to'] is not None or data['date_to'] != '') and (
                data['day'] is not None or data['day'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                sttp = ShortTermsTrainingProgram.objects.filter(id=data['id'], teacher=teacher).get()
                sttp.name = data['name']
                sttp.organization = data['organization']
                sttp.year = data['year']
                sttp.date_form = data['date_form']
                sttp.date_to = data['date_to']
                sttp.day = data['day']
                sttp.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(sttp.teacher.id),
                        'id': str(sttp.id),
                        'name': sttp.name,
                        'organization': sttp.organization,
                        'year': sttp.year,
                        'date_form': sttp.date_form,
                        'date_to': sttp.date_to,
                        'day': sttp.day,
                        'row': data['row'],
                    }
                }
            except Exception as e:
                print(e)
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_workshops(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['date_form'] is not None or data['date_form'] != '') and (
                data['date_to'] is not None or data['date_to'] != '') and (
                data['day'] is not None or data['day'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                workshop = Workshops.objects.filter(id=data['id'], teacher=teacher).get()
                workshop.name = data['name']
                workshop.organization = data['organization']
                workshop.year = data['year']
                workshop.date_form = data['date_form']
                workshop.date_to = data['date_to']
                workshop.day = data['day']
                workshop.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(workshop.teacher.id),
                        'id': str(workshop.id),
                        'name': workshop.name,
                        'organization': workshop.organization,
                        'year': workshop.year,
                        'date_form': workshop.date_form,
                        'date_to': workshop.date_to,
                        'day': workshop.day,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_oiis(self, data):
        if (data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['invitee'] is not None or data['invitee'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                oii = OtherInstituteInteractions.objects.filter(id=data['id'], teacher=teacher).get()
                oii.organization = data['organization']
                oii.year = data['year']
                oii.invitee = data['invitee']
                oii.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(oii.teacher.id),
                        'id': str(oii.id),
                        'organization': oii.organization,
                        'year': oii.year,
                        'invitee': oii.invitee,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_consultancys(self, data):
        if (data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['work_done'] is not None or data['work_done'] != '') and (
                data['cost'] is not None or data['cost'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                consultancy = Consultancy.objects.filter(id=data['id'], teacher=teacher).get()
                consultancy.organization = data['organization']
                consultancy.year = data['year']
                consultancy.work_done = data['work_done']
                consultancy.cost = data['cost']
                consultancy.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(consultancy.teacher.id),
                        'id': str(consultancy.id),
                        'organization': consultancy.organization,
                        'year': consultancy.year,
                        'work_done': consultancy.work_done,
                        'cost': consultancy.cost,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_awards(self, data):
        if (data['organization'] is not None or data['organization'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['title'] is not None or data['title'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                award = AwardReceived.objects.filter(id=data['id'], teacher=teacher).get()
                award.organization = data['organization']
                award.year = data['year']
                award.title = data['title']
                award.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(award.teacher.id),
                        'id': str(award.id),
                        'organization': award.organization,
                        'year': award.year,
                        'title': award.title,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_projects(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['year'] is not None or data['year'] != '') and (
                data['level'] is not None or data['level'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                project = ProjectGuided.objects.filter(id=data['id'], teacher=teacher).get()
                project.name = data['name']
                project.year = data['year']
                project.level = data['level']
                project.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(project.teacher.id),
                        'id': str(project.id),
                        'name': project.name,
                        'year': project.year,
                        'level': project.level,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

    @database_sync_to_async
    def edit_ecas(self, data):
        if (data['name'] is not None or data['name'] != '') and (
                data['year'] is not None or data['year'] != ''):
            try:
                teacher = Teacher.objects.filter(id=data['teacher']).get()
                eca = ExtraCurricularActivities.objects.filter(id=data['id'], teacher=teacher).get()
                eca.name = data['name']
                eca.year = data['year']
                eca.save()
                return {
                    'status': True,
                    'data': {
                        'teacher': str(eca.teacher.id),
                        'id': str(eca.id),
                        'name': eca.name,
                        'year': eca.year,
                        'row': data['row'],
                    }
                }
            except:
                return {
                    'status': False,
                    'error': 'Data Not Found..!',
                    'data': {'row': data['row'], }
                }
        else:
            return {
                'status': False,
                'error': 'Empty Field is not Allowed..!',
                'data': {'row': data['row'], }
            }

