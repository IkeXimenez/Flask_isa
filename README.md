<p>
    This is one solution for the Umba Test solved by Isaac Ximenez 1 Sep 2021
</p>
<p>
    Python Engineer Test
</p>
<p>
    The solution is based on Stages :
</p>
<p>
    Installation:
</p>
<p>
    Install Python 3.9.6
    <a href="https://www.python.org/downloads/">
        https://www.python.org/downloads/
    </a>
</p>
<p>
    Please refer to the requirements.txt files to check all the installation
    that I used
</p>
<p>
    *Note install this version of Flask-Migrate==2.5.2. (Important)
</p>
<p>
    Install venv for environment isolation.
</p>
<p>
    <strong>Stage 1</strong>
</p>
<ul type="disc">
    <li>
Create a python shell script called        <strong><a href="http://seed.py">seed.py</a></strong> which only
        responsibility will be to populate an SQLite database, with the
information of the GitHub Users API into a        <strong>github_users</strong> table. The required fields will be:
    </li>
    <ul type="circle">
        <li>
            id, username, avatar_url, type, URL
        </li>
    </ul>
    <li>
        By default, the script should populate the database with the first 150
        users from GitHub.
    </li>
</ul>
<p>
    For this test, you will be working with the
    <a href="https://docs.github.com/en/rest/reference/users">
        GitHub Users API
    </a>
    .
</p>
<ul type="disc">
    <li>
Use the        <a href="https://api.github.com/users">https://api.github.com/users</a>
        endpoint which requires no auth
    </li>
</ul>
<p>
    Solution .
</p>
<p>
    I created /seed/seed.py
</p>
<p>
    That seeds this table in sqlLite I used an ID for processing records and
    ID_USER is the ID from the web service
</p>
<div>
    CREATE TABLE GITHUB_USERS
</div>
<div>
    (ID INT PRIMARY KEY NOT NULL,
</div>
<div>
    ID_USER INT ,
</div>
<div>
    USER_NAME CHAR(50),
</div>
<div>
    AVATAR TEXT,
</div>
<div>
    USER_TYPE CHAR(50),
</div>
<div>
    URL TEXT )
</div>
