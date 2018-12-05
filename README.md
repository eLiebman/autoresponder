# autoresponder
A simple sms autoresponder for Google Voice.

googlevoice must be installed for this code to work.
Find it here:
https://github.com/jaraco/googlevoice

Once that's taken care of, you can run this program in the command line with
`$ python autoresponder.py`
It will prompt you for your Google Voice email and password to login.
Once authenticated, the app will check your Google Voice account for unread sms messages,
and reply automatically (edit the `response` variable in the file to set your custom reply).
The message will then be maked as read.
The app will check for new unread messages every 30s as long as it's running.
