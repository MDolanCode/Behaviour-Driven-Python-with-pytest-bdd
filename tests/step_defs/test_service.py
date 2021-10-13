"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from pytest_bdd import scenarios, given, then, parsers

# Shared Variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

# Scenarios

scenarios('../features/service.feature', example_converters=dict(phrase=str))

# Given Steps

# Only given steps are allowed to be fixtures, so this is why there is no when step.

@given('the DuckDuckGo API is queried with "<phrase>"', target_fixture='ddg_response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response

# Then Steps

@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    assert phrase.lower() == ddg_response.json()['Heading'].lower()

@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code

# Advice when using pytest-bdd for testing rest apis
# 2 ways to go about this. 
#   1. You can either specify your scenarios using very imperitive steps mechanically looking at response codes, different fields, header values and parameters or 
#   2. You can try to be more declarative and focus on more end-to-end behaviour such as you call this service, then you call that service and you expect this to be in the system and that to be in the database and describing it in more natural language.
# The latter scenario is much more preferable to write than the former scenario.
# Not to say one is more important than the other, but rather if you are only doing testing individual requests or you want to do more data driven style testing where you crank lots of combinations of inputs on single or double requests. A pytest framework like BDD or cucumber or another BDD framework might not be the best avenue simply because individual requests and data driven requests is usually very programatic and low level. It may be more beneficial to write traditional pytest functions or to use frameworks like Python's Tavern or even to use something like Karate in order to write those tests. You can still use pytest BBD no problem, but it is just something to think about.
# BDD testing really shines with feature level testing, especially with end-to-end tests for multiple services or webUI.