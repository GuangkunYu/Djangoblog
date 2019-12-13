# 基于Django搭建的个人网站

[toc]


@项目开始于2019-11-21

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

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574334789645-a948b678-1978-4cfa-ae63-344b7bfe6ecb.png#align=left&display=inline&height=552&name=image.png&originHeight=552&originWidth=885&size=43162&status=done&style=none&width=885)


## 安装Django

- 在虚拟环境中安装Django2.2.1，首先激活虚拟环境，在虚拟环境中通过pip安装

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574336351561-19882bcb-2408-4d57-b72c-467c4acdf077.png#align=left&display=inline&height=146&name=image.png&originHeight=146&originWidth=763&size=14864&status=done&style=none&width=763)


![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574336503001-c96b3746-31d6-49be-960d-8514bc17ab4b.png#align=left&display=inline&height=139&name=image.png&originHeight=139&originWidth=756&size=14382&status=done&style=none&width=756)


## 安装pycharm

- 编写Python代码的集成开发环境
- 官网下载安装






# 项目工程的创建

## 创建工程

- 因为项目需要上传到GitHub中，所以我们可以直接在本地的GitHub仓库文件夹中直接运行cmd来激活虚拟环境，然后创建工程。



![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574337660046-6fd6fa04-7b85-4026-ac1e-75ed8baa18f4.png#align=left&display=inline&height=297&name=image.png&originHeight=297&originWidth=732&size=37600&status=done&style=none&width=732)

## 启动工程

- 进入MyBlog目录，即manage.py的同级目录，启动Django服务验证我们创建的工程是否能够运行。第一次启动服务时，在manage.py的同级目录中会自动生成一个db.sqlite3 的数据文件。Django服务默认启动在8000端口。用该命令启动的Django服务使用的时Django自带的服务器，支持的最大并发量时200，常用来做开发、测试。

    ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574338365416-9b7e8701-7e48-4933-b53e-38853edfd730.png#align=left&display=inline&height=224&name=image.png&originHeight=224&originWidth=707&size=22902&status=done&style=none&width=707)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574338624831-9309fd37-c498-4452-a175-08b8a09ef981.png#align=left&display=inline&height=529&name=image.png&originHeight=529&originWidth=771&size=47871&status=done&style=none&width=771)

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
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574759216656-d830e3a2-8539-4896-8ce7-9cced6bf1ae5.png#align=left&display=inline&height=595&name=image.png&originHeight=595&originWidth=440&size=35433&status=done&style=none&width=440)

- 选择编译环境为我们最初创建的虚拟环境myenvs
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574759317743-dd4df15c-cf07-4757-807c-bf9cfd23e1cc.png#align=left&display=inline&height=714&name=image.png&originHeight=714&originWidth=1028&size=84062&status=done&style=none&width=1028)
- 

- 启动服务进行验证，如果成功，在浏览器中输入127.0.0.1:8000会出现小火箭。
- 进行基本的配置修改
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574573200543-4bd47fd0-af17-4ff0-8b77-c35dde44214a.png#align=left&display=inline&height=385&name=image.png&originHeight=385&originWidth=610&size=45670&status=done&style=none&width=610)




# 子应用创建与使用


考虑到网站的健壮性和可移植性，我们将使用子应用。方便管理。

## 创建子应用


三种方式：

1. 使用命令cmd创建，必须是在工程总目录下打开cmd，并且激活虚拟环境

`python manage.py startapp appName`


2. pycharm创建工程的时候创建

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574574272832-67ffa4c6-297f-480b-9095-25050399566d.png#align=left&display=inline&height=499&name=image.png&originHeight=499&originWidth=793&size=45325&status=done&style=none&width=793)


3. 在pycharm的Tool中打开run manage.py Task使用命令创建（我采用的方式）

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574574652634-9b8c5e53-38d3-47f8-8256-b9a1ece02e19.png#align=left&display=inline&height=584&name=image.png&originHeight=584&originWidth=887&size=91756&status=done&style=none&width=887)

## 子应用的使用
### 子路由
为了保证子应用中的资源能够被使用，首先我们需要对子应用进行注册
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574577557436-91c1321f-69c5-4ba7-aca7-e52d147c0b6d.png#align=left&display=inline&height=301&name=image.png&originHeight=301&originWidth=402&size=23432&status=done&style=none&width=402)
  
然后在子应用中创建一个子路由，并且在主路由中加入对子路由的引入
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574576306057-24caa1c4-9aea-4b00-912e-f9512b7f963d.png#align=left&display=inline&height=526&name=image.png&originHeight=526&originWidth=1207&size=110976&status=done&style=none&width=1207)

验证路由配置是否正确
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574578846314-7b4289c7-38e1-4fae-90fd-456e22efaec6.png#align=left&display=inline&height=664&name=image.png&originHeight=664&originWidth=1352&size=147817&status=done&style=none&width=1352)

### 子静态系统

1. 在子应用的目录下创建一个static的目录，在该目录下创建与子应用同名的目录用来存放静态文件（CSS、JS、image等）

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574576967184-5ad99926-79ea-478e-98a1-cbeb129e460b.png#align=left&display=inline&height=522&name=image.png&originHeight=522&originWidth=218&size=23260&status=done&style=none&width=218)

2. 对静态文件进行收集，必须先保证子应用已经注册，首先在工程目录下创建一个static目录，第一步注释掉之前的静态文件的配置STATICFILES_DIRS（有冲突），第二步添加静态文件收集配置，第三步收集完成后还原配置文件

      ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574580874246-4ab5327f-a356-4932-9f30-89ab3a4a6a90.png#align=left&display=inline&height=518&name=image.png&originHeight=518&originWidth=928&size=83493&status=done&style=none&width=928)

### 子模板系统
在子应用的目录下创建一个templates的目录，在该目录下创建与子应用同名的目录用来存放模板
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574767537033-c3469d3c-74ef-4314-b283-10b6375046e6.png#align=left&display=inline&height=203&name=image.png&originHeight=203&originWidth=207&size=10232&status=done&style=none&width=207)

#### 模板继承

- 首先创建base.html文件，将模板中所有的公共部分放入这里
- 修改静态文件路径  CTRL+R 可以检索所有进行同时修改
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769778957-4d508323-6839-4ef2-9514-949a61640419.png#align=left&display=inline&height=166&name=image.png&originHeight=166&originWidth=677&size=23345&status=done&style=none&width=677)

- 添加块
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769849887-ad0f0a00-9a53-4db4-b659-f69e956c34be.png#align=left&display=inline&height=90&name=image.png&originHeight=90&originWidth=578&size=6359&status=done&style=none&width=578)
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769869585-35c9d88b-a363-4d22-9cc0-de653425acf5.png#align=left&display=inline&height=92&name=image.png&originHeight=92&originWidth=503&size=5332&status=done&style=none&width=503)
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769892139-84948150-667c-4796-be91-58de5caf0744.png#align=left&display=inline&height=116&name=image.png&originHeight=116&originWidth=513&size=7203&status=done&style=none&width=513)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769917685-ce571f56-5894-4221-9ce0-b997165916f4.png#align=left&display=inline&height=88&name=image.png&originHeight=88&originWidth=542&size=5585&status=done&style=none&width=542)


- 字模板继承父模板，并且打开对应的块添加上字模板独有的内容
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574770420290-4778f09f-a1a7-4f33-acbc-09eea548a262.png#align=left&display=inline&height=368&name=image.png&originHeight=368&originWidth=615&size=30740&status=done&style=none&width=615)

- 之后将每个模板页面都修改好



# ORM的配置和使用

## 配置

### 安装数据库

1. 下载社区版数据库   [mysql-installer](https://dev.mysql.com/downloads/file/?id=489911)
1. 安装数据库   [安装卸载教程](https://www.cnblogs.com/wcwnina/p/9302393.html)
1. 安装可视化工具   Navicat


### Django中配置mysql

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574593120706-98437362-f60a-4f96-b3a5-49a33d62a570.png#align=left&display=inline&height=310&name=image.png&originHeight=310&originWidth=517&size=22520&status=done&style=none&width=517)


### 在数据库中创建blog库

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574777670090-e08c7226-94f7-454c-a9bd-eceb83119f74.png#align=left&display=inline&height=142&name=image.png&originHeight=142&originWidth=671&size=13590&status=done&style=none&width=671)


### 安装pymysql

```python
pip install pymysql
```


### 再次启动项目

当我们再次启动项目时，发现项目启动失败，发生第一个报错信息：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574777798877-f4353a86-a4fc-461a-9736-c1a5092f719c.png#align=left&display=inline&height=109&name=image.png&originHeight=109&originWidth=788&size=10157&status=done&style=none&width=788)
     
原因是：
Django默认使用Python2版本的数据库模块（MySQLdb），而我们使用的               Python3版本使用的是pymysql模块。
解决方案：
在项目的主目录的init.py文件中增加：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778076194-d3202c8e-2c07-4f77-9c1a-af13cdae12c6.png#align=left&display=inline&height=177&name=image.png&originHeight=177&originWidth=675&size=22660&status=done&style=none&width=675)

当我们第二次重新启动项目时，发现项目还是启动失败，发生第二个报错信息：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778212312-82abd2f1-6693-4458-af59-e065eb6e5c46.png#align=left&display=inline&height=142&name=image.png&originHeight=142&originWidth=1133&size=22043&status=done&style=none&width=1133)

原因是：
Django默认检测pymysql版本。
解决方案：
修改源码，找到对应的地方，注释掉相关的判断即可：
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778417090-5d448faf-55af-4091-857a-033a09f7e9db.png#align=left&display=inline&height=589&name=image.png&originHeight=589&originWidth=1312&size=124071&status=done&style=none&width=1312)
当我们第三次重新启动项目时，发现项目还是启动失败，发生第三个报错信息：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778504643-779a57a3-1960-495d-9116-d772e9bd1ff0.png#align=left&display=inline&height=151&name=image.png&originHeight=151&originWidth=988&size=18474&status=done&style=none&width=988)

原因是：
Python3中string没有decode方法，只有encode方法
解决方案：
找到报错的地方，将decode改为encode()即可：
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778682676-5ca6d086-5cf8-4ca3-b9b5-6a7fa8dc2e50.png#align=left&display=inline&height=609&name=image.png&originHeight=609&originWidth=1163&size=116937&status=done&style=none&width=1163)
之后项目就可以启动成功了！

## 使用

### 创建模型
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574854484941-09c5c102-6fec-43ef-b112-5444eb180f76.png#align=left&display=inline&height=416&name=image.png&originHeight=438&originWidth=785&size=38505&status=done&style=none&width=746)

### 数据迁移

1. 在数据迁移之前，检测相关配置是否正确

```python
python manage.py check
```

2. 生成迁移文件

是将模型中的改动，生成相对应修改文件

```python
python manage.py makemigrations
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574854793840-0805bfaf-2053-4e14-8531-b1dc9de8588b.png#align=left&display=inline&height=144&name=image.png&originHeight=144&originWidth=1020&size=16412&status=done&style=none&width=1020)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574854892206-1be713aa-ab7a-400c-9474-762a55fad5eb.png#align=left&display=inline&height=325&name=image.png&originHeight=325&originWidth=281&size=15291&status=done&style=none&width=281)

3. 执行迁移文件

将迁移文件执行，在数据库的表中做相对应的修改和生成表结构

```python
python manage.py migrate
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574855011451-23c82a9c-31c3-4f51-92c1-cce5b2fe4fa1.png#align=left&display=inline&height=286&name=image.png&originHeight=286&originWidth=1079&size=34797&status=done&style=none&width=1079)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574855076644-4f871d2c-0df4-49c6-9046-daa2cedf18ae.png#align=left&display=inline&height=280&name=image.png&originHeight=280&originWidth=595&size=25299&status=done&style=none&width=595)

### 站点管理

1. 后台站点管理，首先得创建超级用户



```python
python manage.py createsuperuser
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574855490908-3aabdd4e-ef5c-4b75-b624-5c57fef0cb24.png#align=left&display=inline&height=283&name=image.png&originHeight=283&originWidth=1046&size=38221&status=done&style=none&width=1046)

2. 注册模型类到站点管理

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574855755012-34762077-790c-4640-ab7f-ee5a99224bf7.png#align=left&display=inline&height=467&name=image.png&originHeight=467&originWidth=819&size=52776&status=done&style=none&width=819)

启动项目，在浏览器输入下列地址，就可以看到Django提供的后台管理系统：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574855904116-e52f20ea-190e-4913-b67a-e6968cfc4db2.png#align=left&display=inline&height=460&name=image.png&originHeight=460&originWidth=1141&size=46056&status=done&style=none&width=1141)

### 修改表结构，添加媒体文件

因为我们要上传图片，还有其他的媒体文件（音频、视频、图片等），将这些文件上传到服务器需要下面两个东西：

1. 需要有文件处理的模块PIL（Python2版本的名称），我们使用的是Python3，Python3的文件处理模块叫做 pillow ，作用是处理图片，参与了人工智能
1. 需要文件存储的位置

安装pillow：

```python
pip install pillow
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574858449607-6fda951b-134a-4f44-ba30-87f96123f45b.png#align=left&display=inline&height=295&name=image.png&originHeight=295&originWidth=1110&size=41975&status=done&style=none&width=1110)

在settings中添加配置：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574858738517-e14a6b08-be2e-4546-bd34-113759cbce87.png#align=left&display=inline&height=529&name=image.png&originHeight=529&originWidth=770&size=82500&status=done&style=none&width=770)

修改模型并进行数据迁移：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574859379660-c6c07f60-ea2c-4bd2-8713-eb107a231ca7.png#align=left&display=inline&height=408&name=image.png&originHeight=408&originWidth=848&size=52599&status=done&style=none&width=848)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574859625366-843abf29-b214-43d2-936d-58dd782c7cdd.png#align=left&display=inline&height=455&name=image.png&originHeight=455&originWidth=1212&size=62102&status=done&style=none&width=1212)

### 在后台中添加数据

上传完数据后，会发现在static目录下自动生成了上传的images文件夹，里面是我们上传的图片文件

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574857189326-698940c7-be81-4b03-9c76-b6581e291328.png#align=left&display=inline&height=449&name=image.png&originHeight=449&originWidth=883&size=33423&status=done&style=none&width=883)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574860066357-7511d3c3-4e66-42e1-bcbc-f6f91cdd9fd4.png#align=left&display=inline&height=281&name=image.png&originHeight=281&originWidth=341&size=15441&status=done&style=none&width=341)

### 修改模板内容

刷新页面，我们就能从数据库拿到数据了:

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574860309417-81d1ab81-c567-44f9-9a49-44f07892c628.png#align=left&display=inline&height=588&name=image.png&originHeight=588&originWidth=1331&size=127506&status=done&style=none&width=1331)


到这里，网站的基本配置已经完成了，如果到后面还有需要的地方，我们在配置，接下来我们将正式进入网站的建设

# 正式进入博客

## 模型创建

科目类型与文章属于一对多关系，所以在文章表中创建一个类型外键，迁移完数据之后，在admin中注册该类到站点管理：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574863244784-0379368e-926e-4f10-be47-833034faefc0.png#align=left&display=inline&height=474&name=image.png&originHeight=474&originWidth=940&size=75742&status=done&style=none&width=940)

## 富文本使用

方便我们在后台写文章，我们选择使用富文本编辑器CKeditor，它是一种和Django结合的富文本编辑器

### 安装富文本编辑器

```python
pip install django-ckeditor
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574863792448-91e3de80-6b09-4cf0-b76f-93f5e9945130.png#align=left&display=inline&height=403&name=image.png&originHeight=403&originWidth=1007&size=60363&status=done&style=none&width=1007)


### 配置富文本

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574864267829-d831b40b-68c5-4948-a434-bf265e6c07b8.png#align=left&display=inline&height=518&name=image.png&originHeight=518&originWidth=914&size=70246&status=done&style=none&width=914)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574864360048-728616c4-244e-4268-80d8-742708b98230.png#align=left&display=inline&height=421&name=image.png&originHeight=421&originWidth=748&size=44240&status=done&style=none&width=748)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574864504726-99cb3857-a313-47c3-b385-cda59eec2ccd.png#align=left&display=inline&height=551&name=image.png&originHeight=551&originWidth=884&size=78074&status=done&style=none&width=884)


### 模型中使用

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574864609753-fa41d981-7c08-4669-9026-5215280c5a66.png#align=left&display=inline&height=271&name=image.png&originHeight=271&originWidth=968&size=41960&status=done&style=none&width=968)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574865036951-34ee4fcf-e3d1-4c5f-8be1-89da832c41a8.png#align=left&display=inline&height=443&name=image.png&originHeight=443&originWidth=1014&size=77888&status=done&style=none&width=1014)

### 站点管理中使用富文本

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574865129835-1183ed87-02b0-4570-a32e-5ded4e98f295.png#align=left&display=inline&height=638&name=image.png&originHeight=638&originWidth=1137&size=37324&status=done&style=none&width=1137)

## 确定思路：

1. 首页的数据根据文章创建时间排序显示
1. 点击首页中的文章类型log跳转至list学无止境页面，显示该文章类型的所有数据
1. 点击文章的图片标题和阅读全文跳转至info文章详情页面，显示文章内容的详细内容


## 修改首页

视图：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574948070161-7bbbd56b-2a24-4db8-9458-878ef26b704d.png#align=left&display=inline&height=238&name=image.png&originHeight=238&originWidth=609&size=22767&status=done&style=none&width=609)

模板：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574948610846-e998a8de-f015-432e-a7e6-b62b0a7841e5.png#align=left&display=inline&height=412&name=image.png&originHeight=412&originWidth=778&size=38604&status=done&style=none&width=778)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574948204028-a88e01e2-5c4c-4866-9972-d7948891daba.png#align=left&display=inline&height=606&name=image.png&originHeight=606&originWidth=1229&size=89585&status=done&style=none&width=1229)

## 修改实现学无止境list页面

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574940996242-d74752c0-386c-429b-b3b4-725e76a0d2d7.png#align=left&display=inline&height=181&name=image.png&originHeight=181&originWidth=687&size=17648&status=done&style=none&width=687)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574941071314-930efcbb-1e02-4d17-aefb-ec720890d60a.png#align=left&display=inline&height=573&name=image.png&originHeight=573&originWidth=1031&size=73282&status=done&style=none&width=1031)

## 增加文章详情页面

路由：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574944124365-f80c80e6-2818-47ac-b855-fb2432f7ad59.png#align=left&display=inline&height=298&name=image.png&originHeight=298&originWidth=354&size=21057&status=done&style=none&width=354)

视图：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574944186569-0dac8866-1319-4cae-9b19-a9d649e52cab.png#align=left&display=inline&height=229&name=image.png&originHeight=229&originWidth=569&size=21833&status=done&style=none&width=569)

模板：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574944408429-e85ec909-bace-4206-bbc4-0c9e65d336e9.png#align=left&display=inline&height=627&name=image.png&originHeight=627&originWidth=1129&size=107921&status=done&style=none&width=1129)

## 添加数据

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574949584407-f24535de-8f06-498f-a9b6-a9f7ea32c007.png#align=left&display=inline&height=395&name=image.png&originHeight=395&originWidth=527&size=42231&status=done&style=none&width=527)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574949600334-0377ba85-f368-49a4-bcfc-ccf2ac37efc4.png#align=left&display=inline&height=289&name=image.png&originHeight=289&originWidth=486&size=25426&status=done&style=none&width=486)



## 实现分页

Django中封装了分页器：paginator
首先，导包

```python
from django.core.paginator import Paginator
```

视图：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574952042170-3257cf02-3796-4104-b1e5-c5ef701729f8.png#align=left&display=inline&height=384&name=image.png&originHeight=384&originWidth=733&size=45778&status=done&style=none&width=733)

模板：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574952098331-c30c0f2c-8167-4b58-9382-ddf6f1b71505.png#align=left&display=inline&height=407&name=image.png&originHeight=407&originWidth=924&size=44116&status=done&style=none&width=924)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574952075918-425d44e0-e298-4262-9ab6-f74438401a16.png#align=left&display=inline&height=180&name=image.png&originHeight=180&originWidth=1064&size=22712&status=done&style=none&width=1064)


## 完善分页

视图：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1575101231441-ea89a65e-fe25-4939-a120-843d61dc8771.png#align=left&display=inline&height=516&name=image.png&originHeight=516&originWidth=1164&size=123783&status=done&style=none&width=1164)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1575101261784-c4367691-6b7a-4ff9-b3e5-0433db414c1d.png#align=left&display=inline&height=273&name=image.png&originHeight=273&originWidth=1094&size=30646&status=done&style=none&width=1094)

模板：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1575101496806-0c4aee25-105c-423e-abe1-cb7b78ab5874.png#align=left&display=inline&height=581&name=image.png&originHeight=581&originWidth=1259&size=117905&status=done&style=none&width=1259)

## 首页优化




![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1575182084874-1c0422da-1a88-4717-aaba-b50e8782328b.png#align=left&display=inline&height=288&name=image.png&originHeight=288&originWidth=931&size=34572&status=done&style=none&width=931)

### 完成首页上拉加载更多

视图(api):

```python
def article_api(request):
    page = int(request.GET.get('page'))
    start = (int(page) - 1) * 12
    end = start + 12
    article = Article.objects.order_by('-art_date').all()[start:end]

    res = []
    for article in article:
        img = str(article.art_img)
        date = str(article.art_date)
        # print(date)
        res.append({
            "id": article.id,
            "art_img": img,
            "art_title": article.art_title,
            "art_description": article.art_description,
            "art_type_id": article.art_type_id,
            "art_type": article.art_type.course_name,
            "art_date": date,
            "art_click": article.art_click,
        })
    result = dict(res=res)

    return JsonResponse(result)
```

前端：

```html
{% verbatim %}
<div class="blogs" id="wrapper">

  <div v-for="art in article">

    <li class="outpart">
      <span class="blogpic" v-model=art>
        <a :href="'/myblog/info/?id='+art.id" class="by_click">
          <img :src="'/static/'+ art.art_img"></a>
      </span>
      <h3 class="blogtitle">
        <a :href="'/myblog/info/?id='+art.id" class="by_click">{{ art.art_title }}</a>
      </h3>
      <div class="bloginfo" v-html="art.art_description">
      </div>
      <div class="autor">
        <span class="lm">
          <a :href="'/myblog/list/?type_id='+art.art_type_id+'&art_id='+art.id"
             :title=art.art_type class="classname">{{ art.art_type }}</a>
        </span>
        <span class="dtime">{{ art.art_date }}</span>
        <span class="viewnum">浏览（<a :href="'/myblog/info/?id='+art.id">{{ art.art_click }}</a>）</span>
        <span class="readmore"><a :href="'/myblog/info/?id='+art.id" class="by_click">阅读原文</a></span>
      </div>
    </li>
  </div>
</div>
{% endverbatim %}
```

```javascript
<script>
        Vue.use(VueResource);
        new Vue({
                el: "#wrapper",
                data: {
                    article: [],
                    page: 1,
                    no_data: false,
                },
                created: function () {
                    url = "/myblog/article_api/?page=" + this.page,
                        this.$http.get(url).then(
                            function (data) {
                                article = data.data.res;
                                this.article = article;
                                this.page += 1;
                            }
                        );
                    window.addEventListener("scroll", this.onscroll)
                },
                methods: {
                    onscroll() {
                        // 计算当前文档的总高度
                       let dh = document.querySelector('body').clientHeight
                        // 浏览器窗口的高度
                        // 视窗高度
                        let outerHeight = document.documentElement.clientHeight;
                        // 滚动高度
                        let scrollTop = document.documentElement.scrollTop;
                        {#console.log(innerHeight, outerHeight, scrollTop)#}
                        if (outerHeight + scrollTop >= dh) {
                            console.log(11111111)
                            if (this.no_data === true) {
                                return false
                            }
                            url = "/myblog/article_api/?page=" + this.page;
                            this.$http.get(url).then(
                                function (data) {
                                    if (data.data.res){
                                        article = data.data.res;
                                        this.article = this.article.concat(article)
                                        console.log(this.article)
                                        this.page = this.page + 1;
                                    }else {
                                        this.no_data = true;
                                    }
                                }
                            ),500
                        }
                    }
                }
            }
        )
    </script>
```

### 添加回到顶部按钮

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1576133118438-61507fad-1e40-47e6-99ff-b3d5d3038361.png#align=left&display=inline&height=502&name=image.png&originHeight=502&originWidth=932&size=45627&status=done&style=none&width=932)


## 所有页面的优化

之后就是对所有的其他一些页面进行优化和扩展，让网站的功能更加齐全
### 详情页

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1576198030777-a6fa7dbb-ad38-471d-afa4-cacebc4103e3.png#align=left&display=inline&height=630&name=image.png&originHeight=630&originWidth=953&size=66987&status=done&style=none&width=953)
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1576197984580-5f9c3067-97ba-41ee-8f86-caccaa53be16.png#align=left&display=inline&height=510&name=image.png&originHeight=510&originWidth=1061&size=69597&status=done&style=none&width=1061)
