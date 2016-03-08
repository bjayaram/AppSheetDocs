#  Understanding the secure flow of data


October 26, 2015 23:24

AppSheet uses industry-standard security protocols and practices to secure
your data. Users of your mobile app interact with a local copy of the data on
the device. This local copy is maintained in a combination of 'HTML5 local
storage' and the file system on the device. There are standard security
mechanisms in place to ensure that unauthorized users cannot see this data.

When users sync their app, changes they make are sent to the AppSheet web
service over an encrypted protocol (HTTPS). AppSheet then applies the changes
to the backend spreadsheet (on Google Drive, Dropbox, etc). The latest version
of the spreadsheet is read (from Google Drive, Dropbox, etc) and sent back to
the mobile app.


## Related articles {.section}

  * [Where is my data cached?](Where-is-my-data-cached-)
  * [Understanding authentication and authorization](Understanding-authentication-and-authorization)
  * [Data access for different classes of users](Data-access-for-different-classes-of-users)
  * [Run mode-- as app creator or app user](Run-mode-as-app-creator-or-app-user)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints)

