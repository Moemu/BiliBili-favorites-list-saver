'''
B站收藏夹saver(GUI)
作者:White_mu(WhitemuTeam)
已知获取收藏夹中的内容API为：
https://api.bilibili.com/x/v3/fav/resource/list?media_id=[收藏夹ID]&pn=[页数]&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp
收藏夹必须公开
'''
import PySimpleGUI as sg
import main

class gui:
    def main():
        txtlist=main.readdatalist()
        layout=[
            [sg.Text('欢迎，请选择您需要查看的收藏夹',font=('黑体 15'))],
            [sg.InputCombo(txtlist,font=('黑体 15'),size=(30,5))],
            [sg.Button('添加',font=('黑体 15')),sg.Button('查看',font=('黑体 15')),sg.Button('更新',font=('黑体 15'))]
        ]
        event,value=sg.Window('主页面',layout=layout).read()
        if event=='添加':
            layout=[
                [sg.Text('请在下列输入框中输入您的收藏夹链接',font=('黑体 15'))],
                [sg.Text('您的收藏夹必须要公开才可让程序访问哦~',font=('黑体 15'))],
                [sg.Input()],
                [sg.Button('提交')]
            ]
            event,value=sg.Window('添加页',layout=layout).read()
            if event=='提交':
                url=value[0]
                vdeioid,vdeiotit,vdeioauthor,faid,fname=main.getfavlist(url)
                vdeiostatus=main.checkstatus(vdeiotit)
                main.writedata(faid,vdeiotit,vdeioid,vdeioauthor,vdeiostatus,fname)
                sg.popup('添加完成，请重新启动程序',font=('黑体 10'))
        elif event=='查看':
            txt=value[0]
            if txt=='这里还什么都没有啊~' or txt=='':
                sg.popup('请指定一个文件!!!',font=('黑体 10'))
                exit()
            main.dataview(txt)
        elif event=='更新':
            main.update()
            sg.popup('更新完成，请重新打开程序',font=('黑体 10'))

if __name__=='__main__':
    gui.main()