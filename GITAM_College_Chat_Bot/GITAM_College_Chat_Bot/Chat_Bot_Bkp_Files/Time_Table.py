import re


sem_list = ['first','second','third','fourth','fifth','sixth','seventh','eighth']
other_branch = 'Chat bot are in progress in future you will get your branch releted information '
other_sem = 'Chat bot are in progress in future you will get your query related information '


def get_sem(msg):
    sem_in_no = re.search('[1-8]',msg)
    if sem_in_no==None:
        for sem_in_alpha in sem_list:
           if sem_in_alpha in msg:
               print(sem_in_alpha)
               sem = sem_list.index(sem_in_alpha)+1
               return sem
        else:
            return 'Not Found'
    sem = sem_in_no[0]
    return sem

def get_branch(msg):
    if ' ce ' in msg or 'computer' in msg or 'cse' in msg or 'science' in msg:
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
        return 'Not Found'

def get_sem_branch_time_table(msg,user_info):
    sem = str(get_sem(msg))
    branch = get_branch(msg)
    if sem=='Not Found':
        print('Sem not found we are checking user details in database')
        sem = user_info[3]

    if branch=='CE':

        if sem=='8':
            return '\static\img\Time_Table\\8_sem.jpeg'
        elif sem=='6':
            return '\static\img\Time_Table\\6_sem.jpeg'
        elif sem=='5':
            return '\static\img\Time_Table\\5_sem.jpeg'
        elif sem=='4':
            return '\static\img\Time_Table\\4_sem.jpeg'
        elif sem=='2':
            return '\static\img\Time_Table\\2_sem.jpeg'
        elif sem=='1':
            return '\static\img\Time_Table\\1_sem.jpeg'
        else:
            return other_sem
    else:
        return other_sem
