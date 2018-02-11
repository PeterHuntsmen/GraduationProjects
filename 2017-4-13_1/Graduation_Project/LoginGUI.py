from Graduation_Project.MySQLDBConnetctor import login_check
from Graduation_Project.MainPage import *

class LoginGUI(object):

    def __init__(self,master=None):
        self.root = master
        self.root.geometry('%dx%d' % (300, 180))
        self.userName = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.userName).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.userName.get()
        secret = self.password.get()
        if(login_check(name,secret) == True):
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title="错误",message="账号或密码错误")