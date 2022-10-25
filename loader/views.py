from flask import Blueprint, render_template, request, send_from_directory
from functions import save_picture, add_post_to_file, ValueError
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='report.log', level=logging.INFO)


@loader_blueprint.route('/post')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["POST"])
def post_added_page():
    post_picture = request.files.get('post_picture')
    post_text = request.form.get('post_text')
    try:
        post_picture_url = save_picture(post_picture)
    except ValueError:
        logging.info(f"Недопустимый формат файл")
        return "Недопустимый формат файла (не картинка)"
    else:
        add_post_to_file({'pic': post_picture_url, 'content': post_text})
        return render_template('post_uploaded.html', post_picture=post_picture_url, post_text=post_text)


@loader_blueprint.route('/uploads/<path:path>')
def static_dir(path):
    return send_from_directory("uploads", path)
