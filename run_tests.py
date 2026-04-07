#!/usr/bin/env python3
"""
Test runner with various options and reporting.
"""

import sys
import unittest
import os
from pathlib import Path

# Add main directory to path
main_dir = Path(__file__).parent
sys.path.insert(0, str(main_dir))

def run_all_tests(verbosity=2):
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Load tests from tests directory
    tests_dir = main_dir / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern='test_*.py'))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_unit_tests(verbosity=2):
    """Run unit tests only."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    tests_dir = main_dir / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern='test_converters.py'))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_integration_tests(verbosity=2):
    """Run integration tests only."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    tests_dir = main_dir / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern='test_integration.py'))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_specific_test(test_name, verbosity=2):
    """Run a specific test."""
    loader = unittest.TestLoader()
    
    try:
        suite = loader.loadTestsFromName(test_name)
        runner = unittest.TextTestRunner(verbosity=verbosity)
        result = runner.run(suite)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def print_test_summary(result):
    """Print test summary."""
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    successful = total_tests - failures - errors
    
    print(f"Total tests: {total_tests}")
    print(f"Successful: {successful} ✓")
    print(f"Errors: {errors} ✗")
    print(f"Failures: {failures} ✗")
    
    if failures > 0:
        print(f"\nFailures:")
        for test, traceback in result.failures:
            print(f"  - {test}")
    
    if errors > 0:
        print(f"\nErrors:")
        for test, traceback in result.errors:
            print(f"  - {test}")
    
    success_rate = (successful / total_tests * 100) if total_tests > 0 else 0
    print(f"\nSuccess rate: {success_rate:.1f}%")
    print("=" * 70)
    
    return result.wasSuccessful()


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Test runner for python-transform',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py                           # Run all tests
  python run_tests.py -u                        # Unit tests only
  python run_tests.py -i                        # Integration tests only
  python run_tests.py -t tests.test_converters  # Specific test
  python run_tests.py -v 1                      # Less info (verbose=1)
  python run_tests.py -a                        # All (default)
        """
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--all', action='store_true',
                       help='Run all tests (default)', default=True)
    group.add_argument('-u', '--unit', action='store_true',
                       help='Run unit tests only')
    group.add_argument('-i', '--integration', action='store_true',
                       help='Run integration tests only')
    group.add_argument('-t', '--test', type=str, metavar='TEST_NAME',
                       help='Run specific test')
    
    parser.add_argument('-v', '--verbosity', type=int, default=2, 
                        choices=[0, 1, 2],
                        help='Verbosity level (0=minimum, 2=maximum)')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("python-transform - Test Runner")
    print("=" * 70)
    print()
    
    # Run appropriate tests
    if args.unit:
        print("Running UNIT TESTS...\n")
        result = run_unit_tests(args.verbosity)
    elif args.integration:
        print("Running INTEGRATION TESTS...\n")
        result = run_integration_tests(args.verbosity)
    elif args.test:
        print(f"Running: {args.test}\n")
        result = run_specific_test(args.test, args.verbosity)
        if result is None:
            sys.exit(1)
    else:
        print("Running ALL TESTS...\n")
        result = run_all_tests(args.verbosity)
    
    # Print summary
    success = print_test_summary(result)
    
    # Exit
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
