import os
import argparse
import unittest
import sys
from fontTools import analysis
from StringIO import StringIO


test_cases = ["FreeMono-simple"]


def get_actual_output(test_name):
    old_stderr = sys.stderr
    old_stdout = sys.stdout

    sys.stderr = open(os.devnull, 'wb')
    sys.stdout = StringIO()

    analysis.main(["-ifv", "TestData/%s.ttx" % test_name])
    output = sys.stdout.getvalue()

    sys.stderr.close()
    sys.stderr = old_stderr
    sys.stdout = old_stdout

    return output


class TestCOI(unittest.TestCase):
    def test_FreeMono_simple(self):
        test_name = "FreeMono-simple"
        actual = get_actual_output(test_name)
        with open('TestData/%s.coi' % test_name) as f:
            expected = f.read()
            self.assertEqual(actual, expected,
                             "output is different for %s" % test_name)

def regen_expected(test_name):
    actual = get_actual_output(test_name)
    with open('TestData/%s.coi' % test_name, "w") as f:
        f.write(actual)


parser = argparse.ArgumentParser(description='Expectation tests.')
parser.add_argument("--regen")
if __name__ == "__main__":
    args = parser.parse_args()
    if args.regen is not None:
        regen_expected(args.regen)
    else:
        unittest.main()
