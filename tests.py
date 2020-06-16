from django.test import TestCase
from django.urls import reverse
from .models import Product, PythonType, Review
from django.contrib.auth.models import User

# Create your tests here.
class PythonTypeTest(TestCase):
    def test_string(self):
        type=PythonType(pythontypename='laptop')
        self.assertEqual(str(type),type.pythontypename)
    
    def test_table(self):
        self.assertEqual(str(PythonType._meta.db_table),'pythontype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=PythonType(pythontypename='tablet')
        self.prod=Product(productname='Ipad',pythontype=self.type, productprice=800.00)

    def test_string(self):
        self.assertEqual(str(self.prod),self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.pythontype),'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(),40.00)

#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=PythonType.objects.create(pythontypename='laptop')
        self.prod=Product.objects.create(productname='product1', pythontype=self.type, user=self.u, 
        productprice=500.00,productentrydate='2019-04-02', productdescription="some kind of laptop")

    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetails', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_number_of_reviews(self):
        reviews=Review.objects.filter(product=self.prod).count()
        self.assertEqual(reviews, 2)

#form test
class ProductFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user1', password='P@ssw0rd1')
        self.type2=TechType.objects.create(pythonname='type1')
    
    def test_productForm(self):
        data={
            'productname' : 'product1',
            'pythontype' : self.type2,
            'user' : self.user2,
            'productprice' : 200.00,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

    def test_productFormInvalid(self):
        data={
            'productname' : 'product1',
            'techtype' : 'type1',
            'user' : self.user2,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())

class New_Product_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=ProductType.objects.create(typename='laptop')
        self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.test_user, productprice=500, productentrydate='2019-04-02',producturl= 'http://www.dell.com', productdescription="a product")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newproduct'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonapp/newProduct/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newproduct'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pythonapp/newproduct.html')