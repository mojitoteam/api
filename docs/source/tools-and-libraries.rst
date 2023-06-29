Tools and Libraries
===================

Operating System
----------------

Our development environment is based on Linux and Windows. We recommend using
Ubuntu LTS or other Debian-based distributions. Anyway, you can use any
operating system you want, but you will need to install all the required
libraries and tools by yourself.

IDEs
----

We don't have a preferred IDE. You can use any IDE you want. This is a list of
IDEs that you can use to develop the project:

* `Visual Studio Code <https://code.visualstudio.com/>`_
* `Sublime Text <https://www.sublimetext.com/>`_
* `Vim <https://www.vim.org/>`_ or `NeoVim <https://neovim.io/>`_
* `PyCharm <https://www.jetbrains.com/pycharm/>`_

Local Development
-----------------

This is a list of **essential** tools and libraries that you will need to
install in your development environment to work on the project:

* `Git <https://git-scm.com/>`_
* `Poetry 1.5 <https://python-poetry.org/>`_
* `Python 3.11 <https://www.python.org/>`_

You can install these tools with the following commands on Ubuntu:

After installing the required tools, you can install some optional tools and
libraries that will help you to develop the project:

* `Docker <https://www.docker.com/>`_ and
  `Docker Compose <https://docs.docker.com/compose/>`_
* `Git Flow <https://github.com/nvie/gitflow>`_
* `asdf <https://asdf-vm.com/>`_



Databases
---------

We use `PostgreSQL 15.3 <https://www.postgresql.org/>`_ as our main database
and we strongly recommend using it in your development environment, but you
can use any database you want since Django supports most of them. If you are
using Docker, we provide a compose file that runs the API with PostgreSQL.
