import os
from bs4 import BeautifulSoup
import pytest

# Get the directory of the current script, then go up one level to the root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILE_PATH = os.path.join(PROJECT_ROOT, 'index.html')

@pytest.fixture
def html_soup():
    assert os.path.exists(HTML_FILE_PATH), f"HTML file does not exist at {HTML_FILE_PATH}"
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup

def test_html_file_exists():
    """Test that the index.html file actually exists."""
    assert os.path.exists(HTML_FILE_PATH)

def test_form_exists(html_soup):
    """Test that a form exists in the HTML."""
    form = html_soup.find('form')
    assert form is not None, "No <form> tag found in HTML"

def test_required_form_elements(html_soup):
    """Test that the form contains required input fields (name, email, student ID, etc.)."""
    form = html_soup.find('form')
    assert form is not None
    
    # Check for specific input fields by id or name
    assert form.find('input', {'id': 'fullName'}) is not None, "Missing 'fullName' input"
    assert form.find('input', {'id': 'email'}) is not None, "Missing 'email' input"
    assert form.find('input', {'id': 'studentId'}) is not None, "Missing 'studentId' input"
    
    # Check for select dropdown
    assert form.find('select', {'id': 'course'}) is not None, "Missing 'course' select dropdown"
    
    # Check for submit button
    submit_button = form.find('button', {'type': 'submit'})
    assert submit_button is not None, "Missing submit button"
