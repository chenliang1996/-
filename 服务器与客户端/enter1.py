#用户登录的类
import pymysql as mp
class Login:
    #初始类-->用户的ID和密码
    def __init__(self):
        self.db = mp.connect(host="localhost",user="root",
                            password="123456",
                            database="verify",
                            charset="utf8")
        self.cursor = self.db.cursor()
    #从数据库核对用户ID
    def Check(self,ID,password):
        try:
            sql = "select password from Verify where PID='%s'" % ID
            self.cursor.execute(sql)
            data1 = self.cursor.fetchone()
            data = data1[0]
        except TypeError:
            self._close()
            return 'shibai'
        else:
            if data == password:
                self._close()
                return 'OK'
            else:
                self._close()
                return 'shibai'
    #修改用户的密码
    def Revise(self, ID, password):
        try:
            sql = "update Verify set password=%d where PID='%s'" % (password,ID)
            self.cursor.execute(sql)
            self.db.commit()
            print('修改成功')
        except Exception as e:
            self.db.rollback()
            print('修改失败', e)
        self._close()
    #关闭游标尺
    def _close(self):
        self.cursor.close()
        self.db.close()     
    #注册记录
    def Register(self, ID, password, username, phnum = 00000000000):
        sql1 = "select * from Verify where PID='%s'" % ID
        sql2 = "select * from Verify where username='%s'" % username
        self.cursor.execute(sql1)
        data1 = self.cursor.fetchone()
        if not data1:
            self.cursor.execute(sql2)
            data2 = self.cursor.fetchone()
            if not data2:
                try:
                    sql = "insert into Verify(PID,password,username,phnum) \
                                values('%s',%d,'%s','%s')"%(ID, password, username, phnum)
                    self.cursor.execute(sql)
                    self.db.commit()
                    return 0  #0代表成功
                except Exception as e:
                    self.db.rollback()
                    return 5,e  #5代表有异常
                self._close()
            else:
                self._close()
                return 1   #代表用户名已存在
        else:
            self._close()
            return 2         #代表账号已经存在


if __name__ == '__main__':
    # ID,password= '陈亮'
    #  = 123456
    Login1 = Login()
    # print(Login1.Check(ID, password))
    # password = 1234567
    # Login1.Revise(ID, password)
    print(Login1.Register('yaocheng',123456,'姚程','12345678901'))

