# Insider Web Case

## Case
1. Visit https://useinsider.com/ and check Insider home page is opened or not
2. Select the “Company” menu in the navigation bar, select “Careers” and check Career
page, its Locations, Teams, and Life at Insider blocks are open or not
3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter
jobs by Location: “Istanbul, Turkey”, and Department: “Quality Assurance”, check the
presence of the job list
4. Check that all jobs’ Position contains “Quality Assurance”, Department contains
“Quality Assurance”, and Location contains “Istanbul, Turkey”
5. Click the “View Role” button and check that this action redirects us to the Lever
Application form page

## Dependencies

- Python
- Pipenv 

> Pre requirements: 
- [Python](hhttps://www.python.org/downloads/release/python-3918/)

## Installation

Use git command

```bash
https://github.com/senakorkmaz/insider-web-case.git
```

1. Run ` pip install pipenv ` to install pipenv if it does not exist.
2. Run ` pipenv install ` to install dependencies with new env.
3. Run ` pipenv shell` to run env.
4. Run ` pipenv run python3 -m pytest --html=report.html` to test.
After the runing test you can check *report.html* file for the report
