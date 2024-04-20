import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserActive(Base):
    __tablename__ = 'user_active'

    user_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(length=20), nullable=False)
    last_name = sq.Column(sq.String(length=20), nullable=False)
    age = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.Integer, nullable=False)
    city_id = sq.Column(sq.Integer, sq.ForeignKey('city_list.city_id'), nullable=False)

    user_rated = relationship('UserRated', back_populates='user_active')
    city_list = relationship('CityList', back_populates='user_active')


class UserRandom(Base):
    __tablename__ = 'user_random'

    random_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(length=10), nullable=False)
    last_name = sq.Column(sq.String(length=10), nullable=False)
    vk_link = sq.Column(sq.String(length=100), nullable=False)
    age = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.Integer, nullable=False)
    city_id = sq.Column(sq.Integer, sq.ForeignKey('city_list.city_id'), nullable=False)

    user_rated = relationship('UserRated', back_populates='user_random')
    photo = relationship('Photo', back_populates='user_random')
    city_list = relationship('CityList', back_populates='user_random')


class UserRated(Base):
    __tablename__ = 'user_rated'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('user_active.user_id'), nullable=False)
    random_id = sq.Column(sq.Integer, sq.ForeignKey('user_random.random_id'), nullable=False)
    like = sq.Column(sq.Boolean, nullable=False, default=False)
    dislike = sq.Column(sq.Boolean, nullable=False, default=False)

    user_active = relationship('UserActive', back_populates='user_rated', cascade='all, delete')
    user_random = relationship('UserRandom', back_populates='user_rated', cascade='all, delete')


class Photo(Base):
    __tablename__ = 'photo'

    id = sq.Column(sq.Integer, primary_key=True)
    random_id = sq.Column(sq.Integer, sq.ForeignKey('user_random.random_id'), nullable=False)
    photo_link = sq.Column(sq.String(length=100), nullable=False)

    user_random = relationship('UserRandom', back_populates='photo', cascade='all, delete')


class CityList(Base):
    __tablename__ = 'city_list'

    city_id = sq.Column(sq.Integer, primary_key=True)
    city = sq.Column(sq.String(length=20), nullable=False)

    user_random = relationship('UserRandom', back_populates='city_list')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)