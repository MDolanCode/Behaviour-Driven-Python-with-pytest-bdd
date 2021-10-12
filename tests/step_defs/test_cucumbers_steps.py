from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket

scenarios('../features/cucumbers.feature')

EXTRA_TYPES = {
    'Number': int,
}

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

# @scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
# def test_add():
#     pass

# @scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket')
# def test_remove():
#     pass

# This function below is a pytest fixture.
# It's used by all of the other step definition functions as a fixture.
# What that means is, when this step is called, and this value is returned, it becomes the fixture value that is dependency-injected 
# into all of the other step definition functions that declare that a fixture by name as an argument.

# Add parsers

@given(parse_num('the basket has "{initial:Number}" cucumbers'), target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parse_num('"{some:Number}" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)

@when(parse_num('"{some:Number}" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)

@then(parse_num('the basket contains "{total:Number}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total