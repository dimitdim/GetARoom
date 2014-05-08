from app import db,models
import time

def analyze(data):
    return 0

nodes=models.Node.query.all()
lastr=[0]*len(nodes)
old_lastr=[0]*len(nodes)
state=[False]*len(nodes)
num=[0]*len(nodes)
for n in range(len(nodes)):
    data=models.Data.query.filter_by(node_id=nodes[n].id).order_by('localtimestamp desc').first()
    lastr[n]=data.last_opened
    last=(data.localtimestamp+(data.last_opened-data.uptime)/1000)
    print 'Initial:'
    print str(n)+': '+str(last)
print 'Updates:'
while True:
    for n in range(len(nodes)):
        data=models.Data.query.filter_by(node_id=nodes[n].id).order_by('localtimestamp desc').first()
        old_lastr[n]=lastr[n]
        lastr[n]=data.last_opened
        if lastr[n]!=old_lastr[n]:
            state[n]=True
        if state[n]:
            if lastr[n]==old_lastr[n]: num[n]+=1
            else: num[n]=0
        if num[n]>5:
            last=(data.localtimestamp+(data.last_opened-data.uptime)/1000)
            stat=analyze(data)
            print str(n)+': '+last+': '+str(stat)
            new=models.Status(last,stat,nodes[n])
            db.session.add(new)
            db.session.commit()
            state=False
            num=0
    time.sleep(10)