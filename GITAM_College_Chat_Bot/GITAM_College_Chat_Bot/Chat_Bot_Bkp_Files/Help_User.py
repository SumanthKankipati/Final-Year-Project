def return_help_content(user_info):
    if user_info[0]=='You':
        user_info[0]=''
    #"<style>body {font-family: 'Tangerine', serif;font-size: 16px;}</style>"
    content ="<h4>Hello <font color='#0CFD5B'><strong>"+user_info[0]+"</strong></font> I am AI bot of <font color='#0CFD5B'><strong>GITAM</strong></font>  " \
            "<br>"\
            "I am here to answer your queries" \
            "<br><br><font color='#88FDE0'>Such as, </font><br></h4>" \
            "<br><font color='#F7FB05'><strong>1. </strong></font>Get <strong><font color='#F7FB05'>Your Details</strong></font>" \
            "<br>ex: My name" \
            "<br>ex: My subjects"\
            "<br>" \
            "<br><font color='#F7FB05'><strong>2. </strong></font>Get <strong><font color='#F7FB05'>College Details</font></strong>" \
            "<br>## Website, cell no, etc" \
            "<br>ex: Address of college" \
            "<br>ex: Available branches in college" \
            "<br>ex: What are branches in college" \
            "<br>" \
            "<br><font color='#F7FB05'><strong>3. </strong></font>Get <strong><font color='#F7FB05'>Department Flour</strong></font> details" \
            "<br>ex: Where is cse department" \
            "<br>ex: Where is computer department" \
            "<br>" \
            "<br><font color='#F7FB05'><strong>4. </strong></font>Get all list of any <font color='#F7FB05'><br><strong>Branch and Semester Subjects </strong></font>" \
            "<br>ex: What are my semester subjects" \
            "<br>ex: What are subjects of 7 semester in <br>CSE branch" \
            "<br>" \
            "<br><font color='#F7FB05'><strong>5. </strong></font>Get <strong><font color='#F7FB05'>Todays Lectures</font></strong> (Time table) details" \
            "<br>ex: My todays lectures" \
            "<br>ex: Show me time table of 4 sem CE department"\
            "<br>ex: Time table of 5 sem cse branch" \
            "<br>"\
            "<br><font color='#F7FB05'><strong>6. </strong></font>Get <strong><font color='#F7FB05'>subject query</font></strong> answers" \
            "<br>ex: What is python" \
            "<br>ex: Who is created computer"\
            "<br>ex: what is difference between polymorphism and inheritance" \
            "<br>"

    return content



# content ="<h4><font color='red'>Hello <strong>"+user_info[0]+"</strong> I am AI bot of <strong>SRPCE</strong> " \
#     "<br>"\
#     "I am here to answer your queries" \
#     "<br>Such as <br></h4>" \
#     "<br>1. Get subject details of any <br><strong>Branch and Semester. </strong>" \
#     "<br>ex: What are subjects of 7 semester in EXTC branch" \
#     "<br>ex: What are my semester subjects" \
#     "<br>" \
#     "<br>2. Get <strong>HOD</strong> details of any Department " \
#     "<br>ex: Who is the Head of CE Department" \
#     "<br>ex: Who is HOD of CE Department" \
#     "<br>" \
#     "<br>3. Get <strong>College</strong> details" \
#     "<br>## Branch, website, cell no, address, etc" \
#     "<br>ex: Available branches in college" \
#     "<br>ex: What are branches in college" \
#     "<br>ex: Address of college" \
#     "<br>" \
#     "<br>4. Get allocated <strong>Teacher Details</strong> of any subjects" \
#     "<br>ex: What is teacher name of WSN subject" \
#     "<br>ex: Who is project incharge of CE department" \
#     "<br>ex: Who is my project guide" \
#     "<br>" \
#     "<br>5. Get <strong>Todays Lectures</strong> (Time table) details" \
#     "<br>ex:what are todays lectures in CE department" \
#     "<br>ex:my todays lectures" \
#     "<br>ex:show time table of IT department" \
#     "<br>" \
#     "<br>6. Get <strong>Department Flour</strong> details" \
#     "<br>ex:where is polytechnic department" \
#     "<br>ex:where is enhineering department" \
#     "<br>" \
#     "<br>7. Get <strong>Your</strong> details" \
#     "<br>ex:my name" \
#     "<br>ex:my subjects"
