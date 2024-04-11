import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserActive(Base):
    __tablename__ = 'user_active'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(length=40), nullable=False)
    last_name = sq.Column(sq.String(length=40))
    age = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.Integer, nullable=False)
    city_id = sq.Column(sq.Integer, nullable=False)

    user_matching = relationship('UserMatching', back_populates='user_active')


class UserRandom(Base):
    __tablename__ = 'user_random'

    id = sq.Column(sq.Integer, primary_key=True)
    random_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(length=40), nullable=False)
    last_name = sq.Column(sq.String(length=40), nullable=False)
    vk_link = sq.Column(sq.String(length=100), nullable=False)
    age = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.Integer, nullable=False)
    city_id = sq.Column(sq.Integer, nullable=False)

    user_matching = relationship('UserMatching', back_populates='user_random')
    photo = relationship('Photo', back_populates='user_random')


class UserMatching(Base):
    __tablename__ = 'user_matching'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('user_active.user_id'), nullable=False)
    random_id = sq.Column(sq.Integer, sq.ForeignKey('user_random.random_id'), nullable=False)
    like = sq.Column(sq.Boolean, nullable=False, default=False)
    dislike = sq.Column(sq.Boolean, nullable=False, default=False)

    user_active = relationship('UserActive', back_populates='user_matching', cascade='all, delete')
    user_random = relationship('UserRandom', back_populates='user_matching', cascade='all, delete')


class Photo(Base):
    __tablename__ = 'photo'

    id = sq.Column(sq.Integer, primary_key=True)
    random_id = sq.Column(sq.Integer, sq.ForeignKey('UserRandom.random_id'), nullable=False)
    photo_link = sq.Column(sq.String, nullable=False)

    user_random = relationship('UserRandom', back_populates='photo', cascade='all, delete')


class CityList(Base):
    __tablename__ = 'city_list'

    id = sq.Column(sq.Integer, primary_key=True)
    city_id = sq.Column(sq.Integer, sq.ForeignKey('UserRandom.city_id'), nullable=False)
    city = sq.Column(sq.String(length=20), nullable=False)

    user_random = relationship('UserRandom', back_populates='city_list')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
