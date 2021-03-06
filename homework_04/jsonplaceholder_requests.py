"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class DataUser:
    name: str
    username: str
    email: str


@dataclass
class DataPost:
    title: str
    body: str
    userId: int


def set_user(data_user: dict) -> DataUser:
    dt_user = DataUser(data_user['name'], data_user['username'], data_user['email'])
    return dt_user


def set_post(data_post: dict) -> DataPost:
    dt_post = DataPost(data_post['title'], data_post['body'], data_post['userId'])
    return dt_post


SET_DICT = {'user': set_user, 'post': set_post}


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_data(url: str) -> dict:
    async with ClientSession() as session:
        fetched_data = await fetch_json(session, url)
    return fetched_data


async def set_data(url: str, name_item: str) -> list:
    list_of_data_item = []
    data = await fetch_data(url)
    for item in data:
        data_item = SET_DICT[name_item](item)
        list_of_data_item.append(data_item)
    return list_of_data_item


async def run_creating_data() -> tuple:
    """
    Fetching and setting data to DataClass and returns tuple of creating data
    :return: tuple_of_data
    """
    users_data, posts_data = await asyncio.gather(set_data(USERS_DATA_URL, 'user'), set_data(POSTS_DATA_URL, 'post'))
    return users_data, posts_data
