#  Run mode-- as app creator or app user


October 26, 2015 23:36

The mobile app that you build communicates with the AppSheet backend, and it
is the AppSheet backend that communicates with your cloud data provider (eg:
Google Drive) to fetch or update data.

For security reasons, the cloud data provider will not let AppSheet access
your data unless AppSheet has the permissions to do so. Whenever a user or app
creator signs in, he/she grants AppSheet the permission to act on their
behalf.



**As app creator**

In the default run mode ('as app creator'), the AppSheet backend accesses data
with the identity of the app creator. So if you are the app creator, and you
have access to the spreadsheet that the app is based on, you can distribute
your app to other people who do not have direct access to that data but the
app still works fine.

There is a security setting in the Advanced Editor which allows you to change
the run mode to 'as app user'. As the name suggests, in this mode, the
AppSheet backend will try to access the app data with the identity of the app
user. This will fail for apps that don't enforce sign in. And even if the user
does sign into the app, it may still fail if the user doesn't have permissions
to access the source spreadsheet and folder.



**As app user**

So what's the benefit of the 'as app user' run mode? It is a stricter security
mechanism (ensures that the permissions model of the cloud data provider are
strictly maintained). It is also an auditing mechanism, especially for cloud
providers like Google Drive and Box that maintain audit histories of all
updates made to documents. If the app runs 'as app user', each change to the
app recorded in the audit history will carry the identity of the specific user
who made the change. Please be aware that if the app user does not have
permissions to access the underlying data (eg: the spreadsheet on Google Drive
that holds the app's data), the app will fail for that user.

To avoid any confusion, this option has no bearing on the mode in which the
app itself runs on the mobile device. The user who signs in is always the
current user and expressions like @(_USERNAME) and @(_USEREMAIL) always
reflect the current signed-in user, never the app creator.

Was this article helpful?

0 out of 0 found this helpful

  * [Facebook](http://www.facebook.com/share.php?title=Run+mode--+as+app+creator+or+app+user&u=https%3A%2F%2Fappsheethelp.zendesk.com%2Fhc%2Fen-us%2Farticles%2F205857667-Run-mode-as-app-creator-or-app-user)
  * [Twitter](https://twitter.com/share?lang=en&text=Run+mode--+as+app+creator+or+app+user&url=https%3A%2F%2Fappsheethelp.zendesk.com%2Fhc%2Fen-us%2Farticles%2F205857667-Run-mode-as-app-creator-or-app-user)
  * [LinkedIn](http://www.linkedin.com/shareArticle?mini=true&source=AppSheet&title=Run+mode--+as+app+creator+or+app+user&url=https%3A%2F%2Fappsheethelp.zendesk.com%2Fhc%2Fen-us%2Farticles%2F205857667-Run-mode-as-app-creator-or-app-user)
  * [Google+](https://plus.google.com/share?hl=en-us&url=https%3A%2F%2Fappsheethelp.zendesk.com%2Fhc%2Fen-us%2Farticles%2F205857667-Run-mode-as-app-creator-or-app-user)

Have more questions? [Submit a request](/hc/en-us/requests/new)

#### 0 Comments

Article is closed for comments.

## Related articles {.section}

  * [Maintaining an audit trail](Maintaining-an-audit-trail)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)
  * [Data access for different classes of users](Data-access-for-different-classes-of-users)
  * [Controlling data updates](Controlling-data-updates)
  * [Expressions](Expressions)

