 Scenario: A Dealer can always play  # features/dealer.feature:38
    Given a dealer                    # features/steps/steps.py:5
    When the round starts             # features/steps/steps.py:28
    Then the dealer chooses a play    # features/steps/steps.py:44

1 feature passed, 0 failed, 0 skipped
16 scenarios passed, 0 failed, 0 skipped
48 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.011s
