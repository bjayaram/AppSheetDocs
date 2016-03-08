#  How do I make sure each user sees only their own data?


January 31, 2016 21:26

Security filters are yes/no expressions optionally associated with each table
in the app. They will typically utilize some properties of the app user to
limit the data shown to the app user.

**See Advanced Editor>Settings>Security**

** **Examples:**

To limit access by User Email:

  * [EmailColumn] = USEREMAIL()

To limit access by User Email Domain:

  * CONTAINS(USEREMAIL(), [EmailDomainColumn])

It is possible to build more complex logic as well ---
AND/OR/NOT/functions/derefs, etc.

Note: Both the USEREMAIL() and the USERNAME() functions require that the app
has enabled user authentication (i.e. app users are required to sign in to use
the app). It is preferable to use USEREMAIL() instead of USERNAME() because it
is always guaranteed to be available for a signed-in user.


## Related articles {.section}

  * [Expressions](Expressions)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-)
  * [Data access for different classes of users](Data-access-for-different-classes-of-users)
  * [Run mode-- as app creator or app user](Run-mode-as-app-creator-or-app-user)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)

