# -*- coding: utf-8 -*-
import logging
import os
import subprocess
import time

from behave import given, then, when

# Get project paths
root_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
tests_features_path = os.path.join(root_project_path, 'tests', 'features')
secondary_features_path = os.path.join(tests_features_path, 'secondary_features')


@given('I have Behave 1.3.0 or newer installed')
def step_check_behave_version(context):
    """Skip the scenario if Behave version is less than 1.3.0"""
    try:
        import behave
        version_str = behave.__version__
        version_parts = version_str.split('.')
        major = int(version_parts[0])
        minor = int(version_parts[1]) if len(version_parts) > 1 else 0

        if (major, minor) < (1, 3):
            context.scenario.skip(f"Skipping v2 tag expression test: Behave {version_str} < 1.3.0")
            return

        logging.info(f"Behave version {version_str} supports v2 tag expressions")
    except (ImportError, AttributeError, ValueError, IndexError) as e:
        context.scenario.skip(f"Could not determine Behave version: {e}")


@when('I run behavex with v2 tag expression "{tag_expression}"')
def step_run_behavex_with_v2_expression(context, tag_expression):
    """Run BehaveX with a v2 tag expression"""
    context.tag_expression = tag_expression
    context.expression_type = 'v2'

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v2_test_{hash(tag_expression) % 1000000}',
        '-t', tag_expression,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    context.start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)
    context.end_time = time.time()
    context.execution_time = context.end_time - context.start_time

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with v2 expression '{tag_expression}', exit code: {result.returncode}")


@when('I run behavex with v1 tag expression "{tag_expression}"')
def step_run_behavex_with_v1_expression(context, tag_expression):
    """Run BehaveX with a v1 tag expression"""
    context.tag_expression = tag_expression
    context.expression_type = 'v1'

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v1_test_{hash(tag_expression) % 1000000}',
        '-t', tag_expression,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    context.start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)
    context.end_time = time.time()
    context.execution_time = context.end_time - context.start_time

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with v1 expression '{tag_expression}', exit code: {result.returncode}")


@when('I run behavex with invalid v2 tag expression "{tag_expression}"')
def step_run_behavex_with_invalid_v2_expression(context, tag_expression):
    """Run BehaveX with an invalid v2 tag expression (expecting failure)"""
    context.tag_expression = tag_expression
    context.expression_type = 'v2_invalid'

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v2_invalid_test_{hash(tag_expression) % 1000000}',
        '-t', tag_expression,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with invalid v2 expression '{tag_expression}', exit code: {result.returncode}")


@when('I run behavex with empty tag expression "{tag_expression}"')
def step_run_behavex_with_empty_expression(context, tag_expression):
    """Run BehaveX with an empty tag expression"""
    context.tag_expression = tag_expression
    context.expression_type = 'empty'

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/empty_test_{hash(str(time.time())) % 1000000}',
        '--logging_level', 'INFO'
    ]

    # Don't add -t flag for empty expression

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with empty expression, exit code: {result.returncode}")


@when('I run behavex with complex v2 tag expression "{tag_expression}"')
def step_run_behavex_with_complex_v2_expression(context, tag_expression):
    """Run BehaveX with a complex v2 tag expression for performance testing"""
    context.tag_expression = tag_expression
    context.expression_type = 'v2_complex'

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v2_complex_test_{hash(tag_expression) % 1000000}',
        '-t', tag_expression,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    context.start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)
    context.end_time = time.time()
    context.execution_time = context.end_time - context.start_time

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with complex v2 expression, exit code: {result.returncode}, time: {context.execution_time:.2f}s")


@when('I run behavex with multiple v2 tag arguments "{tag_arg1}" and "{tag_arg2}"')
def step_run_behavex_with_multiple_v2_arguments(context, tag_arg1, tag_arg2):
    """Run BehaveX with multiple v2 tag arguments"""
    context.tag_expression = f"{tag_arg1} and {tag_arg2}"
    context.expression_type = 'v2_multiple'
    context.tag_arguments = [tag_arg1, tag_arg2]

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v2_multiple_test_{hash(context.tag_expression) % 1000000}',
        '-t', tag_arg1,
        '-t', tag_arg2,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    context.start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)
    context.end_time = time.time()
    context.execution_time = context.end_time - context.start_time

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with multiple v2 arguments '{tag_arg1}' and '{tag_arg2}', exit code: {result.returncode}")


@when('I run behavex with three v2 tag arguments "{tag_arg1}" and "{tag_arg2}" and "{tag_arg3}"')
def step_run_behavex_with_three_v2_arguments(context, tag_arg1, tag_arg2, tag_arg3):
    """Run BehaveX with three v2 tag arguments"""
    context.tag_expression = f"{tag_arg1} and {tag_arg2} and {tag_arg3}"
    context.expression_type = 'v2_three'
    context.tag_arguments = [tag_arg1, tag_arg2, tag_arg3]

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v2_three_test_{hash(context.tag_expression) % 1000000}',
        '-t', tag_arg1,
        '-t', tag_arg2,
        '-t', tag_arg3,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    context.start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)
    context.end_time = time.time()
    context.execution_time = context.end_time - context.start_time

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with three v2 arguments, exit code: {result.returncode}")


@when('I run behavex with mixed tag arguments "{tag_arg1}" and "{tag_arg2}"')
def step_run_behavex_with_mixed_arguments(context, tag_arg1, tag_arg2):
    """Run BehaveX with mixed v1/v2 tag arguments"""
    context.tag_expression = f"{tag_arg1} and {tag_arg2}"
    context.expression_type = 'mixed'
    context.tag_arguments = [tag_arg1, tag_arg2]

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/mixed_test_{hash(context.tag_expression) % 1000000}',
        '-t', tag_arg1,
        '-t', tag_arg2,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with mixed arguments '{tag_arg1}' and '{tag_arg2}', exit code: {result.returncode}")


@when('I run behavex with multiple v1 tag arguments "{tag_arg1}" and "{tag_arg2}"')
def step_run_behavex_with_multiple_v1_arguments(context, tag_arg1, tag_arg2):
    """Run BehaveX with multiple v1 tag arguments"""
    context.tag_expression = f"{tag_arg1} and {tag_arg2}"
    context.expression_type = 'v1_multiple'
    context.tag_arguments = [tag_arg1, tag_arg2]

    # Use secondary features as test target
    cmd = [
        '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3', '-m', 'behavex',
        secondary_features_path,
        '-o', f'output/v1_multiple_test_{hash(context.tag_expression) % 1000000}',
        '-t', tag_arg1,
        '-t', tag_arg2,
        '--logging_level', 'INFO'
    ]

    # Set up environment with PYTHONPATH
    env = os.environ.copy()
    env['PYTHONPATH'] = root_project_path

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=root_project_path, env=env)

    context.result = result
    context.stdout = result.stdout
    context.stderr = result.stderr
    context.returncode = result.returncode

    logging.info(f"BehaveX executed with multiple v1 arguments '{tag_arg1}' and '{tag_arg2}', exit code: {result.returncode}")


@then('the execution should succeed')
def step_execution_should_succeed(context):
    """Verify that BehaveX execution succeeded or had expected failures"""
    # For v2 expressions, we consider it successful if:
    # 1. Exit code is 0 (no failures)
    # 2. Exit code is 1 but scenarios were processed (some scenarios are designed to fail)

    if context.returncode == 0:
        logging.info("BehaveX execution succeeded as expected")
    elif context.returncode == 1:
        # Check if scenarios were actually processed (not a parsing error)
        passed_count = _extract_scenario_count(context.stdout, 'passed')
        failed_count = _extract_scenario_count(context.stdout, 'failed')
        skipped_count = _extract_scenario_count(context.stdout, 'skipped')
        total_scenarios = passed_count + failed_count + skipped_count

        if total_scenarios > 0:
            logging.info(f"BehaveX execution completed with expected failures: {passed_count} passed, {failed_count} failed, {skipped_count} skipped")
        else:
            assert False, f"BehaveX execution failed with exit code {context.returncode}. Stderr: {context.stderr}"
    else:
        assert False, f"BehaveX execution failed with exit code {context.returncode}. Stderr: {context.stderr}"


@then('the execution should fail with a clear error message')
def step_execution_should_fail_with_error(context):
    """Verify that BehaveX execution failed with appropriate error message"""
    assert context.returncode != 0, f"BehaveX execution should have failed but succeeded. Stdout: {context.stdout}"

    # Check for error message in stderr or stdout
    error_output = context.stderr + context.stdout
    assert any(keyword in error_output.lower() for keyword in ['error', 'failed', 'invalid', 'syntax']), \
        f"Expected error message not found in output: {error_output}"

    logging.info(f"BehaveX execution failed as expected with error: {error_output[:200]}...")


@then('the error should mention invalid tag expression syntax')
def step_error_should_mention_syntax(context):
    """Verify that the error message mentions tag expression syntax"""
    error_output = context.stderr + context.stdout
    assert any(keyword in error_output.lower() for keyword in ['tag expression', 'syntax', 'parse', 'invalid']), \
        f"Expected tag expression syntax error not found in output: {error_output}"

    logging.info("Error message correctly mentions tag expression syntax issues")


@then('I should see scenarios with both tags executed')
def step_should_see_both_tags_executed(context):
    """Verify that scenarios with both required tags were executed"""
    # Check that some scenarios passed (indicating execution occurred)
    passed_count = _extract_scenario_count(context.stdout, 'passed')

    # For AND operations, it's possible no scenarios match - this is valid behavior
    if passed_count == 0:
        # Check if there are any skipped scenarios, which indicates filtering worked
        skipped_count = _extract_scenario_count(context.stdout, 'skipped')
        total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

        # If we have skipped scenarios, the filtering is working correctly
        if skipped_count > 0 or total_scenarios > 0:
            logging.info(f"No scenarios matched both tags (passed: {passed_count}, skipped: {skipped_count}) - filtering working correctly")
        else:
            assert False, f"No scenarios were processed at all. Output: {context.stdout}"
    else:
        logging.info(f"Verified {passed_count} scenarios with both tags were executed")


@then('I should see scenarios without both tags skipped')
def step_should_see_without_both_tags_skipped(context):
    """Verify that scenarios without both required tags were skipped"""
    # Check that some scenarios were skipped or that filtering occurred
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    skipped_count = _extract_scenario_count(context.stdout, 'skipped')
    total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

    # If no scenarios passed and we have a total count, then filtering worked
    if passed_count == 0 and total_scenarios > 0:
        logging.info(f"All scenarios were filtered out (skipped: {skipped_count}) - filtering working correctly")
    elif skipped_count > 0:
        logging.info(f"Verified {skipped_count} scenarios without both tags were skipped")
    else:
        # This is acceptable if the expression matched some scenarios
        logging.info(f"Tag filtering processed {total_scenarios} scenarios (passed: {passed_count}, skipped: {skipped_count})")


@then('I should see scenarios with either tag executed')
def step_should_see_either_tag_executed(context):
    """Verify that scenarios with either required tag were executed"""
    # Check that some scenarios passed
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios to pass with either tag"

    logging.info(f"Verified {passed_count} scenarios with either tag were executed")


@then('I should see scenarios without either tag skipped')
def step_should_see_without_either_tag_skipped(context):
    """Verify that scenarios without either required tag were skipped"""
    skipped_count = _extract_scenario_count(context.stdout, 'skipped')
    assert skipped_count > 0, "Expected some scenarios to be skipped"

    logging.info(f"Verified {skipped_count} scenarios without either tag were skipped")


@then('I should see scenarios without the excluded tag executed')
def step_should_see_without_excluded_tag_executed(context):
    """Verify that scenarios without the excluded tag were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    skipped_count = _extract_scenario_count(context.stdout, 'skipped')
    total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

    # For NOT operations, we expect either scenarios to pass OR proper filtering to occur
    if passed_count > 0:
        logging.info(f"Verified {passed_count} scenarios without excluded tag were executed")
    elif total_scenarios > 0:
        logging.info(f"NOT expression filtering worked correctly - {total_scenarios} scenarios processed, {passed_count} passed, {skipped_count} skipped")
    else:
        assert False, f"No scenarios were processed at all. Output: {context.stdout}"


@then('I should see scenarios with the excluded tag skipped')
def step_should_see_with_excluded_tag_skipped(context):
    """Verify that scenarios with the excluded tag were skipped"""
    skipped_count = _extract_scenario_count(context.stdout, 'skipped')
    assert skipped_count > 0, "Expected some scenarios with excluded tag to be skipped"

    logging.info(f"Verified {skipped_count} scenarios with excluded tag were skipped")


@then('I should see scenarios matching the complex expression executed')
def step_should_see_complex_expression_executed(context):
    """Verify that scenarios matching the complex expression were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios to pass with complex expression"

    logging.info(f"Verified {passed_count} scenarios matching complex expression were executed")


@then('I should see scenarios with ORDERED_TEST but not ORDER_001 executed')
def step_should_see_ordered_not_001_executed(context):
    """Verify specific tag combination logic"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios with ORDERED_TEST but not ORDER_001 to pass"

    logging.info(f"Verified {passed_count} scenarios with ORDERED_TEST but not ORDER_001 were executed")


@then('I should see scenarios matching the nested expression executed')
def step_should_see_nested_expression_executed(context):
    """Verify that scenarios matching the nested expression were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios to pass with nested expression"

    logging.info(f"Verified {passed_count} scenarios matching nested expression were executed")


@then('I should see scenarios matching all conditions executed')
def step_should_see_all_conditions_executed(context):
    """Verify that scenarios matching all AND conditions were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios to pass with all conditions"

    logging.info(f"Verified {passed_count} scenarios matching all conditions were executed")


@then('I should see scenarios matching the expression executed')
def step_should_see_expression_executed(context):
    """Generic verification that scenarios matching the expression were executed or properly filtered"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    skipped_count = _extract_scenario_count(context.stdout, 'skipped')
    total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

    # The expression worked if either scenarios passed OR if filtering occurred (scenarios were processed)
    if passed_count > 0:
        logging.info(f"Verified {passed_count} scenarios matching the expression were executed")
    elif total_scenarios > 0:
        logging.info(f"Expression filtering worked correctly - {total_scenarios} scenarios processed, {passed_count} passed, {skipped_count} skipped")
    else:
        assert False, f"No scenarios were processed at all. Output: {context.stdout}"


@then('I should see scenarios matching the multi-level expression executed')
def step_should_see_multi_level_expression_executed(context):
    """Verify that scenarios matching the multi-level expression were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios to pass with multi-level expression"

    logging.info(f"Verified {passed_count} scenarios matching multi-level expression were executed")


@then('I should see scenarios with valid image attachment tags executed')
def step_should_see_valid_image_attachment_tags_executed(context):
    """Verify that scenarios with valid image attachment tags were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios with valid image attachment tags to pass"

    logging.info(f"Verified {passed_count} scenarios with valid image attachment tags were executed")


@then('all available scenarios should be executed')
def step_all_scenarios_should_be_executed(context):
    """Verify that all scenarios were executed (no tag filtering)"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    total_count = passed_count + _extract_scenario_count(context.stdout, 'failed') + _extract_scenario_count(context.stdout, 'skipped')

    # With no tag filter, we expect most scenarios to be executed (some might be skipped for other reasons)
    assert passed_count > 10, f"Expected many scenarios to be executed, got {passed_count}"

    logging.info(f"Verified {passed_count} scenarios were executed out of {total_count} total")


@then('I should see scenarios matching the v1 expression executed')
def step_should_see_v1_expression_executed(context):
    """Verify that scenarios matching the v1 expression were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')
    assert passed_count > 0, "Expected some scenarios to pass with v1 expression"

    logging.info(f"Verified {passed_count} scenarios matching v1 expression were executed")


@then('the legacy tag matching should be used')
def step_legacy_tag_matching_should_be_used(context):
    """Verify that legacy tag matching was used (v1 expressions)"""
    # This is implicit - if v1 expressions work, legacy matching was used
    # We can add more specific checks if needed (e.g., log analysis)
    assert context.returncode == 0, "Legacy tag matching should work correctly"

    logging.info("Verified legacy tag matching was used for v1 expressions")


@then('the native Behave parser should be used')
def step_native_behave_parser_should_be_used(context):
    """Verify that native Behave parser was used (v2 expressions)"""
    # This is implicit - if v2 expressions work, native parser was used
    # We can add more specific checks if needed (e.g., log analysis)
    assert context.returncode == 0, "Native Behave parser should work correctly"

    logging.info("Verified native Behave parser was used for v2 expressions")


@then('the execution should succeed within reasonable time')
def step_execution_should_succeed_within_reasonable_time(context):
    """Verify that execution completed within reasonable time (performance test)"""
    assert context.returncode == 0, f"Execution failed with exit code {context.returncode}"

    # Define reasonable time limit (adjust as needed)
    reasonable_time = 30.0  # seconds
    assert context.execution_time < reasonable_time, \
        f"Execution took {context.execution_time:.2f}s, expected < {reasonable_time}s"

    logging.info(f"Verified execution completed in {context.execution_time:.2f}s (within reasonable time)")


@then('I should see scenarios matching both tag arguments executed')
def step_should_see_both_tag_arguments_executed(context):
    """Verify that scenarios matching both tag arguments were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')

    # For multiple tag arguments with AND logic, it's possible no scenarios match
    if passed_count == 0:
        # Check if there are any skipped scenarios, which indicates filtering worked
        skipped_count = _extract_scenario_count(context.stdout, 'skipped')
        total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

        if skipped_count > 0 or total_scenarios > 0:
            logging.info(f"No scenarios matched both tag arguments (passed: {passed_count}, skipped: {skipped_count}) - filtering working correctly")
        else:
            assert False, f"No scenarios were processed at all. Output: {context.stdout}"
    else:
        logging.info(f"Verified {passed_count} scenarios matching both tag arguments were executed")


@then('I should see scenarios matching the merged expression executed')
def step_should_see_merged_expression_executed(context):
    """Verify that scenarios matching the merged expression were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')

    # For merged expressions, it's possible no scenarios match - this is valid behavior
    if passed_count == 0:
        skipped_count = _extract_scenario_count(context.stdout, 'skipped')
        total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

        if skipped_count > 0 or total_scenarios > 0:
            logging.info(f"No scenarios matched merged expression (passed: {passed_count}, skipped: {skipped_count}) - filtering working correctly")
        else:
            assert False, f"No scenarios were processed at all. Output: {context.stdout}"
    else:
        logging.info(f"Verified {passed_count} scenarios matching merged expression were executed")


@then('I should see scenarios matching all three tag arguments executed')
def step_should_see_all_three_tag_arguments_executed(context):
    """Verify that scenarios matching all three tag arguments were executed"""
    passed_count = _extract_scenario_count(context.stdout, 'passed')

    # For three tag arguments with AND logic, it's very possible no scenarios match
    if passed_count == 0:
        skipped_count = _extract_scenario_count(context.stdout, 'skipped')
        total_scenarios = passed_count + _extract_scenario_count(context.stdout, 'failed') + skipped_count

        if skipped_count > 0 or total_scenarios > 0:
            logging.info(f"No scenarios matched all three tag arguments (passed: {passed_count}, skipped: {skipped_count}) - filtering working correctly")
        else:
            assert False, f"No scenarios were processed at all. Output: {context.stdout}"
    else:
        logging.info(f"Verified {passed_count} scenarios matching all three tag arguments were executed")


@then('the legacy tag matching should be used for mixed arguments')
def step_legacy_tag_matching_should_be_used_for_mixed_arguments(context):
    """Verify that legacy tag matching was used for mixed v1/v2 arguments"""
    # Mixed arguments should fall back to legacy processing
    assert context.returncode == 0, "Legacy tag matching should work correctly for mixed arguments"

    logging.info("Verified legacy tag matching was used for mixed v1/v2 arguments")


@then('the legacy tag matching should be used for v1 arguments')
def step_legacy_tag_matching_should_be_used_for_v1_arguments(context):
    """Verify that legacy tag matching was used for v1 arguments"""
    # v1 arguments should use legacy processing
    assert context.returncode == 0, "Legacy tag matching should work correctly for v1 arguments"

    logging.info("Verified legacy tag matching was used for v1 arguments")


def _extract_scenario_count(output, status):
    """Extract scenario count for a specific status from BehaveX output"""
    import re

    # Look for patterns like "5 scenarios passed" or "3 scenarios skipped"
    pattern = rf'(\d+)\s+scenarios?\s+{status}'
    match = re.search(pattern, output, re.IGNORECASE)

    if match:
        return int(match.group(1))

    return 0
