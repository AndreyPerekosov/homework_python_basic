"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio


from models import create_tables, Session, User, Post
from jsonplaceholder_requests import run_creating_data


async def load_data(async_session, data_users, data_posts):
    users_to_load = []
    posts_to_load = []
    for item in data_users:
        users_to_load.append(User(name=item.name, username=item.username, email=item.email))
    for item in data_posts:
        posts_to_load.append(Post(title=item.title, body=item.body, user_id=item.userId))
    async with async_session() as session:
        async with session.begin():
            session.add_all(users_to_load)
            session.add_all(posts_to_load)


async def async_main():
    await create_tables()
    data_users, data_posts = await run_creating_data()
    await load_data(Session, data_users, data_posts)


def main():
    main_coro = async_main()
    asyncio.run(main_coro)


if __name__ == "__main__":
    main()
