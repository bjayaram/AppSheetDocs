#  Controlling data inputs with column constraints


February 22, 2016 18:04

Every column definition has a type (that specifies what values are allowed in
the column) as well as flags that specify whether the column is hidden,
whether it is required for input, etc. This is adequate for many apps, but
sometimes a more dynamic or data-driven mechanism is needed. This is what
Column Constraints provide-- a column constraint is an [expression](Expressions.md) that is dynamically computed to determine
the behavior of a specific column.

Three different column constraints can be defined for each column:

  * Show_If
  * Valid_If
  * Required_If

To add a column constraint, use the Column Structure tab of the Data pane in
the [Advanced Editor](Advanced-app-customizations.md) and click the "Edit" icon at the left of the corresponding
column definition.



**Expression components**

These expression components utilize the following formatting:

  * Name any column using square brackets around the exact column name: `[ColumnName]`. When combining a `[ColumnName]` with another value, put the expression in (parentheses).
  * Use `[_THIS]` as a "virtual column name." It refers to the value of the current column (used in Valid_If, Show_If, Required_If conditions).
  * Use `[_THISROW]` as a "virtual reference column." It refers to the current row. For example, use [_THISROW].[ColumnName].
  * Highlight all values with "quotes," except for numeric values: **"Value"**.
  * Numeric values are noted just as they are, e.g **10**.



**Show_If**

A Show_If column constraint is used when an input field should be shown or
hidden depending on the values of one or more earlier field values in the
form.

A Show_If constraint is a condition expression that determines whether or not
an input for this column should be shown in a form. This is usually based on
the values of other columns. For example, the condition expression
_**[UserRating] = "5"** _will display this column if the value in the
"UserRating" column is "5". The condition expression _**[Status] = "Green"
**_will display this column if the value in the "Status" column is
"Green"_**.**_

The special column name "_THIS" is used to refer to the current column being
constrained. For example, a Show_If condition of _**ISBLANK([_THIS])**_ can be
used to show an input field only if the column itself is blank. The column
will be hidden, once a data value has been entered and saved for the column.

Show_If conditions can also be defined on Page Header columns to
[conditionally show or hide entire pages](206435467).



**Valid_If**

Every input in a form is checked for validity based on its type. For example,
a column of Number type will not accept "Hello" as an input. A Valid_If column
constraint is used in situations where the validity of the input requires
richer data-dependent logic.

A Valid_If constraint is a condition expression that determines whether or not
the form input for this column is valid. For example, the [Quote Calculator
sample](https://www.appsheet.com/template/AppDef?appName=RateCalculator-71626)
utilizes a Valid_If condition to ensure that the Cost Per Hour must be less
than $20.

Here are examples of commonly used Valid_If constraints:

  1. Does the value of the column satisfy a simple condition? 
    * For example, comparing the value with a constant: `[_THIS] > 5`
    * For example, comparing the value with another column: `[_THIS] > [ColumnA]`
  2. Is the value of the column in a list? 
    * A list of constant values. For example: `{100, 200, 300}`
    * A list of values from a column in another table. For example: `LookupTable[ColumnC] ` This is particularly useful if the list of allowed values should itself be allowed to change while the app is being used.
    * A list of values from specific rows in another table. For example: `SELECT(LookupTable[ColumnC], [ReportDate] > Today() - 7)`_specifies that the rows in LookupTable should be filtered to find those where ReportDate is within the last week, and the corresponding values in ColumnC of LookupTable become the allowed list of valid values.

Whenever a list of allowed values is provided, it is actually a syntactic
shortform for an expression that uses the IN function. For example, `{100,
200, 300} ` is the same as `IN([_THIS], {100, 200, 300})`. In input forms
in the mobile app, columns with such Valid_If constraints are provided with
dropdowns or enumeration selectors that reflect the list of choices.



**Valid_If and Dependent Dropdowns**

Dependent dropdowns are a common design pattern in apps that capture input.
For example, consider an app like [this Lead Tracker
sample](https://www.appsheet.com/samples/An-app-to-add-and-update-sales-leads?appGuidString=2f43eb0a-1dbf-417f-9e2d-ccb8b9600d02) that asks for the
'Lead Region' (America, Asia, Europe) and then for a 'Country' within that
region. This is actually requires relatively complex logic, but AppSheet tries
to make it simple. Dependent dropdowns are driven by a separate lookup table.

In the sample, there is a separate 'Regions' lookup table with two columns:
'Region' and 'Country'. This acts as the lookup table for allowed combinations
of regions and countries. [Here is the table data](https://www.appsheet.com/te
mplate/showtable?allowExternalRedirect=false&appName=DependentDropdowns-16350&tableName=Regions) used in the sample.

The 'Lead Region' column has a regular Valid_If constraint:
`Regions[Region]`. Therefore, when a new entry is being added, the input
for this column shows three choices: America, Asia, and Europe.

Likewise, the 'Country' column also specifies a similar Valid_If constraint:
`Regions[Country]`. However, because it follows the 'Lead Region' column
and because both specify columns from the same lookup table 'Regions',
AppSheet recognizes the intent and implements a dependent dropdown.

Internally, AppSheet creates an expression to capture the allowed set of
values for the 'Country' column. The expression must say (in English** Look at the Regions table
  * Filter the rows to make sure that the Region column of the table matches the value in the 'Lead Region' column of the row being edited in the form
  * Now extract the 'Country' column from those filtered rows
  * Eliminate any duplicates --- these are the allowed countries** Recompute this list each time the 'Lead Region' is changed

Strictly for an expression afficionado, here is the full underlying AppSheet
expression: `IN( [_THIS], SELECT(Regions[Country], [_THISROW].[Lead Region] = [Region]))`

While most app creators will never need to express something this complicated,
you could infact provide this expression as a Valid_If constraint. It is
useful to know for advanced use cases. For example, instead of using an
equality condition, an app creator could use inequality or richer expressions
to build very expressive dynamic dropdowns.



**Required_If **

A 'required' input is one that must be filled in before the record can be
saved. A Required_If column constraint is used when a field is 'required'
depending on the values of earlier form inputs.

A Required_If constraint is a condition expression that indicates whether a
specific column is 'required' in an input form. It is usually based on the
values of other columns (e.g. `[Country Of Birth] = "USA"`).



**Best practices**

Column constraints give you the power to define very subtle or complex
conditions, but end-users will only see the resulting behavior. As an app
creator, it is important to provide adequate explanations for the columns
affected by these expressions--particularly for Valid_If conditions, so that
users will know how to proceed if they provide an invalid column value. The
best way to do so is by providing meaningful column descriptions.

When these expressions reference other fields in the row (not just `[_THIS]`),
it is best to ensure that they are always "backward" references to fields that
the end-user has already seen (meaning columns that come _before_ the column
being considered in the spreadsheet and appear _above_ the column being
considered in the Column Structure tab). Conditions containing "forward"
references may be confusing to end-users and may cause problems with multi-
page forms.


## Related articles {.section}

  * [Expressions](Expressions.md)
  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)
  * [App formulas](App-formulas.md)
  * [Defining and using slices](Defining-and-using-slices.md)
  * [Column types](Column-types.md)

