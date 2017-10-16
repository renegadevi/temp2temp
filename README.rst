temp2temp
=========

**temp2temp** is a temperature conversion package between Celcius, Delisle, Fahrenheit, Kelvin, Rankine, Reaumur, Newton and Romer

.. image:: https://img.shields.io/pypi/v/temp2temp.svg
  :target: https://pypi.python.org/pypi/temp2temp
  :alt: Version on PyPI

.. image:: https://img.shields.io/pypi/l/temp2temp.svg
  :target: https://gitlab.com/renegadevi/temp2temp/raw/master/LICENCE.txt
  :alt: Licence


Introduction
------------

A complete temperature conversion package for python3. Simply convert from Celcius to example Reaumor or Newton to Kelvin.


Background
----------

I could only find packages that had Celsius to Fahrenheit or Kelvin, which I found a bit lacking as I would not define it as a 'complete' package that others may need in the future.

It's is currently in beta stage as I am now in the process now to properly test and verify the results and if there's any conversions errors that could happen.

Usage example
-------------

**Import all temperature conversions**

.. code-block:: python

    import temp2temp

    temp2temp.Celsius.to_kelvin(321)
    >>> 594.15

    temp2temp.Rankine.to_newton(321)
    >>> -31.2895

.. code-block:: python

    from temp2temp import *

    Celsius.to_kelvin(321)
    >>> 594.15

    Rankine.to_newton(321)
    >>> -31.2895


**Import just specific classes**

.. code-block:: python

    from temp2temp import Celsius, Rankine

    temp2temp.Celsius.to_kelvin(321)
    >>> 594.15

    temp2temp.Rankine.to_newton(321)
    >>> -31.2895


Licence
-------

**temp2temp** is licensed under the MIT licence. See LICENCE.txt for details.