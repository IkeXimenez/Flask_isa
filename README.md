<p>
    This is one solution for the Xcompany Test solved by Isaac Jimenez 1 Sep 2021
</p>
<p>
    Python Engineer Test
</p>
<p>
    Project
</p>
<p>
    /Flask_isa
</p>
<p>
        /database/ -----------------------------Directory for creating and seed
    SQLite db using seed.py
</p>
<p>
    /flaskisa/--------------------------------FLASK App wrap (package) to use
    manage.py
</p>
<p>
    /seed/------------------------------------directory of seed.py and
    seedpost.py
</p>
<p>
    App.py------------------------------------None wrap Flask application
</p>
<p>
    dbmanage.py---------------------------Flask-migrate script
</p>
<p>
    manage.py------------------------------Flask-script for Flask cmd
</p>
<p>
    requirements.txt----------------------Python installs.
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
<p>
    <strong>,</strong>
    <strong>seedToPostgreSQLevidence.jpg</strong>
</p>
<ul type="disc">
    <li>
        The Flask application will have a view that will show the information
of all the users of the database as a grid or table.        <strong>Completed</strong>
    </li>
    <li>
        Default pagination should be 25 but should be configurable using query
        parameters.
    </li>
    <li>
        <strong>Completed</strong>
    </li>
    <li>
The View needs to be responsive even with a large amount of data.        <strong>Completed</strong>
    </li>
    <li>
On clicking the profile, it should redirect to the GitHub user profile.        <strong>Completed</strong>
    </li>
</ul>
<p>
    <strong></strong>
</p>
<p>
    <strong></strong>
</p>
<p>
    <strong>Example:</strong>
</p>
<p>
    localhost:5000/
</p>
<p>
    localhost:5000/users?pagination=&lt;limit&gt;
</p>
<p>
    localhost:5000/users/&lt;int:page&gt;
</p>
<p>
    localhost:5000/users/&lt;int:page&gt;?pagination=&lt;limit&gt;
</p>
<p>
    Solution:
</p>
<p>
    <strong>Completed I am using the following routes</strong>
</p>
<p>
    <strong>@app.route("/")</strong>
</p>
<p>
    <strong>@app.route("/users")</strong>
</p>
<p>
    <strong>
        @app.route("/users/&lt;int:page_num&gt;") and pagination parameter
    </strong>
</p>
<p>
    <strong></strong>
</p>
<p>
    <strong>localhost:5000/</strong>
</p>
<p>
    <strong>localhost:5000/users?pagination=&lt;limit&gt;</strong>
</p>
<p>
    <strong>localhost:5000/users/&lt;int:page&gt;</strong>
</p>
<p>
    <strong>
        localhost:5000/users/&lt;int:page&gt;?pagination=&lt;limit&gt;
    </strong>
</p>
<p>
    <strong></strong>
</p>
<p>
    <strong>completed</strong>
</p>
<p>
    <strong>Evidence :</strong>
    <strong> </strong>
    <strong>
        <a href="http://flaskisa.herokuapp.com/">
            http://flaskisa.herokuapp.com/
        </a>
    </strong>
</p>
<p>
    <strong></strong>
</p>
<p>
    The flask application should include management scripts for running,
testing database migration, creation if necessary, using    <strong>flask-script </strong>and <strong>flask-migrate</strong> are
    recommended, but not mandatory.
</p>
<p>
    <strong>completed</strong>
</p>
<p>
    <strong>Solution= I used flask-script and flask-migrate.</strong>
</p>
<ul>
    <li>
        <strong>
            Note flask-migrate was a real pain in .. use the version I told you
            before
        </strong>
    </li>
    <li>
        <strong>/Flask_isa/manage.py</strong>
    </li>
</ul>
<p>
    <strong>
        /Flask_isa/venv/Scripts/python.exe /Flask_isa/manage.py runserver
    </strong>
</p>
<p>
    <strong>Evidence:</strong>
    <strong>UnitTestformanagepyScript1Sep2021.txt</strong>
</p>
<p>
    # Database management <strong>Flask_isa/dbmanage.py</strong>
</p>
<p>
    <strong>
        /Flask_isa/venv/Scripts/python.exe /Flask_isa/dbmanage.py db init
    </strong>
</p>
<p>
    <strong>Evidence: UnitTestdbmanageDB_INIT_1sep2021.txt</strong>
</p>
<p>
    <strong>
        /Flask_isa/venv/Scripts/python.exe /Flask_isa/dbmanage.py db migrate
    </strong>
</p>
<p>
    <strong>Evidence:</strong>
    <strong>UnitTestdbmanageDB_MIGRATE1sep2021</strong>
</p>
<p>
    ### Stage 3
</p>
<p>
    Extend the flask application to also support a RestAPI endpoint. The
    endpoint will return a JSON containing the information stored in the
    database.
</p>
<p>
    - The endpoint should support parameters
</p>
<p>
    - To filter by username, id
</p>
<p>
    - Order by id or type
</p>
<p>
    - Paginate and control pagination size
</p>
<p>
    **Example:**
</p>
<p>
    localhost:5000/api/users/profiles # 25 pagination by default
</p>
<p>
    localhost:5000/api/users/profiles?page=&lt;page&gt;
</p>
<p>
    localhost:5000/api/users/profiles?pagination=&lt;pagination&gt;
</p>
<p>
    localhost:5000/api/users/profiles?order_by=&lt;id|type&gt;
</p>
<p>
    localhost:5000/api/users/profiles?username=&lt;term&gt;
</p>
<p>
    localhost:5000/api/users/profiles?id=&lt;id&gt;
</p>
<p>
    <strong>Completed</strong>
</p>
<p>
    <strong>
        Evidence=
        <a href="http://flaskisa.herokuapp.com/">
            http://flaskisa.herokuapp.com/
        </a>
    </strong>
</p>
<p>
    <strong></strong>
</p>
<p>
    <strong>Stage 4</strong>
</p>
<p>
    This is optional if you are applying for an internship to S1 (jr) role This
    is not optional for S2 - Sr. and beyond roles
</p>
<p>
    Deploy the application into any cloud provided of your choice. AWS / Azure
    / Google Cloud / Heroku. You should send the link to your application in
    the response email.
</p>
<ul type="disc">
    <li>
The application should be deployed as a container application using        <strong>Docker</strong>
    </li>
</ul>
<p>
    <strong></strong>
</p>
<p>
    <strong>Completed</strong>
</p>
<p>
    <strong>
        Evidence=
        <a href="http://flaskisa.herokuapp.com/">
            http://flaskisa.herokuapp.com/
        </a>
    </strong>
</p>
<p>
    <strong></strong>
</p>
