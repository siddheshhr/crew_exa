#!/usr/bin/env python
from newsletter.crew import Newsletter
import os

def load_html_template():
    # Get the directory of the current file (main.py)
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Build the absolute path to the newsletter template file
    template_path = os.path.join(base_path, 'config', 'newsletter_template.html')
    
    with open(template_path, 'r') as file:
        html_template = file.read()
    
    return html_template


def run():
    # Gather inputs for the newsletter
    inputs = {
        'topic': input('Enter the topic for your newsletter: '),
        'personal_message': input('Enter a personal message for your newsletter: '),
        'html_template': load_html_template()
    }
    # Build and kickoff the crew with the given inputs
    Newsletter().crew().kickoff(inputs=inputs)

