'''SELECT'''

# SELECT * FROM product;
# Product.objects.all() # ORM

# SELECT name, price FROM product;
# Product.objects.only('name', 'price') # ORM

# SELECT * FROM product WHERE условие;
# Product.objects.filter(условие) # ORM

'''сравнение'''

# ==
# SELECT * FROM product WHERE category_id == 'tv';
# Product.objects.filter(category_id == 'tv') # ORM

# >
# SELECT * FROM product WHERE price > 30000;
# Product.objects.filter(price__gt=30000) # ORM (gt = greater than)

# <
# SELECT * FROM product WHERE price < 30000;
# Product.objects.filter(price__lt=30000) # ORM (lt = less than)

# >=
# SELECT * FROM product WHERE price >= 30000;
# Product.objects.filter(price__gte=30000) # ORM

# <=
# SELECT * FROM product WHERE price <= 30000;
# Product.objects.filter(price__lte=30000) # ORM

# !=
# SELECT * FROM product WHERE NOT category_id = 'tv';
# Product.objects.filter(~Q(category_id = 'tv)) # ORM
# Product.objects.exclude(category_id = 'tv') # ORM


# # IN

# SELECT * FROM product WHERE category_id IN ('tv', 'smartphones');
# Product.objects.filter(categoru_id__in=['tv', 'smartphones']) # ORM

# # BETWEEN

# SELECT * FROM product WHERE price BETWEEN 40000 and 50000;
# Product.objects.filter(price__range=[40000, 50000])

# # LIKE
# # ILIKE

'str'
# SELECT * FROM product WHERE name LIKE 'Apple Iphone 13';
# Product.objects.filter(name__exact='Apple Iphone 13') # ORM

# SELECT * FROM product WHERE name ILIKE 'Apple Iphone 13';
# Product.objects.filter(name__iexact='Apple Iphone 13') # ORM

'str%'
# SELECT * FROM product WHERE name LIKE 'Apple%';
# Product.objects.filter(name__startswtih='Apple') # ORM

# SELECT * FROM product WHERE name ILIKE 'Apple%';
# Product.objects.filter(name__istartswith='Apple') # ORM

'%str'
# SELECT * FROM product WHERE name LIKE '%13';
# Product.objects.filter(name__endswith='13') # ORM

# SELECT * FROM product WHERE name ILIKE '%13';
# Product.objects.filter(name__iendswith='13') # ORM

'%str%'
# SELECT * FROM product WHERE name LIKE '%Apple%';
# Product.objects.filter(name__contains='Apple') # ORM

# SELECT * FROM product WHERE name ILIKE '%Apple%';
# Product.objects.filter(name__icontains='Apple) # ORM

# # ORDER BY

# SELECT * FROM product ORDER BY price ASC; # в порядке возрастания
# Product.obejcts.order_by('price') # ORM

# SELECT * FROM product ORDER BY price DESC; # в порядке убывания
# Product.obejcts.order_by('-price') # ORM

# # LIMIT
# SELECT * FROM product LIMIT 10;
# Product.objects.all()[:10]

# SELECT * FROM product LIMIT 10 OFFSET 5;
# Product.objects.all()[5:15]

'''INSERT'''

# INSERT INTO product(...) VALUES (...);
# Product.objects.create(name='...', description='...', ',,,')  # ORM

# product = Product(name='...', description='...')
# product.save()

# INSERT INTO product(fields) VALUES (...), (...);
# Product.objects.bulk_create([Product(...), Product(...), ]) # ORM

'''UPDATE'''
# UPDATE product SET price = 50000;
# Product.objects.update(price=50000) # ORM

# UPDATE product SET price = 50000 WHERE category_id = 'notebooks';
# Product.objects.filter(category_id='notebooks').update(price=50000) # ORM

'''DELETE'''
# DELETE FROM product;
# Product.objects.delete() # ORM

# DELETE FROM product WHERE price > 50000;
# Product.objects.filter(price__gt=50000).delete() # ORM

'''получение одного объекта'''

# Category.objects,get(slug='tv')
# Product.objects.get(id=2) 

'''количество записей'''

# SELECT COUNT(*) FROM product;
# Product.objects.count()

# SELECT COUNT(*) FROM product WHERE price < 20000;
# Product.objects.filter(price__lt=20000).count()





