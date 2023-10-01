from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse

from .models import Robot

from orders.models import Order

from customers.models import Customer

from R4C.settings import EMAIL_HOST_USER


serials_list = []
for order in Order.objects.all().values('robot_serial'):
    serials_list.append(order['robot_serial'])


@receiver(post_save, sender=Robot)
def notify_customer(sender, instance, created, **kwargs):
    """
    Функиця уведомления покупателя о появлении в наличии нужного робота
    """

    orders = Order.objects.filter(robot_serial=instance.serial).values()

    # Услвоие выполняется, если создаётся объект класса Robot с серийным номером, 
    # фигурирующиим в списке серийных номеров объектов класса Order
    if created and instance.serial in serials_list:
        for order in orders:
            # Использую filter(), потому что серийный номер не уникален.
            # Иначе бы использовал get()
            robots = Robot.objects.filter(serial=instance.serial)
            customer = Customer.objects.get(id=order['customer_id'])

            send_mail(
                message=(
                    f'Добрый день!\n'
                    f'Недавно вы интересовались нашим роботом модели '
                    f'{robots[0].model}, версии {robots[0].version}.\n'
                    f'Этот робот теперь в наличии. Если вам подходит '
                    f'этот вариант - пожалуйста, свяжитесь с нами.'
                ),
                subject='Информация о роботе, которым вы интересовались!',
                from_email=EMAIL_HOST_USER,
                recipient_list=[customer.email]
            )

            return HttpResponse(f'Письмо отправлено по адресу {customer.email}!')
