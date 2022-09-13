from faker import Faker

from src.models import User

fake = Faker('uk_UA')


class ExceptionValidation(Exception):
    pass


def add_user(*args, **kwargs):
    user = User(**kwargs)
    user.save()
    return f'User {user.name} added to database'


def delete_user(*args, **kwargs):
    user = User.objects.get(name=kwargs['name'])
    user.delete()
    return f'User {user.name} deleted from database'


def get_user(*args, **kwargs):
    user = User.objects.get(name=kwargs['name'])
    return f'User {user.name}, Phone: {user.phone}, Email: {user.email}, Address: {user.address}, Date: {user.added_on.date()}'


def get_all_users(*args, **kwargs):
    users = User.objects()
    if users:
        return '\n'.join([f'User {user.name}, Phone: {user.phone}, Email: {user.email}, Address: {user.address}, Date: {user.added_on.date()}' for user in users])


def update_user(*args, **kwargs):
    user = User.objects.get(name=kwargs['name'])
    user.phone = kwargs['phone']
    user.email = kwargs['email']
    user.address = kwargs['address']
    user.save()
    return f'User {user.name} updated'


def add_random_users(*args, **kwargs):
    for _ in range(100):
        user = User(name=fake.name(), phone=fake.phone_number(), email=fake.email(), address=fake.address())
        user.save()
    return '100 random users added to database'
