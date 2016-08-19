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
 * ``U`` - user ids. Must be in format ``U<id>``. Where ``<id>`` is ID of user. For all users use ``UA``
 * ``SG`` - sonet group ids. Must be in format ``SG<id>``. Where ``<id>`` is ID of sonet group.
 * ``DR`` - departament ids. Must be in format ``DR<id>``. Where ``<id>`` is ID of departament.

**Result fields:**

Added message id

**Possible errors:**

 * ``ERROR_IN_ACTION`` - You can not add two identical consecutive messages


**Example:** ::

 bx24.call('log.blogpost.add', {
        'POST_MESSAGE': 'Test message',
        'POST_TITLE': 'Test title',
        'SPERM': {
            # Add to user with id 1 and for all authorized users
            'U': ['U1', 'UA'],

            # Add to groups with ids 12 and 14
            'SG': ['SG14', 'SG12'],

            # Add to departament with ids 1 and 9
            'DR': ['DR1', 'DR9']
        }})

**Result:** ::

 {u'result': 68}


log.blogpost.get
----------------

Get message list from Activity Stream for current users

**Result fields:**

* ``result`` - Messages list
* ``total`` - Total messages count

**Example:** ::

 bx24.call('log.blogpost.get')

**Result:** ::

 {u'result': [{u'AUTHOR_ID': u'1',
              u'BLOG_ID': u'1',
              u'CATEGORY_ID': u'',
              u'CODE': None,
              u'DATE_PUBLISH': u'20.08.2016 01:19:54',
              u'DETAIL_TEXT': u'Test message',
              u'ENABLE_COMMENTS': u'Y',
              u'HAS_COMMENT_IMAGES': None,
              u'HAS_IMAGES': u'N',
              u'HAS_PROPS': u'N',
              u'HAS_SOCNET_ALL': u'N',
              u'HAS_TAGS': u'N',
              u'ID': u'76',
              u'MICRO': u'N',
              u'NUM_COMMENTS': u'0',
              u'PUBLISH_STATUS': u'P',
              u'TITLE': u'Test title',
              u'VIEWS': None},
             ...
             ],
 u'total': 18}




log.blogpost.getusers.important
-------------------------------

Return list of user ids that read important message

**Parameters:**

* ``POST_ID`` - Important message id

**Result fields:**

* ``result`` - List of user ids that read important message

**Possible errors:**

 * ``Wrong post ID`` - If parameter ``POST_ID`` not passed to method


**Example:** ::

 bx24.call('log.blogpost.getusers.important', {'POST_ID': 66})

**Result:** ::

 {u'result': [u'1']}

