#  Keys


January 07, 2016 20:54

A 'key' **uniquely** identifies each individual row in the table.

The key may be a single column (such as Employee ID) or a composite column
(such as FirstName and LastName).

When end-users change data on a mobile device, they are not actually
interacting with the spreadsheet at that moment. They make the change to a
local copy of the data and AppSheet needs to make sure the change can be
applied to the spreadsheet sometime later (when the device is online and the
user syncs the changes).

Without a key to uniquely identify the row changes, AppSheet would find it
impossible to apply the change to the appropriate spreadsheet row.

Here's more about [keys and how to choose one](How-should-I-choose-a-key-.md).


## Related articles {.section}

  * [How should I choose a key?](How-should-I-choose-a-key-.md)
  * [Specifying a key](Specifying-a-key.md)
  * [Slices](Slices.md)
  * [Concurrent usage with multiple users](Concurrent-usage-with-multiple-users.md)
  * [Customizing input forms](Customizing-input-forms.md)

