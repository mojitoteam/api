Installation Guide
==================

This page describes how to setup a local Mojito server for development
purposes.

.. note::

  Before you begin, make sure you have the recommended
  :ref:`Tools and Libraries`. This guide assumes you have installed them.

First things first, clone the Mojito repository:

.. code-block:: bash

  $ git clone https://github.com/mojitoteam/api.git
  $ cd api

You can now install the dependencies:

.. code-block:: bash

  $ poetry install
  # If you want to build the documentation, run this instead:
  $ poetry install --with docs
