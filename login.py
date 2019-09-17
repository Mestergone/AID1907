
class User:
    def __init__(self):
        self.db = pymysql.connect(user='root',
                                  passwd = '123456',
                                  database=database,
                                  charset='utf8')
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        sql = "select * from user where name = %s"
        self.cur.execute(sql,[name])
        r = self.cur.fetchone()
        #查找到说明用户存在
        if r:
            return False

        sql = "insert into user (name,passwd) \
              values (%s,%s)"
        try:
            self.cur.execute(sql,[name,password])
            self.db.commit()
            return True
        except:
            self.db.rollback()

    def login(self,name,passwd):
        sql = "select * from user where name = %s and passwd = %s"






if __name__ == '__main__':
    user = User()

    if user.register('Abby','123'):
        print("注册成功")

    if user.login('Abby','123'):
        print("登录成功")





























import pymysql

def login(user_name,password):
    db = pymysql.connect(user='root',
                         password='123456',
                         database='user',
                         charset='utf8')
    cur = db.cursor()
    sql = "select * from user where user == %s;" %(user_name)
    if not sql:
        if sql[1] == password:
            return True
        else:
            return "密码错误"
    else:
        return "未找到该用户"

user_name = input("用户名:")
password = input("密码:")

login(user_name,password)



















