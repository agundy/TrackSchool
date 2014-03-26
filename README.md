4xB  |   Blackboard, But Better
===============================

Academic Management System to supplement RPI's LMS system. We felt that LMS didn't not supply all of the functionality need for students and groups on campus. Below are some of the features we would like to implement. 

Core Functionality:
-------------------
-Track School related assignments

-integrate w/ Google Calender

-Manage Class Grades

-Prioritize by grade(impact on class standing)

-Recommend best time to do homework(consider sleep/early classes)

-Actively remind to input assignments

Getting Started:
----------------
To get a working development environment
```bash
pip install -r requirements.txt
cd trackSchool
make start
```

To get a development environment with some test data already in the database, instead invoke
```bash
make test
```