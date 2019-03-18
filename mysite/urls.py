# 路由配置模块
from mysite import views

# 路由配置
urlpaterns = [
    (r'/', views.IndexHandler)
]
