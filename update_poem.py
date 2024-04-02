import json
import random
import numpy as np
import requests

def fetch_poem():
    d = ['tang', 'song']
    k = np.random.randint(0,2)
    ind = np.random.randint(0, [57, 254][k]) * 1000
    url = f"https://raw.githubusercontent.com/TLI2958/chinese-poetry/master/%E5%85%A8%E5%94%90%E8%AF%97/poet.{d[k]}.{int(ind)}.json"
    response = requests.get(url)
    poems = response.json()
    selected_poem = random.choice(poems)
    return selected_poem

def format_poem(poem):
    # Combine the title, author, and paragraphs of the poem for Markdown
    poem_content = f"### {poem['title']}\n\n*{poem['author']}*\n\n" + '\n'.join(poem['paragraphs']) + '\n'
    return poem_content

def update_readme(poem_content):
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Locate the start and end markers for the poem in the README
    start_index = content.index('<!-- POEM_START -->') + 1
    end_index = content.index('<!-- POEM_END -->')

    # Replace the content between the markers with the new poem
    content[start_index:end_index] = [poem_content + '\n']

    # Write the updated content back to the README
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.writelines(content)

# Fetch a random poem from the URL
selected_poem = fetch_poem()
# Format the poem for Markdown
poem_markdown = format_poem(selected_poem)
# Update the README with the selected poem
update_readme(poem_markdown)
