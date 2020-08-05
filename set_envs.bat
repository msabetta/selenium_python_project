@ECHO OFF
setx -m SELENIUM_TEST_AUTO_ENV "%CD%\envs\test-automation\"
setx -m SELENIUM_TEST_AUTO_ENV_SCRIPTS "%CD%\envs\test-automation\Scripts\"
setx path "%PATH%;%SELENIUM_TEST_AUTO_ENV%" /M
setx path "%PATH%;%SELENIUM_TEST_AUTO_ENV_SCRIPTS%" /M