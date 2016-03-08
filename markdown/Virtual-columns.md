#  Virtual columns


January 09, 2016 00:22

A virtual column, as the name suggests, is a column of a table in the app that
doesn't have an actual column in the underlying spreadsheet. Instead, it is
automatically computed via an [app formula expression](Expressions.md).

In order to define a virtual column, use the Advanced Editor>Data>Column
Structure, and add a virtual column to any of the column structures. You can
specify an appropriate formula expression and the type of the column is
automatically detected by AppSheet. Typically, a virtual column utilizes the
values of other columns in the same row.

Here are three common use cases for virtual columns:

  1. **To combine other columns**: in an app that captures a FirstName and a LastName, a virtual column with the formula `CONCATENATE([LastName], ", ", [FirstName])` can be used to create a FullName.
  2. **To construct conditional values**: in an app that captures contact information, a virtual column called PreferredPhoneNumber may be defined with the formula `IF([UseMobilePhone?],[MobilePhoneNumber],[PhoneNumber])` 
  3. **To construct complex yes/no values**: in an app that captures orders, a virtual column called Important? may be defined with the formula `OR([Amount] > 1000,[Quantity] > 100)`

The ability to create complex yes/no values is really important when they are
used in other expressions like slice conditions, column constraints, etc. In
short, any time there is a need for a complex condition in an app, it is best
to create a virtual column to represent the complex condition, and then use
the virtual column wherever needed.


## Related articles {.section}

  * [Expressions](Expressions.md)
  * [App formulas](App-formulas.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [Defining and using slices](Defining-and-using-slices.md)
  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)

