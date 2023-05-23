
"""
Python provides an efficient way to automate the testing of a function's
output. 
"""

#### Testing a Function - Unit Tests and Test Cases ####

"""
The module unittest from the Python standard library provides tools for
testing your code. A unit test verifies that one specific aspect of a function's
behavior is correct. A test case is a collection of unit tests that together prove
that a function behaves as it's supposed to, within the full range of situations
you expect it to handle. A good test case considers all the possible
kinds of input a function could receive and includes tests to represent each
of these situations. 

A test case with full coverage includes a full range of unit
tests covering all the possible ways you can use a function. Achieving full
coverage on a large project can be daunting. It's often good enough to write
tests for your code's critical behaviors and then aim for full coverage only if
the project starts to see widespread use
"""

## A Passing Test

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

""" The above function is stored in name_function.py """

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
if __name__ == '__main__':
    unittest.main()

""" The above function is stored in test_name_function.py """

# Output ->
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK


## A Failing Test

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

""" 
The above function is stored in name_function.py and then test_name_function.py 
is run again 
"""

# Output ->
# E
# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)
# Do names like 'Janis Joplin' work?
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#     File "test_name_function.py", line 8, in test_first_last_name
#         formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# FAILED (errors=1)


## Responding to a Failed Test

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

""" The above function is stored in name_function.py """

# Output ->
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK


## Adding New Tests

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

""" The above function is stored in test_name_function.py and triggered """

# Output ->
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK


#### Testing a Class ####

## A Variety of Assert Methods

"""
Assert Methods Available from the unittest Module
Method                      Use
assertEqual(a, b)           Verify that a == b
assertNotEqual(a, b)        Verify that a != b
assertTrue(x)               Verify that x is True
assertFalse(x)              Verify that x is False
assertIn(item, list)        Verify that item is in list
assertNotIn(item, list)     Verify that item is not in list
"""

## A Class to Test

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

""" The above function is stored in survey.py """

## Testing the AnonymousSurvey Class

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()

""" The above function is stored in test_survey.py """

## The setUp() Method

"""
In test_survey.py we created a new instance of AnonymousSurvey in each test
method, and we created new responses in each method.

The unittest.TestCase class has a setUp() method that allows you to create 
these objects once and then use them in each of your test methods. When you 
include a setUp() method in a TestCase class, Python runs the setUp() method 
before running each method starting with test_. Any objects created in the setUp() 
method are then available in each test method you write.
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

"""
When you're testing your own classes, the setUp() method can make
your test methods easier to write. You make one set of instances and attributes
in setUp() and then use these instances in all your test methods. This
is much easier than making a new set of instances and attributes in each
test method.

Note: When a test case is running, Python prints one character for each unit test as it is
completed. A passing test prints a dot, a test that results in an error prints an E, and
a test that results in a failed assertion prints an F. This is why you'll see a different
number of dots and characters on the first line of output when you run your test cases.
If a test case takes a long time to run because it contains many unit tests, you can
watch these results to get a sense of how many tests are passing.
"""

