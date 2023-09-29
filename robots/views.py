import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse

from .models import Robot
from .forms import NewRobotForm

# Create your views here.


@csrf_exempt  # отключение csrf-токена для проверки работы функции через Postman
def post(request):
    """
    Функция создания объектов класса "Robot"
    """

    if request.method != 'POST':
        return HttpResponse(
            'Not POST method!'
        )

    else:
        data = json.loads(request.body)
        robot_form = NewRobotForm(data)

        if robot_form.is_valid():
            new_object = Robot.objects.create(
                serial=data["serial"],
                model=data["model"],
                version=data["version"],
                created=data["created"]
            )

            return HttpResponse(
                f'Информация о новом роботе {new_object.model}-'
                f'{new_object.version} добавлена в Базу Данных.'
            )

        else:
            errors = robot_form.errors.get_json_data()
            response_text = ''
            for key, value in errors.items():
                response_text += f'Ошибка в поле {key}: {value[0]["message"]}.\n'

            return HttpResponse(
                response_text
            )
