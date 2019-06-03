from flask import Flask, render_template, url_for, request, redirect, abort

app = Flask(__name__)

fruits_list = ['pineapple', 'banana', 'strawberry']
vegetables_list = ['cucumber', 'potato', 'carrot']


@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/')
def redirect_to_main():
    return redirect(url_for('main_page'))


@app.route('/error_page')
def error_test():
    abort(501, 'Our program has an error')


@app.errorhandler(501)
def error_501_handler(error):
    return render_template('error_page.html')


@app.route('/fruits')
@app.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
def fruits(value=None):
    if request.method == 'POST':
        do_post_fruit(value)
        return "Successfully added a new fruit"
    if request.method == 'DELETE':
        do_delete_fruit(value)
        return "Successfully deleted the fruit"
    else:
        return do_get_fruit()


def do_get_fruit():
    return render_template('fruits.html', fruits_list=fruits_list)


def do_delete_fruit(value):
    for i, elem in enumerate(fruits_list):
        if elem == value:
            fruits_list.pop(i)


def do_post_fruit(value):
    fruits_list.append(value)


@app.route('/vegetables')
@app.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables(value=None):
    if request.method == 'POST':
        do_post_vegetable(value)
        return "Successfully added a new vegetable"
    if request.method == 'DELETE':
        do_delete_vegetable(value)
        return "Successfully deleted the vegetable"
    else:
        return do_get_vegetable()


def do_get_vegetable():
    return render_template('vegetables.html', vegetables_list=vegetables_list)


def do_delete_vegetable(value):
    for i, elem in enumerate(vegetables_list):
        if elem == value:
            vegetables_list.pop(i)


def do_post_vegetable(value):
    vegetables_list.append(value)


if __name__ == '__main__':
    app.run(debug=True)