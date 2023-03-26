#!/usr/bin/python3
"""Test for amenity module"""
from unittest import TestCase
import pep8
from models import Amenity, BaseModel, Base


class TestAmenity(TestCase):
    """ model klas for amenity"""

    def test_superclass_is_correclty_composed(self):
        '''checks that it inherits from ``BaseModel``'''
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(Amenity, Base))

    def test_init_works(self):
        '''checks that klas can be initialized'''
        a = Amenity(name="Electricity")
        self.assertIsInstance(a, Amenity)

    def test_name_is_required(self):
        '''checks that name cannot be null'''
        with self.assertRaises(Exception):
            a = Amenity()
            a.save()

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/amenity.py',])
        self.assertEqual(p.total_errors, 0)