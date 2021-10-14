@cucumber-basket
Feature: Cucumber Basket
    As a gardener,
    I want to carry cucumbers in a basket,
    So that I don't drop them all.

@add
Scenario Outline: Add cucumbers to a basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

# No limit to table size, but recommended to keep it small and should really only focus on equivilance classes of the iputs that you need.
# It will be tempting to make it big, but remember you don't have to test everything. Every test is going to encur a run time and a resources load.
    Examples: Amounts
        | initial   | some      | total |
        | 2         | 4         | 6     |
        | 0         | 3         | 3     |
        | 5         | 5         | 10    |

@remove
Scenario: Remove cucumbers from a basket
    Given the basket has "8" cucumbers
    When "3" cucumbers are removed from the basket
    Then the basket contains "5" cucumbers