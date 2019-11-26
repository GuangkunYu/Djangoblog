# 基于Django搭建的个人网站



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
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574759216656-d830e3a2-8539-4896-8ce7-9cced6bf1ae5.png#align=left&display=inline&height=595&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=595&originWidth=440&search=OpenFileorProject%20Hidepath%20CAL%20D%3A%20EL%20Chromedownload%20Cloud%20documents%20downloads%20GitHub%20Djangoblog%20MyBlog%20idea%20MyBlog%20MyBlogApp%20static%20db.sqlite3%20managepy%20%E5%B1%B1%E4%B8%8E%20egitattributes%20README.md%20MySOLdata%20%E4%B8%AD%E5%85%AC%20Draganddropafleinothespaceabovetoquickylocateitinthete%20Cancel%20OK&size=35433&status=done&width=440)

- 选择编译环境为我们最初创建的虚拟环境myenvs
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574759317743-dd4df15c-cf07-4757-807c-bf9cfd23e1cc.png#align=left&display=inline&height=714&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=714&originWidth=1028&search=K%20Settings%20AyBIOGPROjcTINTErPrETEr%20%E5%B9%BAForcurrentproject%20ProjectInterpreteR%20Python3.5%28MyBlog%29Dinstadeveoplancondnvnee%20APPEARANcE%26BEHAVior%20Keymap%20dpython3.5%28MyBlog%29D%3Ainstaldeveloplancondlenvmepythonexe%20Pac%20EditOR%20aPython3.6D%3Ainstallldeveloplanacondapythonexe%20certif%20plugins%20ShowAlI...%20%E7%9C%81%20VersionConTroL%203.5.2%203.8.0%20python%200%20Background%2040.2.0%2042.0.1%20setuptools%20Changelists%20%E5%B1%80%20o%20ve%2014.1%20CommitDialog%2014.16.27012%2014.16.27012%20v52015run%20Confirmation%20%E5%92%B1%200.31.1%200.33.6%20wheel%20FiIleStatusColors%200.2%20wincertstore%20GitHub%20lgnoredFiles%20lssueNavigation%20Shelf%20%E5%9B%9B%E5%9B%9B%E4%B8%96%E5%95%A4%20CVS%20Git%20Mercural%20Perforce%20Subversion%20Proicct%3AMyBlog%20Projectlnterpreter%20ProjectStructure%20BuILDEXECUTIONDEPlOyMENT%20LIONNEISNAESHCRAMAUMIANLE%20OK%20Cancel%20Apply%20oncontror%20TerminartryinonConsore&size=84062&status=done&width=1028)
- 

- 启动服务进行验证，如果成功，在浏览器中输入127.0.0.1:8000会出现小火箭。
- 进行基本的配置修改
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574573200543-4bd47fd0-af17-4ff0-8b77-c35dde44214a.png#align=left&display=inline&height=385&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=385&originWidth=610&search=%23Internationalization%20%23https%3A%2F%2Fdocsdjangoproject.com%2Fen%2F22%20%E8%AF%AD%E8%A8%80%E9%85%8D%E7%BD%AE%20%E4%BD%BF%E7%94%A8%E4%B8%AD%E6%96%87%20LANGUAGECODE%20zh-haNS%27%20%23%E6%97%B6%E5%8C%BA%E9%85%8D%E7%BD%AE%20Asia%2FShanghai%27%20%E4%BD%BF%E7%94%A8%E4%B8%9C%E5%85%AB%E5%8C%BA%20TIMEZONE%20%3A%E7%BF%BB%E8%AF%91%E7%B3%BB%E7%BB%9F%20USEII8NTruE%20%E6%95%B0%E6%8D%AE%E6%9C%AC%E5%9C%B0%E5%8C%96%E9%85%8D%E7%BD%AE%20USELION%E4%BA%8CTrue%20%23%E6%98%AF%E5%90%A6%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20%23True%E4%BD%BF%E7%94%A8Django%E9%BB%98%E8%AE%A4%E6%97%B6%E5%8C%BA%2C%E5%86%85%E7%BD%AE%E6%97%B6%E5%8C%BA%20%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20%23False%20%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20USETZ%20False&size=45670&status=done&width=610)




# 子应用创建与使用


考虑到网站的健壮性和可移植性，我们将使用子应用。方便管理。

## 创建子应用


三种方式：

1. 使用命令cmd创建，必须是在工程总目录下打开cmd，并且激活虚拟环境

`python manage.py startapp appName`


2. pycharm创建工程的时候创建

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574574272832-67ffa4c6-297f-480b-9095-25050399566d.png#align=left&display=inline&height=499&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=499&originWidth=793&search=BE%20NewProject%20PurePython%20C%3AUserslygkPycharmProjectsluntitled%20Location%3A%20Django%20FIasK%20%3FProjectlnterpreterNewVirtualenvenvironment%20GoogleAppEngine%20MoReSettings%20Pyramid%20Web2py%20Templatelanguage%3A%20Django%20dScientific%20Templatesfolder%3A%20templates%20ANGulaRCLI%20AngularJS%20Applicationname%3A%20Bootstrap%20EnableDjangoadmin%20Foundation%20HTML5Boilerplate%20ReactAPPp%20ReactNative%20Create&size=45325&status=done&width=793)


3. 在pycharm的Tool中打开run manage.py Task使用命令创建（我采用的方式）

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574574652634-9b8c5e53-38d3-47f8-8256-b9a1ece02e19.png#align=left&display=inline&height=584&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=584&originWidth=887&search=MyBlog%5BEAdocumentsiGitHubiDjangoblogBlog%29ycharm%20RefactorR%20FileEditViewNavigateCo%20Code%20Iools%20SWindow%20Help%20IVBIOGPMyBIOG%20Tasks%26Contexts%20IDEScriptingConsole%20%E4%B8%83%20AnalyzeStackTrace...%20MyBlogE%3ADocumentsGItH%20%E7%B2%BECaptureMemorySnapshot%20DMyBlog%20init_.py%20PythonConsole...%20Ctrl%2BAlt%2BR%20RunmanagePyTasK...%20settingSPY%20ShowCodeCoverageData%20Ctrl%2BAlt%2BF6%20urls.PY%20VimEmulator%20wsgi.py%20DMyBlogAPP%20Deployment%20%3Fdb.%20lite3%20ADDNewBas%20man%20gepy%20HTTPCIAnt%20EverywhereDoubleShift%20%E5%B1%B1External%20ibraries%20tSHsession...%20ScratchesandConsoles%20Vagolnt%20FileCtrl%2BShift%2BN%20PYO%20YOpCProfilesnapshot%20managepy%40myBlo%20Blog%20%40MyB1og%20StartappMyBlogApp%20%22D%3Ainstalildeve%20ycharm2018.3.5binunnerw64.exeD%3Ainstaldevelopanacon%20TrackingLilebyfolderpa%20pattern%3Ami%20Followingfileswereaffecte%20E%3AdocumentsGitHubDjangoblogMylogMlogati%20enanJis%20%E5%8F%A3x%20Processfinishedwithexitcodeo&size=91756&status=done&width=887)

## 子应用的使用
### 子路由
为了保证子应用中的资源能够被使用，首先我们需要对子应用进行注册
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574577557436-91c1321f-69c5-4ba7-aca7-e52d147c0b6d.png#align=left&display=inline&height=301&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=301&originWidth=402&search=%23Applicationdefinition%20%E6%B3%A8%E5%86%8CAPP%E7%9A%84%20%E6%B3%A8%E5%86%8C%E5%AD%90%E5%BA%94%E7%94%A8%20INSTALLEDAPPS%20django.contrib.admin%2C%20django.contrib.auth%2C%20diango.contrib.contenttypes%20django.contrib.sessions%2C%20django.contrib.messages%27%2C%20%27django.contrib.staticfiles%20MyBlogApp%27&size=23432&status=done&width=402)
  
然后在子应用中创建一个子路由，并且在主路由中加入对子路由的引入
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574576306057-24caa1c4-9aea-4b00-912e-f9512b7f963d.png#align=left&display=inline&height=526&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=526&originWidth=1207&search=FiIle%20NaviqATe%20Edit%20View%20HelP%20MyBloG%20MyBloGApp%20rls.py%20jMyBIog%20MyBloglurls.py%20Projec%20MyBlogAppiurispyx%20MyBloglurls.py%202alold%20MyBlo%20BlogENDocumentsIGILH1%20fromdjangourls%20rtfromappimportVviews%20Simportupat%20MyBloG%202.AddaURLtourlpatterns%3Apathe%2Cviews%2Chomenm%20init_py%20CIASS-BaSEDVieWs%201.Addanimport%3Afromother_app.viesimportHome%20wsqipy%202.AddaULtourlpatterns%3Apathe%2CHomeasieo%2C%20AMyBloGAPP%20IncIudinganotherURlconf%20migrations%20I.Importtheincludefunction%3Afromdjangourlsimp%20Dtemplates%20_init_py%202AddaURLtourlpatterns%3Apath%28blog%2Cincludeb%2014%20admin.py%2015%20apPs.py%20romdjango.contribimportadmin%2016%20modclspy%20%E7%99%BDfromdjango.urlsimportpathincude%20tests.py%2019%20%E4%B8%80urlpatterns%20db.sglite3%20pathCadmin%2F%2Cadminsite.urls%29%20manage.py%20%E5%B1%B1ExternalLibraries%20%2Cinclude%28MyBlogApp.urls%29%29%20path%28%20h%28myblogapp%2F%2Cinc%20ScratchesandConsoles&size=110976&status=done&width=1207)

验证路由配置是否正确
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574578846314-7b4289c7-38e1-4fae-90fd-456e22efaec6.png#align=left&display=inline&height=664&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=664&originWidth=1352&search=DMYBLOGAPP%20MyBlog%20MyBlog%20%E5%AE%9D%20Git%3A%20%E5%AD%90%E8%B7%AF%E7%94%B1%20%E4%B8%BB%E8%B7%AF%E7%94%B1%20%E8%A7%86%E5%9B%BE%20IADDANIPORFROWr%2BVIews%20Gfromdjanzo.urlsimportpath%20Qfromdiango%2Cshortcutsimporede%202AddauRLtourlparterns%3Apatheviews.ho%20Qfromdjango.httpimportHtpReose%20fromMyBlorAppviewsimpo%20Class-BasedViews%20I.Addanimport%3Afrowother_appviesimport%20Purlpatterns%202.AddauLtourIpatternspath%20pathC%20IncIudinganothertRLconf%20efdemo%28request%29%3A%20I.Importtheincludefunction%3Afrowdjang.%20returnHttpResponse%28%E8%B7%AF%E5%B1%B1%E9%85%8D%E6%99%BA%E6%AD%A3%E7%A1%AE%27%29%202.AddaLRLtourlpatterns%3Apat%2016%20omdjango.contribimportadmin%20fromdjango.urlsimportath%2Cincue%20urlpatterns%20pathCadmin%2F%20P%2Cadmin.siteurls%29%20pathCmyblogapp%2FincludeCMyBlogApp.url%20127.0.0.1%3A8000%2Fmybloaooo%2Fdemo%2F%20%E6%97%A0%E7%97%98%E6%A9%99%E5%BC%8F%20%E5%8F%91%E9%80%81%E8%AF%97%E6%B1%82%20%E8%B7%AF%E7%94%B1%E9%85%8D%E4%B8%93%E6%AD%A3%E7%A1%AE&size=147817&status=done&width=1352)

### 子静态系统

1. 在子应用的目录下创建一个static的目录，在该目录下创建与子应用同名的目录用来存放静态文件（CSS、JS、image等）

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574576967184-5ad99926-79ea-478e-98a1-cbeb129e460b.png#align=left&display=inline&height=522&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=522&originWidth=218&search=Project%20MyBlogEdocumentsGitHub%29%20.MyBlog%20J_init_-py%20settings.py%20urlspy%20wsgi.py%20.MyBlogApP%20migrations%20static%20myblogapp%20Css%20images%20templates%20_init_py%20adminpy%20appspy%20modelspy%20urls.py%20viewspy%20%3Fdb.sqlite%20managepy&size=23260&status=done&width=218)

2. 对静态文件进行收集，必须先保证子应用已经注册，首先在工程目录下创建一个static目录，第一步注释掉之前的静态文件的配置STATICFILES_DIRS（有冲突），第二步添加静态文件收集配置，第三步收集完成后还原配置文件

      ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574580874246-4ab5327f-a356-4932-9f30-89ab3a4a6a90.png#align=left&display=inline&height=518&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=518&originWidth=928&search=urls.py%20Project%20settings.py%20MYBloGEDOCUMENTsLGItHubIDjangoble%20%23%E6%95%B0%E6%8D%AE%E6%9C%AC%E5%9C%B0%E5%8C%96%E9%85%8D%E7%BD%AE%20119%20MyBlog%20120%20USELION-True%20init_-Py%20%E7%99%BD%E6%98%AF%E5%90%A6%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20settings.py%20urls.Py%20%23True%E4%BD%BF%E7%94%A8Django%E9%BB%98%E8%AE%A4%E6%97%B6%E5%8C%BA%2C%E5%86%85%E7%BD%AE%E6%97%B6%E5%8C%BA%20wsgipy%20%23False%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20DMyBlogAPP%20USETZFaIsE%20124%20static%20admin%20125%20myblogapp%20126%20Staticfiles%28CSS%2CJavaScript%2CImages%29%20css%20https%3A%2F%2Fdocs.djangoproject.come%2F2.%2Fwaicfe%20127%20images%20%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%E9%85%8D%E7%BD%AE%20128%20djs%20db.sglite3%20STATICURL-%27%2Fstatic%2F%202manage.py%20STATICFILESDIRS-%28%20130%20%E5%B1%B1ExternalLibraries%20131%20os.path.join%28BASEDIR%27sTati%29%20ScratchesandConsoles%20132%20%23%E6%94%B6%E9%9B%86%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%20133%20134%20STATICROOT%20OOTospath.join%28BASEDIRsTtic%29%20135&size=83493&status=done&width=928)

### 子模板系统
在子应用的目录下创建一个templates的目录，在该目录下创建与子应用同名的目录用来存放模板
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574767537033-c3469d3c-74ef-4314-b283-10b6375046e6.png#align=left&display=inline&height=203&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=203&originWidth=207&search=Project%20BlogE%3AdocumentsGItHub%20Blog%20MyBlog%20imigrations%20static%20templates%20Amyblog%20base.html&size=10232&status=done&width=207)

#### 模板继承

- 首先创建base.html文件，将模板中所有的公共部分放入这里
- 修改静态文件路径  CTRL+R 可以检索所有进行同时修改
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769778957-4d508323-6839-4ef2-9514-949a61640419.png#align=left&display=inline&height=166&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=166&originWidth=677&search=%3Clinkhref%22%20E%22static%2Fmyblog.css%2Fbase.cssrel-%27s%20%3Clinkhref-%22%20static%2Fmyblog%2Fcss%2Findex.css%22rel-%27stye%20%3Clinkhref-%22%20Vstatic%2Fmyblog%2Fcss%2Fm.css%22re%20s%22rel-%27stylesheet%22%3E%20%3C%21--%5BifltIE9%5D7%20%3Cscriptsrc-%22%20Vstatic%2Fmyblog%2F%20is%2Fmodernizrjs%27script%20%3C%21%5Bendif%5D--%3E&size=23345&status=done&width=677)

- 添加块
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769849887-ad0f0a00-9a53-4db4-b659-f69e956c34be.png#align=left&display=inline&height=90&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=90&originWidth=578&search=%3Ctitle2f%25blocktitle%25%20ckx%3Ctitle%29%20endb1ock&size=6359&status=done&width=578)
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769869585-35c9d88b-a363-4d22-9cc0-de653425acf5.png#align=left&display=inline&height=92&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=92&originWidth=503&search=61ockstyle%25%20endb1ock%25&size=5332&status=done&width=503)
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769892139-84948150-667c-4796-be91-58de5caf0744.png#align=left&display=inline&height=116&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=116&originWidth=513&search=%E5%86%85%E5%AE%B9%23%20IBb1ockcontentY%20Bendb1ock%E5%B7%9E&size=7203&status=done&width=513)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574769917685-ce571f56-5894-4221-9ce0-b997165916f4.png#align=left&display=inline&height=88&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=88&originWidth=542&search=%25%20b1ock%20script%20Bendblock%25&size=5585&status=done&width=542)


- 字模板继承父模板，并且打开对应的块添加上字模板独有的内容
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574770420290-4778f09f-a1a7-4f33-acbc-09eea548a262.png#align=left&display=inline&height=368&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=368&originWidth=615&search=views.py%20index.htmlx%20urls.pY%20base.html%20tingsPy%20%27myblog%2Fbase.html%27%20%E7%82%92%20extends%20WfAb1ocktitle%E9%AA%86%20%E5%8D%9A%E5%AE%A2%E9%A6%96%E9%A1%B5%20endb1ock%E5%A5%96%20%E9%AA%91%20ckcontent%20kdivclass-picshow%20%3Carticle%20%3Cdivclass-%27blank%27%2F%2Fdiv%29%20Vendb1ock%E5%88%AB&size=30740&status=done&width=615)


- 之后将每个模板页面都修改好



# ORM的配置和使用

## 配置

### 安装数据库

1. 下载社区版数据库   [mysql-installer](https://dev.mysql.com/downloads/file/?id=489911)
1. 安装数据库   [安装卸载教程](https://www.cnblogs.com/wcwnina/p/9302393.html)
1. 安装可视化工具   Navicat


### Django中配置mysql

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574593120706-98437362-f60a-4f96-b3a5-49a33d62a570.png#align=left&display=inline&height=310&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=310&originWidth=517&search=%23MySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E9%85%8D%E7%BD%AE%20DATABASES%E4%BA%8CA%20%27default%27%3Af%20ENGINE%27%3A%27django.db.backends.mysql%20NAME%3A%27b1og%2C%20%27USER%27%3A%27root%2C%20PASSWORD%3A%27root%27%2C%20HOST%3A%27127.0.0.1%2C%20PORT%3A%273306%27%2C&size=22520&status=done&width=517)


### 在数据库中创建blog库

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574777670090-e08c7226-94f7-454c-a9bd-eceb83119f74.png#align=left&display=inline&height=142&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=142&originWidth=671&search=MySQL%20%E5%AF%B9%E8%B1%A1%20blog%20%E5%88%A0%E9%99%A4%E8%A1%A8%20%E6%96%B0%E5%BB%BA%E8%A1%A8%20%E5%AF%BC%E5%85%A5%E5%90%91%E5%AF%BC%21%20%E6%89%93%E5%BC%80%E8%A1%A8%20%E8%AE%BE%E8%AE%A1%E8%A1%A8%20%E5%AF%BC%E5%87%BA%E5%90%91%E5%AF%BC%20informationschema%20%E8%87%AA%20mysql%20performanceschema%20sys&size=13590&status=done&width=671)


### 安装pymysql

```python
pip install pymysql
```


### 再次启动项目

当我们再次启动项目时，发现项目启动失败，发生第一个报错信息：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574777798877-f4353a86-a4fc-461a-9736-c1a5092f719c.png#align=left&display=inline&height=109&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=109&originWidth=788&search=err%20from%20ErrorloadingMySQLdbmo%20django.core.exceptions%2CImproperlyConfigured%3AE%20module.%20Didyouinstal%2011mysqlclient%3F&size=10157&status=done&width=788)
     
原因是：
Django默认使用Python2版本的数据库模块（MySQLdb），而我们使用的               Python3版本使用的是pymysql模块。
解决方案：
在项目的主目录的init.py文件中增加：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778076194-d3202c8e-2c07-4f77-9c1a-af13cdae12c6.png#align=left&display=inline&height=177&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=177&originWidth=675&search=Project3-%20_init_.py%3E%20index.html%20settingSPY%20BlogEdocumentsGitHub%20tpymysq1%20importp%20Blog%20pymysql.install_asMySoLdbo%20init%20settings.Py%20urls.py%20wsgi.py%20MyBlog&size=22660&status=done&width=675)

当我们第二次重新启动项目时，发现项目还是启动失败，发生第二个报错信息：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778212312-82abd2f1-6693-4458-af59-e065eb6e5c46.png#align=left&display=inline&height=142&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=142&originWidth=1133&search=FileD%3Ainstalleelonlanacondlensmkn%20sqlNbase.pyline36in%3C%20%3Cmodule%29%20rnewerisreauired%3Ayouhave%25s%25Database._version%20raiseImproperlyConfigured%28mysqlclient1.3.weri%20django.core.exceptions.mropelyconfigured%3Amysqlclient1%20nt1.3.13ornewerisrequired%3Byouhave0.9.3&size=22043&status=done&width=1133)

原因是：
Django默认检测pymysql版本。
解决方案：
修改源码，找到对应的地方，注释掉相关的判断即可：
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778417090-5d448faf-55af-4091-857a-033a09f7e9db.png#align=left&display=inline&height=589&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=589&originWidth=1312&search=Project%20BlogE%3AdocumentlGithub%20%23isort%3Askip%20ionsimportDatabaseOperations%20rom.operationsim%20aBlog%20%23isort%3Askip%20schemaimportDatabaseSchemaditor%20_init-py%20setting5py%20From.walidationiportDatabaseaidati%20%23isort%3AskiD%20urls.py%20wsgipy%20versionDAtabase.VersioniNO%20MyBlog%20ifversion%3C%281%2C313%29%3A%20dmysqlclientL.3oeerisreouredyouheti%20raiseImproperlyConfigured%28m%20dtamplates%20Amyblog%20abouthtml%20%23MYSQLDBrETURNTIMEcOLUmSaStim%20LLelta-theyaremoreliketimedeltain%20FeLigNedandIncLudedays--andDjango%20%23termsofactualbehayiorastheyare%20Aiexpectstime%20diBlog%20returnimportmodule%25s%2Cbasebackendname%29%20p%22line126inimport_module%20FileDALinstalidevelonianacondaenensihim%20return_bootstrap.gcdimportnamelevel%3Aacka%20FileD%3AlinstaliNdevelopianacondale%20site-packagesldiangoldhlbackendsmyqbas%20figuredemysqlclient1.uae%20t1.3.13ornewerisrequired%3Byouhave0.9.3.%20ured%3Amysqlclient1%20django.corerexceptions%2CIm&size=124071&status=done&width=1312)
当我们第三次重新启动项目时，发现项目还是启动失败，发生第三个报错信息：

![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778504643-779a57a3-1960-495d-9116-d772e9bd1ff0.png#align=left&display=inline&height=151&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=151&originWidth=988&search=%E4%BA%8Cself.db.ops.%20b.opslastexecuted_queryself.cuosaram%20File%22D%3Ainstalldeveloplanacondalenvsmv%20s1iblsite-packagesdiangodbbackendssation%20querysquerydecodeerrors-replace%20trobjecthasnoattribute%27dlecode%20AttributeError%3A%27str%27object&size=18474&status=done&width=988)

原因是：
Python3中string没有decode方法，只有encode方法
解决方案：
找到报错的地方，将decode改为encode()即可：
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574778682676-5ca6d086-5cf8-4ca3-b9b5-6a7fa8dc2e50.png#align=left&display=inline&height=609&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=609&originWidth=1163&search=roject%20indexhtml%20settingspy%20initp%20operationspy%20BlogEdocUMenLSLGIHuB%20SeeMySQLDbcursorspyinthesourcedistribution%20143%20Blog%20executed%27%2CNone%20144%20query-getattrcursore%20init_py%20None%3A%20145%20settingspy%20query%20yisno%20urls.py%20146%20errors-replace%29%20ueryencode%20wsgLpy%20147%20returnguery%20MyBlog%20148%20dmigrations%20static%20149%20defnolimit%20templates%20150%20ndedbytheMySoLdocumentation%20%2A64-1%2Casrecomm%20%3Amyblog%20abouthtml%20DatabaseOparationslast%20iqueryisnotNone%20lastexecuted_queryo%20diBlog%20ifself.features.issql_autoisnull_enabled%20its-packagesldjangolutilslfunctional.ovine80%2Ci%20FileD%3Alinstallideveloplanacondalenvsmen%20in_get%20res%E4%BA%8Cinstance._dict_%5Bself.name%5DJ%E4%BA%8Cse%20nameJ%E4%B8%89self.func%28instehce%29%20FileD%3Ainstalildeveloplanacondalensensl%20enyslliblsitepackasesdianokbbackendsmu%20cursor.execute%28%27SELECT%40USQLAUTOISNULL%27%29%20te-packasesldiangoldblbackendslutilsplinXeute%20FileD%3Ainstaildeveloplanacondalensent%20sql%E4%B8%89self.db.opslastexecutedquery%28self.cursors%20ndsImvsaloperations.ovline146inlas%20Filep%3Alinstallldeveloplanacondalensmeltakae%20query%E4%BA%8Cquerydecodeerrors-rep1a%20ttributeError%3A%27strobjecthasnoattributedeco&size=116937&status=done&width=1163)
之后项目就可以启动成功了！

## 使用


