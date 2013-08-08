[CritSend](http://www.critsend.com/) Test Proyect
=====================

Description
-----------

Using Django, build a system to upload/display large TX and CSV files (over
 100MB). The user flow/error management will be very important.

Optional
--------
- Add an API

Constraints
-----------
- the application should be easy to install
- the code should be written in pure python using the Python standard library
 only (any Python2.*) and Django
- data should be managed as Unicode
- server should managed several post/get request at the same time

Input Data Format
-----------------
Data will be send throw post request and define in json format as follow:

`
{ 'data' : ' { "data1": "a1", "data2": "a2" } ' }
`

where 'data' is the key of the form where are the data
and 'values' are in a json dump to be parsed, stored, etc ..

Deliverables
------------
- the application should run on a server and able to receive remote posted
 data. We will try them.
- an access to that server so we can see how you have installed your app
- sources should available on bitbucket/github (with doc)