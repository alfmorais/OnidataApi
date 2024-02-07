from datetime import datetime

import factory
import pytz
from django.contrib.auth.models import User
from factory.fuzzy import FuzzyDateTime
from faker import Faker


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.django.Password("pw")


class LoansFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "loans.Loans"

    id = factory.Sequence(lambda n: n)
    amount = factory.Faker(
        "pydecimal",
        positive=True,
        left_digits=7,
        right_digits=2,
    )
    interest_rate = factory.Faker(
        "pydecimal",
        positive=True,
        left_digits=7,
        right_digits=2,
    )
    ip_address = Faker().ipv4()
    date = FuzzyDateTime(datetime(2024, 2, 5, 0, 0, 0, tzinfo=pytz.UTC))
    bank = factory.Faker("company")
    customer = factory.SubFactory(UserFactory)
    installments = factory.Faker(
        "pyint",
        min_value=1,
        max_value=5,
        step=1,
    )
    cet_amount = factory.Faker(
        "pydecimal",
        positive=True,
        left_digits=7,
        right_digits=2,
    )
    iof_interest_rate = factory.Faker(
        "pydecimal",
        positive=True,
        left_digits=7,
        right_digits=2,
    )
    insurance = factory.Faker(
        "pydecimal",
        positive=True,
        left_digits=7,
        right_digits=2,
    )


class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "payments.Payment"

    id = factory.Sequence(lambda n: n)
    loan = factory.SubFactory(LoansFactory)
    installment_amount = factory.Faker(
        "pydecimal",
        positive=True,
        left_digits=7,
        right_digits=2,
    )
    installment_number = factory.Faker(
        "pyint",
        min_value=1,
        max_value=5,
        step=1,
    )
    date = FuzzyDateTime(datetime(2024, 2, 5, 0, 0, 0, tzinfo=pytz.UTC))
    is_paid = factory.Faker("pybool")
