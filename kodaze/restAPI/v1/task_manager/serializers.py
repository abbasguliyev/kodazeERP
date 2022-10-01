from rest_framework import serializers
from restAPI.core import DynamicFieldsCategorySerializer

from company.models import Position
from task_manager.models import Advertisement, TaskManager, UserTaskRequest
from restAPI.v1.company.serializers import PositionSerializer
from restAPI.v1.account.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class PositionForTaskManagerSerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']

class UserForTaskManagerSerializer(DynamicFieldsCategorySerializer):
    position = PositionForTaskManagerSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'fullname', 'phone_number_1', 'position']

class TaskManagerSerializer(DynamicFieldsCategorySerializer):
    creator = UserForTaskManagerSerializer(read_only=True)
    position = PositionForTaskManagerSerializer(read_only=True)
    employee = UserForTaskManagerSerializer(read_only=True)

    users = serializers.CharField(write_only=True,required=False, allow_null=True)
    positions = serializers.CharField(write_only=True,required=False, allow_null=True)

    class Meta:
        model = TaskManager
        fields = (
            'id',
            'title', 
            'body', 
            'creator', 
            'created_date', 
            'end_date', 
            'old_date', 
            'position', 
            'employee', 
            'status',
            'users',
            'positions'
        )


class UserTaskRequestSerializer(DynamicFieldsCategorySerializer):
    creator = UserForTaskManagerSerializer(read_only=True)

    class Meta:
        model = UserTaskRequest
        fields = "__all__"

class AdvertisementSerializer(DynamicFieldsCategorySerializer):
    creator = UserForTaskManagerSerializer(read_only=True)

    position = PositionForTaskManagerSerializer(read_only=True)
    positions = serializers.CharField(write_only=True,required=False, allow_null=True)

    class Meta:
        model = Advertisement
        fields = (
            'id',
            'title', 
            'creator', 
            'body', 
            'created_date', 
            'position', 
            'positions'
        )