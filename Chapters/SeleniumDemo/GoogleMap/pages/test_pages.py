import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_google_maps_distance(driver):
    driver.get("https://www.google.com/maps")

    # Accept cookies if shown
    try:
        accept_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Accept') or contains(., 'agree')]]"))
        )
        accept_button.click()
    except:
        pass  # Cookie dialog not shown

    # Click Directions

    directions = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Directions']"))
    )
    directions.click()


    # Enter "Chennai" as source
    from_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-0']//input"))
    )
    from_input.send_keys("Chennai")
    from_input.send_keys(Keys.ENTER)

    # Enter "Bangalore" as destination
    to_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='directions-searchbox-1']//input"))
    )
    to_input.send_keys("Bangalore")
    to_input.send_keys(Keys.ENTER)

    # Wait for distance info to show
    distance_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'km')]"))
    )
    # "//div[contains(@class, 'section-directions-trip-distance') or contains(text(), 'km')]"

    distance = distance_element.text   
    print(f"Distance from Chennai to Bangalore: {distance}")
    assert "km" in distance
