# InternshipIMS
PyQT5 Application to count inventory (Inventory Management System)

# Installation

* Requires Python version 3.9.7 to run.
* Clone this repository to your local machine using ``git clone https://github.com/ARSTechnologies/InternshipIMS.git``.
* Create a virtual environment inside the same directory. [Tutorial link here](https://docs.python.org/3/library/venv.html).
* Run ``pip install -r requirements.txt`` to install required packages.
* Open your Terminal (on Linux) or Command Prompt (on Windows) to the root project directory and activate your virtual environment.
* Run ``execute.bat``.

# To initialize a new database

* In the script file ``db.py``, edit the variable ``database`` under the ``main()`` function to the filename of the database to your desired database.
* Edit the initializing SQL query given by the ``inventory`` variable under the ``main()`` function of the same script file.
* Run the edited file ``db.py`` with ``python db.py`` in the Terminal.
* A new database with the filename assigned to ``database`` will be created in the directory ``/db``.
* Please do not forget to rename the new database name from ``inventory.db`` in the script file ``interface.py`` with the appropriate extension.

# To transfer an existing database

* Simply copying and pasting a SQLite database file into the directory ``/db`` is sufficient to use any existing database.
* Please do not forget to rename the existing database name from ``inventory.db`` in the script file ``interface.py`` with the appropriate extension.
