from peewee import *

db = SqliteDatabase('database/history.db')


class BaseModel(Model):
    class Meta:
        database = db


class History(BaseModel):
    uid = TextField()
    chat_id = TextField()
    datetime = TextField()
    city = TextField()
    command = TextField()


class Hotels(BaseModel):
    uid = TextField()
    hotel_id = TextField()
    name = TextField()
    address = TextField()
    price = TextField()
    link = TextField()


class Photos(BaseModel):
    hotel_id = TextField()
    photo = TextField()


def create_tables():
    with db:
        db.create_tables([History, Hotels, Photos])


def drop_tables():
    with db:
        db.drop_tables([History, Hotels, Photos])


def set_history(uid, chat_id, datetime, city, command):
    History.create(uid=uid, chat_id=chat_id, datetime=datetime, city=city, command=command)


def get_history(chat_id):
    return History.select().where(History.chat_id == chat_id)


def set_hotels(uid, hotel_id, name, address, price, link):
    Hotels.create(uid=uid, hotel_id=hotel_id, name=name, address=address, price=price, link=link)


def get_hotels(uid):
    return Hotels.select().where(Hotels.uid == uid)


def set_photos(hotel_id, photo):
    Photos.create(hotel_id=hotel_id, photo=photo)


def get_photos(hotel_id):
    return Photos.select().where(Photos.hotel_id == hotel_id)


def clear_database():
    with db:
        for model in [History, Hotels, Photos]:
            model.delete().execute()
