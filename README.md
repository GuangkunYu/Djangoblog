# 基于Django搭建的个人网站


@ 项目开始于2019-11-21

# 开发环境安装配置及工具

- Windows10操作系统

- 考虑到该项目需要开源到GitHub中（不打算开源的可以忽略这点），所以我们首先安装GitHub桌面版软件，进行相关配置（[desktop使用教程](https://help.github.com/cn/desktop/getting-started-with-github-desktop)）并创建我们的远程仓库[Djangoblog](https://github.com/GuangkunYu/Djangoblog)。

## 安装anaconda

- 为了有一个纯净的开发环境，我们选择使用虚拟环境anaconda，首先安装anaconda3-5。
  - 使用虚拟环境的原因：
    - 便于管理，避免不必要的麻烦
  - 选择anaconda的原因：
    - 不需要安装Python
    - 创建的虚拟环境可以选择Python版本
    - 解决依赖关系

## 创建虚拟环境

- 创建虚拟环境,我们的项目将在虚拟环境中开发

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574334789645-a948b678-1978-4cfa-ae63-344b7bfe6ecb.png#align=left&display=inline&height=552&name=image.png&originHeight=552&originWidth=885&search=&size=43162&status=done&width=885)


## 安装Django

- 在虚拟环境中安装Django2.2.1，首先激活虚拟环境，在虚拟环境中通过pip安装

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574336351561-19882bcb-2408-4d57-b72c-467c4acdf077.png#align=left&display=inline&height=146&name=image.png&originHeight=146&originWidth=763&search=&size=14864&status=done&width=763)


![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574336503001-c96b3746-31d6-49be-960d-8514bc17ab4b.png#align=left&display=inline&height=139&name=image.png&originHeight=139&originWidth=756&search=&size=14382&status=done&width=756)


## 安装pycharm

- 编写Python代码的集成开发环境
- 官网下载安装






# 项目工程的创建

## 创建工程

- 因为项目需要上传到GitHub中，所以我们可以直接在本地的GitHub仓库文件夹中直接运行cmd来激活虚拟环境，然后创建工程。



![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574337660046-6fd6fa04-7b85-4026-ac1e-75ed8baa18f4.png#align=left&display=inline&height=297&name=image.png&originHeight=297&originWidth=732&search=&size=37600&status=done&width=732)

## 启动工程

- 进入MyBlog目录，即manage.py的同级目录，启动Django服务验证我们创建的工程是否能够运行。第一次启动服务时，在manage.py的同级目录中会自动生成一个db.sqlite3 的数据文件。Django服务默认启动在8000端口。用该命令启动的Django服务使用的时Django自带的服务器，支持的最大并发量时200，常用来做开发、测试。

    ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574338365416-9b7e8701-7e48-4933-b53e-38853edfd730.png#align=left&display=inline&height=224&name=image.png&originHeight=224&originWidth=707&search=&size=22902&status=done&width=707)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574338624831-9309fd37-c498-4452-a175-08b8a09ef981.png#align=left&display=inline&height=529&name=image.png&originHeight=529&originWidth=771&search=&size=47871&status=done&width=771)

### 执行启动命令常见的方式：

```python
# 启动项目，默认端口为本机8000
python manage.py runserver

# 启动项目，端口为9000
python manage.py runserver 127.0.0.1:9000
    
# 启动项目，任意地址访问9000端口
python manage.py runserver 0.0.0.0:9000
```

## pycharm打开Django项目

- 在工程总目录MyBlog即manage.py的上级目录打开项目
- 选择编译环境为我们最初创建的虚拟环境myenvs
- 启动服务进行验证，如果成功，在浏览器中输入127.0.0.1:8000会出现小火箭。
