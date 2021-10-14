"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.
Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

from _pytest.warning_types import PytestExperimentalApiWarning
import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com'

# Scenarios
scenarios('../features/web.feature')

# Fixtures
@pytest.fixture
def browser():
    # For this example, we will use Firefox.
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    # With Selenium Driver you need to do careful setup and clean up and pytest makes that easy with the power of fixtures.

    # Initialize Firefox webdriver
    b = webdriver.Firefox() 
    # Set an implicite wait time of 10s.
    b.implicitly_wait(10) 
    # It will yield that for setup so anytime this fixture is called by a step it will receive that Firefox webdriver instance.
    yield b 
    # It will quit the webdriver. Quitting is very important because if you don't quit there is a chance that the browser process or driver process could become a zombie. If it is a zombie it will use up system resources, and it could even lock system resources like files or directories, so want to make sure it will clean up after any webdriver you are using.
    b.quit() 

# Given Steps
@given('the DuckDuckGo home page is displayed', target_fixture='ddg_home')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)

# When Steps
@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)

# Then Steps
@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list.
    # (A more comprehensive test would check results for matching phrases).
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase.
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase 
