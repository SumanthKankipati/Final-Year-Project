import random

GITAM_Departments = '<strong>Here is list of Available Departments</strong><br><br>' \
                    "<strong>Under Graduation Programs</strong><br>" \
                    "1. Computer Science and Engineering (CSE)<br>" \
                    "<i><h6><h6>CSE ( Artificial Intelligence and Machine Learning )</h6></i>" \
                    "<i><h6>CSE ( Cyber Security )</h6></i>" \
                    "<i><h6>CSE ( Data Science )</h6></i>" \
                    "<i><h6>CSE ( Internet of Things )</h6></i>" \
                    "2. Aerospace Engineering<br>" \
                    "3. Biotechnology<br>" \
                    "4. Civil Engineering<br>" \
                    "5. Electronics and Communication Engineering (ECE)<br>" \
                    "<i><h6>ECE ( Artifical Intelligence and Machine learning )</h6></i>" \
                    "<i><h6>ECE ( IoT )</h6></i>" \
                    "<i><h6>ECE ( VLST Design )</h6></i>" \
                    "6. Electrical and Electronics Engineering (EEE)<br>" \
                    "<i><h6>EEE ( Robotics and Automation )</h6></i>" \
                    "7. Mechanical Engineering (ME)<br>" \
                    "<i><h6>ME ( Artifical Intelligence and Machine learning )</h6></i>" \
                    "<i><h6>ME ( Electric and Hybrid Vehicles )</h6></i>" \
                    "For Further Details <a href=https://gat.gitam.edu>Visit Here</a><br>" \
                    "<br><strong>Post Graduation Programs</strong><br>" \
                    "1. Aero Space Engineering<br>" \
                    "2. Cyber Forensics & Information Security<br>" \
                    "3. Computer Science And Engineering<br>" \
                    "4. Data Sciences<br>" \
                    "5. Electronics Design & Technology<br>" \
                    "6. Food Processing Technology<br>" \
                    "7. Machine Design<br>" \
                    "8. Machine Design And Robotics<br>" \
                    "9. Manufacturing Technology & Automation<br>" \
                    "10. Power Systems & Automation<br>" \
                    "11. Structural Engineering<br>" \
                    "12. VLSI Design<br>" \
                    "For Further Details <a href=https://gat.gitam.edu>Visit Here</a><br>" \
 \

# Basic Response
bas_resp = ['<strong>Okay</strong>', '<strong>Got it</strong>']

# Contact Details
college_website = bas_resp[random.randint(0, 1)] + '<a href=https://www.gitam.edu target=_blank > Click Here</a>'
college_phone_no = '<strong>Call <i><h6> 08455-221200 / 1 / 2 / 3 / 4</strong>'

