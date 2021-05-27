from Chat_Bot_Skills.GITAM_College_Constant import *
from Chat_Bot_Skills.Help_User import return_help_content
from Chat_Bot_Skills.Semester_Subjects import get_subjects, get_sem_branch


def chk_msg(user_msg, user_info):
    msg = user_msg.lower().strip()

    # About User
    if 'my name' in msg:
        if user_info[0] == "there":
            return 'Hello there'
        else:
            return 'Hello ' + user_info[0]

    elif 'my subject' in msg or 'my syllabus' in msg or 'subjects of my semester' in msg or 'my semester subjects' in msg or 'subject of my semester' in msg or 'my semester subject' in msg:
        if user_info[0] == "there":
            return 'Please explore your question'
        else:
            return get_subjects(user_info[3], user_info[4])

    elif 'my branch' in msg or 'my department' in msg:
        if user_info[0] == "there":
            return 'Please explore your question'
        else:
            return 'You belong to ' + user_info[4] + ' branch'

    # Department Subjects query
    elif 'tell me subject' in msg or 'tell me syllabus' in msg or 'subjects of' in msg or 'subject of' in msg or 'syllabus of' in msg or 'subject in' in msg or 'syllabus in' in msg or 'subjects in' in msg or 'syllabus' in msg:
        return get_sem_branch(msg, user_info)

    # About College
    elif 'branch in college' in msg or 'branches in your college' in msg or 'branch in your college' in msg or 'branches in college' in msg or 'available departments' in msg or 'departments' in msg or 'available department' in msg or 'branches of your college' in msg or 'branch of your college' in msg or 'branches available' in msg or 'branch available' in msg or 'department available' in msg or 'college branches' in msg or 'college branch' in msg:
        return GITAM_Departments
    elif 'website of college' in msg or 'college website' in msg or 'website' in msg or 'website of' in msg:
        return college_website
    elif 'phone no of college' in msg or 'college number' in msg or 'college cell number' in msg or 'phone number' in msg or 'cell number' in msg:
        return college_phone_no

    # For user help
    elif 'help' in msg or 'command' in msg or msg == '' in msg:
        return return_help_content(user_info)

    elif 'what is ml' in msg:
        return "Machine learning (ML) is the study of computer algorithms that improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as 'training data', in order to make predictions or decisions without being explicitly programmed to do so."

    elif 'what is gitam' in msg:
        return "Gandhi Institute of Technology and Management, formerly GITAM University and GITAM College of Engineering, is a private institute deemed to be university, located in Visakhapatnam, Andhra Pradesh. It was founded in 1980 by a group of intellectuals and industrialists of Andhra Pradesh led by M. V. V. S. Murthi"

    else:
        return None
