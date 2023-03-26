#!/usr/bin/python3
""" """
import pep8
from unittest import TestCase, skipUnless
from models import State, Base, BaseModel
from environ import get_env


class TestState(TestCase):
    """ """
    def test_superclass_is_correclty_composed(self):
        '''checks that it inherits from ``BaseModel``'''
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(State, Base))

    def test_init_works(self):
        '''checks that klas can be initialized'''
        a = State(name="Electricity")
        self.assertIsInstance(a, State)

    def test_name_is_required(self):
        '''checks that name cannot be null'''
        with self.assertRaises(Exception):
            a = State()
            a.save()

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/state.py',])
        self.assertEqual(p.total_errors, 0)

    @skipUnless(get_env('HBNB_TYPE_STORAGE') == 'db', "not a db")
    def test_tablename_is_correct(self):
        '''checks that model have appropriate table name'''
        self.assertEqual(State.__tablename__, 'states')
