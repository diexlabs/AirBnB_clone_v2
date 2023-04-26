#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from environ import get_env

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        ForeignKey('places.id'),
        primary_key=True, nullable=True
    ),
    Column(
        'amenity_id',
        ForeignKey('amenities.id'),
        primary_key=True, nullable=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(
        String(60),
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    user = relationship('User', back_populates='places')
    city = relationship('City', back_populates='places')

    if get_env('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', order_by='Review.id',
            back_populates='place', cascade='delete'
        )
        amenities = relationship(
            'Amenity', secondary=place_amenity,
            viewonly=False, backref='places',
            order_by='Amenity.id'
        )
    else:
        @property
        def reviews(self):
            '''reviews property for file storage'''
            from review import Review
            from models import storage
            all_reviews = storage.all(Review).values()
            return [r for r in all_reviews if r.user_id == self.id]

        @property
        def amenities(self):
            '''amenities property for db storage'''
            from models import storage
            from amenity import Amenity
            all_amenities = storage.all(Amenity).values()
            return [a for a in all_amenities if a.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            '''add an amenities to the list of amenities'''
            from amenity import Amenity
            if type(obj) == Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
