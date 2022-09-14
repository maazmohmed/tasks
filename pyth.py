import pymysql
conn = pymysql.connect(user='root', password='',host='localhost',database='pyth_php')
cursor = conn.cursor()
i = True
while i == True:
    function = input("Enter desired operation")
    if function == "insert":
        data1 = input("Enter value of 1st column")
        data2 = input("Enter value of second column")
        query='insert into tbl_py values({},{});'.format(data1,data2)
        r = cursor.execute(query)
    elif function == "update":
        column = input("Enter which column to update")
        old_data = input(("enter old data"))
        new_data = input("Enter new data")
        query = "UPDATE tbl_py SET {} = {} WHERE {} = {}".format(column,new_data,column,old_data)
        r = cursor.execute(query)
    elif function == "delete":
        data = input("Enter value of one of the elements to delete")
        column = input("Enter column name of given data")
        query = 'delete from tbl_py where {}={}'.format(data,column)
        r = cursor.execute(query)
    elif function == "fetch":
        query = "select * from tbl_py"
        r = cursor.execute(query)
        data=cursor.fetchall()
        print(data)
    elif function == "end":
        i = False
