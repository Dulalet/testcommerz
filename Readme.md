Запуск: 
- 
docker build -t backend .

docker-compose up

URL:
-

- admin/ - Админ панель

- employees/ - список всех сотрудников. Поиск и сортировка доступны через интерфейс DRF и через параметры (например, /employees/?ordering=name&search=natural)

- employees/create/ - создать сотрудника
- employees/<uuid:pk>/ - редактировать сотрудника по uuid
- employees/<uuid:pk>/delete/ - удалить сотрудника
  - login/ - авторизация

      email
    
      password

  - register/ - регистрация

      email
    
      first_name 
    
      last_name
    
      password

- logout/ - выход из системы
- get_token/ - получить токен авторизации сотрудника
- password_change/ - смена пароля