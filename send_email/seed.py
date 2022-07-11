import email
from email.headerregistry import Address
from unicodedata import name
from models import send_mail
from faker import Faker
fake = Faker

def sendb (n):
    for i in range(0,n):
        send_mail.objects.create(
            name = fake.name(),
            
            content = fake.address(),
        )