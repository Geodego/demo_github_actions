# demo_github_actions
demo including basic tasks using Github Actions

We use the Python starter workflow. This Action installs Python and the requirements for your application (if there are any). Lastly it runs flake8 and pytest -- the build fails if either a test fails or certain flake8 errors are hit.

In principle, one should run flake8 and pytest before you commit your code since that can be faster than waiting on the automated build process but this piece of automation ensures any contributors to the code also pass flake8 and pytest and they get checked in case you don't run them yourself. It also ensures that both of these pass when the code is built in a clean environment. The file used is python-app.yaml
