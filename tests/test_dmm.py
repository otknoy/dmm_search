from unittest import TestCase
from nose.tools import ok_, eq_
import dmm

class TestDMM(TestCase):
    def setUp(self):
        print('before test')

    def tearDown(self):
        print('after test')

    def test_hoge(self):
        ok_(dmm.DMM)
