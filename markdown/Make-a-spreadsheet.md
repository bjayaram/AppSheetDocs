#  Make a spreadsheet


January 05, 2016 23:21

AppSheet builds an app based on the “table” structure of data in your
spreadsheet. AppSheet will attempt to understand the structure of your
spreadsheet and [there are simple ways to help with that](Effective-use-of-column-headers.md). 
The more complex your
structure is, the more difficult it is for AppSheet to translate it into a
working mobile app. For example, pivot tables don’t work well with AppSheet’s
system.

First, you’ll want to make sure your spreadsheet is neat and tidy. Make sure
your columns are clear and if possible, add a couple of rows of data before
you publish. Your spreadsheet should also have a defined set of columns and
corresponding headers. AppSheet will read the table in the **first worksheet**
of your spreadsheet to translate it into a mobile app. You’ll have the chance
to utilize other worksheets in the workbook later.

Assign meaningful headers to the columns in your spreadsheet-- this will help
AppSheet identify the values in those columns. Try to use common titles in
English (we plan to support more languages in future releases). For example,
if you are adding a column with telephone numbers, it helps AppSheet identify
the values in that column as telephones if the title (header) of the column is
called Telephone, or Telephones, or Phone Number.


![Column Headers](../article_attachments/204739088/Screen_Shot_2016-01-05_at_3.04.49_PM.png)

AppSheet will more quickly recognize the columns if the format of each cell in the column is the same. For example, if you have a column with dates, make sure that all of the dates in the column share the same format.

![Column Data format](../article_attachments/204757217/Screen_Shot_2016-01-05_at_3.04.49_PM.png)

Finally, new data should be added as new rows, not as columns.

![New row added](../article_attachments/204757237/Screen_Shot_2016-01-05_at_3.04.49_PM.png)

In the next section, we'll show you the different ways you can begin [creating apps](Create-an-app.md). 

## Related articles {.section}

  * [Create an app](Create-an-app.md)
  * [Effective use of column headers](Effective-use-of-column-headers.md)
  * [Basic app customizations](Basic-app-customizations.md)
  * [Extracting structure from cloud spreadsheets](Extracting-structure-from-cloud-spreadsheets.md)
  * [Sign in ](Sign-in-.md)

