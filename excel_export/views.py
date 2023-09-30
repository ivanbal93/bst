import tablib

from datetime import datetime, timedelta

from django.http import HttpResponse

from robots.models import Robot

# Create your views here.

today = datetime.today()
actual_date = today - timedelta(days=7)


def export_to_xls(request):
    """
    Функция экспорта .xls со сводкой о производстве роботов
    """

    # Форирование списка доступных моделей
    models_queryset = Robot.objects.all().values('model')
    models_list = []
    for obj in models_queryset:
        if obj['model'] not in models_list:
            models_list.append(obj['model'])

    # Список датасетов, на основе которых будет сформирована итоговая таблица
    ds_list = []
    for model_title in models_list:
        ds = tablib.Dataset()
        ds.title = model_title
        data = [("Модель", "Версия", "Количество за неделю")]
        queryset = (Robot.objects.filter(model=model_title)
                    .values('model', 'version', 'created'))

        for obj in queryset:
            model = obj['model']
            version = obj['version']
            count = Robot.objects.filter(
                model=model,
                version=version,
                created__gte=actual_date
            ).count()

            if (model, version, count) not in data:
                data.append((model, version, count))

        for d in data:
            ds.append(d)

        ds_list.append(ds)

    return HttpResponse(
        tablib.Databook(ds_list).export('xlsx'),
        headers={
            'Content-Type': 'application/vnd.ms-excel',
            'Content-Disposition': 'attachment; filename="Сводка.xls"',
        },
        charset='UTF-8'
    )
