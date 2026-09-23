#!/usr/bin/env python3
"""Validate a built PHINDER site before publishing (standard library only)."""
import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.canonical = None
        self.redirect = False
        self.filter_values = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # The navigation script assigns this target to the theme page-body wrapper.
        if 'page-body' in attrs.get('class', '').split():
            self.ids.add('main-content')
        # HugoBlox publication hashes are filter values, not element IDs.
        if tag == 'option' and attrs.get('value'):
            self.filter_values.add(attrs['value'])
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for key in ('href', 'src', 'poster'):
            if attrs.get(key):
                self.links.append((tag, key, attrs[key]))
        if tag in ('img', 'source') and attrs.get('srcset'):
            for item in attrs['srcset'].split(','):
                self.links.append((tag, 'src', item.strip().split()[0]))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.redirect = True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--base-url', default='https://phinder-eic.github.io/')
    args = parser.parse_args()
    root = args.directory.resolve()
    base = args.base_url.rstrip('/') + '/'
    host = urlsplit(base).netloc
    pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
    errors = set()
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        url = urljoin(base, relative.removesuffix('index.html'))
        if page.canonical and not page.canonical.startswith(base):
            errors.add(f'{relative}: incorrect canonical {page.canonical}')
        for tag, attr, value in page.links:
            if value.startswith(('data:', 'mailto:', 'tel:', 'javascript:')) or value == '#':
                continue
            parsed = urlsplit(urljoin(url, value))
            if parsed.hostname in ('localhost', '127.0.0.1') or (parsed.hostname or '').endswith('.trycloudflare.com'):
                errors.add(f'{relative}: preview URL {value}')
            if parsed.netloc != host or parsed.scheme not in ('http', 'https'):
                continue
            target = root / unquote(parsed.path).lstrip('/')
            if not target.suffix or target.is_dir():
                target = target / 'index.html'
            if not target.is_file():
                errors.add(f'{relative}: missing {value}')
            elif tag == 'a' and parsed.fragment and target in pages and not pages[target].redirect:
                fragment = unquote(parsed.fragment)
                is_filter = parsed.path == '/publication/' and ('.pubtype-' + fragment) in pages[target].filter_values
                if fragment not in pages[target].ids and not is_filter:
                    errors.add(f'{relative}: missing anchor {value}')
    for route in ('science', 'technology', 'use-cases', 'consortium', 'news', 'publication', 'publications', 'people'):
        if not (root / route / 'index.html').is_file():
            errors.add(f'Missing required route /{route}/')
    for route in ('submit', 'research/example', 'research/example1', 'research/example2', 'research/example3', 'members/dasdas'):
        if (root / route / 'index.html').exists():
            errors.add(f'Obsolete draft unexpectedly published: /{route}/')
    for filename in ('sitemap.xml', 'robots.txt', 'index.json'):
        if not (root / filename).is_file():
            errors.add(f'Missing {filename}')
    if (root / 'index.json').is_file():
        json.loads((root / 'index.json').read_text())
    for filename in ('sitemap.xml', 'robots.txt'):
        if (root / filename).is_file():
            text = (root / filename).read_text()
            if re.search(r'localhost|127\.0\.0\.1|trycloudflare\.com', text):
                errors.add(f'{filename}: preview URL leaked into production')
    if errors:
        print('\n'.join(sorted(errors)), file=sys.stderr)
        print(f'FAILED: {len(errors)} issues across {len(pages)} HTML pages.', file=sys.stderr)
        return 1
    print(f'PASS: {len(pages)} HTML pages; internal links, anchors, assets, canonical URLs, required routes and draft exclusions.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
