from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog as tkFD
from Graduation_Project.MySQLDBConnetctor import search_summary_for_text
from Graduation_Project.MySQLDBConnetctor import insert
from Graduation_Project.MySQLDBConnetctor import search_for_orientation
from Graduation_Project.MySQLDBConnetctor import query_for_required_text
from Graduation_Project.MySQLDBConnetctor import query_for_numbers_of_recording
from Graduation_Project.MySQLDBConnetctor import query_for_single_summary
from Graduation_Project.MySQLDBConnetctor import query_for_single_orientation
from Graduation_Project.MySQLDBConnetctor import query_for_single_keyword
from Graduation_Project.keywords import keywords
from Graduation_Project.Graph import statistics
from Graduation_Project.participle import division
from Graduation_Project.POS_Tagging import POS_Tagging

class InputFrame(Frame):  # 继承Frame类

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.pathVar = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='选择路径: ').grid(row=1, stick=W, pady=10)
        self.path = Entry(self, textvariable=self.pathVar).grid(row=1, column=1, stick=E)
        Button(self,text='选取文件',command=self.openfile).grid(row=1, column=2, stick=E)
        Button(self,text="将文件插入数据库",command=self.insertFile).grid(row=1, column=3, stick=E)
        Button(self,text="进行分词",command=self.division_of_text).grid(row=2, column=2,stick=E)
        Button(self,text="对文件做词性分析", command=self.POS_Analysis).grid(row=2, column=3, stick=E)

    def openfile(self):
        self.filename=tkFD.askopenfilename(filetypes=[("text Files", "*.txt")])
        self.pathVar.set(self.filename)

    def insertFile(self):
        try:
            insert(self.filename)
            self.keywords = keywords(self.filename)
            showinfo(title="关键字",message=self.keywords)
            showinfo(title="插入成功",message="成功插入数据")
        except:
            showerror(title="Error",message="出现错误！")
            showinfo(title="Message",message=self.filename)

    def division_of_text(self):
        text_of_division = division(self.filename)
        showinfo(title="分词结果为：",message=text_of_division)

    def POS_Analysis(self):
        text_of_POS_Tagging = POS_Tagging(self.filename)
        showinfo(title="词性分析结果为：",message=text_of_POS_Tagging)

class QueryFrame(Frame):  # 继承Frame类

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.keywordVar = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self, text='查询,请输入关键词').pack()
        self.temp = Entry(self,textvariable=self.keywordVar).pack()
        Button(self,text="开始查询概要",command=self.queryForSummaryByKeywords).pack()
        Button(self,text="开始查询倾向",command=self.queryForOrientationByKeywords).pack()
        Button(self,text="开始查询文本",command=self.queryForText).pack()

    def queryForText(self):
        self.keywords_of_text = self.keywordVar.get()
        self.text = query_for_required_text(self.keywords_of_text)
        showinfo(title="原始文本为：",message=self.text)

    def queryForSummaryByKeywords(self):
        self.keywords_of_text_final=self.keywordVar.get()
        self.summary = search_summary_for_text(self.keywords_of_text_final)
        if self.summary != 'None':
            showinfo(title="主旨为：",message=self.summary)
        else:
            showinfo(title="Error",message="出错！")

    def queryForOrientationByKeywords(self):
        self.keywords_of_text_final = self.keywordVar.get()
        self.orientation = search_for_orientation(self.keywords_of_text_final)
        if self.orientation != 'None':
            showinfo(title="倾向性值", message=self.orientation)
            if (int(self.orientation)>=7):
                showinfo(title="Excellent",message="趋势非常好！")
            if (int(self.orientation)>= 5) & (int(self.orientation)< 7):
                showinfo(title="Good", message="趋势正在向好的方向发展！")
            if (int(self.orientation)<= -7):
                showinfo(title="Bad", message="趋势恶化中...")
            if (int(self.orientation)> -7 & int(self.orientation)<= -5):
                showinfo(title="Worsening", message="趋势正在变坏...")
        else:
            showinfo(title="Error",message="出错")

class CountFrame(Frame):  # 继承Frame类

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.pathVar = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='选择路径: ').grid(row=1, stick=W, pady=10)
        self.path = Entry(self, textvariable=self.pathVar).grid(row=1, column=1, stick=E)
        Button(self,text='选取文件', command=self.openfile).grid(row=1, column=2, stick=E)
        Button(self,text='绘制词频统计图',command=self.getStatistics).grid(row=1, column=3, stick=E)

    def openfile(self):
        self.filename = tkFD.askopenfilename(filetypes=[("text Files", "*.txt")])
        self.pathVar.set(self.filename)

    def getStatistics(self):
        statistics(self.filename)

class AboutFrame(Frame):  # 继承Frame类

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self,text="此软件为上海电力学院计算机科学与技术学院计算机科学与技术系").pack()
        Label(self,text="2013053班刘水所做，学号20131752").pack()
        Label(self,text="盗版必究！").pack()

class QueryResultFrame(Frame):  # 继承Frame类

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self, text="关键词").grid(row=1, column=1, stick=E)
        Label(self, text="倾向值").grid(row=1, column=2, stick=E)
        Label(self, text="主旨").grid(row=1, column=3, stick=E)
        number_of_records = query_for_numbers_of_recording()
        for i in range(int(number_of_records)):
            Label(self, text=query_for_single_keyword(i)).grid(row=(i+3),column=1, stick=E)
            Label(self, text=query_for_single_orientation(i)).grid(row=(i+3),column=2, stick=E)
            Label(self, text=query_for_single_summary(i)).grid(row=(i+3),column=3, stick=E)