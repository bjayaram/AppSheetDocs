#  Concurrent usage with multiple users


June 15, 2015 17:50

Apps built with AppSheet are meant for multiple concurrent users. This leads
to the natural question -- how do we deal with multiple people updating the
data?

The simple rule is that 'the last writer wins'.

  * The changes of each user are isolated until a sync occurs. At this point, AppSheet attempts to replay the user's changes in order against the backend spreadsheet.
  * The unit of change is a single row. Many applications partition well so that no two users update the same row.
  * If two users happen to change the same row, the last user's change is what persists. In fact, someone could also update the data directly in the backend spreadsheet. This is treated no differently from any other data update.

There are three cases during sync when this behavior is exposed to users of
your app:

  * If the user adds a row but a row with the same key already exists, then that row is _updated_ with the new data.
  * If the user deletes a row but no row with that key exists, then that change is ignored.
  * If the user edits a row but no row with that key exists, then that change is ignored because clearly some other user explicitly deleted it first.

## Related articles {.section}

  * [Data access for different classes of users](Data-access-for-different-classes-of-users)
  * [Specifying a key](Specifying-a-key)
  * [Transferring app ownership to another user](Transferring-app-ownership-to-another-user)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)
  * [Modifying column structure in the editor](Modifying-column-structure-in-the-editor)

