from app import db,models
import sys

inp=sys.argv
node=models.Node(inp[1],inp[2],inp[3])
db.session.add(node)
db.session.commit()
files=inp[4:]
length=10
for filename in files:
	f=open(filename,'r')
	headings=f.readline().rstrip('\n').split(',')
	headings = headings + ['Blank']*(length-len(headings))
	for line in f:
		d=line.rstrip('\n').split(',')
		d=d+[-1]*(length-len(d))
		dd=models.Data(d[0],d[2],d[3],d[4],d[5],d[6],d[7],node)
		db.session.add(dd)
	db.session.commit()
	f.close()
