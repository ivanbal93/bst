1) pip install -r requirements.txt
2) python3 manage.py runserver
3) python3 manage.py shell:

	1) from customers.models import Customer
   	2) from orders.models import Order
   	3) from robots.models import Robot
 	4) customer = Customer.objects.create(email=<электронная почта>)
	5) Order.objects.create(customer=Customer.objects.get(id=customer.id), robot_serial='m1_v1')
     	6) Robot.objects.create(serial='m1_v1', model='m1', version='v1', craeted='2023-01-01 00:00:01')
        
7) Письмо о появлении робота в наличии приходит при создании объекта Robot, если его серийный номер фигурирует в списке серийных номеров из заказов Order
