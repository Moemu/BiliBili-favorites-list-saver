'''
B站收藏夹saver(函数库)
By White_mu(WhitemuTeam)
'''
import requests as r
import PySimpleGUI as sg
import json,os

header={'User-Agent':'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}

def getfavlist(url,faid=None):
    #获取收藏夹ID
    if faid==None:
        faid=url.split('?fid=')[1].split('&')[0]
    vdeioid=[]
    vdeiotit=[]
    vdeioauthor=[]
    for i in range(1,51):
        apiurl='https://api.bilibili.com/x/v3/fav/resource/list?media_id='+faid+'&pn='+str(i)+'&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp'
        try:
            getjson=r.get(apiurl,headers=header).text
        except:
            sg.Popup('请检查您是否联网或打开代理...请联网且关闭代理后重试',font=('黑体 10'))
            exit()
        fjson=json.loads(getjson)['data']['medias']
        if fjson==None:
            break
        for a in range(0,20):
            try:
                tit=fjson[a]['title']
                bvid=fjson[a]['bv_id']
                author=fjson[a]['upper']['name']
                vdeiotit.append(tit)
                vdeioid.append(bvid)
                vdeioauthor.append(author)
            except:
                fname=json.loads(getjson)['data']['info']['title']
                break
    return vdeioid,vdeiotit,vdeioauthor,faid,fname

def checkstatus(vdeiotit):
    time=0
    vdeiostatus=[]
    for i in vdeiotit:
        if i=='已失效视频':
            vdeiostatus.append('invalid')
        else:
            vdeiostatus.append('Normal')
    time+=1
    return vdeiostatus

def writedata(faid,vdeiotit,vdeioid,vdeioauthor,vdeiostatus,fname):
    name=faid+'：'+fname+'.txt'
    sen=''
    for i in range(len(vdeioid)):
        tit=vdeiotit[i]
        bvid=vdeioid[i]
        status=vdeiostatus[i]
        author=vdeioauthor[i]
        sen=sen+'标题:'+tit+' 作者:'+author+' BV:'+bvid+' 状态:'+status+'\n'
    with open(name,'w',encoding='utf-8') as f:
        print(sen,file=f)

def readdatalist():
    try:
        os.chdir('data')
    except:
        os.mkdir('data')
        os.chdir('data')
    txtlist=os.listdir()    
    if txtlist==[]:
        txtlist=['这里还什么都没有啊~']
    return txtlist

def dataview(txt):
    try:
        with open(txt,'r',encoding='utf-8') as f:
            data=f.readlines()
    except:
        sg.popup('数据库为空，请添加一个收藏夹吧~')
    sen=[[sg.Text('本次展示的是一部分数据，若要查看全部数据，请打开txt文件',font=('黑体 10'))]]
    author=[]
    for a in range(20): #此处更改一次性显示的数量  
        try:
            i=data[a]
            for b in range(len(data)):
                try:
                    adata=data[b].split('作者:')[1].split(' BV:')[0]
                    author.append(adata)
                except:
                    pass
        except:
            break
        if i=='\n':
            break
        status=i.split('状态:')[1].split('\n')[0]
        if status=='Normal':
            line=[sg.Text(i.split('\n')[0],font=('黑体 10'))]
        else:
            line=[sg.Text(i.split('\n')[0],font=('黑体 10'),text_color='Red')]
        sen.append(line)
    sen.append([sg.Button('使用作者名搜索'),sg.Button('打开txt文件'),sg.Button('退出')])
    event=sg.Window(title=txt,layout=sen).Read()
    if event[0]=='打开txt文件':
        ml='start '+txt
        os.system(ml)
    elif event[0]=='使用作者名搜索':
        layout=[
            [sg.Text('输入该视频作者名字',font=('黑体 10'))],
            [sg.Input(font=('黑体 10'))],
            [sg.Button('提交')]
        ]
        value=sg.Window(title='使用作者名搜索',layout=layout).Read()
        time=1
        sen=[]
        while True:
            try:
                num=author.index(value[1][0],time)
                time+=1
                sdata=data[num].strip('\n')
            except IndexError: #解决某种不应该出现的报错
                break
            except:
                sg.popup('此内容未找到，请检查输入是否正确',font=('黑体 10'))
                exit()
            status=sdata.split('状态:')[1]
            if status=='Normal':
                line=[sg.Text(sdata,font=('黑体 10'))]
            else:
                line=[sg.Text(sdata,font=('黑体 10'),text_color='Red')]
            sen.append(line)
        sen.append([sg.Button('确认',font=('黑体 10'))])
        sg.Window('搜索结果',layout=sen).Read()

def update():
    '''
    更新收藏夹列表
    注意：此函数较为复杂，可能存在较多Bug
    '''
    for txt in os.listdir():
        faid=txt.split('：')[0]
        url=None
        #获取目前最新的数据
        vdeioid,vdeiotit,vdeioauthor,faid,fname=getfavlist(url,faid)
        vdeiostatus=checkstatus(vdeiotit)
        #获取原有数据库中的数据
        try:
            with open(txt,'r',encoding='utf-8') as f:
                data=f.readlines()
        except:
            sg.popup('数据库为空，请添加一个收藏夹吧~')
            return None
        tit=[]
        author=[]
        bvid=[]
        status=[]
        data_len=len(data)-1
        for num in range(data_len):
            tdata=data[num].split('标题:')[1].split(' 作者')[0]
            tit.append(tdata)
            adata=data[num].split('作者:')[1].split(' BV号')[0]
            author.append(adata)
            bdata=data[num].split('BV:')[1].split(' 状态')[0]
            bvid.append(bdata)
            sdata=data[num].split('状态:')[1].split('\n')[0]
            status.append(sdata)
        #比较阶段：检查新数据status中有无invalid元素，并尝试从数据库中获取源有标题
        for n in range(len(vdeiostatus)):
            s=vdeiostatus[n]
            if s=='invalid':
                #获取该视频BV号
                bvdeioid=vdeioid[n]
                if bvdeioid in bvid:
                    #获取到原有视频库中的位置
                    num_bvid=bvid.index(bvdeioid)
                    old_video_tit=tit[num_bvid]
                    #无论是否在老数据库中有没有源标题，都替换获取到的标题
                    vdeiotit[n]=old_video_tit
        #写入文件（强行覆盖原有数据库）
        writedata(faid,vdeiotit,vdeioid,vdeioauthor,vdeiostatus,fname)