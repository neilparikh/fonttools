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

    analysis.main(["-ifp", "TestData/%s.ttx" % test_name])
    output = sys.stdout.getvalue()

    sys.stderr.close()
    sys.stderr = old_stderr
    sys.stdout = old_stdout

    return output


class TestCOI(unittest.TestCase):
    def common(self, test_name):
        actual = get_actual_output(test_name)
        with open('TestData/%s.ttx.coi' % test_name) as f:
            expected = f.read()
            self.assertEqual(actual, expected,
                             "output is different for %s" % test_name)

    def test_FreeMono_simple(self):
        self.common("FreeMono-simple")

    def test_FreeMono_call_endf(self):
        self.common("FreeMono-call-endf")

    def test_FreeMono_empty_fdef(self):
        self.common("FreeMono-empty-fdef")

    def test_FreeMono_gfv(self):
        self.common("FreeMono-gfv")

    def test_FreeMono_max_no_simplify(self):
        self.common("FreeMono-max-no-simplify")

    def test_FreeMono_max(self):
        self.common("FreeMono-max")

    def test_FreeMono_jmpr(self):
        self.common("FreeMono-jmpr")

    def test_FreeMono_jrot_jrof(self):
        self.common("FreeMono-jrot-jrof")

    def test_FreeMono_pop(self):
        self.common("FreeMono-pop")

    def test_FreeMono_simple_if(self):
        self.common("FreeMono-simple-if")

    def test_FreeMono_simple_if(self):
        self.common("FreeMono-skip-inst")


def regen_expected(test_name):
    actual = get_actual_output(test_name)
    with open('TestData/%s.ttx.coi' % test_name, "w") as f:
        f.write(actual)


parser = argparse.ArgumentParser(description='Expectation tests.')
parser.add_argument("--regen")
if __name__ == "__main__":
    args = parser.parse_args()
    if args.regen is not None:
        regen_expected(args.regen)
    else:
        unittest.main()
