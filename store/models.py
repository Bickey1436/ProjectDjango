from django.db import models

#Production - Products # Many to many

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=225)
    featured_product= models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
 
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount=models.FloatField()   
    
class Product(models.Model):
    sku=models.CharField(max_length=10, primary_key=True)
    slug=models.SlugField(default='-')
    title=models.CharField(max_length=255)
    description=models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory=models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection= models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions= models.ManyToManyField(Promotion, related_name='products') 
    
#class collection(models.Model):
    #title = models.CharField(max_length=225)
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    
    
    MEMBERSHIP_CHOICE = [
    ('BRONZE', 'Bronze'),
    ('SILVER', 'Silver'),
    ('GOLD', 'Gold'),
]
    First_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    Phone=models.CharField(max_length=15, unique=True)
    birth_date=models.DateTimeField(null=True)
    models.CharField(max_length=20,choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE)
    
    class Meta:
            db_table = 'store_customers'
            indexes = [
                models.Index(fields=['last_name','First_name'])
            ]
            
    
class Order(models.Model):
    STATUS_COMPLETED='C'
    STATUS_FAILED='F'
    STATUS_PENDING='P'
    
    STATUS=[('STATUS_COMPLETED','Complete'),
            ('STATUS_FAILED','Failed'),
            ('STATUS_PENDING','Pending')]
    
    Placed_At =models.DateTimeField(auto_now=True,)
    Payment_status =models.CharField(max_length=20, choices=STATUS, default=STATUS_PENDING)
    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItems(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.PROTECT)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)
    
#class Promotion(models.Model):
   # description = models.CharField(max_length=255)
   # discount=models.FloatField()
    
    
    
class Address (models.Model):
    street =models.CharField(max_length=225)
    city=models.CharField(max_length=225)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #on_delete=models.set_NULL, #on_delete.PROTECT, #on_delete.DEFAULT)
    
    #if the child associated with parents, delete the child first , on_delete=models.protect, on_delete=models.CASCADE,
    # a collection can have multiple products
    
    
    
    
    