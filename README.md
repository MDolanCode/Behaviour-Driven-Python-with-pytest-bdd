# --------------------------------------
# A brief intro to BDD
# --------------------------------------

Why do we need a new software development process like BDD?
    * Software development happens rapidly, and teams are pushed to continuously deliver new products and features.
    * As a result, in the development process, 2 things suffer: collaboration and test automation. 

Common Software Development Problem
* Team miscommunication.
* Poor planning.
* Poor documentation.
* Testers don't know the features.
* Automation is difficult to develop.
* Missed deadlines.

How can we solve these problems?
    * The answer is pretty simple — return the focus to the behaviors of the features being developed. 
    * This may seem a little bit too simple, but it's the behaviors of the features being developed that deliver value to the end user.

Behaviour
* In software terms, a behavior is how a feature operates. It can be defined as a scenario of inputs, actions, 
  and outcomes. We could also call it a “feature function”, so to speak. A product or feature exhibits countless behaviors.
    * Submitting forms on a website.
    * Searching for desired results.
    * Saving a document.
    * Making REST API Calls.
    * Running CLI commands.

Examples of Behaviours

* Web UI
    * Login and logout.
    * Navigating through pages.
    * Submitting forms.

* Service API
    * Making successful calls.
    * Verifying system state change.
    * Receiving expected errors.

* Real Life
    * Adding items to a shopping cart.
    * Paying for those items at checkout.
    * Eating bamboo.

* Focusing on individual behaviors brings major efficiencies to both the development and the testing of software features.

Individual Behaviours
* Separating individual behaviours makes it easy to define a system without unnecessary repetition or complication.
    
    Search for "shoes" from a store's home page ---> Select the first link on the search results page <--- Load results for "shoes" from a saved query

* Separating these behaviors makes the developers and the testers do each individual behavior well because care and attention will be given directly to it. 
  And furthermore, the application simply becomes a composition of multiple behaviors working together.

* Behavior driven development then is simply a process that puts behaviors first in both development and in testing.

Behaviour-Driven Development

* BDD is a process that puts behaviours first in development and in testing.
    * Three Amigos Meetings bring everyone together. Business, development and testing come together to knock heads and get on the same page.
    * Example Mapping helps everyone define and learn stories. Learn what it's about in terms of its rules, examples and any questions people may have.
    * Specification by Example defines behaviours clearly. Describe and define behaviors using a more formalized language, so that things are crystal clear.
    * Behaviour Implementation produces features and tests. The features get developed and the tests are automated.

* BBD is a refinement, not and overhaul, of existing processes!

Specifying a Behaviour
* Behavior specifications are the main artifacts of the BDD process.
    * They are, in effect, the requirements, acceptance criteria and test cases for the behaviors. And if a team is using a BDD test automation framework, they also become the test script.

Gherkin
* Gherkin, by far, is the most popular specification language because most test frameworks use Gherkin.
* For example, if I have a Cucumber Basket behavior, my Gherkin scenario could look like this.

Example
Add cucumbers to a basket:

    # GIVEN an initial state
    Given the basket has 2 cucumbers

    # WHEN an action is taken
    When 4 cucumbers are added to the basket

    # THEN verify outcomes
    Then the basket contains 6 cucumbers

* These behaviors specifications, as we can see, are written in plain language so that anyone on the team could understand them.
* They're self-documenting and they're descriptive. Gherkin is not meant to be a programming language, but rather a business specification language.

* Since behavior specs are basically test cases, it only makes sense to automate them using some sort of test framework.

Test Automation

* Behaviours are identified early in development using plain-language descriptions (Gherkin) that tell what more than how.
* A BDD test framework separates test cases from test code. It will "glue" each step to a Python function to run it like a script.
    * And that's exactly what BDD test frameworks do. They will glue each one of those Gherkin steps, based on its text, 
      to some sort of method or function in a programming language, such as Python, so that the BDD test framework can run all those scenarios, like scripts.

Python BDD Test Frameworks

* behave - One of the most popular ones is behave, which has been around for a while. It's very similar to the Cucumber project.
* radish - Another good choice is the radish framework which extends the Gherkin language with things like constants and scenario loops, making it a little bit more friendly for programmatic testing.
* lettuce - lettuce is another framework that's been around for quite some time and is also similar to Cucumber. Although, it doesn't seem to have as much activity anymore.

* pytest-bdd - The reason why we've chosen pytest-bdd is because it is a plugin for pytest, which is one of the best test frameworks in Python, 
  and also one of the most popular. Pytest makes it very easy to write simple but powerful tests. It also comes with a bunch of other plugins such as for code coverage, or html reports, or parallel execution.

Why do Behaviour-Driven Development?

The main benefits of BDD are better collaboration and automation.

1. Everyone can contribute, not just programmers.
2. Do things properly from the start.
3. Step reuse creates a snowball effect.





