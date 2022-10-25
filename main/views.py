from flask import Blueprint, render_template,request
import functions
import logging
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    searching_posts = functions.get_by_content(str(request.args['s']))
    logging.info(f"Выполнен поиск по запросу {str(request.args['s'])}")
    return render_template('post_list.html', searching_request=request.args['s'], searching_posts=searching_posts)
