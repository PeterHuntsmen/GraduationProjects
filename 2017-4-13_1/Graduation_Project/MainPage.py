from Graduation_Project.view import *

class MainPage(object):

    def __init__(self,master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.queryResultPage = QueryResultFrame(self.root)
        self.inputPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label="选择路径",command=self.inputData)
        menubar.add_command(label="查询",command=self.queryData)
        menubar.add_command(label="绘制词频图",command=self.countData)
        menubar.add_command(label="数据库所有结果", command=self.queryResultData)
        menubar.add_command(label="关于",command=self.aboutDisp)
        self.root['menu'] = menubar

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.queryResultPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.queryResultPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()
        self.queryResultPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()
        self.queryResultPage.pack_forget()

    def queryResultData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        self.queryResultPage.pack()
