Task checklist item Methods
===========================

Provides work with check list elements in tasks.


task.checklistitem.getmanifest
------------------------------
Returns the list of methods and their description.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::



task.checklistitem.getlist
--------------------------
Returns the list of elements of check lists in a task.

**Parameters:**

* ``TASKID`` - Task identifier. Required parameter.
* ``ORDER`` -  The sorting field can take the following values:
 * ``ID`` – check list element identifier;
 * ``CREATED_BY`` – identifier of the user who has created the element;
 * ``TOGGLED_BY`` – identifier of the user who has modified the check list element status;
 * ``TOGGLED_DATE`` – the time when the check list element status was changed;
 * ``TITLE`` – check list element header;
 * ``SORT_INDEX`` – element sorting index;
 * ``IS_COMPLETE`` – the element is marked as completed;
  The sorting direction can take the following values:
 * ``asc`` – ascending;
 * ``desc`` – descending;
  Optional. By default it is filtered by descending identifier of a check list element.

**Result fields:**

* ``result`` - Checklist items list
 * ``CREATED_BY`` -
 * ``ID`` -
 * ``IS_COMPLETE`` -
 * ``SORT_INDEX`` -
 * ``TASK_ID`` -
 * ``TITLE`` -
 * ``TOGGLED_BY`` -
 * ``TOGGLED_DATE`` -

**Example:** ::

 bx24.call('task.checklistitem.getlist',
              {'TASKID': 1682},
              {'ORDER': {'ID': 'asc'}})

**Result:** ::

 {u'result': [{u'CREATED_BY': u'1',
              u'ID': u'2',
              u'IS_COMPLETE': u'N',
              u'SORT_INDEX': u'0',
              u'TASK_ID': u'1682',
              u'TITLE': u'Test item',
              u'TOGGLED_BY': None,
              u'TOGGLED_DATE': u''},
             ...
             ]}


task.checklistitem.get
----------------------
Returns a check list element by its identifier.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::


task.checklistitem.add
----------------------
Adds a new check list element to the task.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::


task.checklistitem.update
-------------------------

Updates check list element data.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::


**Result:** ::


task.checklistitem.delete
-------------------------
Deletes a check list element.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::


task.checklistitem.complete
---------------------------
Marks a check list element as completed.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::


task.checklistitem.renew
------------------------
Marks a completed check list element as active again.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::


task.checklistitem.moveafteritem
--------------------------------
Moves a check list element in the list and places it after the indicated one.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::


task.checklistitem.isactionallowed
----------------------------------
Checks if an action is permitted for a check list element.

**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -

**Example:** ::



**Result:** ::




