from rest_framework import serializers
from account.models import User

from company.models import Holding, Team, Office, Company, Section, Position

from holiday.models import (
    HoldingWorkingDay,
    EmployeeArrivalAndDepartureTimes,
    EmployeeWorkingDay,
    TeamWorkingDay,
    TeamExceptionWorker,
    OfficeWorkingDay,
    OfficeExceptionWorker,
    CompanyWorkingDay,
    CompanyExceptionWorker,
    SectionWorkingDay,
    SectionExceptionWorker,
    PositionWorkingDay,
    HoldingExceptionWorker,
    PositionExceptionWorker
)

from restAPI.v1.company.serializers import HoldingSerializer, TeamSerializer, OfficeSerializer, CompanySerializer, SectionSerializer, PositionSerializer
from restAPI.v1.account.serializers import UserSerializer


class HoldingWorkingDaySerializer(serializers.ModelSerializer):
    holding = HoldingSerializer(read_only=True)
    holding_id = serializers.PrimaryKeyRelatedField(
        queryset=Holding.objects.all(), source='holding', write_only=True
    )
    
    class Meta:
        model = HoldingWorkingDay
        fields = "__all__"

class EmployeeWorkingDaySerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='employee', write_only=True,
    )
    
    class Meta:
        model = EmployeeWorkingDay
        fields = "__all__"

class EmployeeArrivalAndDepartureTimesSerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='employee', write_only=True,
    )
    
    class Meta:
        model = EmployeeArrivalAndDepartureTimes
        fields = "__all__"


class TeamWorkingDaySerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True,
    )
    
    class Meta:
        model = TeamWorkingDay
        fields = "__all__"

class OfficeWorkingDaySerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)
    office_id = serializers.PrimaryKeyRelatedField(
        queryset=Office.objects.all(), source='office', write_only=True,
    )
    
    class Meta:
        model = OfficeWorkingDay
        fields = "__all__"

class CompanyWorkingDaySerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True
    )
    
    class Meta:
        model = CompanyWorkingDay
        fields = "__all__"

class SectionWorkingDaySerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), source='section', write_only=True
    )
    
    class Meta:
        model = SectionWorkingDay
        fields = "__all__"

class PositionWorkingDaySerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(), source='position', write_only=True,
    )
    
    class Meta:
        model = PositionWorkingDay
        fields = "__all__"

# ------------------------------------------------------------------

class HoldingExceptionWorkerSerializer(serializers.ModelSerializer):
    working_day = HoldingWorkingDaySerializer(read_only=True)
    working_day_id = serializers.PrimaryKeyRelatedField(
        queryset=HoldingWorkingDay.objects.all(), source='working_day', write_only=True,
    )

    exception_workers = serializers.StringRelatedField(read_only=True, many=True)
    exception_workers_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='exception_workers', write_only=True, many=True
    )
    
    class Meta:
        model = HoldingExceptionWorker
        fields = "__all__"

class CompanyExceptionWorkerSerializer(serializers.ModelSerializer):
    working_day = CompanyWorkingDaySerializer(read_only=True)
    working_day_id = serializers.PrimaryKeyRelatedField(
        queryset=CompanyWorkingDay.objects.all(), source='working_day', write_only=True,
    )

    exception_workers = serializers.StringRelatedField(read_only=True, many=True)
    exception_workers_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='exception_workers', write_only=True, many=True
    )
    
    class Meta:
        model = CompanyExceptionWorker
        fields = "__all__"

class OfficeExceptionWorkerSerializer(serializers.ModelSerializer):
    working_day = OfficeWorkingDaySerializer(read_only=True)
    working_day_id = serializers.PrimaryKeyRelatedField(
        queryset=OfficeWorkingDay.objects.all(), source='working_day', write_only=True,
    )

    exception_workers = serializers.StringRelatedField(read_only=True, many=True)
    exception_workers_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='exception_workers', write_only=True, many=True
    )
    
    class Meta:
        model = OfficeExceptionWorker
        fields = "__all__"

class SectionExceptionWorkerSerializer(serializers.ModelSerializer):
    working_day = SectionWorkingDaySerializer(read_only=True)
    working_day_id = serializers.PrimaryKeyRelatedField(
        queryset=SectionWorkingDay.objects.all(), source='working_day', write_only=True,
    )

    exception_workers = serializers.StringRelatedField(read_only=True, many=True)
    exception_workers_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='exception_workers', write_only=True, many=True
    )
    
    class Meta:
        model = SectionExceptionWorker
        fields = "__all__"

class TeamExceptionWorkerSerializer(serializers.ModelSerializer):
    working_day = TeamWorkingDaySerializer(read_only=True)
    working_day_id = serializers.PrimaryKeyRelatedField(
        queryset=TeamWorkingDay.objects.all(), source='working_day', write_only=True,
    )

    exception_workers = serializers.StringRelatedField(read_only=True, many=True)
    exception_workers_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='exception_workers', write_only=True, many=True
    )
    
    class Meta:
        model = TeamExceptionWorker
        fields = "__all__"

class PositionExceptionWorkerSerializer(serializers.ModelSerializer):
    working_day = PositionWorkingDaySerializer(read_only=True)
    working_day_id = serializers.PrimaryKeyRelatedField(
        queryset=PositionWorkingDay.objects.all(), source='working_day', write_only=True,
    )

    exception_workers = serializers.StringRelatedField(read_only=True, many=True)
    exception_workers_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='exception_workers', write_only=True, many=True
    )
    
    class Meta:
        model = PositionExceptionWorker
        fields = "__all__"