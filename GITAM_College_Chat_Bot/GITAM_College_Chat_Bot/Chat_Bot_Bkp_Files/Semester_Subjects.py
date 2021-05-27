import re
import os
import sqlite3

sem_list = ['first','second','third','fourth','fifth','sixth','seventh','eighth']
other_branch = 'Chat bot are in progress you in future you will get your branch related information '
other_sem = 'semester data not found please explore it or make correct your spelling'

def get_sem(msg):
    sem_in_no = re.search('[1-8]',msg)
    if sem_in_no==None:
        for sem_in_alpha in sem_list:
           if sem_in_alpha in msg:
               print(sem_in_alpha)
               sem = sem_list.index(sem_in_alpha)+1
               return sem
        else:
            return other_sem
    sem = sem_in_no[0]
    return sem


def get_branch(msg):
    if ' ce ' in msg or 'computer' in msg  or 'computer science' in msg or 'cse' in msg :
        return 'CE'
    elif ' it ' in msg or 'information technology' in msg:
        return 'IT'
    elif ' cv ' in msg or 'civil' in msg:
        return other_branch
    elif ' me ' in msg or 'mechanical' in msg:
        return other_branch
    elif ' ee' in msg or 'electrical' in msg:
        return other_branch
    elif ' extc ' in msg or 'electronics & telecommunication' in msg:
        return other_branch
    elif  ' mba ' in msg:
        return other_branch
    elif ' mca ' in msg:
        return other_branch


    elif msg.startswith('ce ') or msg.endswith(' ce'):
        return 'CE'
    elif msg.startswith('it ') or msg.endswith(' it'):
        return 'IT'
    elif msg.startswith('cv ') or msg.endswith(' cv'):
        return other_branch
    elif msg.startswith('me ') or msg.endswith(' me'):
        return other_branch
    elif msg.startswith('ee ') or msg.endswith(' ee'):
        return other_branch
    elif msg.startswith('extc ') or msg.endswith(' extc'):
        return other_branch
    elif msg.startswith('mba ') or msg.endswith(' mba'):
        return other_branch
    elif msg.startswith('mca ') or msg.endswith(' mca'):
        return other_branch
    else:
        return 'Branch Not Found'

def get_sem_branch(msg,user_info):
    sem = str(get_sem(msg))
    branch = get_branch(msg)
    if sem==other_sem:
        return sem
    elif branch==other_branch:
        return other_branch
    elif branch=='Branch Not Found':
        return get_subjects(sem,user_info[4])
    else: return get_subjects(sem,branch)

def get_subjects(sem,branch):
    cwd = os.getcwd()
    database_path = cwd+'\Chat_Bot_Database\syllabus_chatbot.db'
    print(database_path)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = cursor.execute("SELECT * from "+"`"+branch+"`"+" WHERE semester="+"'"+sem+"'"+"")
    all_subjects=data.fetchone()

    if all_subjects==None:
        return 'Data Not Found'
    else:
        subject = '<font color="#0CFD5B"><strong>Subject_Code  |  Subject_Name '+'<br /></font></strong>'
        for i in range(1,11):
            try:
                if all_subjects[i]=='':
                    pass
                else:
                    subject = subject + '<br />' + str(i) +' - '+ all_subjects[i] +'<br />'
            except Exception as e:
                print(e)
        return subject

# get_subjects('one aatwa  two   sem','nn')
# if any(sem in str for x in a):
# user_info = ['Sahil','21','4','8','CE']
# print(get_subjects('8','ce'))
