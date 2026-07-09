import os
import re
from urllib.parse import urlparse

def extract_links(filepath):
    """Extract all href and src links from an HTML file"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find all href and src links
    href_pattern = r'href=["\']([^"\']+)["\']'
    src_pattern = r'src=["\']([^"\']+)["\']'
    
    links = []
    links.extend(re.findall(href_pattern, content))
    links.extend(re.findall(src_pattern, content))
    
    return links

def is_valid_local_link(link, source_dir, root_dir):
    """Check if a local link points to an existing file"""
    # Skip external links, anchors, mailto, javascript, etc.
    if link.startswith(('http://', 'https://', '#', 'mailto:', 'javascript:', 'data:')):
        return True, None
    
    # Skip CSS/JS assets (we'll check them separately if needed)
    if link.startswith(('assets/', '../assets/', '../../assets/')):
        return True, None
    
    parsed = urlparse(link)
    path = parsed.path
    
    if not path:  # Just an anchor or empty
        return True, None
    
    # Calculate target path
    if path.startswith('/'):
        # Absolute path from root (not common in static sites)
        target_path = os.path.join(root_dir, path.lstrip('/'))
    else:
        # Relative path
        target_path = os.path.normpath(os.path.join(source_dir, path))
    
    # Check if file exists
    if os.path.isfile(target_path):
        return True, None
    else:
        # Check if it's a directory with index.html
        if os.path.isdir(target_path) and os.path.isfile(os.path.join(target_path, 'index.html')):
            return True, None
        return False, target_path

def main():
    root_dir = os.getcwd()
    all_files = []
    
    # Get all HTML files
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('.html'):
                all_files.append(os.path.join(root, f))
    
    print(f"Checking {len(all_files)} HTML files...\n")
    
    broken_links = []
    checked_count = 0
    
    for filepath in all_files:
        source_dir = os.path.dirname(filepath)
        rel_filepath = os.path.relpath(filepath, root_dir)
        
        links = extract_links(filepath)
        checked_count += 1
        
        for link in links:
            is_valid, target_path = is_valid_local_link(link, source_dir, root_dir)
            if not is_valid:
                broken_links.append({
                    'source': rel_filepath,
                    'link': link,
                    'target': os.path.relpath(target_path, root_dir) if target_path else 'N/A'
                })
    
    # Report results
    if broken_links:
        print(f"❌ Found {len(broken_links)} broken links:\n")
        for i, bl in enumerate(broken_links, 1):
            print(f"{i}. Source: {bl['source']}")
            print(f"   Link: {bl['link']}")
            print(f"   Missing: {bl['target']}")
            print()
    else:
        print("✅ No broken links found!")
    
    print(f"\nChecked {checked_count} files. {len(broken_links)} broken links found.")

if __name__ == '__main__':
    main()
