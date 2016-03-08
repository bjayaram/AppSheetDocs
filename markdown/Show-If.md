#  Show_If


February 22, 2016 18:05

**Expression components**

These expression components utilize the following formatting:

  * Name any column using square brackets around the exact column name: [ColumnName]. When combining a [ColumnName] with another value, put the expression in (parentheses).
  * Use [_THIS] as a "virtual column name." It refers to the value of the current column (used in Valid_If, Show_If, Required_If conditions).
  * Use [_THISROW] as a "virtual reference column." It refers to the current row. For example, use [_THISROW].[ColumnName].
  * Highlight all values with "quotes," except for numeric values: "Value".
  * Numeric values are noted just as they are, e.g 10.



**Show_If**

A Show_If column constraint is used when an input field should be shown or
hidden depending on the values of one or more earlier field values in the
form.

A Show_If constraint is a condition expression that determines whether or not
an input for this column should be shown in a form. This is usually based on
the values of other columns. For example, the condition expression
`[UserRating] = "5"` will display this column if the value in the "UserRating"
column is "5". The condition expression `[Status] = "Green"` will display this
column if the value in the "Status" column is "Green".

The special column name "_THIS" is used to refer to the current column being
constrained. For example, a Show_If condition of `ISBLANK([_THIS])` can be
used to show an input field only if the column itself is blank. The column
will be hidden, once a data value has been entered and saved for the column.

Show_If conditions can also be defined on Page Header columns to
[conditionally show or hide entire pages](206435467).


## Related articles {.section}

  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching)
  * [Valid_If](Valid-If)
  * [Other expressions](Other-expressions)
  * [Presentation types](Presentation-types)
  * [Required_If](Required-If)

