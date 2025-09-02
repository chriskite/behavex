Feature: Tag Expressions v2 (Behave 1.3.0+ Style) Support

  As a BehaveX user
  I want to use v2 tag expressions (Behave 1.3.0+ style) with Behave 1.3.0+
  So that I can leverage advanced boolean logic for test filtering

  Background:
    Given I have Behave 1.3.0 or newer installed

  @TAG_EXPRESSIONS_V2 @BASIC
  Scenario: Basic NOT operation with v2 expressions (should match most scenarios)
    When I run behavex with v2 tag expression "not @NONEXISTENT_TAG"
    Then the execution should succeed
    And I should see scenarios without the excluded tag executed

    @TAG_EXPRESSIONS_V2 @BASIC
  Scenario: Basic OR operation with v2 expressions
    When I run behavex with v2 tag expression "@PASSING_TAG_1 or @PASSING_TAG_2"
    Then the execution should succeed
    And I should see scenarios matching the v2 expression

  @TAG_EXPRESSIONS_V2 @BASIC
  Scenario: Basic AND operation with v2 expressions (existing combination)
    When I run behavex with v2 tag expression "@PASSING_TAG_3 and @PASSING_TAG_3_1"
    Then the execution should succeed
    And I should see scenarios matching the v2 expression

  @TAG_EXPRESSIONS_V2 @ADVANCED
  Scenario: Complex AND/OR combination with v2 expressions
    When I run behavex with v2 tag expression "@AUTORETRY_3 or @AUTORETRY_5"
    Then the execution should succeed
    And I should see scenarios matching the v2 expression

  @TAG_EXPRESSIONS_V2 @ADVANCED
  Scenario: Complex NOT with AND operation using v2 expressions
    When I run behavex with v2 tag expression "@ORDERED_TEST and not @ORDER_001"
    Then the execution should succeed
    And I should see scenarios matching the v2 expression

  @TAG_EXPRESSIONS_V2 @ADVANCED
  Scenario: Nested parentheses with v2 expressions
    When I run behavex with v2 tag expression "(@AUTORETRY or @PRIORITY_TEST) and not @AUTORETRY_PERMANENT_FAILURE"
    Then the execution should succeed
    And I should see scenarios matching the v2 expression

  @TAG_EXPRESSIONS_V2 @ADVANCED
  Scenario: Multiple AND operations with v2 expressions
    When I run behavex with v2 tag expression "@PRIORITY_TEST and @PRIORITY_001"
    Then the execution should succeed
    And I should see scenarios matching the v2 expression

  @TAG_EXPRESSIONS_V2 @CORNER_CASE
  Scenario: Case insensitive operations with v2 expressions
    When I run behavex with v2 tag expression "@AUTORETRY AND @AUTORETRY_RECOVERABLE"
    Then the execution should succeed
    And I should see exactly "1" scenarios executed for case insensitive AND

  @TAG_EXPRESSIONS_V2 @CORNER_CASE
  Scenario: Mixed case operations with v2 expressions
    When I run behavex with v2 tag expression "@AUTORETRY Or @PRIORITY_TEST"
    Then the execution should succeed
    And I should see exactly "6" scenarios executed for mixed case OR

  @TAG_EXPRESSIONS_V2 @CORNER_CASE
  Scenario: NOT at beginning with v2 expressions
    When I run behavex with v2 tag expression "NOT @AUTORETRY_PERMANENT_FAILURE and @AUTORETRY"
    Then the execution should succeed
    And I should see exactly "2" scenarios executed for NOT at beginning

  @TAG_EXPRESSIONS_V2 @CORNER_CASE
  Scenario: Complex expression with multiple parentheses levels
    When I run behavex with v2 tag expression "(@PRIORITY_TEST and @PRIORITY_001) or (@ORDERED_TEST and @ORDER_001)"
    Then the execution should succeed
    And I should see exactly "2" scenarios executed for multi-level parentheses

  @TAG_EXPRESSIONS_V2 @CORNER_CASE
  Scenario: Expression with special characters in tag names
    When I run behavex with v2 tag expression "@IMAGE_ATTACHMENT and @HTML_REPORT"
    Then the execution should succeed
    And I should see exactly "1" scenarios executed for special characters

  @TAG_EXPRESSIONS_V2 @ERROR_HANDLING
  Scenario: Invalid v2 expression syntax should fail gracefully
    When I run behavex with invalid v2 tag expression "@PASSING_TAG_1 and"
    Then the execution should fail with a clear error message
    And the error message should mention tag expression syntax

  @TAG_EXPRESSIONS_V2 @ERROR_HANDLING
  Scenario: Unbalanced parentheses should fail gracefully
    When I run behavex with invalid v2 tag expression "(@PASSING_TAG_1 and @PASSING_TAG_2"
    Then the execution should fail with a clear error message
    And the error message should mention tag expression syntax

  @TAG_EXPRESSIONS_V2 @EMPTY_TAGS
  Scenario: Empty expression should pass all scenarios
    When I run behavex with empty tag expression ""
    Then the execution should succeed
    And all available scenarios should be executed

  @TAG_EXPRESSIONS_V2 @COMPATIBILITY
  Scenario: v1 expressions should still work (backward compatibility)
    When I run behavex with v1 tag expression "~@NONEXISTENT,@PASSING_TAG_1"
    Then the execution should succeed
    And I should see scenarios matching the v1 expression executed
    And the legacy tag matching should be used

  @TAG_EXPRESSIONS_V2 @COMPATIBILITY
  Scenario: Mixed v1 and v2 detection should work correctly
    When I run behavex with v1 tag expression "@PASSING_TAG_1,@PASSING_TAG_2"
    Then the execution should succeed
    And the legacy tag matching should be used
    When I run behavex with v2 tag expression "@PASSING_TAG_1 or @PASSING_TAG_2"
    Then the execution should succeed
    And the native Behave parser should be used

  @TAG_EXPRESSIONS_V2 @PERFORMANCE
  Scenario: Large complex v2 expression should perform well
    When I run behavex with complex v2 tag expression "(@AUTORETRY or @PRIORITY_TEST or @ORDERED_TEST) and not @AUTORETRY_PERMANENT_FAILURE"
    Then the execution should succeed within reasonable time
    And I should see exactly "8" scenarios executed for complex expression

  @TAG_EXPRESSIONS_V2 @MULTIPLE_TAGS
  Scenario: Multiple v2 tag arguments should be merged with AND
    When I run behavex with multiple v2 tag arguments "@AUTORETRY" and "@AUTORETRY_RECOVERABLE"
    Then the execution should succeed
    And I should see scenarios matching the expression with minimum count "1"

  @TAG_EXPRESSIONS_V2 @MULTIPLE_TAGS
  Scenario: Multiple v2 tag arguments with complex expressions
    When I run behavex with multiple v2 tag arguments "@AUTORETRY" and "not @AUTORETRY_PERMANENT_FAILURE"
    Then the execution should succeed
    And I should see exactly "2" scenarios executed for complex multiple arguments

  @TAG_EXPRESSIONS_V2 @MULTIPLE_TAGS
  Scenario: Multiple v2 tag arguments with parentheses
    When I run behavex with multiple v2 tag arguments "@PRIORITY_TEST" and "not @PRIORITY_001"
    Then the execution should succeed
    And I should see exactly "2" scenarios executed for parentheses multiple arguments

  @TAG_EXPRESSIONS_V2 @MULTIPLE_TAGS
  Scenario: Three v2 tag arguments should be merged properly
    When I run behavex with three v2 tag arguments "@AUTORETRY" and "not @AUTORETRY_PERMANENT_FAILURE" and "not @SKIP"
    Then the execution should succeed
    And I should see exactly "2" scenarios executed for three arguments

  @TAG_EXPRESSIONS_V2 @MULTIPLE_TAGS
  Scenario: Mixed v1 and v2 multiple arguments should use v1 processing
    When I run behavex with mixed tag arguments "~@NONEXISTENT" and "@PASSING_TAG_1"
    Then the execution should succeed
    And the legacy tag matching should be used for mixed arguments

  @TAG_EXPRESSIONS_V2 @MULTIPLE_TAGS
  Scenario: Multiple v1 tag arguments should work as before
    When I run behavex with multiple v1 tag arguments "~@NONEXISTENT" and "@PASSING_TAG_1"
    Then the execution should succeed
    And the legacy tag matching should be used for v1 arguments
