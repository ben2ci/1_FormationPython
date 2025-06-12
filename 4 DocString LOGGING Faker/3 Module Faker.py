# -*- coding: utf-8 -*-
from faker import Faker

faker = Faker(locale="fr_FR")

print(faker.unique.name())

for _ in range(10):
    print(faker.first_name())
    print(faker.last_name())
    print(faker.email())
