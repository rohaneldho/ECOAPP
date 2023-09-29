


    
def signin(name,password):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="ronsia123",auth_plugin="mysql_native_password",database="eco")
    cur=mydb.cursor(buffered=True)
    cur.execute('select * from ecousers where username = "%s" and password = "%s" ' %(name,password))
    L=cur.fetchone()
    if L==None:
        cur.execute('insert into ecousers (username,password) values ("%s","%s")'%(name,password))
        mydb.commit()
    else:
        print("name:",L[0])
        print("password:",L[1])
        print("nop:",L[2])
        print("tc:",L[3])
        print("pc:",L[4])
        return L;
        
    
A=list(signin("Rohan","Ronsia000"))
print(A)