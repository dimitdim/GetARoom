from app import db,models
import time

nodes=models.Node.query.filter_by(id=3).all()
for node in nodes:
    datas=models.Data.query.filter_by(node_id=node.id).order_by('localtimestamp desc').all()
    print len(datas)
    state=False
    n=0
    lastr=datas[0].last_opened
    for data in datas:
        old_lastr=lastr
        lastr=data.last_opened
        if lastr!=old_lastr:
            state=True
        if state:
            if lastr==old_lastr: n+=1
            else: n=0
        if n>5:
            last=(data.localtimestamp+(data.last_opened-data.uptime)/1000)
            print last
            new=models.Status(last,1,node)
            db.session.add(new)
            db.session.commit()
            state=False
            n=0
