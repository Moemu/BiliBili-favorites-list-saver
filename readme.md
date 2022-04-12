# B站收藏夹列表saver

# 前言

B站收藏夹列表saver是一个基于Python开发，拥有GUI的一款工具，用于爬取您的收藏夹列表，旨在拯救您的B站逐渐变灰的收藏夹，它的部分截图如下：

![](https://s3.bmp.ovh/imgs/2021/10/4c6b3f734f1954d8.png)

# 使用

## 运行

### 使用源码运行

本程序基于Python3环境开发，请确保您已经提前配置好Python3环境

安装库：

```powershell
pip install requests
pip install PySimpleGUI
```

clone此仓库

运行GUI.py

### 使用封装后的exe文件运行

从[Releases](https://github.com/WhitemuTeam/BiliBili-favorites-list-saver/releases)下载最新的`BiliBili-favorites-list-saver.exe`，但部分电脑可能存在报错情况，这是由于Pyinstaller的封包问题引起的错误，因此我们推荐使用Windows10 x64以上的系统来使用此exe

### 自动运行

我们提供了一个AutoUpdate程序，该程序会自动更新收藏夹列表，请将其添加进启动项中即可

## 使用

打开此程序，我们会看到程序生成了一个名为“主界面”的GUI窗口并生成了一个名为"data"的文件夹（data文件夹非常重要，里面会有你的收藏夹数据）

一开始里面是没有能查看的收藏夹的，我们需要添加一个

点击添加按钮，跳转到"添加页"，输入你的收藏夹链接（类似于https://space.bilibili.com/1655970980/favlist?fid=1380825080&ftype=create
在Web端的个人空间处可以看到这个链接，**收藏夹必须公开，除非你[定义Cookie](#定义Cookie)，不然程序无法获取到你的收藏夹列表**）后点击提交

此时程序会在data文件夹生成一个以收藏夹ID+收藏夹名命名的txt文件，它的结构类似于：

```txt
标题:深度系统与UOS的差别 作者:White_mu BV:BV1m5411x7Ri 状态:Normal
标题:已失效视频 作者:White_mu BV:BV1UK4y1t76P 状态:invalid
```

重启程序，此时在主页面的下拉选项中就可以看到这个txt文件，选中它并点击查看就能查看里面的信息

**注意，由于显示器能容纳的行数有限，这个页面只能显示最高20行的数据，我们推荐您通过该页面下的"打开txt文件"按钮打开txt查看或者通过"使用作者名搜索"方式搜索视频数据(此方法不限制最高行数)，或者通过更改main.py中的第83行代码来修改最高显示行数**

这个信息包括了某个视频的标题，作者，BV号以及它的状态(分为"Normal"(正常)和"invalid(失效)")，invalid(失效)视频会特别用红色标记

![](https://i.bmp.ovh/imgs/2021/10/33a17839a7b73df9.png)

当数据量较多时，我们可以使用作者名搜索来检索某些视频，只需要点击使用作者名搜索按钮即可

同样的，我们还可以点击打开txt文件来查看全部数据

## 定义Cookie

若您需要获取您的私密收藏夹，则您需要获取登录Cookie

你需要使用浏览器登录到Bilibili并进入https://api.bilibili.com/x/v3/fav/resource/list

在此页面按下F12进入开发人员工具，切换到Network(网络)选项卡，此时刷新网页，过后你会看到一个list行，点击list行，在新弹出页面中找到headers(请求标头)，在其下方找到cookie一行，复制cookie以后的内容（该内容不加深）

返回到软件主页面点击高级按钮，粘贴复制的内容，点击提交即可

# 关于

作者：Moemu

Email: [master@muspace.top](mailto://master@muspace.top)

Blog: https://muspace.top/

