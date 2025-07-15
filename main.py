from handler.handler import app
from model.post import db, Post
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

def init_db():
    """初始化数据库"""
    db.connect()
    db.create_tables([Post], safe=True)
    db.close()

def main():
    print("正在启动 blog-backend 服务器...")
    init_db()
    origins = [
        "https://cat-paw-blog.netlify.app",
        "localhost",
        "localhost:8888"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
