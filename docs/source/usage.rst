Usage
=====

.. _installation:

Installation
------------

To try Kuwaiba, first install it to local machine using docker:

.. code-block:: console

   docker container run -dp 8080-8081:8080-8081 --name kuwaiba-server neotropic/kuwaiba:v2.1-nightly

Starting 
--------

From your browser access `<http://localhost:8080/kuwaiba>`_ and login using ``admin`` and password ``kuwaiba``

To add a new building use `Navigation` knob at the top menu and choose `Navigation` text button.
In the new window simply choose `Go to Root`, then choose a continent / country / city and from the kebab menu 
to the right of city info choose `add New Object`.
Select a class `building` and print the name. That's it. You can find the new building in the city.