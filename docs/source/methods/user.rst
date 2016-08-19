User Methods
============

User Methods


user.fields
-----------

List user field names.

**Result fields:**

List user fields names


**Example:** ::

 bx24.call('user.fields')


**Result:** ::

 {u'result': {u'ACTIVE': u'Active',
             u'EMAIL': u'E-mail',
             u'ID': u'ID',
             u'LAST_NAME': u'Last name',
             u'NAME': u'First name',
             u'PERSONAL_BIRTHDAY': u'Date of birth',
             u'PERSONAL_CITY': u'City',
             u'PERSONAL_COUNTRY': u'Country',
             u'PERSONAL_FAX': u'Fax',
             u'PERSONAL_GENDER': u'Sex',
             u'PERSONAL_ICQ': u'ICQ',
             u'PERSONAL_MOBILE': u'Private cellular',
             u'PERSONAL_PAGER': u'Pager',
             u'PERSONAL_PHONE': u'Private phone',
             u'PERSONAL_PHOTO': u'Photo',
             u'PERSONAL_PROFESSION': u'Job title',
             u'PERSONAL_STATE': u'State',
             u'PERSONAL_STREET': u'Street',
             u'PERSONAL_WWW': u'Home page',
             u'PERSONAL_ZIP': u'Zip',
             u'SECOND_NAME': u'Middle name',
             u'UF_DEPARTMENT': u'Departments',
             u'UF_DISTRICT': u'District',
             u'UF_FACEBOOK': u'Facebook',
             u'UF_INTERESTS': u'Interests',
             u'UF_LINKEDIN': u'LinkedIn',
             u'UF_PHONE_INNER': u'Extension number',
             u'UF_SKILLS': u'Skills',
             u'UF_SKYPE': u'Skype',
             u'UF_TWITTER': u'Twitter',
             u'UF_WEB_SITES': u'Other websites',
             u'UF_XING': u'Xing',
             u'WORK_COMPANY': u'Company',
             u'WORK_PHONE': u'Company phone',
             u'WORK_POSITION': u'Position'}}


user.current
------------

Retrieve current user information.


**Result fields:**

List user fields values


**Example:** ::

 bx24.call('user.current')


**Result:** ::

 {u'result': {u'ACTIVE': True,
             u'EMAIL': u'user@example.com',
             u'ID': u'1',
             u'LAST_NAME': u'Test',
             u'NAME': u'User',
             u'PERSONAL_BIRTHDAY': u'',
             u'PERSONAL_CITY': None,
             u'PERSONAL_COUNTRY': None,
             u'PERSONAL_FAX': None,
             u'PERSONAL_GENDER': u'',
             u'PERSONAL_ICQ': None,
             u'PERSONAL_MOBILE': None,
             u'PERSONAL_PAGER': None,
             u'PERSONAL_PHONE': None,
             u'PERSONAL_PHOTO': None,
             u'PERSONAL_PROFESSION': None,
             u'PERSONAL_STATE': None,
             u'PERSONAL_STREET': None,
             u'PERSONAL_WWW': None,
             u'PERSONAL_ZIP': None,
             u'SECOND_NAME': None,
             u'UF_DEPARTMENT': [1],
             u'UF_DISTRICT': None,
             u'UF_FACEBOOK': None,
             u'UF_INTERESTS': None,
             u'UF_LINKEDIN': None,
             u'UF_PHONE_INNER': None,
             u'UF_SKILLS': None,
             u'UF_SKYPE': None,
             u'UF_TWITTER': None,
             u'UF_WEB_SITES': None,
             u'UF_XING': None,
             u'WORK_COMPANY': None,
             u'WORK_PHONE': None,
             u'WORK_POSITION': None}}


user.add
--------

Invite user.

**Parameters:**

* ``EMAIL`` - User email for send invite

**Result fields:**

User id

**Possible errors:**

 * A user with e-mail ``email`` already exists.


**Example:** ::

 bx24.call('user.add', {'EMAIL': 'user@example.com'})

**Result:** ::

 {u'result': 6}

user.update
-----------

Update user information.

**Parameters:**

* ``ID`` - User id. Field is required
* ``users.fields`` - Any ``user.fields`` except ``ID`` and ``EMAIL``

**Possible errors:**

 * Invalid file type for field PERSONAL_PHOTO // TODO Example update photo

**Example:** ::

 bx24.call('user.update', {'ID': 1, 'NAME': 'Another name'})

**Result:** ::

 {u'result': True}


user.get
--------

List filtered users.

**Parameters:**

* ``sort`` - Sorted-by field
* ``order`` - Sort order: ``ASC`` - ascending, ``DESC`` - descending
* ``users.fields`` - In addition, any ``user.fields`` parameters may be used as filter.

**Result fields:**

List of users


**Example:** ::

 bx24.call('user.get', {'sort': 'ID', 'order': 'DESC', 'EMAIL': '%@example.com%'})


**Result:** ::

 {u'result': [{u'ACTIVE': True,
              u'EMAIL': u'user60@example.com',
              u'ID': u'60',
              u'LAST_NAME': 'Test',
              u'NAME': 'User60',
              u'PERSONAL_BIRTHDAY': u'',
              u'PERSONAL_CITY': None,
              u'PERSONAL_COUNTRY': None,
              u'PERSONAL_FAX': None,
              u'PERSONAL_GENDER': u'',
              u'PERSONAL_ICQ': None,
              u'PERSONAL_MOBILE': None,
              u'PERSONAL_PAGER': None,
              u'PERSONAL_PHONE': None,
              u'PERSONAL_PHOTO': None,
              u'PERSONAL_PROFESSION': None,
              u'PERSONAL_STATE': None,
              u'PERSONAL_STREET': None,
              u'PERSONAL_WWW': None,
              u'PERSONAL_ZIP': None,
              u'SECOND_NAME': None,
              u'UF_DEPARTMENT': False,
              u'UF_DISTRICT': None,
              u'UF_FACEBOOK': None,
              u'UF_INTERESTS': None,
              u'UF_LINKEDIN': None,
              u'UF_PHONE_INNER': None,
              u'UF_SKILLS': None,
              u'UF_SKYPE': None,
              u'UF_TWITTER': None,
              u'UF_WEB_SITES': None,
              u'UF_XING': None,
              u'WORK_COMPANY': None,
              u'WORK_PHONE': None,
              u'WORK_POSITION': None},
              ...
             ],
 u'total': 50}

