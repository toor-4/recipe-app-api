from django.test import TestCase
from core.models import Category, MenuItem
from decimal import Decimal


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(slug='test-category', title='Test Category')

    def test_title_content(self):
        category = Category.objects.get(id=1)
        expected_object_title = f'{category.title}'
        self.assertEqual(expected_object_title, 'Test Category')

    def test_slug_field(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.slug, 'test-category')


class MenuItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(
            slug='test-category',
            title='Test Category')
        MenuItem.objects.create(
            title='Test Item',
            price=10.99,
            category=test_category)

    def test_title_content(self):
        menu_item = MenuItem.objects.get(id=1)
        expected_object_title = f'{menu_item.title}'
        self.assertEqual(expected_object_title, 'Test Item')

    def test_price_value(self):
        menu_item = MenuItem.objects.get(id=1)
        expected_price = Decimal('10.99')
        self.assertEqual(menu_item.price, expected_price)

    def test_featured_default(self):
        menu_item = MenuItem.objects.get(id=1)
        self.assertFalse(menu_item.featured)

    def test_category_relation(self):
        menu_item = MenuItem.objects.get(id=1)
        related_category = menu_item.category
        self.assertEqual(related_category.title, 'Test Category')
