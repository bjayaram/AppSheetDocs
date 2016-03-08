#  Required_If


February 22, 2016 18:03

**Expression components**

These expression components utilize the following formatting:

  * Name any column using square brackets around the exact column name: `[ColumnName]`. When combining a `[ColumnName]` with another value, put the expression in (parentheses).
  * Use `[_THIS]` as a "virtual column name." It refers to the value of the current column (used in Valid_If, Show_If, Required_If conditions).
  * Use `[_THISROW]` as a "virtual reference column." It refers to the current row. For example, use `[_THISROW].[ColumnName]`.
  * Highlight all values with "quotes," except for numeric values: "Value".
  * Numeric values are noted just as they are, e.g 10.

**Required_If **

A 'required' input is one that must be filled in before the record can be
saved. A Required_If column constraint is used when a field is 'required'
depending on the values of earlier form inputs.

A Required_If constraint is a condition expression that indicates whether a
specific column is 'required' in an input form. It is usually based on the
values of other columns (e.g. `[Country Of Birth] = "USA"`).


## Related articles {.section}

  * [Show_If](Show-If.md)
  * [Valid_If and Dependent Dropdowns](Valid-If-and-Dependent-Dropdowns.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [AppSheet is NOT...](AppSheet-is-NOT-.md)
  * [Valid_If](Valid-If.md)

