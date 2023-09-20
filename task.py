# By Murat Yalvach, Dmitrii Kasper.
# В этом файле планируется выполнение задания студентами.


'''
Инструкция по установке:
1) Установите aiohttp командой "pip install aiohttp" или "pip3 install aiohttp" или "python -m pip install aiohttp".
2) Установите jwt командой "pip install pyjwt".
3) Выполните необходимые задания в функциях handle_post() и authenticate().
4) После выполнения заданий запустите сервер командой "python task.py" (или другой, если у вас используется "python3", "python3.9" и т.д.).
5) Сайт будет по-умолчанию доступен по адресу "localhost:8080" в браузере.
6) На сайте введите например своё имя в поле "Логин:" и свою фамилию в поле "Пароль."
    Если задания из п.3 выполнены правильно, то в пункте "Ваш токен:" вам будет выведен сгенерированный токен.
    Скопируйте данный токен, и вставьте его в поле "Введите ваш токен, а затем проверьте его:".
    Нажмите на кнопку "Проверить", если всё сделано правильно, вам будет выведен тот логин, который вы вводили.
    Он будет выведен в формате "Вы {login}".
'''

from aiohttp import web
import jwt


async def handle_index(request):
    return web.FileResponse('index.html')


async def handle_post(request):
    user_data = await request.json()
    
    user_login = user_data.get('login', '')
    user_password = user_data.get('password', '')
    
    payload :dict = # Здесь необоходимо создать словарь с полями "login": user_login и "password": user_password.
    
    encoded_jwt = # Используя метод jwt.encode() создать токен с использованием полезной нагрузки payload.
    
    data_to_return = {
        'final_token': encoded_jwt
    }
    
    return web.json_response(data_to_return)


async def authenticate(request):
    data = await request.json()
    token = data.get('token', '')
    is_successful = False
    
    try:
        decoded_payload :dict = # Используя метод jwt.decode() докедировать токен. Учесть, что алгоритм кодирования и 
                                    # декодирования должен быть одинаковым.
        user_login = # Получить из словаря decoded_payload значение логина.
        is_successful = True
        result = f"Вы {user_login}"
    except jwt.ExpiredSignatureError:
        result = "Токен истёк"
    except jwt.DecodeError:
        result = "Ошибка декодирования токена"
        
    data_to_return = {
        'decrypted': result,
        'is_successful': is_successful
    }
    
    return web.json_response(data_to_return)




app = web.Application()
app.router.add_get('/', handle_index)
app.router.add_post('/handle_post', handle_post)
app.router.add_post('/authenticate', authenticate)
app.router.add_static('/static', path='static')


if __name__ == "__main__":
    web.run_app(app)