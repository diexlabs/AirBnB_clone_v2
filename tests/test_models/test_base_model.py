#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import pep8
import datetime
from uuid import UUID
import json
import os
from environ import get_env


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.klas = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.klas()
        self.assertEqual(type(i), self.klas)

    def test_kwargs(self):
        """ """
        i = self.klas()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.klas()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    # @unittest.skipUnless(get_env('HBNB_TYPE_STORAGE') == 'db')
    # def test_save(self):
    #     """ Testing save """
    #     i = self.klas()
    #     i.save()
    #     key = self.name + "." + i.id
    #     with open('file.json', 'r') as f:
    #         j = json.load(f)
    #         self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.klas()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.klas()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.klas(**n)


    def test_id(self):
        """ """
        new = self.klas()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.klas()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.klas()
        self.assertEqual(type(new.updated_at), datetime.datetime)

    def test_pep8(self):
        '''checks module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/base_model.py',])
        self.assertEqual(p.total_errors, 0)

    def test_docstring(self):
        '''test klas is well documented'''
        self.assertIsNotNone(self.klas.__doc__)
        self.assertIsNotNone(self.klas.__init__.__doc__)
        self.assertIsNotNone(self.klas.save.__doc__)
        self.assertIsNotNone(self.klas.to_dict.__doc__)
        self.assertIsNotNone(self.klas.delete.__doc__)