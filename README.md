# demo_github_actions
demo including basic tasks using Github Actions

Actions added:
- We use the Python starter workflow. This Action installs Python and the requirements for your application (if there are any). Lastly it runs flake8 and pytest -- the build fails if either a test fails or certain flake8 errors are hit. In principle, one should run flake8 and pytest before you commit your code since that can be faster than waiting on the automated build process but this piece of automation ensures any contributors to the code also pass flake8 and pytest and they get checked in case you don't run them yourself. It also ensures that both of these pass when the code is built in a clean environment. The file used is python-app.yaml

- The second Action is a scheduled job that uses a Unix time-based job scheduler called cron. This Action simply marks issues and pull requests as stale if they have no activity. If you go to stale.yaml's repo then you will see that there are many more options than shown in the default YAML file. This Action is particularly useful for large projects, e.g. open-source projects, since it helps with the maintenance of issues and pull requests. It makes it easier to track what is current or not, and what may need attention without manually combing through the issues and pull requests. The file used is stale.yaml
