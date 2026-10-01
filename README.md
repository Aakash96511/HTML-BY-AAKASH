# Student Registration Form with CI/CD

This project contains a simple HTML student registration form, along with automated tests and CI/CD pipeline configurations.

## Project Structure

- `index.html`: The HTML file containing the student registration form.
- `requirements.txt`: Python dependencies needed for running the tests (`pytest` and `beautifulsoup4`).
- `tests/test_html.py`: Python script to test the existence and structure of the HTML file.
- `.github/workflows/ci.yml`: GitHub Actions workflow that automatically runs tests on push/pull requests.
- `Jenkinsfile`: Jenkins declarative pipeline configuration to run the tests.

## Running Tests Locally

1. Create a Python virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:
   ```bash
   pytest tests/
   ```

## CI/CD Automation

### GitHub Actions
The `.github/workflows/ci.yml` file is configured to run the tests automatically whenever code is pushed to the `main` branch. Simply commit and push this repository to GitHub, and the Actions tab will show the test results.

### Jenkins
The `Jenkinsfile` provides a Pipeline script. To use it in Jenkins:
1. Create a new "Pipeline" job in Jenkins.
2. Under the "Pipeline" section, select "Pipeline script from SCM".
3. Configure your Git repository URL.
4. Set the script path to `Jenkinsfile`.
5. Run the build.
