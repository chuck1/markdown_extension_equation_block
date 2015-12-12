from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor, ListIndentProcessor
from markdown.util import etree
import re
import json

class MyBlockParser(BlockProcessor):
	
	RE  = re.compile("^([\w_]+\n)?(\\\\\\\\\\[(.*\n.*)*\\\\\\\\\\])$")
	RE1 = re.compile("^([\w_]+\\n)?(\\\\\\\\\\[(.*\\n.*)*\\\\\\\\\\])$")
	
        def __init__(self, parser):
            super(MyBlockParser, self).__init__(parser)
            self.mycount = 0

	def test(self, parent, block):
                b = bool(self.RE.search(block))
                b1 = bool(self.RE1.search(block))
		print 'test',repr(block), b, b1
		return b
		
	def run(self, parent, blocks):
		print
		print 'run', repr(blocks)
		#print 'state', self.parser.state

                raw_block = blocks.pop(0)

                m = self.RE.match(raw_block)
                
                
                print "label", repr(m.group(1))
                print "eq   ", repr(m.group(2))

                """

                class_name = 'question'

		

                if m.group(1):
                    j = json.loads(m.group(1))
                    #print "extra data", j
                    try:
                        class_name = j['class']
                    except: pass
		
		#print 'm', m.start(), m.end()
		
		
                """
		tab = etree.SubElement(parent, 'table')
                tab.attrib['class'] = 'equation'
		
       		tr = etree.SubElement(tab, 'tr')
       		td0 = etree.SubElement(tr, 'td')
       		td1 = etree.SubElement(tr, 'td')
                td0.text = m.group(2)

                self.mycount += 1
                td1.text = str(self.mycount)
                if m.group(1):
                    td1.attrib['id'] = "eq_" + m.group(1)[:-1]
                #print div.attrib
		
		#self.parser.parseBlocks(div, [raw_block[m.end():]])
		#blocks.insert(0, raw_block[m.end():])
                
                #self.parser.state.reset()

		#return True

class MyExtension(Extension):
	def extendMarkdown(self, md, md_globals):
		md.parser.blockprocessors.add('equation_block',
			MyBlockParser(md.parser),
			'>indent')

