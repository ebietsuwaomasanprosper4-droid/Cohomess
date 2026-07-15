from pathlib import Path
import re

root = Path('.')
files = list(root.glob('*.html')) + list((root / 'complonents').glob('*.html'))

nav_map = {
    'Home': 'index.html',
    'Properties': 'properties.html',
    'Find Roommate': 'findroomate.html',
    'Explore': 'emememme.html',
    'Blog': 'blog.html',
    'Account': 'account.html',
    'My Listings': 'mylisting.html',
    'Saved Properties': 'savedproperty.html',
    'Add Property': 'addproperty.html',
    'Account Settings': 'accountsettings.html',
    'Roommate': 'findroomate.html',
    'About Us': 'index.html',
    'Privacy Policy': 'index.html',
    'Terms of Use': 'index.html',
    'Buy': 'properties.html',
    'Sell': 'addproperty.html',
    '@Thecohomes': 'index.html',
    'Thecohomes': 'index.html',
}

fixed_count = 0
for path in files:
    text = path.read_text(encoding='utf-8')
    original = text

    # fix malformed duplicated quotes
    text = re.sub(r'href="([^"]+)""', r'href="\1"', text)
    text = re.sub(r"href='([^']+ )''", r"href='\1'", text)
    text = re.sub(r'href=\"\"', 'href=""', text)

    # fix logo anchor and generic anchors to real pages
    for label, href in nav_map.items():
        pattern = re.compile(rf'(<a[^>]*?)href=(?:["\'])(?:#|""|\'\')(?:["\'])([^>]*?>\s*{re.escape(label)}\s*</a>)', re.IGNORECASE)
        text = pattern.sub(rf'\1href="{href}"\2', text)

    # fix broken specific page names
    text = text.replace('href="find-roommate.html"', 'href="findroomate.html"')
    text = text.replace('href="explore.html"', 'href="emememme.html"')
    text = text.replace('href="propeerties.html"', 'href="properties.html"')
    text = text.replace('href="index.html""', 'href="index.html"')
    text = text.replace('href="properties.html""', 'href="properties.html"')
    text = text.replace('href="findroomate.html""', 'href="findroomate.html"')
    text = text.replace('href="emememme.html""', 'href="emememme.html"')
    text = text.replace('href="blog.html""', 'href="blog.html"')
    text = text.replace('href="login.html""', 'href="login.html"')
    text = text.replace('href="register.html""', 'href="register.html"')
    text = text.replace('href="account.html""', 'href="account.html"')
    text = text.replace('href="mylisting.html""', 'href="mylisting.html"')
    text = text.replace('href="savedproperty.html""', 'href="savedproperty.html"')
    text = text.replace('href="addproperty.html""', 'href="addproperty.html"')
    text = text.replace('href="accountsettings.html""', 'href="accountsettings.html"')

    if text != original:
        path.write_text(text, encoding='utf-8')
        fixed_count += 1

print(f'Updated {fixed_count} files out of {len(files)}.')
