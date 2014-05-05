from app import db, models
import time

nodes=models.Node.query.all()
while True:
    for node in nodes:
        data=models.Data.query.filter_by(node_id=node.id).order_by('localtimestamp desc').first()
        last=(data.localtimestamp+(data.last_opened-data.uptime)/1000)
        stat=models.Status.query.filter_by(node_id=node.id).order_by('start desc').first()
        if stat == None or stat.start != last:
            new=models.Status(last,1,node)
            db.session.add(new)
            db.session.commit
    time.sleep(10)