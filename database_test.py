import mysql.connector

name_var="Aniket"
age_var= "29"
email_var= "a@gmail.com"
gender_var= "Male"
usertype= "Student"

conn= mysql.connector.connect(host="localhost",username="root",password="password@123",database="test")
my_cursor=conn.cursor(buffered=True)
my_cursor.execute("insert into user_information values (%s, %s, %s, %s, %s)", (name_var,age_var,email_var,gender_var,usertype))
conn.commit()
conn.close()