#  Understanding authentication and authorization


June 15, 2015 17:37

AppSheet uses the industry-standard OAuth protocol to secure access to your
cloud file system. Let us describe the process when you sign up with AppSheet
through your Google account. The process is similar if your account is through
Dropbox, Box, etc.

On sign up on our website, you are redirected to a Google page where you are
asked if you are willing to authorize AppSheet with a requested set of
permissions. Here is what you are agreeing to and why:

  * You let AppSheet verify your identity. This is so that we know can associate a unique identity with each user.
  * You let AppSheet know your email. This is so that we can send you email as you create apps.
  * You let AppSheet read your files and folders. This is so that you can select spreadsheets and images to use in the app.
  * You let AppSheet make copies of data into your cloud file system and edit that data. This is so that you can make copies of apps.
  * You let AppSheet read and write your spreadsheets. This is what it is all about after all.

We really do not like asking for permissions to your data and have worked to
try to keep this minimal while still providing useful functionality.

Once you go through the auth process, Google and AppSheet use internal
identifiers (called access tokens) to allow AppSheet software to act on your
behalf. To explain this simply:

  * Whenever one of your apps is used, AppSheet has to read and write your data from Google. It does this using your access token. Your access token is never used with anyone else's apps so your data is appropriately protected.
  * You can completely revoke permissions by going to your Google Drive options and disabling AppSheet.


## Related articles {.section}

  * [Sign in ](Sign-in-)
  * [Data access for different classes of users](Data-access-for-different-classes-of-users)
  * [Understanding the secure flow of data](Understanding-the-secure-flow-of-data)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints)

