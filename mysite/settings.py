# 项目配置信息文件

# 基础包
import os

# 第三方包
from tornado.options import define

# 基础路由
BASE_URL = os.path.dirname(__file__)

# 默认项目启动端口配置
define('port', default=8001, help='项目启动默认端口')

# 网页模板及静态文件配置
config = {
    # 网页文件
    'template_path': os.path.join(BASE_URL, 'templates'),
    # 静态文件
    'static_path': os.path.join(BASE_URL, 'static'),
    # 调试模式：开启
    'debug': True,
    # cookie密钥

}
