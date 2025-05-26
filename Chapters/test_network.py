

# conftest.py or test file
import pytest
from seleniumwire import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(seleniumwire_options={
        'request_storage_base_dir': 'requests_log'  # optional logging
    }, options=options)

    yield driver

    driver.quit()


def test_modify_headers(driver):
    def interceptor(request):
        print("Interceptor is called")
        if "httpbin.org" in request.url:
            request.headers['User-Agent'] = 'pytest-agent'
            print(f"Modified request to: {request.url}")

    driver.request_interceptor = interceptor
    driver.get("https://httpbin.org/headers")

    # Grab the response body
    for request in driver.requests:
        if request.response and "httpbin.org/headers" in request.url:
            body = request.response.body.decode("utf-8")
            print(body)
            assert "pytest-agent" in body

            import pdb;pdb.set_trace()
            print(request.response.status_code)
            


