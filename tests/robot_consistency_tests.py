from selenium import webdriver
import pytest
from selenium.common.exceptions import WebDriverException
from src.data_retrieve import retrieve_map_data, retrieve_table_data
import chromedriver_autoinstaller
import shutil

# Helper functions to check WebDriver availability
def is_chrome_driver_installed():
    # Install the correct ChromeDriver if not already installed
    chromedriver_autoinstaller.install()
    return shutil.which("chromedriver") is not None

def is_firefox_driver_installed():
    return shutil.which("geckodriver") is not None

@pytest.fixture
def driver():
    try:
        # Determine which WebDriver to use
        if is_chrome_driver_installed():
            driver = webdriver.Chrome()
        elif is_firefox_driver_installed():
            driver = webdriver.Firefox()
        else:
            pytest.fail("No WebDriver found: Please install Chrome or Firefox WebDriver.")

        # Open the target application
        driver.get("http://localhost:3000")
        yield driver

    except WebDriverException as e:
        pytest.fail(f"WebDriver error: {e}")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

# Check consistency for all robots
@pytest.mark.parametrize("robot_id", ["Robot 1", "Robot 2", "Robot 3"])
def test_robot_consistency(driver, robot_id):

    robot_table_data = retrieve_table_data(driver)
    robot_map_data = retrieve_map_data(driver)

    table_info = robot_table_data.get(robot_id)
    map_info = robot_map_data.get(robot_id)

    assert table_info is not None, f"{robot_id} missing in table view."
    assert map_info is not None, f"{robot_id} missing in map view."
    assert table_info['x'] == map_info['x'], f"{robot_id} X position mismatch: Table {table_info['x']} vs Map {map_info['x']}."
    assert table_info['y'] == map_info['y'], f"{robot_id} Y position mismatch: Table {table_info['y']} vs Map {map_info['y']}."
