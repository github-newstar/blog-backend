from peewee import *
from loguru import logger
from datetime import datetime
from model.post import Post

@logger.catch
def createpost(title, content, author, tags)->bool:
    newPo = Post()
    newPo.title = title
    newPo.content = content
    newPo.author = author
    newPo.tags = tags
    try:
        newPo.save()
    except:
        return False
    return True
@logger.catch
def getPostsList()->list:
    try:
        # 获取所有博客文章，按创建时间倒序排列
        posts = Post.select().order_by(Post.created_at.desc())
        # 将查询结果转换为字典列表，便于JSON序列化
        posts_list = []
        for post in posts:
            posts_list.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author,
                'tags': post.tags,
                'created_at': post.created_at.isoformat() if post.created_at else None
            })
        return posts_list
    except Exception as e:
        logger.error(f"获取博客列表失败: {e}")
        return []

@logger.catch
def getPostById(id)->dict:
    try:
        posts = Post.select().where(Post.id == id)
        # 将查询结果转换为字典列表，便于JSON序列化
        return{
            'id': posts[0].id,
            'title': posts[0].title,
            'content': posts[0].content,
            'author': posts[0].author,
            'tags': posts[0].tags,
            'created_at': posts[0].created_at.isoformat() if posts[0].created_at else None
        }
    except Exception as e:
        logger.error(f"获取博客列表失败: {e}")
        return {}
@logger.catch
def deletepost(id)->bool:
    try:
        posts = Post.select().where(Post.id == id)
        if posts:
            posts[0].delete_instance()
            return True
        else:
            return False
    except Exception as e:
        logger.error(f"删除博客失败: {e}")
        return False