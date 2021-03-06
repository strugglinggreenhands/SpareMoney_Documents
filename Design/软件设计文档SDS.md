# 软件设计文档
## 目录
- [开发规划](##开发规划)
  - [开发人员](###开发人员)
  - [开发计划](###开发计划)
  - [开发环境和工具](###开发环境和工具)
  - [开发规范](###开发规范)

- [总体设计数据结构](##总体设计数据结构)
  - [概念术语描述](###概念术语描述)
  - [基本设计描述](###基本设计描述)
    - 系统总体逻辑结构图
    - 系统部署结构图
  - [主要界面流程描述](###主要界面流程描述)
    - 登陆注册功能界面流程
    - 发布任务功能界面流程
    - 接受任务功能界面流程
  - [模块列表](###模块列表)
  - [后端文件结构](###后端文件结构)
- [数据结构（数据库）](##数据结构)
- [接口规范](##接口规范)
  - [<注册登录API>](###<注册登录API>)
  - [<任务中心API>](###<任务中心API>)
  - [<个人中心API>](###<个人中心API>)
- [附录](##附录)
  - [第三方组件](###第三方组件)
  - [参考资料](###参考资料)
 

## 开发规划
### 开发人员
|学号  姓名 英文名|角色|
|:--:|:--:|
|16340251 谢冰澄 Beatrix | PM、UI设计师|
|15352307 汤伟杰 twj15352307|QA工程师，产品经理|
|16340184 邱婷 AaronCyril|后端|
|16340254 谢济锴 Jack|后端设计师，开发经理|
|16340263 许海晨 Andy|前端程序员|
|16340262 徐艺 Eva|前端程序员|
|16340223 王思诚 wsc16340223|后端程序员|
|16340104 蓝华琳 RinHuA|DevOps工程师|

### 开发计划表
- 前端

|功能|预计开始时间|预计工作日|
|:--:|:--:|:--:|
|确定页面功能|第10周|2|
|确定页面分布|第11周|3|
|草稿初定|第12周|7|
|html 与 css|第13周|7|
|js | 第14周|7|


- 后端

|功能|预计开始时间|预计工作日|
|:--:|:--:|:--:|
|确定架构|第10周|7|
|确定后端模块|第11周|1|
|实现API|第12周|3|
|实现API|第13周|3|
|检测API正确性|第14周|3|

### 开发环境和工具

|工具|功能|
|:--:|:--:|
|mySQL|提供数据库服务|
|PyCharm|django开发IDE|


### 开发规范
|文档名称|位置|
|:--:|:--:|
|系统目录规范.md|Document|

## 总体设计

### 基本设计描述
- 设计思路
  - 在本次实验中，我们从业务和功能出发，应用了客户端-服务端的传统相应模式，部署web页面。
- 系统总体逻辑结构图
  - ![用例图](../images/Usecase_diagram.png)
  
- 系统部署结构图
  - ![topo](../images/topo.png)

### 主要界面流程描述

- 登陆注册功能界面流程

<table><tr><td ><center><img src="https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B4.png?raw=true" > 用例图 </center></td><td ><center><img src="https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A84.png?raw=true" > 活动图 </center></td></tr></table>

- 发布任务功能界面流程

<table><tr><td ><center><img src="https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B2.png?raw=true" > 用例图 </center></td><td ><center><img src="https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A82.png?raw=true" > 活动图 </center></td></tr></table>

- 接受任务功能界面流程

<table><tr><td ><center><img src="https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B1.png?raw=true" > 用例图 </center></td><td ><center><img src="https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A81.png?raw=true" > 活动图 </center></td></tr></table>

### 模块列表

- models
  - 数据库结构

- forms
  - 登录注册表单与发布任务表单

- views
  - 后端实现的功能与接口

### 后端文件结构

```python
└─backend
    ├─.idea
    │  └─libraries
    ├─img                       # readme所需图片
    ├─login
    │  ├─migrations             # 配置文件
    │  ├─templates
    │  │  └─login               # 前端html代码
    │  ├─__pycache__            # 配置文件
    │  ├─admin.py               # 注册models
    │  ├─apps.py                # 注册项目app
    │  ├─forms.py               # 登录、注册、任务表单
    │  ├─models.py              # 数据库中表的结构
    │  ├─views.py               # 接口与功能实现
    │  └─tests.py               # 测试用例
    ├─mysite_login
    │  ├─settings.py            # 项目设置，如数据库连接，host地址等
    │  ├─urls.py                # 路由地址
    │  └─__pycache__            # 配置文件
    ├─static
    │  ├─bootstrap-3.3.7-dist   # 第三方css与js包
    │  ├─css                    # css文件
    │  └─js                     # js文件
    ├─venv                      # 项目环境所需包等
    ├─manage.py                 # 管理项目脚本
    └─readme.md                 # 安装使用说明

```

## 数据结构
- 数据库关系列表

|关系（表名）|作用|
|:--:|:--:|
|用户信息表(login_user)|存储用户的用户名、密码、邮箱和性别，记录分数|
|任务表(Transaction)|记录任务的详细信息(编号,类型,奖励,发布者,联系电话,详情,发起时间和截止时间,接受情况和完成情况|  

## 接口规范
### <注册登录API>
- 接口1——login(request)
  - 接受前端发回的请求request，若请求类型为POST，接受并获取前端的表单(form)内容，进行登录操作。输入的数据均合法时，在数据库表(login_user)中进行匹配查询，查询到则登录，获取用户的信息，保持登录状态。
- 接口2——register(request)
  - 接受前端发回的请求request，若请求类型为POST，接受并获取前端的表单(form)内容，进行注册操作。输入的数据均合法时，在数据库表（login_user）中加入新的用户并记录该用户的注册信息，之后跳转到登录(login)界面。

### <任务中心API>
- 接口1——up_trans(request)
  - 接受前端发回的请求request，若请求类型为POST，接受并获取前端的表单(form)内容，进行任务发布操作。输入的数据均合法时，在数据库表(login_transaction)中加入新的任务并记录任务和发布者的详细信息，之后跳转到主界面。
- 接口2——find_trans(request)
  - 接受前端发回的请求request，若请求类型为GET，将数据库表(login_transaction)中所有任务的信息一一列举并显示在页面上。
- 接口3——accept_trans(request)
  - 接受前端发回的请求request，若请求类型为POST，在数据库表(login_transaction)中查询并找到任务，修改任务的接受状况为True，将接受者修改为发送请求的用户。
- 接口4——my_doing(request)
  - 接受前端发回的请求request，若请求类型为GET，在数据库表(login_transaction)中查询该用户*正在进行*的任务列表，在前端页面显示列表中所有任务的详细信息。若请求类型为POST，在数据库表(login_transaction)中查询到选中的任务，将接受情况设置为False，并将接受人清空。
- 接口5——my_finish(request)
  - 接受前端发回的请求request，若请求类型为GET，在数据库表(login_transaction)中查询该用户*已经完成*的任务列表，在前端页面显示列表中所有任务的详细信息。
- 接口6——my_upload(request)
  - 接受前端发回的请求request，若请求类型为GET，在数据库表(login_transaction)中查询该用户*已经发布*的任务列表，在前端页面显示列表中所有任务的详细信息。若请求类型为POST，在数据库表(login_transaction)中查询到选中的任务，将完成情况设置为True，并将对应的分数加到接受人用户的账户中。
- 接口7——delete_trans(request)
  - 接受前端发回的请求request，若请求类型为GET，显示任务信息；若请求类型为POST，在数据库表(login_transaction)中查询到选中的任务，将该行删除，之后返回到任务中心界面。  

### <个人中心API>
- 接口1——membership(request)
  - 接受前端发回的请求request，若请求类型为GET，显示个人信息。
- 接口2——modify_info(request)
  - 接受前端发回的请求request，若请求类型为POST，接受并获取前端的表单(form)内容，对密码进行修改操作。输入的数据均合法时，在数据库表(login_user)中查询并找到该用户，修改该用户的密码，之后跳转到登录界面。
- 接口3——logout(request)
  - 接受前端的请求request，登出用户。

### <数据库API>
- 定义数据库存储过程接口
每个数据模型都继承django.db.models.Model。他们的父类Model包含了所有必要的和数据库交互的方法，并提供了一个简介漂亮的数据库定义语法。每个模型相当于单个的数据库表（这种情况例外的是多对多的关系，多对多关系的时候会多生成一张关系表），每个属性也是这个表中的一个字段。属性名就是字段名，它的类型（例CharField）相当于数据库的字段类型（例如varchar）。
- 接口1——User(models.Model)
- 接口2——Transaction(models.Model)



## 附录
### 第三方组件
|组件名|版本|用途|
|:--:|:--:|:--:|
|bootstrap|3.3.7|优秀的css框架，优化css文件，美化前端页面|
|jQuery|3.2.1|优秀的JavaScript库，简化JavaScript编程。|

### 参考资料
- bootstrap官方中文文档https://v3.bootcss.com
- django官方文档https://docs.djangoproject.com

