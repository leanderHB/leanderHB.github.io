import os
import re
import shutil
from datetime import datetime

# Define paths
OBSIDIAN_VAULT = "/home/leander/Documents/Obsidian Vault/Thesis"
OBSIDIAN_VAULT_IMAGES = "/home/leander/Documents/Obsidian Vault/plaatjes"
JEKYLL_SITE = "/home/leander/Documents/github_site_leanderHB/leanderHB.github.io"
POSTS_DIR = os.path.join(JEKYLL_SITE, "_posts")
IMAGES_DIR = os.path.join(JEKYLL_SITE, "assets", "images")
RAW_MARKDOWN_DIR = os.path.join(JEKYLL_SITE, "assets", "md")
INCLUDES_DIR = os.path.join(JEKYLL_SITE, "_includes")
TOC_FILE = os.path.join(INCLUDES_DIR, "toc.md")

# Create necessary directories
for dir_path in [POSTS_DIR, IMAGES_DIR, RAW_MARKDOWN_DIR, INCLUDES_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# Clear previous posts and TOC
for file in os.listdir(POSTS_DIR):
    os.remove(os.path.join(POSTS_DIR, file))
with open(TOC_FILE, 'w') as toc:
    toc.write("# Table of Contents\n")

def copy_image(image_name):
    """Copy an image to the images directory and return the updated content reference."""
    image_path = os.path.join(OBSIDIAN_VAULT_IMAGES, image_name)
    if os.path.isfile(image_path):
        shutil.copy(image_path, os.path.join(IMAGES_DIR, image_name))
        return f'<img src="/assets/images/{image_name}" class="img-fluid rounded z-depth-1" alt="{image_name}">'
    print(f"Warning: Image {image_name} not found.")
    return f"![[{image_name}]]"  # Return original if not found

def find_file_in_subdirectories(file_name, search_directory):
    """Search for a file in the specified directory and its subdirectories."""
    for dirpath, _, filenames in os.walk(search_directory):
        if file_name in filenames:
            return os.path.join(dirpath, file_name)
    return None  # Return None if the file is not found

def process_links(content, base_filename):
    """Process internal links in the content to convert them to Jekyll-compatible links."""
    link_pattern = r'\[\[(.*?)\]\]'

    def replace_link(match):
        original_link = match.group(1)
        name = original_link.split("#")[0]
        file_path = os.path.join(root, name + ".md")

        if not os.path.isfile(file_path):
            file_path = find_file_in_subdirectories(name + ".md", root)

        if file_path is None:
            print(f"File not found: {name}.md")
            return match.group(0)

        date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')
        new_filename = f"{date}-{name.lower().replace(' ', '-')}.md"
        return f"[{name}]({{% link _posts/{new_filename} %}})"

    return re.sub(link_pattern, replace_link, content)

def process_content(content):
    """Process markdown content for images, math blocks, and links."""
    # Handle image references
    content = re.sub(r'!\[\[(.+?\.(png|jpg|jpeg|gif))\]\]', lambda match: copy_image(match.group(1)), content)
    # Replace block math with a scrollable div
    content = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-container">\\[\1\\]</div>', content, flags=re.DOTALL)
    # Replace inline math
    content = re.sub(r'\$(.*?)\$', r'$$\1$$', content)
    return content

def write_front_matter(new_file, title, date):
    """Write the front matter and additional CSS to the new Jekyll post."""
    new_file.write(f"---\nlayout: post\ntitle: \"{title}\"\ndate: {date}\n---\n")
    new_file.write("""
<style>
.math-container {
    max-width: 100%;
    overflow-x: auto;
    white-space: nowrap;
}
</style>\n
""")

def process_markdown_file(file_path):
    """Process individual markdown files from the Obsidian vault."""
    filename = os.path.basename(file_path)
    date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')
    new_filename = f"{date}-{filename.lower().replace(' ', '-')}"
    new_filename_no_date = filename.lower().replace(' ', '-').replace(".md", "")
    new_file_path = os.path.join(POSTS_DIR, new_filename)

    with open(file_path, 'r') as original_file:
        content = original_file.read()

    content = process_content(content)
    content = process_links(content, filename)

    # Write content to the new Jekyll post
    with open(new_file_path, 'w') as new_file:
        write_front_matter(new_file, filename[:-3], date)
        new_file.write(content)

        # Add link to raw markdown file at the bottom of the post
        raw_markdown_path = os.path.join(RAW_MARKDOWN_DIR, filename)
        shutil.copy(file_path, raw_markdown_path)
        raw_link = f'\n\n[View Raw Markdown](/assets/md/{filename})\n'
        new_file.write(raw_link)

    # Add to Table of Contents
    with open(TOC_FILE, 'a') as toc:
        toc.write(f"- [{filename[:-3]}](../{new_filename_no_date})\n")

def process_overview_file(file_path):
    """Process the overview markdown file differently, writing to the includes directory."""
    filename = os.path.basename(file_path)
    new_file_path = os.path.join(INCLUDES_DIR, filename)

    with open(file_path, 'r') as original_file:
        content = original_file.read()

    content = process_content(content)
    content = process_links(content, filename)

    with open(new_file_path, 'w') as new_file:
        new_file.write(content)

# Process all markdown files in the Obsidian vault
for root, _, files in os.walk(OBSIDIAN_VAULT):
    for file in files:
        if file.endswith('.md'):
            if file.lower() == "overview.md":
                process_overview_file(os.path.join(root, file))
            else:
                process_markdown_file(os.path.join(root, file))

print("Conversion complete! Posts created in", POSTS_DIR, "and TOC created in", TOC_FILE)
