import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")   # We can put all/any fixtures that we want to use
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)  # Look in conftest.py file to see how to return a value from fixtures

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):

        print("Running method B")
