#! /usr/bin/env python3
# URL_finder.py - Finds URLs that begin with http:// or https:// on the clipboard.

import pyperclip, re

# the regex
url_regex = re.compile(r'https?:\//[a-z0-9.\-_/]+\.[a-z0-9_\-/]+')

# import from clipboard

text = str(pyperclip.paste())
# print(url_regex.findall(text))
for matches in url_regex.findall(text):

# paste the urls found
	if len(matches) > 0:
		pyperclip.copy(matches)
