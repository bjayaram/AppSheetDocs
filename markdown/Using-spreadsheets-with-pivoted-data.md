#  Using spreadsheets with pivoted data


January 28, 2016 23:57

Most spreadsheet data uses field names as column headers and data entries in
each row, but what should your data is pivoted with field names down the first
column and data entries in the other columns? For example, if employee names
are used as column headers and employee attributes as rows.

AppSheet doesn't work with pivoted data. This is because apps are generated
from the column structure of the data. The column structure tells the app the
"shape" of the data that it needs to process. This structure needs to stay
stable as the app is being used. New data should take the form new rows and
changes to data should take the form of row edits or row deletes.

Luckily most data can be re-pivoted so that the attributes of each data item
form column headers and the values of each data item are represented in a row.
This is very easy to do in a spreadsheet. In Google Spreadsheets or Excel, you
first copy the data and then use 'Paste Transpose'.



## Related articles {.section}

  * [Many identical apps](Many-identical-apps)
  * [Expressions](Expressions)
  * [Presentation types](Presentation-types)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-)
  * [Including PDF's in your application](Including-PDF-s-in-your-application)

