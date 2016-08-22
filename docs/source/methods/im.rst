IM Methods
==========

IM Methods

im.notify
---------

Notify specified user.

**Parameters:**

* ``to`` - Recipient ID
* ``message`` -	Message text
* ``type`` -	Author message: ``USER`` or ``SYSTEM``. If set ``SYSTEM`` message send from application.  ``USER`` is a default value.

**Result fields:**

Notify message id.

**Example:** ::

 bx24.call('im.notify', {'to': 1,
                         'message': 'Hello, world!',
                         'type': 'SYSTEM'})

**Result:** ::

 {u'result': 24}
