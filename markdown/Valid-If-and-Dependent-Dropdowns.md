#  Valid_If and Dependent Dropdowns


February 22, 2016 18:06



**Expression components**

These expression components utilize the following formatting:

  * Name any column using square brackets around the exact column name: [ColumnName]. When combining a [ColumnName] with another value, put the expression in (parentheses).
  * Use [_THIS] as a "virtual column name." It refers to the value of the current column (used in Valid_If, Show_If, Required_If conditions).
  * Use [_THISROW] as a "virtual reference column." It refers to the current row. For example, use [_THISROW].[ColumnName].
  * Highlight all values with "quotes," except for numeric values: "Value".
  * Numeric values are noted just as they are, e.g 10.



**Valid_If**

Every input in a form is checked for validity based on its type. For example,
a column of Number type will not accept "Hello" as an input. A Valid_If column
constraint is used in situations where the validity of the input requires
richer data-dependent logic.

A Valid_If constraint is a condition expression that determines whether or not
the form input for this column is valid. For example, the [Quote Calculator
sample](https://www.appsheet.com/template/AppDef?appName=RateCalculator-71626)
utilizes a Valid_If condition to ensure that the Cost Per Hour must be less
than $20.

Here are examples of commonly used Valid_If constraints:

  1. Does the value of the column satisfy a simple condition? 
    * For example, comparing the value with a constant: _[_THIS] > 5_
    * For example, comparing the value with another column: _[_THIS] > [ColumnA]_
  2. Is the value of the column in a list? 
    * A list of constant values. For example: _{100, 200, 300}_
    * A list of values from a column in another table. For example: _LookupTable[ColumnC] . _This is particularly useful if the list of allowed values should itself be allowed to change while the app is being used.
    * A list of values from specific rows in another table. For example: _SELECT(LookupTable[ColumnC], [ReportDate] > Today() - 7) _specifies that the rows in LookupTable should be filtered to find those where ReportDate is within the last week, and the corresponding values in ColumnC of LookupTable become the allowed list of valid values.

Whenever a list of allowed values is provided, it is actually a syntactic
shortform for an expression that uses the IN function. For example, _{100,
200, 300} _is the same as _IN([_THIS], {100, 200, 300}). _In input forms in
the mobile app, columns with such Valid_If constraints are provided with
dropdowns or enumeration selectors that reflect the list of choices.



**Valid_If and Dependent Dropdowns**

Dependent dropdowns are a common design pattern in apps that capture input.
For example, consider an app like [this Lead Tracker
sample](https://www.appsheet.com/samples/An-app-to-add-and-update-sales-
leads?appGuidString=2f43eb0a-1dbf-417f-9e2d-ccb8b9600d02) that asks for the
'Lead Region' (America, Asia, Europe) and then for a 'Country' within that
region. This is actually requires relatively complex logic, but AppSheet tries
to make it simple. Dependent dropdowns are driven by a separate lookup table.

In the sample, there is a separate 'Regions' lookup table with two columns:
'Region' and 'Country'. This acts as the lookup table for allowed combinations
of regions and countries. 
[Here is the table data](https://www.appsheet.com/template/showtable?allowExternalRedirect=false&appName=DependentDropdowns-16350&tableName=Regions) used in the sample.

The 'Lead Region' column has a regular Valid_If constraint: `Regions[Region]`.
Therefore, when a new entry is being added, the input for this column shows
three choices: America, Asia, and Europe.

Likewise, the 'Country' column also specifies a similar Valid_If constraint:
`Regions[Country]`. However, because it follows the 'Lead Region' column and
because both specify columns from the same lookup table 'Regions', AppSheet
recognizes the intent and implements a dependent dropdown.

Internally, AppSheet creates an expression to capture the allowed set of
values for the 'Country' column. The expression must say (in English** Look at the Regions table
  * Filter the rows to make sure that the Region column of the table matches the value in the 'Lead Region' column of the row being edited in the form
  * Now extract the 'Country' column from those filtered rows
  * Eliminate any duplicates --- these are the allowed countries** Recompute this list each time the 'Lead Region' is changed

Strictly for an expression afficionado, here is the full underlying AppSheet
expression: `IN( [_THIS], SELECT(Regions[Country], [_THISROW].[Lead Region] = [Region]))`

While most app creators will never need to express something this complicated,
you could infact provide this expression as a Valid_If constraint. It is
useful to know for advanced use cases. For example, instead of using an
equality condition, an app creator could use inequality or richer expressions
to build very expressive dynamic dropdowns.



## Related articles {.section}

  * [Valid_If](Valid-If.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [Show_If](Show-If.md)
  * [Lists expressions](Lists-expressions.md)
  * [Limits on data size](Limits-on-data-size.md)

