# 第三方包
from tornado.web import RequestHandler


# 基础视图处理类
class BaseHandler(RequestHandler):
    pass


# 根视图处理类
class IndexHandler(BaseHandler):

    def get(self):
        self.render('index.html')