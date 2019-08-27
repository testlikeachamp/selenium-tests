# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(scope='session',
#                 params=[
#                     webdriver.Chrome,
#                     # webdriver.Firefox,
#                 ],
#                 ids=['Chrome',
#                      # 'Firefox'
#                      ])
# def driver(request):
#     # Create a new instance of a driver
#     options = webdriver.ChromeOptions()
#     # options.binary_location = '/usr/bin/google-chrome-unstable'
#     options.add_argument('headless')
#     options.add_argument('window-size=1200x600')
#     driver = request.param(
#         options=options
#     )
#     yield driver
#     driver.quit()


import time

import docker
import pytest
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # for remote selenium

selenium_hub_port = 8899


@pytest.fixture(scope='session',
                params=[
                    'chrome',
                    'firefox'
                ])
def run_browser_in_docker(request):
    client = docker.from_env()
    # docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.12.0-cobalt
    container = client.containers.run(
        "selenium/standalone-{}:latest".format(request.param),
        ports={4444: selenium_hub_port},
        volumes={'/dev/shm': {'bind': '/dev/shm', 'mode': 'rw'}},
        detach=True
    )
    time.sleep(3)  # TODO: make this smarter :)
    yield request.param
    container.remove(force=True)


@pytest.fixture(scope='session',
                params=[
                    # webdriver.Chrome,
                    # webdriver.Firefox,
                    webdriver.Remote
                ],
                ids=[
                    # 'Chrome',
                    # 'Firefox',
                    'Remote'
                ])
def driver(request, run_browser_in_docker):
    # Create a new instance of a driver
    options = webdriver.ChromeOptions()
    # options.binary_location = '/usr/bin/google-chrome-unstable'
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    # driver = request.param(
    #     options=options
    # )
    driver = request.param(
        command_executor='http://127.0.0.1:{}/wd/hub'.format(selenium_hub_port),
        desired_capabilities=DesiredCapabilities.CHROME if run_browser_in_docker == 'chrome' else DesiredCapabilities.FIREFOX,
    )
    yield driver
    driver.quit()
