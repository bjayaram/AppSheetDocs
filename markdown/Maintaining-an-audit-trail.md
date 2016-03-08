#  Maintaining an audit trail


January 23, 2016 00:12

In some apps, it is important to know who made each update. A pre-requisite
for this is, of course, that users must be required to sign in to use the app.

The simplest mechanism is for the app to maintain an extra column of type
Email to hold the user's email. If you provide @(_USEREMAIL) as the Default
value of this column, then every new row entered will automatically populate
with the email address of the currently logged in user.

Some apps require a richer audit-trail, to maintain the history of changes
made by different users. Typically, the backend cloud storage provider has an
auditing mechanism. For example, Google Spreadsheets provide a Change History
that shows a detailed list of changes made, when they were made, who made
them, etc. In order to utilize this backend audit history, it is important
that the AppSheet app run with the security setting '[As App User](/hc/en-
us/articles/205857667-Run-mode-as-app-creator-or-user)'. Each potential app
user should also be given permissions to access the backend spreadsheet.


## Related articles {.section}

  * [How do I design a secure app?](How-do-I-design-a-secure-app-)
  * [Expressions](Expressions)
  * [Column types](Column-types)
  * [Plan upgrade required](Plan-upgrade-required)
  * [Printing your data](Printing-your-data)

