import pytest

@pytest.yield_fixture()
def setUp():      # Can be any name not only setUp
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")    # Under scope can be module,session,class...
def oneTimeSetUp(request, browser, osType):      # Can be any name not only oneTimeSetUp
    print("Running one time setUp")
    if browser == "chrome":
        value = 10
        print("Running tests on Chrome")
    else:
        value = 20
        print("Running tests on Unknown browser")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="module")  # Instead module in scope we can use session
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="module")
def osType(request):
    return request.config.getoption("--osType")
