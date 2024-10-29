# 8-Automation-Assignment

## Project Overview

The goal of this project is to ensure data consistency for robots across two representations:
1. **Table View**: A tabular format displaying each robot's attributes, including `x` and `y` coordinates.
2. **Map View**: A visual representation of robots positioned using CSS grid styling based on their coordinates.
## Features

- Retrieves robot data from both a table and a map view.
- Compares the x and y positions of the robots for consistency.
- Provides clear assertions and error messages for discrepancies.
- Uses Selenium for web interaction and Pytest for testing.

## Requirements

- **Python**: Version 3.10+
- **Selenium**: For web automation
- **Google Chrome/Firefox**
- **ChromeDriver/GeckoDriver for Firefox**: Ensure it matches your browser version
- **Pytest**

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SlafkoS/8-Automation-Assignment
2. Change into the project directory:
   ```bash
   cd 8-Automation-Assignment
3. Install requirements:
   ```bash
   pip install -r requirements.txt
## Running the Tests
1. Run the server : python -m http.server 3000
   ```bash
   python -m http.server 3000
2. Open second terminal and run the test:
   ```bash
   pytest tests\robot_consistency_tests.py
## Test Description
The tests include consistency checks for each robot:

Test Cases:
- test_robot1_consistency: Verifies that Robot 1’s position in the table matches its position on the map.
- test_robot2_consistency: Verifies that Robot 2’s position in the table matches its position on the map.
- test_robot3_consistency: Verifies that Robot 3’s position in the table matches its position on the map.

## Fixtures
- driver(): A fixture to initialize and close the ChromeDriver or Firefox driver for each test.