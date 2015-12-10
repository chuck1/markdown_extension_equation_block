from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor, ListIndentProcessor
from markdown.util import etree
import re
import json

class MyBlockParser(BlockProcessor):
	
	RE = re.compile("^\\\\\\\\\\[(.*\n.*)*\\\\\\\\\\]$")
	
	def test(self, parent, block):
                b = bool(self.RE.search(block))
		print 'test',repr(block), b
		return b
		
	def run(self, parent, blocks):
		print
		print 'run', repr(blocks)
		#print 'state', self.parser.state

                raw_block = blocks.pop(0)
                
                """

                class_name = 'question'

		
		m = self.RE.search(raw_block)

                if m.group(1):
                    j = json.loads(m.group(1))
                    #print "extra data", j
                    try:
                        class_name = j['class']
                    except: pass
		
		#print 'm', m.start(), m.end()
		
		div = etree.SubElement(parent, 'div')
                div.attrib['class'] = class_name
		#print div.attrib
		
		self.parser.parseBlocks(div, [raw_block[m.end():]])
		#blocks.insert(0, raw_block[m.end():])
		
                """

		return False

class MyExtension(Extension):
	def extendMarkdown(self, md, md_globals):
		md.parser.blockprocessors.add('equation_block',
			MyBlockParser(md.parser),
			'>indent')

