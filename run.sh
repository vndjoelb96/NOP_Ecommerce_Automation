
# Run your Python script
#pytest -s -v -m "sanity" --html=./Reports/sanityCases.html testCases/ --browser chrome

pytest -s -v -m "regression" --html=./Reports/regressionCases.html testCases/ --browser firefox

