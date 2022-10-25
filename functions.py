import json
import logging
from json import JSONDecodeError



class ValueError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


def load_posts(path='posts.json'):
    """
    Открывает файл 'posts.json'.
    Загружает данные из файла.
    """
    # Ошибка: Файл отсутствует или не хочет превращаться в список
    try:
        with open(path, 'r', encoding='utf-8') as file:
            posts_list = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        print("Ошибка чтения данных постов")
    else:
        return posts_list


def get_by_content(post_content):
    """
    Ищет совпадения по контенту поста.
    Возвращает те посты, у которых совпадения есть.
    """
    posts_by_content = []
    posts_list = load_posts()
    for post in posts_list:
        if post_content.lower() in post["content"].lower():
            posts_by_content.append(post)
    return posts_by_content


def save_picture(post_picture):
    """
    Сохраняет изображение в папку uploads/images.
    Возвращает путь к файлу.
    """
    filename = post_picture.filename
    filetype = filename.split('.')[-1]
    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        # Ошибка: Загруженный файл - не картинка
        raise ValueError("Expected: 'jpg', 'jpeg', 'svg', 'png'")
    # Ошибка: Ошибка при загрузке файла
    try:
        post_picture.save(f"./uploads/images/{filename}")
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        print(f"No such file or directory: {filename}")
    else:
        return f'/uploads/images/{filename}'


def save_posts_in_json(posts_list, path='posts.json'):
    """
    Сохраняет список постов в файле posts.json.
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(posts_list, file)
    except (JSONDecodeError, FileNotFoundError):
        print("Ошибка чтения данных постов")


def add_post_to_file(post):
    """
    1) С помощью функции load_posts выгружает
    все посты в виде списка.
    2) Дополняет список новым постом.
    3) С помощью функции save_posts_in_json
    сохраняет список постов в файле posts.json
    """
    posts_list = load_posts()
    posts_list.append(post)
    save_posts_in_json(posts_list)
