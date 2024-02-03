# Selenium Hybrid framework

# Run Tests with Pytest

`Pytest -s -v testCases/test_login.py --browser chrome`

In order to run the tests with HTML reports

`Pytest -s -v --html=Reports/report.html testCases/test_login.py --browser chrome`

To run specific tags:

`Pytest -s -v -m "sanity" --html=Reports/report.html testCases/test_login.py --browser chrome`


