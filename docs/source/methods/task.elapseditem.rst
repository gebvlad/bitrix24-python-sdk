Task elapsed items Methods
==========================

Task elapsed items Methods


task.elapseditem.getmanifest
----------------------------
Returns a list of methods and their description.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.elapseditem.getlist
------------------------
Returns a list of entries about the elapsed time for a task.

**Parameters:**

* ``TASKID`` - Task identifier. Required parameter.
* ``ORDER`` - Array for result sorting. Sorting field may take the following values:
 * ``ID`` – identifier of the entry about elapsed time;
 * ``USER_ID`` – identifier of the user on whose behalf the entry about the elapsed time was made;
 * ``MINUTES`` – elapsed time, minutes;
 * ``SECONDS`` – elapsed time, seconds ;
 * ``CREATED_DATE`` – entry creation date;
 * ``DATE_START`` – start date;
 * ``DATE_STOP`` – end date.
  Sorting direction can take the following values:
 * ``asc`` – ascending;
 * ``desc`` – descending;
  Optional. By default it is filtered by descending of the entry elapsed time identifier.
* ``FILTER`` -  Filtered field can take the following values: 
 * ``ID`` – comment identifier;
 * ``USER_ID`` – identifier of the user on whose behalf the entry about the elapsed time was made;
 * ``CREATED_DATE`` – entry creation date.
  Filtration type may be indicated before the name of the field to be filtered:
 * ``"!"`` – not equal;
 * ``"<"`` – less;
 * ``"<="`` – less or equal;
 * ``">"`` – more;
 * ``">="`` – more or equal.
  filter values - a single value or an array.
  Optional. By default entries are not filtered.

**Result fields:**

* ``result`` -
 * ``COMMENT_TEXT`` -
 * ``CREATED_DATE`` -
 * ``DATE_START`` -
 * ``DATE_STOP`` -
 * ``ID`` -
 * ``MINUTES`` -
 * ``SECONDS`` -
 * ``SOURCE`` -
 * ``TASK_ID`` -
 * ``USER_ID`` -


**Example:** ::

 bx24.call('task.elapseditem.getlist',
              {'TASKID': 1682},
              {'ORDER': {'ID': 'asc'}},
              {'FILTER': {'USER_ID': 1, '>ID': 2}})

**Result:** ::

 {u'result': [{u'COMMENT_TEXT': u'Test description',
              u'CREATED_DATE': u'2016-08-01T00:00:00+03:00',
              u'DATE_START': u'2016-08-22T21:31:44+03:00',
              u'DATE_STOP': u'2016-08-22T21:31:44+03:00',
              u'ID': u'4',
              u'MINUTES': u'60',
              u'SECONDS': u'3600',
              u'SOURCE': u'2',
              u'TASK_ID': u'1682',
              u'USER_ID': u'1'},
             ...
             ]}

task.elapseditem.get
--------------------
Returns an entry about the elapsed time for a task by its identifier.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.elapseditem.add
--------------------
Add time spent to the task.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.elapseditem.delete
-----------------------
Deletes the entry about elapsed time.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.elapseditem.isactionallowed
--------------------------------
Verify whether the action is allowed.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.elapseditem.update
-----------------------
Change parameters of the time spent record.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::




