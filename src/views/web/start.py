from flask import Flask, render_template, request, redirect

from src.controllers.category_controller import CategoryController


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    controller = CategoryController()
    data = controller.read()
    return render_template('category.html', title="Product", data=data)

@app.route('/product/form')
def product_create():
    # TODO: refactor
    category_id = request.args.get('id')
    if category_id:
        controller = CategoryController()
        data = controller.read_by_id(category_id)
        return render_template('category_form.html', title="Category Update", data=data)
    return render_template('category_form.html', title="Category Create")

@app.route('/product/save')
def product_save():
    # TODO: refactor
    category_id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')

    controller = CategoryController()
    if category_id:
        controller.update(category_id, name, description)
    else:
        controller.create(name, description)

    return redirect('/category')

@app.route('/product/delete')
def product_delete():
    # TODO: refactor
    category_id = request.args.get('id')
    controller = CategoryController()
    controller.delete(category_id)

    return redirect('/category')

# Pages category
@app.route('/category')
def category():
    controller = CategoryController()
    data = controller.read()
    return render_template('category.html', title="Category", data=data)

@app.route('/category/form')
def category_create():
    category_id = request.args.get('id')
    if category_id:
        controller = CategoryController()
        data = controller.read_by_id(category_id)
        return render_template('category_form.html', title="Category Update", data=data)
    return render_template('category_form.html', title="Category Create")

@app.route('/category/save')
def category_save():
    category_id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')

    controller = CategoryController()
    if category_id:
        controller.update(category_id, name, description)
    else:
        controller.create(name, description)

    return redirect('/category')

@app.route('/category/delete')
def category_delete():
    category_id = request.args.get('id')
    controller = CategoryController()
    controller.delete(category_id)

    return redirect('/category')




if __name__ == "__main__":
    app.run(debug=True)