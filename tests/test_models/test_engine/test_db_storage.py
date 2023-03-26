#!/usr/bin/python3
'''Test for ``engine/db_storage``'''
from unittest import TestCase, skipUnless
import MySQLdb
import pep8
from models.engine.db_storage import DBStorage
from models import City, State
from environ import get_env

@skipUnless(get_env('HBNB_TYPE_STORAGE') == 'db', 'not a relational db')
class TestDbStorage(TestCase):
    '''TestCase for DBStorage'''

    def setUp(self) -> None:
        '''create a storage object'''
        
        self.session = self.storage._DBStorage__session
        self.session.query(State).delete()
        self.session.query(City).delete()
        self.session.commit()

    @classmethod
    def setUpClass(cls) -> None:
        '''sets up a DBStorage class'''
        cls.storage = DBStorage()
        cls.storage.reload()

    def tearDown(self) -> None:
        '''closes connection to database and other clean ups'''
        pass

    def test_new_works(self):
        '''checks that new objects can be added'''
        new = State(name='Enugu')
        self.storage.new(new)

        self.assertIn(new, self.storage._DBStorage__session.new)
            

    def test_save_works(self):
        '''checks that save method saves to database'''
        before = self.session.query(State).count()
        new = State(name="California")
        self.storage.new(new)
        self.storage.save()
        after = self.session.query(State).count()
        self.assertEqual(after, before + 1)

    def test_all_works(self):
        '''checks that ``all`` method works properly'''        
        for i in range(5):
            s = State(name=f'State {i}')
            self.storage.new(s)
            self.storage.save()
        states = self.storage.all(State).values()
        state_id = list(states)[0].id
        city = City(name="first city", state_id=state_id)
        self.storage.new(city)
        self.storage.save()
        self.assertEqual(len(states), 5)
        for state in states:
            self.assertTrue(isinstance(state, State))
        all = self.storage.all().values()
        self.assertEqual(len(all), 6)
        self.assertIn(city, all)

    def test_delete_works(self):
        '''checks that ``delete`` method actually deletes'''
        s = State(name="California")
        self.storage.new(s)
        self.storage.save()
        self.assertEqual(len(self.storage.all()), 1)
        self.storage.delete(s)
        self.storage.save()
        self.assertEqual(len(self.storage.all()), 0)

            

    def test_attributes(self):
        '''checks that appropriate attributes are available'''
        self.assertTrue(hasattr(self.storage, '_DBStorage__session'))
        self.assertTrue(hasattr(self.storage, '_DBStorage__engine'))

    def test_methods(self):
        '''checks that appropriate methods are available'''
        self.assertTrue(hasattr(self.storage, 'new'))
        self.assertTrue(hasattr(self.storage, 'save'))
        self.assertTrue(hasattr(self.storage, 'reload'))
        self.assertTrue(hasattr(self.storage, 'all'))
        self.assertTrue(hasattr(self.storage, 'delete'))

    def test_init_works(self):
        '''checks that init correctly initializes'''
        self.assertTrue(isinstance(self.storage, DBStorage))

    def test_pep8(self):
        '''test module uses style guide'''
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/db_storage.py',])
        self.assertEqual(p.total_errors, 0, "Fix pep8")

    def test_docstrings(self):
        '''checks that module is properly documented'''
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)