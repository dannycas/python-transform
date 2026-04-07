#!/usr/bin/env python3
"""
Runner dla testów z różnymi opcjami i raportowaniem.
"""

import sys
import unittest
import os
from pathlib import Path

# Dodaj główny katalog do path
main_dir = Path(__file__).parent
sys.path.insert(0, str(main_dir))

def run_all_tests(verbosity=2):
    """Uruchom wszystkie testy."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Załaduj testy z katalogu tests
    tests_dir = main_dir / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern='test_*.py'))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_unit_tests(verbosity=2):
    """Uruchom tylko unit testy."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    tests_dir = main_dir / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern='test_converters.py'))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_integration_tests(verbosity=2):
    """Uruchom tylko testy integracyjne."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    tests_dir = main_dir / 'tests'
    suite.addTests(loader.discover(str(tests_dir), pattern='test_integration.py'))
    
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    return result


def run_specific_test(test_name, verbosity=2):
    """Uruchom konkretny test."""
    loader = unittest.TestLoader()
    
    try:
        suite = loader.loadTestsFromName(test_name)
        runner = unittest.TextTestRunner(verbosity=verbosity)
        result = runner.run(suite)
        return result
    except Exception as e:
        print(f"Błąd: {e}")
        return None


def print_test_summary(result):
    """Wydrukuj podsumowanie testów."""
    print("\n" + "=" * 70)
    print("PODSUMOWANIE TESTÓW")
    print("=" * 70)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    successful = total_tests - failures - errors
    
    print(f"Całkowita liczba testów: {total_tests}")
    print(f"Pomyślne: {successful} ✓")
    print(f"Błędy: {errors} ✗")
    print(f"Awarie: {failures} ✗")
    
    if failures > 0:
        print(f"\nAwarunki:")
        for test, traceback in result.failures:
            print(f"  - {test}")
    
    if errors > 0:
        print(f"\nBłędy:")
        for test, traceback in result.errors:
            print(f"  - {test}")
    
    success_rate = (successful / total_tests * 100) if total_tests > 0 else 0
    print(f"\nStosunek sukcesu: {success_rate:.1f}%")
    print("=" * 70)
    
    return result.wasSuccessful()


def main():
    """Główna funkcja."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Runner dla testów python-transform',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Przykłady:
  python run_tests.py                           # Uruchom wszystkie testy
  python run_tests.py -u                        # Tylko unit testy
  python run_tests.py -i                        # Tylko testy integracyjne
  python run_tests.py -t tests.test_converters  # Konkretny test
  python run_tests.py -v 1                      # Mało informacji (verbose=1)
  python run_tests.py -a                        # Wszystko (domyślnie)
        """
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--all', action='store_true',
                       help='Uruchom wszystkie testy (domyślnie)', default=True)
    group.add_argument('-u', '--unit', action='store_true',
                       help='Uruchom tylko unit testy')
    group.add_argument('-i', '--integration', action='store_true',
                       help='Uruchom tylko testy integracyjne')
    group.add_argument('-t', '--test', type=str, metavar='TEST_NAME',
                       help='Uruchom konkretny test')
    
    parser.add_argument('-v', '--verbosity', type=int, default=2, 
                        choices=[0, 1, 2],
                        help='Poziom szczegółowości (0=minimum, 2=maximum)')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("python-transform - Test Runner")
    print("=" * 70)
    print()
    
    # Uruchom odpowiednie testy
    if args.unit:
        print("Uruchamianie UNIT TESTS...\n")
        result = run_unit_tests(args.verbosity)
    elif args.integration:
        print("Uruchamianie INTEGRATION TESTS...\n")
        result = run_integration_tests(args.verbosity)
    elif args.test:
        print(f"Uruchamianie: {args.test}\n")
        result = run_specific_test(args.test, args.verbosity)
        if result is None:
            sys.exit(1)
    else:
        print("Uruchamianie WSZYSTKICH TESTS...\n")
        result = run_all_tests(args.verbosity)
    
    # Wydrukuj podsumowanie
    success = print_test_summary(result)
    
    # Zakończenie
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
