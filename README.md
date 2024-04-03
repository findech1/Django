How To Install the Django Web Framework on Ubuntu 22.04
Published on May 12, 2022
Django
Python Frameworks
Ubuntu 22.04
Python
Ubuntu
Default avatar
By Brian Boucheron and Jamon Camisso

How To Install the Django Web Framework on Ubuntu 22.04
Not using Ubuntu 22.04?
Choose a different version or distribution.
Ubuntu 22.04
Introduction
Django is a full-featured Python web framework for developing dynamic websites and applications. Using Django, you can quickly create Python web applications and rely on the framework to do a good deal of the heavy lifting.

In this guide, you will get Django up and running on an Ubuntu 22.04 server. After installation, you will start a new project to use as the basis for your site.

Different Methods
There are different ways to install Django, depending upon your needs and how you want to configure your development environment. These have different advantages and one method may lend itself better to your specific situation than others.

Some of the different methods include:

Global install from packages: The official Ubuntu repositories contain Django packages that can be installed with the conventional apt package manager. This is simple, but not as flexible as some other methods. Also, the version contained in the repositories may lag behind the official versions available from the project.
Install with pip in a virtual environment: You can create a self-contained environment for your projects using tools like venv and virtualenv. A virtual environment allows you to install Django in a project directory without affecting the larger system, along with other per-project customizations and packages. This is typically the most practical and recommended approach to working with Django.
Install the development version with git: If you wish to install the latest development version instead of the stable release, you can acquire the code from the Git repo. This is necessary to get the latest features/fixes and can be done within your virtual environment. Development versions do not have the same stability guarantees as more stable versions, however.
Prerequisites
Before you begin, you should have a non-root user with sudo privileges available on your Ubuntu 22.04 server. To set this up, follow our Ubuntu 22.04 initial server setup guide.

Global Install from Packages
If you wish to install Django using the Ubuntu repositories, the process is very straightforward.

First, update your local package index with apt:

sudo apt update
Next, check which version of Python you have installed. 22.04 ships with Python 3.10 by default, which you can verify by typing:

python3 -V
You should see output like this:

Output
Python 3.10.4
Next, install Django:

sudo apt install python3-django
You can test that the installation was successful by typing:

django-admin --version
Output
3.2.12
This means that the software was successfully installed. You may also notice that the Django version is not the latest stable version. To learn more about how to use the software, skip ahead to learn how to create sample project.

Install with pip in a Virtual Environment
The most flexible way to install Django on your system is within a virtual environment. We will show you how to install Django in a virtual environment that we will create with the venv module, part of the standard Python 3 library. This tool allows you to create virtual Python environments and install Python packages without affecting the rest of the system. You can therefore select Python packages on a per-project basis, regardless of conflicts with other projects’ requirements.

Let’s begin by refreshing the local package index:

sudo apt update
Check the version of Python you have installed:

python3 -V
Output
Python 3.10.4
Next, let’s install pip and venv from the Ubuntu repositories:

sudo apt install python3-pip python3-venv
Now, whenever you start a new project, you can create a virtual environment for it. Start by creating and moving into a new project directory:

mkdir ~/newproject
cd ~/newproject
Next, create a virtual environment within the project directory using the python command that’s compatible with your version of Python. We will call our virtual environment my_env, but you should name it something descriptive:

python3 -m venv my_env
This will install standalone versions of Python and pip into an isolated directory structure within your project directory. A directory will be created with the name you select, which will hold the file hierarchy where your packages will be installed.

To install packages into the isolated environment, you must activate it by typing:

source my_env/bin/activate
Your prompt should change to reflect that you are now in your virtual environment. It will look something like (my_env)username@hostname:~/newproject$.

In your new environment, you can use pip to install Django. Regardless of your Python version, pip should just be called pip when you are in your virtual environment. Also note that you do not need to use sudo since you are installing locally:

pip install django
You can verify the installation by typing:

django-admin --version
Output
4.0.4
Note that your version may differ from the version shown here.

To leave your virtual environment, you need to issue the deactivate command from anywhere on the system:

deactivate
Your prompt should revert to the conventional display. When you wish to work on your project again, re-activate your virtual environment by moving back into your project directory and activating:

cd ~/newproject
source my_env/bin/activate
Development Version Install with Git
If you need a development version of Django, you can download and install Django from its Git repository. Let’s do this from within a virtual environment.

First, let’s update the local package index:

sudo apt update
Check the version of Python you have installed:

python3 -V
Output
Python 3.10.4
Next, install pip and venv from the official repositories:

sudo apt install python3-pip python3-venv
The next step is cloning the Django repository. Between releases, this repository will have more up-to-date features and bug fixes at the possible expense of stability. You can clone the repository to a directory called ~/django-dev within your home directory by typing:

git clone git://github.com/django/django ~/django-dev
Change to this directory:

cd ~/django-dev
Create a virtual environment using the python command that’s compatible with your installed version of Python:

python3 -m venv my_env
Activate it:

source my_env/bin/activate
Next, you can install the repository using pip. The -e option will install in “editable” mode, which is necessary when installing from version control:

pip install -e ~/django-dev
You can verify that the installation was successful by typing:

django-admin --version
Output
4.0.4.2
Again, the version you see displayed may not match what is shown here.

You now have the latest version of Django in your virtual environment.

Creating a Sample Project
With Django installed, you can begin building your project. We will go over how to create a project and test it on your development server using a virtual environment.

First, create a directory for your project and change into it:

mkdir ~/django-test
cd ~/django-test
Next, create your virtual environment:

python3 -m venv my_env
Activate the environment:

source my_env/bin/activate
Install Django:

pip install django
To build your project, you can use django-admin with the startproject command. We will call our project djangoproject, but you can replace this with a different name. startproject will create a directory within your current working directory that includes:

A management script, manage.py, which you can use to administer various Django-specific tasks.
A directory (with the same name as the project) that includes the actual project code.
To avoid having too many nested directories, however, let’s tell Django to place the management script and inner directory in the current directory (notice the ending dot):

django-admin startproject djangoproject .
To migrate the database (this example uses SQLite by default), let’s use the migrate command with manage.py. Migrations apply any changes you’ve made to your Django models to your database schema.

To migrate the database, type:

python manage.py migrate
You will see output like the following:

Output
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
Finally, let’s create an administrative user so that you can use the Djano admin interface. Let’s do this with the createsuperuser command:

python manage.py createsuperuser
You will be prompted for a username, an email address, and a password for your user.

Modifying ALLOWED_HOSTS in the Django Settings
To successfully test your application, you will need to modify one of the directives in the Django settings.

Open the settings file by typing:

nano ~/django-test/djangoproject/settings.py
Inside, locate the ALLOWED_HOSTS directive. This defines a list of addresses or domain names that may be used to connect to the Django instance. An incoming request with a Host header that is not in this list will raise an exception. Django requires that you set this to prevent a certain class of security vulnerability.

In the square brackets, list the IP addresses or domain names that are associated with your Django server. Each item should be listed in quotations, with separate entries separated by a comma. If you want requests for an entire domain and any subdomains, prepend a period to the beginning of the entry:

~/django-test/djangoproject/settings.py
ALLOWED_HOSTS = ['your_server_ip_or_domain', 'your_second_ip_or_domain', . . .]
When you are finished, save the file and exit your editor.

Testing the Development Server
Once you have a user, you can start up the Django development server to see what a fresh Django project looks like. You should only use this for development purposes. When you are ready to deploy, be sure to follow Django’s guidelines on deployment carefully.

Before you try the development server, make sure you open the appropriate port in your firewall. If you followed the initial server setup guide and are using UFW, you can open port 8000 by typing:

sudo ufw allow 8000
Start the development server:

python manage.py runserver your_server_ip:8000
Visit your server’s IP address followed by :8000 in your web browser:

http://your_server_ip:8000
You should see something that looks like this:

Django public page

To access the admin interface, add /admin/ to the end of your URL:

http://your_server_ip:8000/admin/
This will take you to a log in screen:

Django admin login

If you enter the admin username and password that you just created, you will have access to the main admin section of the site:

Django admin page

For more information about working with the Django admin interface, please see “How To Enable and Connect the Django Admin Interface.”

When you are finished looking through the default site, you can stop the development server by typing CTRL-C in your terminal.

The Django project you’ve created provides the structural basis for designing a more complete site. Check out the Django documentation for more information about how to build your applications and customize your site.

Conclusion
You should now have Django installed on your Ubuntu 22.04 server, providing the main tools you need to create powerful web applications. You should also know how to start a new project and launch the developer server. Leveraging a complete web framework like Django can help make development faster, allowing you to concentrate only on the unique aspects of your applications.

If you would like more information about working with Django, including in-depth discussions of things like models and views, please see our Django development series.
