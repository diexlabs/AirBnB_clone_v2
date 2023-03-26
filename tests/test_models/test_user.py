#!/usr/bin/python3
""" """
import pep8
from unittest import TestCase
from models import User, Base, BaseModel


class TestUser(TestCase):
    """ """

    def test_superclass_is_correclty_composed(self):
        '''checks that it inherits from ``BaseModel``'''
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(User, Base))

    def test_init_works(self):
        '''checks that klas can be initialized'''
        r = User(
            email="email",
            password="password"
        )
        self.assertIsInstance(r, User)

    def test_email_is_required(self):
        '''checks that text cannot be null'''
        with self.assertRaises(Exception):
            a = User(password="password")
            a.save()

    def test_password_is_required(self):
        '''checks that place id cant be null'''
        with self.assertRaises(Exception):
            c = User(email="email")
            c.save()

    def test_place_id_is_required(self):
        '''checks that user id cant be null'''
        with self.assertRaises(Exception):
            c = User(text="Oregon", place_id=self.place.id)
            c.save()

    def test_tablename_is_correct(self):
        '''checks that model have appropriate table name'''
        self.assertEqual(User.__tablename__, 'users')

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/user.py',])
        self.assertEqual(p.total_errors, 0)
