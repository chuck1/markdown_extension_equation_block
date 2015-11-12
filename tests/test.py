import markdown
from myextension import MyExtension

r = '?\n- hi\n- hi'

s = markdown.markdown(r, extensions=[MyExtension()])


print 'result'
print s


