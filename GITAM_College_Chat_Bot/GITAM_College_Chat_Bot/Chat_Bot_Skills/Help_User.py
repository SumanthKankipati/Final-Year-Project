def return_help_content(user_info):
    if user_info[0] == 'You':
        user_info[0] = ''
    "<style>body {font-family: 'Tangerine', serif;font-size: 16px;}</style>"
    content = "<h4>Hello <font color='#0CFD5B'> <strong>"+user_info[0]+"</strong></font> , Welcome! Want to gather information? Let me help you out!  " \
            "<br>"\
            " Here are a few things I can help with:" \
            "<br><br><font color='#88FDE0'>Such as, </font><br></h4>" \
            "<br><font color='#F7FB05'><strong>1. </strong></font>Get <strong><font color='#F7FB05'>College Details</font></strong>" \
            "<br>ex: Website, phone no., etc" \
            "<br>ex: Available branches in college" \
            "<br>ex: What are branches in college" \
            "<br>" \
            "<br><font color='#F7FB05'><strong>2. </strong></font>Get <strong><font color='#F7FB05'>Department Flour</strong></font> details" \
            "<br>ex: Where is cse department" \
            "<br>ex: Where is computer department" \
            "<br>" \
            "<br><font color='#F7FB05'><strong>3. </strong></font>Get all list of any <font color='#F7FB05'><br><strong>Branch and Semester Subjects </strong></font>" \
            "<br>ex: What are subjects of 7 semester in <br>CSE branch" \
            "<br>" \
            "<br><font color='#F7FB05'><strong>4. </strong></font>Get <strong><font color='#F7FB05'>Time Table</font></strong> (Time table) details" \
            "<br>ex: Show me time table of 4 sem CE department"\
            "<br>ex: Time table of 5 sem" \
            "<br>ex: Display time table of 5 sem" \
            "<br>"\
            "<br><font color='#F7FB05'><strong>5. </strong></font>Get <strong><font color='#F7FB05'>Hod Information</font></strong> details" \
            "<br>ex: Who is head of computer department"\
            "<br>ex: Who is hod of mechanical" \
            "<br>"\
            "<br><font color='#F7FB05'><strong>6. </strong></font>Get <strong><font color='#F7FB05'>subject query</font></strong> answers" \
            "<br>ex: What is python" \
            "<br>ex: what is difference between polymorphism and inheritance" \
            "<br>"

    return content



