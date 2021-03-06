# coding=utf-8
import pymysql

db = pymysql.connect('localhost', 'root', '863063', '58tc', charset='utf8')  # 创建数据连接，设置utf8格式，显示中文
cursor = db.cursor()  # 使用cursor()方法获取操作游标
# 创建表
# cursor.execute('DROP table if EXISTS lzy') #如果存在则删除
create = '''
    create table lzyy(
        id int primary key not null,
        title varchar(100) not null,
        price int(10) not null,
        date char(20) not NULL 
    )
'''

add = '''
   insert into lzyy(id,title,price,date)VALUES(2121,1,22,22);
'''

delete = '''
delete from lzy WHERE id = 1
'''
update = '''
update lzy set price =10000 WHERE id =1
'''

query = '''
select * from lzy
'''
try:
    cursor.execute(add)
    print("插入成功")
    # data = cursor.fetchall()  #查询时需要
    # print(data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()

# cursor.execute('select * from users ')  # SQL操作
# data = cursor.fetchall()  # fetchall()获取所有数据
# for data_one in data:
#     print(data_one)
# db.close()
