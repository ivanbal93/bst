1) pip install -r requirements.txt
2) python3 manage.py runserver
3) Запуск через Postman:

	URL: 
		http://127.0.0.1:8000/api/v1/robots/post/
	method: 
		POST
	body example:
		{"serial": "m1_v1", "model": "m1", "version": "v1", "created": "2023-09-28 14:00:00"}
		
4) Скачать информацию о роботах, произведённых за последнюю неделю: 
	http://127.0.0.1:8000/export
	
5) Письмо о появлении робота в наличии приходит при создании объекта Robot, если его серийный номер фигурирует в списке серийных номеров из заказов Order
