#!/usr/bin/env python
import markdown
from markdown_extension_equation_block import MyExtension

r = '?\n- hi\n- hi'

with open("test.md", 'r') as f:
    r = f.read()

s = markdown.markdown(r, extensions=[MyExtension()])


print 'result'
print s


