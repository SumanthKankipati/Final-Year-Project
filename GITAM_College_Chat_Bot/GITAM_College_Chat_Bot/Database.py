import sqlite3
import os


def createDabase():
    global conn, cursor
    cwd = os.getcwd()
    database_path = cwd+'\Chat_Bot_Database\student_details.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `student` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, stud_name TEXT, stud_email TEXT, stud_password TEXT, stud_roolNo TEXT, stud_year TEXT, stud_branch TEXT, stud_sem, todayDate TEXT)")
    print('Database Created')


def InsertData(stud_name, stud_email, stud_password, stud_roolNo, stud_year, stud_sem, stud_branch, todayDate):
    cwd = os.getcwd()
    database_path = cwd+'\Chat_Bot_Database\student_details.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
#    query = "INSERT INTO `person`(name,gender,dob,contact,address,photo,description,pdf) VALUES({},{},{},{},{},{},{},{});".format(str(name),str(gender),str(dob),int(contact),str(address),str(photo),str(description),str(pdf))
    cursor.execute("INSERT INTO `student` (stud_name,stud_email,stud_password,stud_roolNo,stud_year,stud_sem,stud_branch,todayDate) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (str(stud_name),str(stud_email),str(stud_password),str(stud_roolNo),str(stud_year),str(stud_sem),str(stud_branch),str(todayDate)))
    conn.commit()
    print('Inserted Data')


def read_cred(stud_email, stud_password):
    cwd = os.getcwd()
    database_path = cwd+'\Chat_Bot_Database\student_details.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT stud_name,stud_roolNo,stud_year,stud_sem,stud_branch FROM student WHERE stud_email ="+"'"+stud_email+"'"+" and stud_password ="+"'"+stud_password+"'"+"")
    fetch = cursor.fetchone()
    print(fetch)
    return fetch


def Insert_Sub_Data(sem, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10):
    cwd = os.getcwd()
    database_path = cwd+'\Chat_Bot_Database\syllabus_chatbot.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
#    query = "INSERT INTO `person`(name,gender,dob,contact,address,photo,description,pdf) VALUES({},{},{},{},{},{},{},{});".format(str(name),str(gender),str(dob),int(contact),str(address),str(photo),str(description),str(pdf))
    cursor.execute("INSERT INTO `IT` (semester,sub_1,sub_2,sub_3,sub_4,sub_5,sub_6,sub_7,sub_8,sub_9,sub_10) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (sem,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9,sub10))
    conn.commit()
    print('Inserted Data')


def get_subjects(sem):
    conn = sqlite3.connect('syllabus_chatbot.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * from `IT` WHERE semester="+"'"+sem+"'"+"")
    all_subjects=data.fetchone()
    conn.commit()
    if all_subjects==None:
        return 'Data Not Found'
    else:
        subject = 'Subject_Code | Subject_Type | Subject_Name '+'<br />'
        for i in range(1,11):
            try:
                if all_subjects[i]=='':
                    pass
                else:
                    subject = subject + '<br />' + str(i) +' - '+ all_subjects[i] +'<br />'
            except Exception as e:
                print(e)
        return subject






