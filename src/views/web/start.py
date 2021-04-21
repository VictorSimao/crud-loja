from flask import Flask, render_template, request, redirect

from src.controllers.category_controller import CategoryController
from src.controllers.product_controller import ProductController


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/product')
def product():
    controller = ProductController()
    data = controller.read()
    return render_template('product.html', title="Product", data=data)


@app.route('/product/form')
def product_create():
    product_id = request.args.get('id')
    controller = CategoryController()
    data_category = controller.read()
    
    if product_id:
        controller = ProductController()
        data_product = controller.read_by_id(product_id)
        
        return render_template('product_form.html', title="Product Update", data_product=data_product, data_category=data_category)
    return render_template('product_form.html', title="Product Create", data_category=data_category)


@app.route('/product/save')
def product_save():
    # TODO: refactor
    product_id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    args_dict = request.args.to_dict(flat=False)
    categories = args_dict.get('categories', None)

    controller = ProductController()
    if product_id:
        produtct = {
            'id': product_id,
            'name': name,
            'description': description,
            'price': price,
            'categories': categories            
        }
        controller.update(produtct)
    else:
        produtct = {
            'name': name,
            'description': description,
            'price': price,
            'categories': categories            
        }
        controller.create(produtct)

    return redirect('/product')

@app.route('/product/delete')
def product_delete():
    product_id = request.args.get('id')
    controller = ProductController()
    controller.delete(product_id)

    return redirect('/product')

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
