# Product Requirement 产品需求规格说明
项目名：MoneyHong2019挣闲钱网页

|版本 | 修订人 | 日期 |
|:--:|:--:|:--:|
|1.0 | xhc16340263 | 2019.5.9|
|2.0 | xhc16340263 | 2019.6.25|



## 1.引言
### 1.1编写目的
本文档的目的是详细地介绍MoneyHong2019挣闲钱网页所包含的需求，以便查看者能够确认产品的确切需求以及开发人员能够根据需求设计编码。
本文档的预期读者有开发人员，老师/助教，项目经理。
### 1.2背景
大学生活、校园生活的方方面面都有可以互利互惠的地方，当一个中介可以建立起交易双方的信托和联系纽带时，两个需求方的双赢就会变成可能。本项目致力于打造一个中大学生使用的跑腿应用网页，将中大学子的生活琐事变得更共有价值和更有趣味性，实现交易双方的互赢。
## 2.任务概述
### 2.1目标  
中大学生可以利用自己的邮箱自由注册发布任务和接受任务的账号，登陆后就可以根据自己的需要来发布一些挣闲钱的小任务，有接受者接受任务之后，双方可以交流任务细节，完成任务之后发布方需要支付给接受方一定的报酬。这个网页版的挣闲钱app，可以方便大家利用课余时间赚取小额的伙食费，也可以增加同学间交流沟通的机会。一个用户注册账号后既可以发布任务也可以接受任务，实时查询平台的可接受任务和自己发布的任务是否被人接受，很轻量级。
### 2.2用户特点  
持有中大的学号，是在校学生；  
有需要被别人完成的任务；  
可以利用空余时间接受任务，并负责任地完成。  
### 2.3约束  
因为我们服务器资源有限，人力时间有限，所以后台可支持的用户数不多，未做太多额外功能，这只能作为作业提交，要上线为一个成熟的挣闲钱网站，他的部分功能还有待提高。
## 3.需求规定  
### 3.1对功能的规定  
挣闲钱：用户通过学号登陆账户后，进入网站，跳转到我们的任务中心页面，可以选择发布或接受任务，具体实现的功能流程如下：  
1. 打开主页  
2. 未注册的用户点击注册按钮，用邮箱注册，填写昵称，输入密码并确认，注册后直接进入任务中心  
3. 已注册的用户点击登录按钮，使用邮箱和账户密码登陆，登陆后进入任务中心  
4. 任务中心可以看到当前存在的任务，包含问卷、快递、叫早、代买药、带饭几个业务，其中问卷是基本业务；用户可以在每个业务的右侧条目中看到业务的基本信息并决定是否接受。也可以在当前页面下选择发布任务   
5. 可以通过点击个人中心按钮跳转到个人中心，他包含账户信息、我的账户、账户安全、我的消息和退出登录几个模块，可以实现个人账户管理和查看任务状态  
### 3.2对性能的规定  
1. 精度：要按照严格的数据格式输入，对符合数据格式要求的输入进行提示。  
2. 时间特性要求：    
* 软件启动时间：小于1s  
* 系统实时响应时间：软件使用过程中，用户用手指点击各个功能模块时的响应时间需要在用户能够容忍的时间范围之内，要求小于1s  
* 数据更新时间：软件使用过程中，同步刷新时间设置为1s    
* 输入输出要求：输入源为手机或电脑触控及键盘，输出设备为手机或电脑屏幕  
## 4.运行环境规定  
### 4.1设备  
装载有浏览器的手机或电脑  
### 4.2运行环境  
前端：浏览器  
后端：服务器  
### 4.3框架  
django  
## 5.基本验收标准  
|测试项 | 输入/操作 | 需求结果 |
|:--:|:--:|:--:|
|「首页」 | 1、进入首页；2、进入登陆界面；3、进入注册页面| 1、首页基本UI显示正常；2、登陆页面基本UI显示正常；3、注册页面基本UI显示正常|
|「注册」界面 | 1、输入昵称、邮箱、密码、确认密码；2、返回首页；3、注册完毕| 1、注册界面基本UI显示正常；2、可返回首页；3、注册后直接进入任务中心|  
|「登陆」界面 | 1、输入邮箱、密码2、返回首页；3、登陆| 1、登陆界面基本UI显示正常；2、2、可返回首页；3、登陆后直接进入任务中心，任务中心界面基本UI显示正常|  
|「任务中心」界面 | 1、查询已发布的业务；2、前往个人中心；3、发布任务| 1、已发布的任务显示正常；2、可前往个人中心页面，个人中心界面基本UI显示正常；3、可正常发布任务并在对应的任务区块显示|  
|「个人中心」界面 | 1、查看账户信息；2、查询我的任务；3查看我的消息；4、账户安全；5、退出登录| 1、账户信息正常显示个人信息；2、我的任务可以查看未完成、已完成和已发布的任务；3、我的消息可看到积分通知、任务进展和任务提醒；4、账户安全可修改密码或忘记密码；5、可退出登录后回到首页|    
