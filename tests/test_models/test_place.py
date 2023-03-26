#!/usr/bin/python3
""" """
import pep8
from unittest import TestCase
from models import Place, User, Base, BaseModel, City, State


class TestPlace(TestCase):
    """ """

    def setUp(self) -> None:
        '''sets up the test suite'''
        self.state = State(name="California")
        self.user = User(email="password", password="password")
        self.city = City(name="Oregon", state_id=self.state.id)

    def test_superclass_is_correclty_composed(self):
        '''checks that it inherits from ``BaseModel``'''
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(Place, Base))

    def test_init_works(self):
        '''checks that klas can be initialized'''
        p = Place(
            name="California", user_id = self.user.id,
            city_id=self.city.id
        )
        self.assertIsInstance(p, Place)

    def test_name_is_required(self):
        '''checks that text cannot be null'''
        with self.assertRaises(Exception):
            a = Place(
                user_id = self.user.id,
                city_id=self.city.id
            )
            a.save()

    def test_user_id_is_required(self):
        '''checks that place id cant be null'''
        with self.assertRaises(Exception):
            a = Place(
                name = "oregon",
                city_id=self.city.id
            )
            a.save()

    def test_city_id_is_required(self):
        '''checks that user id cant be null'''
        with self.assertRaises(Exception):
            a = Place(
                user_id = self.user.id,
                name="Oregon"
            )
            a.save()

    def test_tablename_is_correct(self):
        '''checks that model have appropriate table name'''
        self.assertEqual(Place.__tablename__, 'places')

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/city.py',])
        self.assertEqual(p.total_errors, 0)
