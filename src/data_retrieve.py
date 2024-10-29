from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def retrieve_table_data(driver):
    """
    Retrieve robot data from the table on the web page.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        dict: A dictionary with robot names as keys and their positions as values.
    """
    robot_table_data = {}
    
    try:
        robots_table = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
        )

        for row in robots_table:
            try:
                name = row.find_element(By.XPATH, "./td[1]").text
                x_position = int(row.find_element(By.XPATH, "./td[2]").text)
                y_position = int(row.find_element(By.XPATH, "./td[3]").text)

                robot_table_data[name] = {
                    "x": x_position,
                    "y": y_position,
                }
            except (ValueError, NoSuchElementException) as e:
                logging.error(f"Error retrieving data from row: {e}")

    except TimeoutException:
        logging.error("Timed out waiting for table to load.")

    return robot_table_data

def retrieve_map_data(driver):
    """
    Retrieve robot position data from the web page.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        dict: A dictionary with robot names as keys and their grid positions as values.
    """
    robot_map_data = {}
    robots = driver.find_elements(By.CSS_SELECTOR, ".robot1, .robot2, .robot3")
    
    # Mapping of class names to robot names
    robot_names = {
        'robot1': 'Robot 1',
        'robot2': 'Robot 2',
        'robot3': 'Robot 3'
    }

    for robot in robots:
        robot_class = robot.get_attribute("class")
        # Default name if robot class not found
        name = "Unknown Robot" 

        # Determine robot name based on class
        for class_key, robot_name in robot_names.items():
            if class_key in robot_class:
                name = robot_name
                break

        # Extract style
        style = robot.get_attribute("style")

        try:
            grid_position = style.split(";")[0].strip().split(": ")[1]
            y_position, x_position = map(int, grid_position.split(" / "))
            robot_map_data[name] = {"x": x_position, "y": y_position}

        except (IndexError, ValueError) as e:
            logging.error(f"Error extracting position for {name}: {e}")

    return robot_map_data