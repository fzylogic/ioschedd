~~~~~~~~
ioschedd
~~~~~~~~

A small configurable daemon to control selection of IO Scheduler options
on a linux server.

Description:
============

ioschedd allows a user to fine-tune their IO scheduler on a per-device basis.

This is particularly handy in the following scenarios:

* A server may boot off of a slow on-board IDE drive, but store all of its data on a fancy RAID controller.
  In this case, you likely want CFQ or deadline on hda, but noop on sd*
* Perhaps your server is hosted somewhere out of your control and you don't have access to change boot parameters
  (say, it's netbooted by your provider) and you'd like to make sure your IO scheduler is changed before your application
  is launched


Dependencies:
=============
Python 2.7


Python Module Dependencies:
===========================
* daemon
* pyudev 0.16+
* yaml
