#  Tracking changes using 'Change' column types


January 13, 2016 22:03

In some apps, it is important to track when and where some data was changed.
For example, in a field service app, it may be important to record when a
certain field was changed.

AppSheet has a simple mechanism to track changes-- via 'Change' column types.
There are three "Change" column types-- **ChangeTimestamp, ChangeCounter,
**and** ChangeLocation**. These column types all have a set of shared
characteristics that are specified via the column Type Qualifier:

  1. What triggers a change: any change to any other column, any change to some specific fields or a single field, or changes to a specific field that result in one of a known set of values
  2. What should happen when such a change is detected: increment a counter (ChangeCounter), set a timestamp to the current time (ChangeTimestamp), or record the current location (ChangeLocation) 

As a simple example, in the [Interview Feedback sample](https://www.appsheet.com/samples/An-app-to-share-interviewer-feedback-on-potential-job-candidates?appGuidString=2bb93705-dd24-4c9f-b051-812887324f9b), the Feedback
table has a Changes column of type ChangeColumn. The type qualifier doesn't
"qualify" the type in any way, so this column will track changes to any other
field in the row. If any other row changes, the value of the Changes column is
incremented.

A more typical example would want to track changes to specific columns,
perhaps even more specifically changes of those columns to specific values. In
the [Store Inventory sample](https://www.appsheet.com/samples/An-app-to-record-store-inventory-Sort-products-by-unique-categories?appGuidString=0c2387ab-c8ca-4477-950e-d66a54a5e067), the Inventory List table has a Date
Checked column. It listens for changes to a specific other column, Quantity In
Stock. And in fact, it looks to see if that value changes to 0. If it does,
then the column records the current timestamp.


## Related articles {.section}

  * [Using a scanner](Using-a-scanner.md)
  * [Grouped views and data filtering](Grouped-views-and-data-filtering.md)
  * [ Viewing external content](-Viewing-external-content.md)
  * [Slices](Slices.md)
  * [Expressions](Expressions.md)

