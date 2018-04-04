import pytest
from selenium import webdriver


@pytest.fixture(scope='session',
                params=[
                    webdriver.Chrome,
                    webdriver.Firefox,
                ],
                ids=['Chrome', 'Firefox'])
def driver(request):
    # Create a new instance of a driver
    driver = request.param()
    yield driver
    driver.quit()
