from peewee import *
from datetime import datetime

db = SqliteDatabase(
        "posts.db",
        pragmas=(
            ('journal_mode', 'wal'),
        )
)
class BasePosts(Model):
    class Meta:
        database = db

class Post(BasePosts):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=100)
    content = TextField(null=False)
    author = CharField(null=False)
    tags = CharField(null=True, default='[]')
    created_at = DateTimeField(default=datetime.now)
    class Meta:
        db_table = 'posts'
        
if __name__ == '__main__':
    db.connect()
    db.create_tables([Post])
    db.close()
