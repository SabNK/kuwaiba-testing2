Best practice in documenting 
--------------------------------------

Terms
~~~~~

* Use hover links to :doc:`Ontology </concepts/ontology>` acronyms or glossary only once per page
    
    .. tip::
        
        .. code-block:: restructuredtext

            :hoverxref:`RTD <rtd-acronym>`


Formatting
~~~~~~~~~~

* Avoid simple links - keep in mind that your link names will be translated then.

    .. error:: 
        Don't: 

        .. code-block:: restructuredtext

            `github account`_
            .. _github account: https://github.com/signup

            
    .. tip:: 
        Do: 

        .. code-block:: restructuredtext

            `github account <github_>`_
            .. _github: https://github.com/signup

* Make a direct link to ``res/`` folder like ``res/<path>``

    .. error:: 
        Don't: 

        .. code-block:: restructuredtext

            .. image:: ../res/start/login_page.png

    .. tip:: 
        Do: 

        .. code-block:: restructuredtext

            .. image:: /res/start/login_page.png