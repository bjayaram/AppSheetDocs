# App Formulas

Sometimes, you want calculations to run in the app while the user is
interacting with the data. To help you achieve that goal, you can specify an
App Formula for every column. An App Formula is an expression that AppSheet
evaluates whenever a user changes a value in a form (while creating a new
record or editing an existing record). Each time such a change occurs, the App
Formula of every column in the record is evaluated and the column is assigned
the result of the formula evaluation. For example, if a record has a Price
column and a Tax column, the Tax column might have an App Formula `[Price]*0.05`
to compute a 5% tax automatically.

In AppSheet's Advanced Editor, you can add App Formulas to any column when you
go to Data>Column Structure.

![add app formula](../article_attachments/204816157/Screen_Shot_2016-01-08_at_2.05.21_PM.png)

Click on the edit icon (seen above) and navigate to the App Formula field to
enter the formula you need for your app. The formula itself is any valid
AppSheet expression that matches the type of the column. You can learn more
about [the different kinds of expressions](Expressions.md) supported by AppSheet.

App Formulas are distinct from  [Spreadsheet Formulas](Spreadsheet-formulas.md). The two mechanisms are
complementary and both add value to your app. Your spreadsheet is a very
powerful tool to run calculations. Those calculations run only when data syncs
back to the spreadsheet.

App Formulas are commonly used to calculate the value of a column when the
user makes updates to the app. When the changes are synced back to the
spreadsheet, the computed value is saved to the corresponding spreadsheet
cell.

App Formulas are also used to define [Virtual Columns](Virtual-Columns.md). These columns do not actually exist in
the spreadsheet but are only computed within the context of the app itself.

## Related articles

  * [Spreadsheet formulas](Spreadsheet-formulas.md)
  * [Column types](Column-types.md)
  * [Customizing input forms](Customizing-input-forms.md)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-.md)
  * [Keys](Keys.md)