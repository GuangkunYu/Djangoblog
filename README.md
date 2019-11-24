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
- 选择编译环境为我们最初创建的虚拟环境myenvs
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

2. 对静态文件进行收集，首先在工程目录下创建一个static目录，第一步注释掉之前的静态文件的配置，第二步添加静态文件收集配置，第三步收集完成后还原配置文件

      ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574580874246-4ab5327f-a356-4932-9f30-89ab3a4a6a90.png#align=left&display=inline&height=518&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=518&originWidth=928&search=urls.py%20Project%20settings.py%20MYBloGEDOCUMENTsLGItHubIDjangoble%20%23%E6%95%B0%E6%8D%AE%E6%9C%AC%E5%9C%B0%E5%8C%96%E9%85%8D%E7%BD%AE%20119%20MyBlog%20120%20USELION-True%20init_-Py%20%E7%99%BD%E6%98%AF%E5%90%A6%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20settings.py%20urls.Py%20%23True%E4%BD%BF%E7%94%A8Django%E9%BB%98%E8%AE%A4%E6%97%B6%E5%8C%BA%2C%E5%86%85%E7%BD%AE%E6%97%B6%E5%8C%BA%20wsgipy%20%23False%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AE%9A%E7%9A%84%E6%97%B6%E5%8C%BA%20DMyBlogAPP%20USETZFaIsE%20124%20static%20admin%20125%20myblogapp%20126%20Staticfiles%28CSS%2CJavaScript%2CImages%29%20css%20https%3A%2F%2Fdocs.djangoproject.come%2F2.%2Fwaicfe%20127%20images%20%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%E9%85%8D%E7%BD%AE%20128%20djs%20db.sglite3%20STATICURL-%27%2Fstatic%2F%202manage.py%20STATICFILESDIRS-%28%20130%20%E5%B1%B1ExternalLibraries%20131%20os.path.join%28BASEDIR%27sTati%29%20ScratchesandConsoles%20132%20%23%E6%94%B6%E9%9B%86%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%20133%20134%20STATICROOT%20OOTospath.join%28BASEDIRsTtic%29%20135&size=83493&status=done&width=928)

### 子模板系统
在子应用的目录下创建一个templates的目录，在该目录下创建与子应用同名的目录用来存放模板
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574576838534-7168db32-c492-4d2c-8970-203f48c90a57.png#align=left&display=inline&height=595&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=595&originWidth=221&search=MyBlog%20init%20settings.py%20urls.py%20wsgipy%20%3FMyBlogAPp%20migrations%20static%20templates%20myblogapp%20about.html%20caselist.html%20index.html%20knowledge.htm%20moodlist.html%20new.html%20newlist.html%20share.html%20template.html%20appspy%20models.py%20testspy%20urls.py%20views.py%20%3F%20db.sqlite3%20managepy&size=25053&status=done&width=221)

#### 模板继承

- 首先创建base.html文件，将模板中所有的公共部分放入这里
- 修改静态文件路径
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574584157502-d8c063e0-99bd-413f-876f-60c3a65281a7.png#align=left&display=inline&height=436&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=436&originWidth=957&search=settings.py%20base.html%20111.html%20urls.P%20viewspy%20src-%22images%20MatchCase%20Words%20Nomatches%20Regex%20QRSRE%2FSTATIE%2FYBLOGAPP%2FIMAGESI%20ExCLuDe%20lnSelection%20Replace%20PreserveCase%20Replaceall%20Chead%3F%20CTRL%2BR%20%3Cmetacharset-%22UTF-8%22%3E%20I%25endblock%25title%29%20%3Ctitle%2Ff%25blocktitle%25endb%20ontent%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%2C%E4%BA%8E%E5%85%89%E5%9D%A4%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%2C%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%E7%BD%91%E7%AB%99%22%3E%20ent%3A%22%E4%BA%8E%E5%85%89%E5%9D%A4%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%2C%E6%98%AF%E4%B8%80%E4%B8%AA%E5%8A%B1%E5%BF%97Python%E5%85%A8%E6%A0%88%E5%BC%80%E5%8F%91%E7%9A%84%E8%8D%89%E6%A0%B9%E7%A8%8B%E5%BA%8F%E5%91%98%E7%9A%84%E5%A5%8B%E6%96%97%201inkhref-%22%2Fstatic%2Fmyblogapp%2Fcss%2Fbasecre%20css%22rel-%27stylesheet%22%27%3E%201inkhref-%22%2Fstatic%2Fmyblogappcsstemlatecstye%2010%20f%25b1ockcssI%25endblock%25%2011%2012%20K%3C%21--%5BifltIE9%5D%20%3Cscriptsrc-%22%2Fstatic%2Fmyblogapp%2Fjs%2Fmodernizrj%2Fscrit%2013%20K%21%5Bendif%5D--%3E%2014%2015%20-K%2Fhead%3E&size=71706&status=done&width=957)

- 添加块
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574584730414-e99eb941-585d-4472-b9e7-29ac559677ec.png#align=left&display=inline&height=341&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=341&originWidth=752&search=head%3F%20%3Cmetacharset%22UTF-8%27%3E%20%25blocktitle%25f%25endblock%25title%29%20%3Ctitlejt%20ntent%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%2C%E4%BA%8E%E5%85%89%E5%9D%A4%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%2C%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%E7%BD%91%E7%AB%99%22%3E%20%3Cmetaname-%22keywordscontent%E4%B8%89%22%E4%B8%AA%E4%BA%BA%E5%8D%9A%E9%83%A8%20ontent%22%E4%BA%8E%E5%85%89%E5%9D%A4%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%2C%E6%98%AF%E4%B8%80%E4%B8%AA%E5%8A%B1%E5%BF%97Python%E5%85%A8%E6%A0%88%E5%BC%80%E5%8F%91%E7%9A%84%20linkhref%22%2Fstatic%2Fmyblogappcs%2Fbasec%20s%22rel-%27stylesheet%27%3E%20%3Clinkhref-%22%2Fstatic%2Fmyblogapcss%2Ftemplatec%20f%25blockcss%E5%B7%9Ef%25endblock%E5%88%AB%20k%3C%21--%5BifltIE9%5D7%20%3Cscriptsrc-%22%2Fstatic%2Fmyblogapp%2Fjs%2Fmodernizrj%20K%3C%21%5Bendif%5D--%3E%20%3C%2Fhead&size=45015&status=done&width=752)
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574584768750-b3522e63-1ced-442d-8457-caa5ce04dad3.png#align=left&display=inline&height=302&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=302&originWidth=323&search=%3Carticle%29%20I%25blockarticle_top%E5%88%AB%20f%25%20%25endb1ock%E5%A5%96%20%25%20I%25b1ockarticleleft%25%20f%25endblock%25%20f%25%20%25%20b1ock%20articleright%20%25endblock%20%3C%2Farticle%3E&size=16779&status=done&width=323)
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574584786117-a7cd084f-9d73-49e4-acb0-c2f6e74478a7.png#align=left&display=inline&height=60&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=60&originWidth=517&search=%3Cscriptsrc-%22%2Fstatic%2Fmyblogapp%2Fj%2Fsilderjs%20Tf%25blockjs%25&size=7416&status=done&width=517)




- 字模板继承父模板，并且打开对应的块添加上字模板独有的内容
- ![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574586821482-336d2e2d-fc21-4c4e-80f4-6b6386e2a453.png#align=left&display=inline&height=638&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=638&originWidth=853&search=MyBlogApplurls.py%20MyBloglurlspy%20index.html%20views.py%20myblogapp%2Fbase.h%20extends%205%25blocktitle%E5%88%86%20YCK%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99%E9%A6%96%E9%A1%B5%20endblock%E5%A5%96%20blockcss%20%3Clinkhref-%22%2Fstatic%2Fmyblogapp%2Fcss%2Find%20rel-%27stylesheet%22%20endblock%E9%AA%8F%20%25b1ockbanner%E5%88%AB%20%3Cdivclass-%22banner%22%20endblock%25%2019%20b1ock%2020%20article_top%20class-title_tj%3E%2021%20P%E6%96%87%E9%9F%B3%3Cspan%3E%E6%8E%A8%E8%8D%90%3C%2Fspan%3C%2Fp%29%20%2Fh2%3E%2023%20%25endb1ock%25%2024%2025%20F%25b1ockarticleleft%25%20%3Cdivclass-%22bloglistleft%22%2026%2039%20endb1ock%E5%B7%9E%2040%2019blockarticle_right%25%20%3Casideclass-%22right%22..%2086%20Bendb1ock%25&size=76112&status=done&width=853)




# ORM的配置和使用

## 安装数据库

1. 下载社区版数据库   [mysql-installer](https://dev.mysql.com/downloads/file/?id=489911)
1. 安装数据库   [安装卸载教程](https://www.cnblogs.com/wcwnina/p/9302393.html)
1. 安装可视化工具   Navicat


## Django中配置mysql
![image.png](https://cdn.nlark.com/yuque/0/2019/png/607838/1574593120706-98437362-f60a-4f96-b3a5-49a33d62a570.png#align=left&display=inline&height=310&name=image.png&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&ocrLocations=%5Bobject%20Object%5D&originHeight=310&originWidth=517&search=%23MySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84%E9%85%8D%E7%BD%AE%20DATABASES%E4%BA%8CA%20%27default%27%3Af%20ENGINE%27%3A%27django.db.backends.mysql%20NAME%3A%27b1og%2C%20%27USER%27%3A%27root%2C%20PASSWORD%3A%27root%27%2C%20HOST%3A%27127.0.0.1%2C%20PORT%3A%273306%27%2C&size=22520&status=done&width=517)

## 在数据库中创建blog表
## 安装pymysql

```python
pip install pymysql
```


[@创建模型来验证数据库配置是否正确](#) 

```sql
[mysqld]
basedir=D:/install/develop/mysql-5.7.27-winx64     # 设置成你的解压路径
datadir=D:/install/develop/mysql-5.7.27-winx64/data   #  数据的存储路径
character-set-server=utf8    #  设置数据库的默认编码格式
explicit_defaults_for_timestamp  #  默认配置
[mysql]
```

