.. include:: substitutions.rst

How to contribute
=================

Code contribution
*****************

Based on:

* http://nvie.com/posts/a-successful-git-branching-model/
* https://help.github.com/articles/fork-a-repo/
* https://help.github.com/articles/about-pull-requests/
* https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/
* https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
* https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

.. note::
    Following procedure is for Windows platform

If you want to contribute your code to |pybio|, please follow this steps:

Setup
-----

1. Fork |pybio|

    a. Navigate to https://github.com/genadijrazdorov/pybio
    #. Fork your own copy of |pybio| by cliking on *Fork* button
    #. You are navigated to your copy GitHub page

#. Clone your fork locally 

    a. Click on *Clone or download* button
    #. Copy your fork url by clicking on *Copy to clipboard* button
    #. Open *Git Bash* console
    #. Change directory to desired one:
        
        .. sourcecode:: bash

            $ cd path/to/local/clone/parent

    #. Clone your fork:

        .. sourcecode:: bash

            $ git clone <Shift+Ins>

#. Add upstream repo

    .. sourcecode:: bash

        $ cd pybio
        $ git remote add upstream https://github.com/genadijrazdorov/pybio.git


*Feature* development
---------------------

1. Checkout develop branch:

    .. sourcecode:: bash

        $ git checkout develop
        
#. Sync with upstream:

    .. sourcecode:: bash

        $ git pull upstream

#. Create and checkout new *feature* branch:

    .. sourcecode:: bash

        $ git checkout -b new-feature-name

#. Develop
           
    a. Create documentation, unit-tests and implementation for new feature
    #. Check your implementation by running doctests and pytests
    #. Add and commit your changes

#. Push your changes to origin:

    .. sourcecode:: bash
        
        $ git push -u origin

#. Create pull request online

    a. Follow instructions from: https://help.github.com/articles/creating-a-pull-request-from-a-fork/

#. Discuss and modify your code with |pybio| developers

#. After *feature* branch is merged sync your fork

    a. Pull from upstream:

        .. sourcecode:: bash

            $ git checkout develop
            $ git pull upstream

    #. Push to origin

        .. sourcecode:: bash

            $ git push




