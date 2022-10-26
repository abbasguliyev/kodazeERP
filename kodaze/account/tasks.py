from api.v1.salary.utils import create_fix_commission
from .models import User
import datetime
from holiday.models import EmployeeWorkingDay

from celery import shared_task
import pandas as pd
from salary.models import SalaryView
from company.models import PermissionForPosition


@shared_task(name='salary_view_create_task')
def salary_view_create_task():
    users = User.objects.all()
    now = datetime.date.today()
    
    d = pd.to_datetime(f"{now.year}-{now.month}-{1}")

    next_m = d + pd.offsets.MonthBegin(1)

    for user in users:
        employee_salary = SalaryView.objects.select_related('employee').filter(
            employee=user, 
            date__year = next_m.year,
            date__month = next_m.month
        )
        if len(employee_salary) != 0:
            continue
        else:
            SalaryView.objects.create(employee=user, date=f"{next_m.year}-{next_m.month}-{1}", final_salary=user.salary).save()
            
    for user in users:
        employee_salary = SalaryView.objects.select_related('employee').filter(
            employee=user, 
            date__year = now.year,
            date__month = now.month
        )
        if len(employee_salary) != 0:
            continue
        else:
            SalaryView.objects.create(employee=user, date=f"{now.year}-{now.month}-{1}", final_salary=user.salary).save()

@shared_task(name='employee_fix_prim_auto_add')
def employee_fix_prim_auto_add():
    create_fix_commission()


@shared_task(name='create_employee_salary_view_task')
def create_employee_salary_view_task(id):
    instance = User.objects.select_related(
                'company', 'office', 'section', 'position', 'team', 'employee_status'
            ).get(id=id)
    user = instance
    now = datetime.date.today()
    
    d = pd.to_datetime(f"{now.year}-{now.month}-{1}")
    next_m = d + pd.offsets.MonthBegin(1)
    
    employee_salary_this_month = SalaryView.objects.select_related('employee').filter(
        employee=user,
        date__year=now.year,
        date__month=now.month
    )
    if len(employee_salary_this_month) == 0:
        SalaryView.objects.create(
            employee=user, date=f"{now.year}-{now.month}-{1}", final_salary=user.salary).save()

    employee_salary_novbeti_ay = SalaryView.objects.select_related('employee').filter(
        employee=user,
        date__year=next_m.year,
        date__month=next_m.month
    )
    if len(employee_salary_novbeti_ay) == 0:
        SalaryView.objects.create(
            employee=user, date=f"{next_m.year}-{next_m.month}-{1}", final_salary=user.salary).save()


@shared_task(name='create_employee_working_day_task')
def create_employee_working_day_task(id):
    instance = User.objects.select_related(
            'company', 'office', 'section', 'position', 'team', 'employee_status'
        ).get(id=id)
    user = instance
    now = datetime.date.today()

    d = pd.to_datetime(f"{now.year}-{now.month}-{1}")

    next_m = d + pd.offsets.MonthBegin(1)

    days_in_this_month = pd.Period(
        f"{now.year}-{now.month}-{1}").days_in_month

    days_in_next_month = pd.Period(
        f"{next_m.year}-{next_m.month}-{1}").days_in_month

    employee_working_day_this_month = EmployeeWorkingDay.objects.select_related('employee').filter(
        employee=user,
        date__year=now.year,
        date__month=now.month
    )
    
    if len(employee_working_day_this_month) == 0:
        employee_working_day = EmployeeWorkingDay.objects.create(
            employee=user,
            working_days_count=days_in_this_month,
            date=f"{now.year}-{now.month}-{1}"
        )
        employee_working_day.save()

    employee_working_day = EmployeeWorkingDay.objects.select_related('employee').filter(
        employee=user,
        date__year=next_m.year,
        date__month=next_m.month
    )
    if len(employee_working_day) == 0:
        employee_working_day = EmployeeWorkingDay.objects.create(
            employee=user,
            working_days_count=days_in_next_month,
            date=f"{next_m.year}-{next_m.month}-{1}"
        )
        employee_working_day.save()

@shared_task(name='create_user_permission_for_position_task')
def create_user_permission_for_position_task(id):
    instance = User.objects.select_related(
            'company', 'office', 'section', 'position', 'team', 'employee_status'
        ).get(id=id)
    user = instance
    user_position = instance.position
    positions = PermissionForPosition.objects.select_related('position', 'permission_group').filter(position=user_position)
    perm_list = set()
    for perm in positions:
        perm_list.add(perm.permission_group)
    print(f"{perm_list=}")
    user.groups.set(perm_list)
    user.save()