Feature: Rule Processing

  @RULE_PROCESSING
  Scenario: Scenarios under Rule sections should be executed by behavex
    Given I have installed behavex
    When I run the behavex command with a rule test
    Then I should see the following behavex console outputs and exit code "0"
      | output_line                          |
      | 3 scenarios passed, 0 failed         |
      | Exit code: 0                         |
    And I should not see error messages in the output
