#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import re
import sys
import os



def convert_md_to_html(md_text):
    """
        COnverts MD to HTML format

        Parameters:
        md_text (string): the html string

        Returns:
        string: the MD string
    """
    # replace headers
    md_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_text, flags=re.M)
    md_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_text, flags=re.M)
    md_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_text, flags=re.M)
    md_text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', md_text, flags=re.M)
    md_text = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', md_text, flags=re.M)
    md_text = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', md_text, flags=re.M)

    # replace bold and italic
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', md_text)
    md_text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', md_text)

    # replace links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md_text)

    # replace images
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2">', md_text)

    # replace code blocks
    md_text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', md_text, flags=re.S)

    # replace inline code
    md_text = re.sub(r'`(.*?)`', r'<code>\1</code>', md_text)

    # replace paragraphs
    md_text = re.sub(r'^([^#\*>\n].+)$', r'<p>\1</p>', md_text, flags=re.M)

    return md_text

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print('Missing <filename>')
        sys.exit(1)

    with open(input_file, 'r') as f:
        markdown_text = f.read()

    html_text = convert_md_to_html(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_text)
    