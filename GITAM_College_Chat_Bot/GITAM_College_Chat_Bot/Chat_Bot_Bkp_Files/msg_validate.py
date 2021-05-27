import random
from Chat_Bot_Bkp_Files.Department_HOD import chk_HOD
from Chat_Bot_Skiils.Help_User import return_help_content
from Chat_Bot_Bkp_Files.Time_Table import get_sem_branch_time_table
from Chat_Bot_Skiils.GITAM_Departments import get_departments
from Chat_Bot_Skiils.Semester_Subjects import get_subjects, get_sem_branch

##### Basic Response
bas_resp = ['<strong>Okay</strong>', '<strong>Got it</strong>', '<strong>Yup</strong>']


############## College details ###########################
###### Available Branches
college_branch = get_departments()


###### Contact Details
college_website = bas_resp[random.randint(0, 2)] + '<a href=https://www.gitam.edu>Click Here</a>'
college_phone_no = '<strong>Call <i><h6> 08455-221200 / 1 / 2 / 3 / 4</strong>'


def chk_msg(user_msg, user_info):
    msg = user_msg.lower().strip()

    ##### About User
    if 'my name' in msg:
        return 'Hello ' + user_info[0]
    elif 'my subject' in msg or 'my syllabus' in msg or 'subjects of my semester' in msg or 'my semester subjects' in msg or 'subject of my semester' in msg or 'my semester subject' in msg:
        return get_subjects(user_info[3], user_info[4])
    elif 'who is my hod' in msg or 'my hod' in msg or 'head of my' in msg:
        return chk_HOD('hod of '+user_info[4].lower())
    elif 'my branch' in msg or 'my department' in msg:
        return 'You are belongs to ' + user_info[4] + ' branch'


    ########## Department Subjects query
    elif 'tell me subject' in msg or 'tell me syllabus' in msg or 'subjects of' in msg or 'subject of' in msg or 'syllabus of' in msg or 'subject in' in msg or 'syllabus in' in msg or 'subjects in' in msg or 'syllabus' in msg:
        return get_sem_branch(msg, user_info)



    ########## About College
    elif 'branch in college' in msg or 'branches in your college' in msg or 'branch in your college' in msg or 'branches in college' in msg or 'available departments' in msg or 'departments' in msg or 'available department' in msg or 'branches of your college' in msg or 'branch of your college' in msg or 'branches available' in msg or 'branch available' in msg or 'department available' in msg or 'college branches' in msg or 'college branch' in msg:
        return college_branch
    elif 'website of college' in msg or 'college website' in msg or 'website' in msg or 'website of' in msg:
        return college_website
    elif 'phone no of college' in msg or 'college number' in msg or 'college cell number' in msg or 'phone number' in msg or 'cell number' in msg:
        return college_phone_no




    ### HOD of Department
    elif 'hod of' in msg or 'head of department' in msg or 'head' in msg or 'hod' in msg:
        return chk_HOD(msg)



    ### principal
    elif 'principal' in msg:
        return '<strong>Dr. I. Jyothi Padmaja</strong><br><img src="static/img/Dep_HOD/principal.jpg" height="200" width="200">'


    ### Department flour
    elif 'civil department' in msg or 'department of civil' in msg or 'where is civil' in msg or 'which is flour the of civil' in msg or  'cv department' in msg or 'department of cv' in msg or 'where is cv' in msg or 'which flour of cv' in msg:
        return bas_resp[random.randint(0, 2)] + '<br>' + "<strong>Civil Department at 5'th floor</strong>"
    elif 'electrical department' in msg or 'department of electronic' in msg or 'where is electrical' in msg or 'which is the flour of electronic' in msg or  'etc department' in msg or 'department of etc' in msg or 'where is etc' in msg or 'which flour of etc' in msg:
        return bas_resp[random.randint(0, 2)] + '<br>' + "<strong>Electrical Department at 3'rd floor</strong>"
    elif 'mechanical department' in msg or 'department of mechanical' in msg or 'where is mechanical' in msg or 'which is the flour of mechanical' in msg or  'me department' in msg or 'department of me' in msg or 'where is me' in msg or 'which flour of me' in msg:
        return bas_resp[random.randint(0, 2)] + '<br>' + "<strong>Mechanical Department at 2'nd floor</strong>"
    elif 'biotechnology department' in msg or 'department of biotechnology' in msg or 'where is biotechnology' in msg or 'which is the flour of biotechnology' in msg:
        return bas_resp[random.randint(0, 2)] + '<br>' + "<strong>Biotechnology Department at 4'th floor</strong>"
    elif 'computer department' in msg or 'department of computer' in msg or 'where is computer' in msg or 'which is the flour of computer' in msg or 'computer science department' in msg or 'department of computer science' in msg or 'where is computer science' in msg or 'which flour of science' in msg or 'cse department' in msg or 'department of cse' in msg or 'where is cse' in msg or 'which is the flour of cse' in msg or 'ce department' in msg or 'flour of cse' in msg or 'department of ce' in msg or 'where is ce' in msg or 'which flour of ce' in msg:
        return bas_resp[random.randint(0, 2)] + '<br>' + "<strong>Computer Department at 1'st floor</strong>"




    #### Time Table
    elif 'time table' in msg or 'table' in msg or 'today lecture' in msg or 'todays lectures' in msg or 'todays lecture' in msg or 'today lectures' in msg:
        path = get_sem_branch_time_table(msg, user_info)
        if path == 'Chat bot are in progress in future you will get your query related information ':
            return '<strong>Chat bot is in progress in future you will get your query related information</strong>'
        return '<center>Here is <strong>Time Table</strong> <br>Now you can look into table</center><br><img src="' + path + '" height="300" width="300">'



    ##### For user help
    elif 'help' in msg or 'command' in msg or msg == '' or '?' in msg:
        return return_help_content(user_info)



    else:return None
