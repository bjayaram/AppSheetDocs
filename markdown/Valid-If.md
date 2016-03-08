#  Valid_If


February 22, 2016 18:05

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
    * For example, comparing the value with a constant: `[_THIS] > 5`
    * For example, comparing the value with another column: `[_THIS] > [ColumnA]`
  2. Is the value of the column in a list? 
    * A list of constant values. For example: `{100, 200, 300}`
    * A list of values from a column in another table. For example: `LookupTable[ColumnC]` . _This is particularly useful if the list of allowed values should itself be allowed to change while the app is being used.
    * A list of values from specific rows in another table. For example: `SELECT(LookupTable[ColumnC], [ReportDate] > Today() - 7)` specifies that the rows in LookupTable should be filtered to find those where ReportDate is within the last week, and the corresponding values in ColumnC of LookupTable become the allowed list of valid values.

Whenever a list of allowed values is provided, it is actually a syntactic
shortform for an expression that uses the IN function. For example, `{100,
200, 300}` is the same as `IN([_THIS], {100, 200, 300})`. In input forms in
the mobile app, columns with such Valid_If constraints are provided with
dropdowns or enumeration selectors that reflect the list of choices.


## Related articles {.section}

  * [Valid_If and Dependent Dropdowns](Valid-If-and-Dependent-Dropdowns.md)
  * [Show_If](Show-If.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [Required_If](Required-If.md)
  * [Math expressions](Math-expressions.md)

