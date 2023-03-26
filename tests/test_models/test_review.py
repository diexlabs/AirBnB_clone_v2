#!/usr/bin/python3
""" """
import pep8
from unittest import TestCase
from models import Review, Base, BaseModel, Place, User, City, State



class TestReview(TestCase):
    """ """

    def setUp(self) -> None:
        '''sets up the test suite'''
        self.user = User(email="password", password="password")
        self.state = State(name="California")
        self.city = City(name="Oregon", state_id=self.state.id)
        self.place = Place(
            name="California", user_id = self.user.id,
            city_id=self.city.id
        )

    def test_superclass_is_correclty_composed(self):
        '''checks that it inherits from ``BaseModel``'''
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(Review, Base))

    def test_init_works(self):
        '''checks that klas can be initialized'''
        r = Review(
            text="Just saying",
            place_id=self.place.id,
            user_id=self.user.id
        )
        self.assertIsInstance(r, Review)

    def test_text_is_required(self):
        '''checks that text cannot be null'''
        with self.assertRaises(Exception):
            a = Review(place_id=self.place.id, user_id=self.user.id)
            a.save()

    def test_place_id_is_required(self):
        '''checks that place id cant be null'''
        with self.assertRaises(Exception):
            c = Review(text="Oregon", user_id=self.user.id)
            c.save()

    def test_place_id_is_required(self):
        '''checks that user id cant be null'''
        with self.assertRaises(Exception):
            c = Review(text="Oregon", place_id=self.place.id)
            c.save()

    def test_tablename_is_correct(self):
        '''checks that model have appropriate table name'''
        self.assertEqual(Review.__tablename__, 'reviews')

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/review.py',])
        self.assertEqual(p.total_errors, 0)
