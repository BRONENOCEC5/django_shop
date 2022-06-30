# # # SELECT

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

# INSERT
# UPDATE
# DELETE



