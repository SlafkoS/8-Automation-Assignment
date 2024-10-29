## Overview

This project automates the process of checking data consistency between a table view and a map view of robots using Selenium. The script retrieves the position data (x and y coordinates) of robots displayed in both views and compares them to ensure consistency. The project includes unit tests written with Pytest.

## Features

- Retrieves robot data from both a table and a map view.
- Compares the x and y positions of the robots for consistency.
- Provides clear assertions and error messages for discrepancies.
- Uses Selenium for web interaction and Pytest for testing.

## Requirements

- Python 3.6 or higher
- Google Chrome (or another browser of your choice)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (make sure the version matches your Chrome version)
- Selenium package
- Pytest framework

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SlafkoS/8-Automation-Assignment
   cd DataConsistencyCheck

   run the server : python -m http.server 3000