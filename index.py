import os
import re

# Get the directory where the script is located
directory = os.path.dirname(os.path.abspath(__file__))

# Regex pattern to match only the specific archive.org link for www.indre.fr
pattern = re.compile(r'https://web\.archive\.org/web/\d{14}/https://www\.indre\.fr/?')

# Replacement string
replacement = '/index.html'

# Process each HTML file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace only the exact links
        new_content = pattern.sub(replacement, content)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated: {filename}")
