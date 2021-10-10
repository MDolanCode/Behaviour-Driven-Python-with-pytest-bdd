from pytest_bdd import scenario, parsers, given, when, then

from cucumbers import CucumberBasket

@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass

@scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket')
def test_remove():
    pass

# This function below is a pytest fixture.
# It's used by all of the other step definition functions as a fixture.
# What that means is, when this step is called, and this value is returned, it becomes the fixture value that is dependency-injected 
# into all of the other step definition functions that declare that a fixture by name as an argument.

# Add parsers

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=dict(Number=int)), target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=dict(Number=int)))
def add_cucumbers(basket, some):
    basket.add(some)

@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=dict(Number=int)))
def remove_cucumbers(basket, some):
    basket.remove(some)

@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)))
def basket_has_total(basket, total):
    assert basket.count == total