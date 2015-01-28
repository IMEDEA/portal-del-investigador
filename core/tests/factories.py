# -*- encoding: UTF-8 -*-

from core.models import UserProfile
from django.contrib.auth.models import User
from random import randint

import factory


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: 'juan{0}'.format(n))
    first_name = 'Juan'
    last_name = 'Doe'
    email = 'juan@example.com'

    @factory.post_generation
    def create_profile(self, *args, **kwargs):
        NIF = 'TRWAGMYFPDXBNJZSQVHLCKE'
        dni = randint(10000000, 99999999)
        UserProfile.objects.create(
            user=self, documento=str(dni) + NIF[dni % 23])


class AdminFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: 'admin{0}'.format(n))
    is_superuser = True
    is_staff = True