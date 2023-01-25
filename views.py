import peewee
from models import Category, Product
def post_category(category_name):
    try:
       category = Category(name = category_name)
       category.save()
       print('SAVED!!!')
    except peewee.IntegrityError:
        print('такая категория уже есть')

def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'{category.id}--{category.name}--{category.created_at}')

def delete_category(category_id):              
    try:
        category = Category.get(id=category_id)
        category.delete_instance()                                   
        print('DeleteD!!!!')
    except peewee.DoesNotExist:
        print('Категория не найдена')          
def update_category(category_id,new_name):
    try:
        category = Category.get(id=category_id)
        category.name = new_name
        category.save()
        print('оБНОВИЛИ')
    except peewee.DoesNotExist:
        print('Категория не найдена')
def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(category.id, end = '\t')
        print(category.name, end = '\t')
        print(category.created_at)
        print(category.product, '!!!')
        for i in category.product:
            print(f'{i.name}--{i.price}---{i.amount}')
    except peewee.DoesNotExist:
        print('Нет такой категории')
def post_product(name,price,amount,category):
    try:
        product = Product(name = name, price= price, amount = amount,category=category)
        product.save()
    except peewee.IntegrityError:
        print('такой категорий не существует')
def get_product():
    product = Product.select
    for i in product:
       print(f'{i.name} --{i.price}---{i.amount}---{i.category.name}---{i.category.id}')
def get_product_by_name(name):
    product = Product.select().where(Product.name==name)
    for i in product:
        print(i.name,i.price)
  