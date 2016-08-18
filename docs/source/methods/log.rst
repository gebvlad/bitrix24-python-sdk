Activity Stream Methods
=======================

Activity Stream methods

log.blogpost.add
----------------

Add a record to the Activity Stream as the current user.

**Parameters:**

* ``POST_MESSAGE`` - Message text
* ``POST_TITLE`` - Message title (optional)
* ``SPERM`` - View message permissions (optional), all authorized users - "UA" by default


**Example:** ::

 bx24.call('log.blogpost.add', {
        'POST_MESSAGE': 'Test message',
        'POST_TITLE': 'Test title',
        'SPERM': {
            'U': ['U1', 'UA'],
            'SG': ['SG14', 'SG12'],
            'DR': ['DR1', 'DR9']
        }})

**Result:** ::

 {u'result': 68}


log.blogpost.get
----------------

**Parameters:**

* ```` -

**Example:** ::

**Result:** ::




log.blogpost.getusers.important
-------------------------------

**Parameters:**

* ```` -

**Example:** ::

**Result:** ::
