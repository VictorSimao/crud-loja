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
            cat_id = item[4].split(',')
            cat_name = item[5].split(',')
            cat_desc = item[6].split(',')
            cat = list(zip(cat_id, cat_name, cat_desc))

            for c in cat:
                category = Category(c[1], c[2], c[0] )            
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


def third():
    sql3 = """
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

    result3 = Dao().execute_query_select(sql3)
    products3 = set([ p[:4] for p in result3 ])                                
    categories3 = [ c[4:] for c in result3 if c[5]] 

    list_products3 = []

    for prod3 in products3: 
        list_categories3 = [Category(c[2], c[3], c[1]) for c in categories3 if c[0]==prod3[0]]
        product3 = Product( prod3[1], prod3[2], prod3[3], list_categories3 , prod3[0] )
        list_products3.append(product3)

def split_cat(cats):
    cat = [c.split(';') for c in cats.split(',')]
    cat = [Category(c[1], c[2], c[0]) for c in cat]
    return cat

def fourth():
    sql = """
    SELECT 
        p.id
        ,p.name
        ,p.description
        ,p.price
        ,group_concat(c.id ||';'|| c.name ||';'|| c.description)
    FROM product as p
    LEFT JOIN product_category as pc 
    ON pc.product_id = p.id 
    LEFT JOIN category as c 
    ON pc.category_id = c.id
    GROUP BY p.id
    """

    result = Dao().execute_query_select(sql)
    list_products = [ Product( p[1], p[2], p[3], split_cat( p[4] if p[4] else None) , p[0] ) for p in result ]

            

   
list_times = []
for i in range(1):
    start = time.time()
    first()
    end = time.time()
    list_times.append(end - start)

av = statistics.mean(list_times)
print(av)

# list_times = []
# for i in range(1):
#     start = time.time()
#     second()
#     end = time.time()
#     list_times.append(end - start)

# av = statistics.mean(list_times)
# print(av)

list_times3 = []
for i in range(1):
    start3 = time.time()
    fourth()
    end3 = time.time()
    list_times3.append(end3 - start3)

av3 = statistics.mean(list_times3)
print(av3)

# product = Product("teste", "teste", "20", categories=[1,2])
# for i in range(10000):
#     ProductDAO().create(product) 

