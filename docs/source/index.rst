SOA-NBP
===================================

.. image:: images/logo1.svg
   :width: 600
   :alt: SOA-NBP
   :align: center

Stochastic Optoacoustic Numerical Breast Phantom (**SOA-NBP**) is a software framework to stochastically generate three-dimensional (3D) distributions of the *functional*, *optical*, and *acousitc properties* of breasts and lesions for use in computational studies of **optical**, **acoustic**, and **optoacoustic (OA) imaging**, also known as **photoacoustic imaging**. The functional, optical, and acoustic numerical breast phatnoms (NBPs) are seperately established via assignmnet of the specific properties of breasts to each tissue type in the anatomical NBPs.

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.


Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Getting started

   parameters
   tissue_insertion

.. toctree::
   :maxdepth: 1
   :caption: SOA-NBP

   soa-nbp/parameters
   soa-nbp/tissue-insertion
   soa-nbp/pde-computation
   soa-nbp/utils

.. toctree::
   :maxdepth: 1
   :caption: Examples

   examples/healthy-anat-nbp.rst
   examples/lesion-inserted-anat-nbp.rst
