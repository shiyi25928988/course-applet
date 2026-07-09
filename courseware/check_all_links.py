import os
import re
from urllib.parse import urlparse

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Find all href links
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    return links

def check_link(link, source_file):
    # Skip external links and anchors
    if link.startswith(('http://', 'https://', '#', 'mailto:', 'javascript:')):
        return None
    # Skip data URIs
    if link.startswith('data:'):
        return None
    
    # Resolve relative path
    source_dir = os.path.dirname(source_file)
    target_path = os.path.normpath(os.path.join(source_dir, link))
    
    # Check if file exists
    if os.path.exists(target_path) and os.path.isfile(target_path):
        return None  # Valid
    else:
        return f"BROKEN: {link} in {source_file} -> {target_path}"

def main():
    broken_links = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                links = extract_links(file_path)
                for link in links:
                    result = check_link(link, file_path)
                    if result:
                        broken_links.append(result)
    
    if broken_links:
        print("Found broken links:")
        for bl in broken_links:
            print(f"  {bl}")
        print(f"\nTotal broken links: {len(broken_links)}")
    else:
        print("No broken links found!")

if __name__ == '__main__':
    main()
