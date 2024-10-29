from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def retrieve_table_data(driver):
    robot_table_data = {}
    robots_table = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
    )

    for row in robots_table:
        name = row.find_element(By.XPATH, "./td[1]").text
        x_position = int(row.find_element(By.XPATH, "./td[2]").text)
        y_position = int(row.find_element(By.XPATH, "./td[3]").text)

        robot_table_data[name] = {
            "x": x_position,
            "y": y_position,
        }
    return robot_table_data

def retrieve_map_data(driver):
    robot_map_data = {}
    robots = driver.find_elements(By.CSS_SELECTOR, ".robot1, .robot2, .robot3")

    for robot in robots:
        robot_class = robot.get_attribute("class")
        # Basic value if none robot is found
        name = "Unknown Robot" 
        if 'robot1' in robot_class:
            name = "Robot 1"
        elif 'robot2' in robot_class:
            name = "Robot 2"
        elif 'robot3' in robot_class:
            name = "Robot 3"

        # This returns style
        style = robot.get_attribute("style")

        # Extract grid-column and grid-row
        try:
            grid_position = style.split(";")[0].strip().split(": ")[1]
            y_position, x_position = map(int, grid_position.split(" / "))
            robot_map_data[name] = {"x": x_position, "y": y_position}

        except (IndexError, ValueError) as e:
            print(f"Error extracting position for {name}: {e}")
    return robot_map_data