.. Sample Doc for pygments-dmdl documentation master file, created by
   sphinx-quickstart on Thu Jun  2 13:30:43 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Sample Doc for pygments-dmdl's documentation!
========================================================

Contents:

.. toctree::
   :maxdepth: 2

.. code-block:: dmdl

   // hoge

   /*
    * aaa
    */

   "desc"
   @attribute.a.b.c
   @attribute()
   @attribute(value = {"a", "b"})
   sample = {
       id : INT;
       name : TEXT;
       amount : INT;
   };

.. code-block:: dmdl

   projective partial = {
       a : BOOLEAN;
       b : DECIMAL;
       c : INT;
   };

.. code-block:: dmdl

   joined sample_extend = sample -> /* comment */ {
       id -> id;
       name -> name;
       amount -> amount;
   } % id + partial -> {
       a -> a;
       b -> b;
       c -> id;
   } % id;

.. code-block:: dmdl

   summarized sum_sample = sample => {
       any id -> id; // hogehoge
       sum int -> sum_int; -- fugafuga
   } % id;




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

