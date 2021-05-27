### HOD of all branches





HOD_CE = '<strong>Dr. K Thammi Reddy</strong><br><img src="static/img/Dep_HOD/cse.jpg" height="200" width="200">'
HOD_ETC = '<strong>Dr. V. Y. Jayasree P</strong><br><img src="static/img/Dep_HOD/ece.jpg" height="200" width="200">'
HOD_ME = '<strong>Dr. Rama Surya</strong><br><img src="static/img/Dep_HOD/mechanical.jpg" height="200" width="200">'
HOD_CV = '<strong>Dr. K Venkata Ramesh</strong><br><img src="static/img/Dep_HOD/civil.jpg" height="200" width="200">'
HOD_BIO = '<strong>Dr. S Khasim Beebi</strong><br><img src="static/img/Dep_HOD/biotechnology.jpg" height="200" width="200">'


def chk_HOD(msg):
    if ' ce ' in msg or 'computer' in msg or 'cse' in msg or 'science' in msg:
        return HOD_CE
    elif ' cv ' in msg or 'civil' in msg:
        return HOD_CV
    elif ' me ' in msg or 'mechanical' in msg:
        return HOD_ME
    elif ' etc ' in msg or 'electrical' in msg or 'electronics' in msg or 'ece' in msg:
        return HOD_ETC
    elif 'biotechnology' in msg:
        return HOD_BIO


    elif msg.startswith('ce ') or msg.endswith(' ce') or msg.endswith(' cse') or msg.startswith('cse '):
        return HOD_CE
    elif msg.startswith('it ') or msg.endswith(' it'):
        return HOD_CV
    elif msg.startswith('me ') or msg.endswith(' me'):
        return HOD_ME
    elif msg.startswith('cv ') or msg.endswith(' cv'):
        return HOD_CV

    else:
        return 'Sorry I did not found any data in our college database of that branch branch'

