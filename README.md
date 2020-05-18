0. Добавить поле phone в модель Student

1. Сделать raise ошибки если в поле phone ввели не цифры. (StudentCreateForm) django raise error in form

2. Student, Teacher поля first_name and last_name сделать str.capitalize(). Добавить в сигнал (pre_save). Создать дата миграцию.

3. Создать мидлварь LogMiddleware которая будет записывать параметры request.path, request.method, execution_time (diff), если запрос был на админку (/admin/)

4. https://github.com/jazzband/django-silk

5. Какая разница между поверхностной и глубокой копией (напромер списков)