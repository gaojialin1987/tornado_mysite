# 第三方包
from tornado.web import Application
from tornado.options import options, parse_command_line
from tornado.ioloop import IOLoop

# 自定义包
from mysite import urls
from mysite import settings


# 主程序入口
if __name__ == '__main__':
    # 识别命令行变量操作
    parse_command_line()
    # 定义app(通过**，引入字典中的键值)
    app = Application(urls.urlpaterns, **settings.config)
    # 启动项目监听端口
    app.listen(options.port)
    # 启动轮询事件
    IOLoop.current().start()