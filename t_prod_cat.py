from src.daos.dao import Dao
from src.models.category_model import Category
from src.models.product_model import Product
from src.daos.product_dao import ProductDAO


import time
import statistics

def first():
    sql = """
        SELECT 
            p.id
            ,p.name
            ,p.description
            ,p.price
            ,group_concat(c.id)
            ,group_concat(c.name)
            ,group_concat(c.description)
        FROM product as p
        LEFT JOIN product_category as pc 
        ON pc.product_id = p.id 
        LEFT JOIN category as c 
        ON pc.category_id = c.id
        GROUP BY p.id
    """

    result = Dao().execute_query_select(sql)
    list_products = []
    for item in result:
        categories = []
        if item[4]:
            cat = [item[4].split(','), item[4].split(','), item[6].split(',')]
            cat_id = item[4].split(',')
            cat_name = item[5].split(',')
            cat_desc = item[6].split(',')

            for i in range(len(cat_id)):
                category = Category(cat_name[i], cat_desc[i], cat_id[i] )            
                categories.append(category)
            
        product = Product( item[1], item[2], item[3], categories , item[0] )
        list_products.append(product)


def second():
    sql = """
    SELECT 
        p.id
        ,p.name
        ,p.description
        ,p.price
        ,pc.product_id
        ,c.id
        ,c.name
        ,c.description
    FROM product as p
    LEFT JOIN product_category as pc 
    ON pc.product_id = p.id 
    LEFT JOIN category as c 
    ON pc.category_id = c.id
    """

    result = Dao().execute_query_select(sql)
    products = [ p[:4] for p in result ]                                     
    categories = [ c[4:] for c in result ] 
    list_products = []
    for prod in set(products):   
        prod_cats = [Category(c[2], c[3], c[1]) for c in categories if c[0]==prod[0]]
        product = Product( prod[1], prod[2], prod[3], prod_cats , prod[0] )
        list_products.append(product)








list_times = []
for i in range(20):
    start = time.time()
    first()
    end = time.time()
    list_times.append(end - start)

av = statistics.mean(list_times)
print(av)

list_times = []
for i in range(20):
    start = time.time()
    second()
    end = time.time()
    list_times.append(end - start)

av = statistics.mean(list_times)
print(av)



# product = Product("teste", "teste", "20", categories=[1,2])
# for i in range(10000):
#     ProductDAO().create(product) 