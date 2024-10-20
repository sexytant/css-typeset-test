import sys
import markdown

fname = sys.argv[1]

md = markdown.Markdown(extensions=['tables'])

with open(f'{fname}.md', 'r') as f:
    text = f.read()

with open(f'{fname}.html', 'w') as f:
    f.write('<link href="layout.css" rel="stylesheet" />')
    f.write(md.convert(text))
