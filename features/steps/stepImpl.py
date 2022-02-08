import requests
from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


# from faker import Faker


@given('the Book details which needs to be added to Library')
def step_impl(context):
    # fake = Faker()
    # fakeisbn = fake.isbn10()

    context.urladd = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.header = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("random", "6969")
    # context.payLoad = addBookPayload(fakeisbn) # using faker plugin


@when('we execute the AddBook Post API method')
def step_impl(context):
    context.response = requests.post(context.urladd, json=context.payLoad, headers=context.header, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    # print(response_json['ID'])
    # print(type(response_json))
    context.bookid = response_json["ID"]
    # print(type(bookid))
    # print(bookid + "123")
    print(context.bookid)
    assert response_json['Msg'] == "successfully added"


# Parameterized Inputs using Example Outline
@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    # fake = Faker()
    # fakeisbn = fake.isbn10()

    context.urladd = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.header = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle)
    # context.payLoad = addBookPayload(fakeisbn) # using faker plugin


# GitHub API validation on repo
@given('I have github auth credential')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('jmtagumpay', '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')


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')  # added ':d' to read it as an integer, lesson 57
def step_impl(context, statusCode):
    print(context.response.json())
    print(context.response.status_code)
    assert context.response.status_code == statusCode  # parameterize to be able to execute same step on other scenarios

