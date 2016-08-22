Task item methods
=================

Task item methods


task.item.getmanifest
---------------------
Show list of methods.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.add
-------------
Create new task.

**Parameters:**

* ``TASKDATA`` - task data fields (TITLE, DESCRIPTION, etc.).

**Result fields:**

Task id

**Example:** ::

 bx24.call('task.item.add', {
        'TASKDATA':{
            'TITLE': 'Test task',
            'DESCRIPTION': 'Task description',
            'RESPONSIBLE_ID': 1
        }
    })


**Result:** ::

 {u'result': 2104}




task.item.list
--------------
Return tasks


**Parameters:**

* ``ORDER`` - Sorting. Fsield is required. The Sort field may have the following values:
 * ``TITLE`` - Task name;
 * ``DATE_START`` - Start date;
 * ``DEADLINE`` - Deadline;
 * ``STATUS`` - Status;
 * ``PRIORITY`` - Priority;
 * ``MARK`` - Rating;
 * ``СREATED_BY`` - Creator;
 * ``RESPONSIBLE_ID`` - Person responsible;
 * ``GROUP_ID`` - Workgroup.
  Sort order may have the following values:
 * ``asc`` - ascending;
 * ``desc`` - descending;
* ``FILTER`` - Filtered field may have the following values:

 * ``ID`` - Task ID;
 * ``PARENT_ID`` - Parent task ID;
 * ``GROUP_ID`` - Workgroup ID;
 * ``CREATED_BY`` - Creator;
 * ``STATUS_CHANGED_BY`` - User who modified task status last;
 * ``PRIORITY`` - Priority;
 * ``FORUM_TOPIC_ID`` - Forum topic ID;
 * ``RESPONSIBLE_ID`` - Person responsible;
 * ``TITLE`` - Task name (May be searched by [%_] template) ;
 * ``TAG`` -  Tag;
 * ``REAL_STATUS`` - Task status. Constants corresponding to task status:
  * ``STATE_NEW`` = 1;
  * ``STATE_PENDING`` = 2;
  * ``STATE_IN_PROGRESS`` = 3;
  * ``STATE_SUPPOSEDLY_COMPLETED`` = 4;
  * ``STATE_COMPLETED`` = 5;
  * ``STATE_DEFERRED`` = 6;
  * ``STATE_DECLINED`` = 7;
 * ``STATUS`` - Sorting status. Similar to REAL_STATUS, but has two additional meta status:
  * ``-2`` - Overdue task;
  * ``-1`` - Newly created task.
 * ``MARK`` - Rating;
 * ``XML_ID`` - External code;
 * ``SITE_ID`` - Website ID;
 * ``ADD_IN_REPORT`` - Add task to report (Y|N);
 * ``DATE_START`` - Start date;
 * ``DEADLINE`` - Deadline;
 * ``CREATED_DATE`` - Date created;
 * ``CLOSED_DATE`` - Date closed;
 * ``CHANGED_DATE`` - Date last modified;
 * ``ACCOMPLICE`` - Participant ID;
 * ``AUDITOR`` - Observer ID;
 * ``DEPENDS_ON`` - Previous task ID;
 * ``ONLY_ROOT_TASKS`` -  Root tasks only (Y|N);
 * ``SUBORDINATE_TASKS`` -  Current user's and subordinates' tasks (Y|N);
 * ``OVERDUED`` -  Were overdue (Y|N);
 * ``DEPARTMENT_ID`` - Department ID.
  Filter type may be specified before filtered field name:
 * ``"!"`` - not equal to
 * ``"<"`` - less than
 * ``"<="`` - less than or equal to
 * ``">"`` - greater than
 * ``">="`` - greater than or equal to
  "filter value" - single value or dict.
* ``NAV_PARAMS`` - Page-by-page navigation. The following options are available:
 * ``nPageSize`` - Number of elements on a page,
 * ``iNumPage`` - Page number.

**Result fields:**

* ``next`` - Offset for next page
* ``total`` - Total elements by filter
* ``result`` - Tasks list
 * ``ACCOMPLICES`` - Contains the user ID's of persons involved in the task (shown in the user interface as participants).
 * ``ADD_IN_REPORT`` - A boolean (Y/N) value which, if set to "Y", includes the task in the performance report.
 * ``ALLOWED_ACTIONS`` -
  * ``ACTION_ACCEPT`` - 
  * ``ACTION_ADD_FAVORITE`` - 
  * ``ACTION_APPROVE`` - 
  * ``ACTION_CHANGE_DEADLINE`` - A boolean (Y/N) value which, if set to "Y", specifies that a responsible person associated with the task is allowed to shift the deadline date.
  * ``ACTION_CHANGE_DIRECTOR`` - 
  * ``ACTION_CHECKLIST_ADD_ITEMS`` - 
  * ``ACTION_CHECKLIST_REORDER_ITEMS`` - 
  * ``ACTION_COMPLETE`` - 
  * ``ACTION_CREATE`` - 
  * ``ACTION_DECLINE`` - 
  * ``ACTION_DEFER`` - 
  * ``ACTION_DELEGATE`` - 
  * ``ACTION_DELETE_FAVORITE`` - 
  * ``ACTION_DISAPPROVE`` - 
  * ``ACTION_EDIT`` - 
  * ``ACTION_ELAPSED_TIME_ADD`` - 
  * ``ACTION_PAUSE`` - 
  * ``ACTION_REMOVE`` - 
  * ``ACTION_RENEW`` - 
  * ``ACTION_START`` - 
  * ``ACTION_START_TIME_TRACKING`` -
 * ``ALLOW_CHANGE_DEADLINE`` - 
 * ``ALLOW_TIME_TRACKING`` - A boolean (Y/N) value which, if set to "Y", specifies that the system keeps tracking of the time spent for the task.
 * ``AUDITORS`` - Contains the user ID's of persons who were set to monitor task progress and results (shown in the user interface as observers).
 * ``CHANGED_BY`` - The user ID of a person who last updated the task.
 * ``CHANGED_DATE`` - Specifies the date the task was last updated.
 * ``CLOSED_BY`` - 	The user ID of a person who completed the task.
 * ``CLOSED_DATE`` - Specifies the date the task was completed.
 * ``COMMENTS_COUNT`` - Contains the number of forum comments.
 * ``CREATED_BY`` - Specifies the user ID of a person who created the task.
 * ``CREATED_BY_LAST_NAME`` - The last name of the task creator.
 * ``CREATED_BY_NAME`` - Contains the first name of a person who created the task.
 * ``CREATED_BY_SECOND_NAME`` - The second name of the task creator.
 * ``CREATED_DATE`` - Specifies the date the task was created.
 * ``DATE_START`` - Specifies the date the task was started.
 * ``DEADLINE`` - Specifies the task deadline date.
 * ``DECLINE_REASON`` - A text description of the reason for rejecting the task.
 * ``DESCRIPTION`` - Specifies the task description.
 * ``DESCRIPTION_IN_BBCODE`` - Specifies the user ID of a person who created the task.
 * ``DURATION_FACT`` - Specifies the time required to complete the task, in minutes.
 * ``DURATION_PLAN`` - 
 * ``DURATION_TYPE`` - 
 * ``END_DATE_PLAN`` - Specifies the date when the task is planned to be finished.
 * ``FAVORITE`` - 
 * ``FORKED_BY_TEMPLATE_ID`` - Contains the ID of a template used to create the task. This field may be empty for tasks created in outdated versions.
 * ``FORUM_ID`` - Specifies the ID of the forum containing comments to the task.
 * ``FORUM_TOPIC_ID`` - Specifies the ID of the forum topic containing comments to the task.
 * ``GROUP_ID`` - Specifies the ID of a workgroup to which this task relates.
 * ``GUID`` - A GUID (globally unique identifier) associated with the task. It can be said, with a fair amount of confidence, that this identifier will always remain unique across multiple databases.
 * ``ID`` - The current task ID. The identifier is unique across the database.
 * ``MARK`` - The rating score given by a task creator.
 * ``MATCH_WORK_TIME`` - 
 * ``MULTITASK`` - 
 * ``PARENT_ID`` - Specifies the ID of a parent task.
 * ``PRIORITY`` - Determines the task priority level.
 * ``REAL_STATUS`` - Determines the task's real status set using the ``STATUS`` field. This field is read-only.
 * ``RESPONSIBLE_ID`` - The user ID of a person to whom the task is assigned.
 * ``RESPONSIBLE_LAST_NAME`` - The last name of the task's responsible person.
 * ``RESPONSIBLE_NAME`` - Contains the first name of a person to whom the task is assigned (a responsible person).
 * ``RESPONSIBLE_SECOND_NAME`` - The second name of the task's responsible person.
 * ``SITE_ID`` - Specifies the ID of the site on which the task was created.
 * ``START_DATE_PLAN`` - Specifies the date when the task is scheduled to start.
 * ``STATUS`` - Use this field to set the meta status for a task.
 * ``STATUS_CHANGED_BY`` - The user ID of a person who changed the task status.
 * ``STATUS_CHANGED_DATE`` - Specifies the date the task status was changed.
 * ``SUBORDINATE`` - A boolean (Y/N) value which, if set to "Y", specifies that at least one of the task participants is subordinate to a current user.
 * ``TASK_CONTROL`` - A boolean (Y/N) value which, if set to "Y", specifies that the task result needs to be approved by a creator. Otherwise, the task will auto close once marked as completed.
 * ``TIME_ESTIMATE`` - Specifies a time estimate for the task.
 * ``TIME_SPENT_IN_LOGS`` - Specifies the actual time spent for the task, in seconds.
 * ``TITLE`` - Specifies the task name.
 * ``VIEWED_DATE`` - Contains the date the task was last viewed in the public area by a currently logged in user.

**Example:** ::

 bx24.call('task.item.list',
            {'ORDER': {'GROUP_ID': 'asc'}},
            {'FILTER': {'CREATED_BY': {0: 1}}},
            {'PARAMS': {'NAV_PARAMS': {'nPageSize': 50, 'iNumPage': 2}}}
        )


**Result:** ::

 {u'next': 2,
 u'result': [{u'ACCOMPLICES': [],
              u'ADD_IN_REPORT': u'N',
              u'ALLOWED_ACTIONS': {u'ACTION_ACCEPT': False,
                                   u'ACTION_ADD_FAVORITE': True,
                                   u'ACTION_APPROVE': False,
                                   u'ACTION_CHANGE_DEADLINE': True,
                                   u'ACTION_CHANGE_DIRECTOR': True,
                                   u'ACTION_CHECKLIST_ADD_ITEMS': True,
                                   u'ACTION_CHECKLIST_REORDER_ITEMS': True,
                                   u'ACTION_COMPLETE': True,
                                   u'ACTION_CREATE': False,
                                   u'ACTION_DECLINE': False,
                                   u'ACTION_DEFER': True,
                                   u'ACTION_DELEGATE': True,
                                   u'ACTION_DELETE_FAVORITE': False,
                                   u'ACTION_DISAPPROVE': False,
                                   u'ACTION_EDIT': True,
                                   u'ACTION_ELAPSED_TIME_ADD': True,
                                   u'ACTION_PAUSE': False,
                                   u'ACTION_REMOVE': True,
                                   u'ACTION_RENEW': False,
                                   u'ACTION_START': True,
                                   u'ACTION_START_TIME_TRACKING': False},
              u'ALLOW_CHANGE_DEADLINE': u'N',
              u'ALLOW_TIME_TRACKING': u'N',
              u'AUDITORS': [],
              u'CHANGED_BY': u'1',
              u'CHANGED_DATE': u'2016-08-21T16:00:44+03:00',
              u'CLOSED_BY': None,
              u'CLOSED_DATE': u'',
              u'COMMENTS_COUNT': u'18',
              u'CREATED_BY': u'1',
              u'CREATED_BY_LAST_NAME': u'Test user',
              u'CREATED_BY_NAME': u'',
              u'CREATED_BY_SECOND_NAME': None,
              u'CREATED_DATE': u'2016-08-21T15:42:46+03:00',
              u'DATE_START': u'',
              u'DEADLINE': u'',
              u'DECLINE_REASON': None,
              u'DESCRIPTION': u'',
              u'DESCRIPTION_IN_BBCODE': u'Y',
              u'DURATION_FACT': None,
              u'DURATION_PLAN': None,
              u'DURATION_TYPE': u'days',
              u'END_DATE_PLAN': u'',
              u'FAVORITE': u'N',
              u'FORKED_BY_TEMPLATE_ID': None,
              u'FORUM_ID': u'11',
              u'FORUM_TOPIC_ID': u'24',
              u'GROUP_ID': u'0',
              u'GUID': u'{e0216129-7751-47b4-beb2-461ea1e87f99}',
              u'ID': u'1684',
              u'MARK': None,
              u'MATCH_WORK_TIME': u'N',
              u'MULTITASK': u'N',
              u'PARENT_ID': None,
              u'PRIORITY': u'1',
              u'REAL_STATUS': u'2',
              u'RESPONSIBLE_ID': u'1',
              u'RESPONSIBLE_LAST_NAME': u'Test user',
              u'RESPONSIBLE_NAME': u'',
              u'RESPONSIBLE_SECOND_NAME': None,
              u'SITE_ID': u's1',
              u'START_DATE_PLAN': u'',
              u'STATUS': u'2',
              u'STATUS_CHANGED_BY': u'1',
              u'STATUS_CHANGED_DATE': u'2016-08-21T15:42:46+03:00',
              u'SUBORDINATE': u'N',
              u'TASK_CONTROL': u'N',
              u'TIME_ESTIMATE': u'0',
              u'TIME_SPENT_IN_LOGS': None,
              u'TITLE': u'Test task #1',
              u'VIEWED_DATE': u'2016-08-21T16:01:07+03:00'}],
 u'total': 212}



task.item.getdata
-----------------
Return task data array.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::



task.item.update
----------------
Update task information.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.delete
----------------
Delete task.
task.item.getdescription
------------------------
Return task description.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.getfiles
------------------
Return array of links to files attached to the task.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.getdependson
----------------------
Return array of parent task IDs.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.getallowedactions
---------------------------
Return array of IDs of allowed task actions.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.getallowedtaskactionsasstrings
----------------------------------------
Return array whose keys are action names and values show whether action is allowed.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.isactionallowed
-------------------------
Assert whether action is allowed.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.delegate
------------------
Delegate task to new user.


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.startexecution
------------------------
Change task status to "In Progress".


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.defer
---------------
Change task status to "Deferred".


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.complete
------------------
Change task status to "Completed" or "Supposedly completed (requires creator's attention)".


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.renew
---------------
Change task status to "Pending".


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.approve
-----------------
Change status of task, waiting for confirmation to "Completed".


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::


task.item.disapprove
--------------------
Change status of task, waiting for confirmation to "Pending".



**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::




----------------


**Parameters:**

* ```` -

**Result fields:**

* ```` -

**Possible errors:**

 * ```` -


**Example:** ::



**Result:** ::



