<p>
    This is one solution for the Umba Test solved by Isaac Jimenez 1 Sep 2021
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

<p>
    How to run the script seed.py :
</p>
<p>
    /Flask_isa/venv/Scripts/python.exe /Flask_isa/seed/seed.py # for 150 users
    by default
</p>
<p>
    /Flask_isa/venv/Scripts/python.exe /Flask_isa/seed/seed.py -t &lt;total&gt;
    # for n users
</p>
<p>
    /Flask_isa/venv/Scripts/python.exe /Flask_isa/seed/seed.py --Total 1000 #
    for n users
</p>
<div>
    <p>
        Evidence: Unit_test_seed_1Sep2021.txt
    </p>
</div>
<p>
    <strong>Stage 2</strong>
</p>
<p>
    Create a Flask application with the following functionality:
</p>
<ul type="disc">
    <li>
        Extend the <strong><a href="http://seed.py/">seed.py</a></strong> to
create a local SQLite database if none exists. This will create a local<strong>github_users.db</strong> file under        <strong>./app/main/database.</strong>
    </li>
</ul>
<p>
    <strong>
        Solution= my seed.py create the database and table if none exits under
        /database/github_users.db
    </strong>
</p>
<p>
    And to seed a PostgreSQL database if configured. The script should
    determine the execution path depending on the existence of a config file.
    In other words, given a config file, the script will seed the configured
    database.
</p>
<p>
    <strong>
        Solution=Install PostgreSQL and create a database and Table
        GITHUB_USERS like in SQLite
    </strong>
</p>
<p>
    <strong>
        under /seed/seedpost.py special script for seed an already created db
        in PostgreSQL
    </strong>
</p>
<p>
    <strong>using /seed/database.ini file for database parameters</strong>
</p>
<p>
    <strong>
        using /seed/config.py for reading the database parameters files
    </strong>
</p>
<p>
    <strong>Evidence= Unit_test_seed_to_PostgreSQL1Sep2021.txt</strong>
</p>
