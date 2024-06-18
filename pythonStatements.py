# first launch python3 interpreter and do the following
# from app import app : necessary to run python3 commands on my local machine terminal

from app import app 
from app import db
from app.models import Student, Class, Major, StudentMajor
from datetime import datetime

# necessary to run python3 commands on my local machine terminal
app.app_context().push()

#create the database file, if it doesn't exist. 
db.create_all()

# add majors
majors = [{'name':'Cpts','department':'School of EECS'},
          {'name':'SE','department':'School of EECS'},
          {'name':'EE','department':'School of EECS'},
          {'name':'ME','department':'Mechanical Engineering'},
          {'name':'MATH','department':'Mathematics'} ]
for t in majors:
      db.session.add(Major(name=t['name'],department=t['department']))
db.session.commit()

c1 = Class(coursenum='322', major='CptS', title='Software Engineering')
db.session.add(c1)
db.session.commit()

# add students
s1 = Student(username='Chanceb', firstname='chance', lastname='bradford', email='cb@gmail.com')
s2 = Student(username='john', firstname='john', lastname='yates', email='jy@gmail.com')
db.session.add(s1)
db.session.add(s2)
db.session.commit()

major1 = Major.query.filter_by(name="CptS").first()
major2 = Major.query.filter_by(name="EE").first()

s1 = Student.query.filter_by(username='chance').first()
s2 = Student.query.filter_by(username='john').first()

assoc1 = StudentMajor(startdate=datetime.utcnow(), primary=True)
assoc1._student = s1
assoc1._major = major1
db.session.add(assoc1)
db.session.commit()

assoc2 = StudentMajor(startdate=None, primary=False)
assoc1._major = major2
s1.majorsofstudent.append(assoc2)
db.session.commit()

assoc3 = StudentMajor(startdate=datetime.utcnow(), primary=True))
assoc3._student = s2
major2.studentsinmajor.append(assoc3)
db.session.add(assoc3)
db.session.commit()

for m in s1.majorsofstudent:
      print(m)

for s in major2.studentsinmajor:
      print(s)

# #retrieve all classes a given student has enrolled in
# #alternative1
# for c in s1.classes:
#       print(c)

# #alternative2
# enrolledClasses = Class.query.join(enrolled, (enrolled.c.classid == Class.id)).filter(enrolled.c.studentid == s1.id).order_by(Class.coursenum).all()

# #check if the student is enrolled in a given class
# s1.classes.filter(enrolled.c.classid == c2.id).count() > 0

# #we can also add students to a classes roster
# s2 = Student.query.filter_by(username='john').first()
# c2.roster.append(s2)
# db.session.commit()

# for c in s2.classes:
#       print(c)

# for s in c2.roster:
#       print(s)

# # import Major model
# from app.models import Major

# # create a major
# newMajor = Major(name="CptS", department="School of EECS")
# db.session.add(newMajor)
# newMajor = Major(name="CE", department="Civil Engineering")
# db.session.add(newMajor)
# db.session.commit()
# Major.query.all()
# for m in Major.query.all():
#         print(m)


# #create class, assign classes majors to the major we just created
# from app.models import Class
# newClass = Class(coursenum='322', major="CptS", title="Software Engineering")
# db.session.add(newClass)
# newClass = Class(coursenum='315', major="CE", title="Fluid mechanics")
# db.session.add(newClass)
# db.session.commit()


# # query and print classes
# Class.query.all()
# Class.query.filter_by(major='CptS').all()
# Class.query.filter_by(major='CptS').first()
# Class.query.filter_by(major='CptS').order_by(Class.title).all()
# Class.query.filter_by(major='CptS').count()

# mymajor = Major.query.filter_by(name='CptS').first()

# for c in mymajor.classes:
#     print(c.major, c.title, c.coursenum)
