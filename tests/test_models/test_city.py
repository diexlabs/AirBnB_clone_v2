#!/usr/bin/python3
""" """
import pep8
from unittest import TestCase
from models import City, Base, BaseModel, State


class test_City(TestCase):
    """ """
    def setUp(self) -> None:
        '''sets up the test suite'''
        self.state = State(name="California")

    def test_superclass_is_correclty_composed(self):
        '''checks that it inherits from ``BaseModel``'''
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, Base))

    def test_init_works(self):
        '''checks that klas can be initialized'''
        a = City(name="California", state_id=self.state.id)
        self.assertIsInstance(a, City)

    def test_name_is_required(self):
        '''checks that name cannot be null'''
        with self.assertRaises(Exception):
            a = City(state_id=self.state.id)
            a.save()

    def test_state_id_is_required(self):
        '''checks that state id cant be null'''
        with self.assertRaises(Exception):
            c = City(name="Oregon")
            c.save()

    def test_tablename_is_correct(self):
        '''checks that model have appropriate table name'''
        self.assertEqual(City.__tablename__, 'cities')

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/city.py',])
        self.assertEqual(p.total_errors, 0)
