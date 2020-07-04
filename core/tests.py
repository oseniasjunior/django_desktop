from unittest import TestCase
from core import helpers


class PrintHelloTestCase(TestCase):
    def test_print_hello_world(self):
        result = helpers.print_hello_world()
        self.assertEquals(result, 'hello world')
