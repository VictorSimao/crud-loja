from flask import Flask, render_template, request, redirect, logging

from src.controller.category_controller import CategoryController
from src.controller.product_controller import ProductController


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    controller = ProductController()
    products = controller.read()
    return render_template('product.html', title="Product", products=products)

@app.route('/product/form')
def product_form():

    category_controller = CategoryController()
    categories = category_controller.read()

    product_id = request.args.get('id')
    if product_id:
        product_controller = ProductController()
        product = product_controller.read_by_id(product_id)
        return render_template('product_form.html', title="Product Update", product=product, categories=categories)
    return render_template('product_form.html', title="Product Create", categories=categories)

@app.route('/product/save')
def product_save():
    product_id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    categories_id = request.args.getlist('cat')

    controller = ProductController()
    if product_id:
        controller.update(product_id, name, description, price, categories_id)
    else:
        controller.create(name, description, price, categories_id)

    return redirect('/product')


@app.route('/product/delete')
def product_delete():
    product_id = request.args.get('id')
    controller = ProductController()
    controller.delete(product_id)

    return redirect('/product')

@app.route('/category')
def category():
    controller = CategoryController()
    data = controller.read()
    return render_template('category.html', title="Category", data=data)

@app.route('/category/form')
def category_form():
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