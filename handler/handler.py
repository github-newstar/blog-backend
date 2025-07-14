from models.post import *
from fastapi import FastAPI
app =  FastAPI()
from pydantic import BaseModel

class postitem(BaseModel):
    title: str
    content: str
    author: str
    tags: str | None = None

@app.post("/v1/posts/create")
async def CreatePost(iterm : postitem):
    if createpost(iterm.title,iterm.content,iterm.author,iterm.tags):
        return {"success":True, "data": "", "message":"Post Created"}
    else:
        return {"success":False, "data": "", "message":"Post Creation Failed"}
@app.get("/v1/posts/list")
async def GetPostsList():
    res = getPostsList()
    if not res:  # 更好的空列表检查
        return {"success": True, "data": [], "message": "No Posts Found"}
    else:
        return {"success": True, "data": res, "message": "Get posts success"}
    
@app.get("/v1/posts/{id}")
async def GetPostById(id: int):
    res = getPostById(id)
    if not res:  # 更好的空列表检查
        return {"success": False, "data": "", "message": "Post Not Found"}
    else:
        return {"success": True, "data": res, "message": "Get post success"}
@app.delete("/v1/posts/{id}")
async def DeletePost(id: int):
    if deletepost(id):
        return {"success": True, "data": "", "message": "Post Deleted"}
    else:
        return {"success": False, "data": "", "message": "Post Deletion Failed"}