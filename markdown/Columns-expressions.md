#  Columns expressions


February 22, 2016 15:21

Expressions may be used in various AppSheet features -- Initial Values, App
Formulas, Virtual Columns and Column Constraints (Valid_If, Show_If,
Required_If) -- to customize app behavior and provide your users with advanced
functionality. Expressions in this article align with the **Columns
Expressions** in the **Expression Builder **of the **Advanced Editor.** The
Expression Builder can be found anywhere you are able to enter a
formula/expression, noted by a little "flask" symbol next to it. Clicking on
the flask will bring up the Expression Builder. The Expression Builder is
"context-aware," i.e. it shows you expressions that are relevant to the
specific table you are editing. Also included in the builder is an "instant"
expression checker, to verify that the expression is valid.



**Expression components**

Use any of the following values as part of an expression:

**Constants**

  * Words, Dates, Times. Highlight all values with **"quotes"**, except for numeric values, e.g. **"Value"**, **"01/01/2016"**, **"12:00:00"**.
  * Numeric values are noted just as they are, e.g **10**. 



**Columns conditions**

Columns Expressions refer to a column to return a value.

**Columns operators**

  * Use **[_THIS]** to refer to the value of the current column (used in Valid_If, Show_If, and Required_If conditions). See [Column Constraints](Controlling-data-inputs-with-column-constraints).
  * Name any column using square brackets around the exact column name: **[ColumnName]**. When combining a [ColumnName] with another value, put the expression in** (parentheses)**. May be used in any expression; however, when used in the Initial Value feature, it may only refer to a separate table.



**Common and complex expressions**

**Common expressions**

  * `([_THIS]>25)`

**Complex expressions**

  * Pending



**Columns expression patterns and examples**

From the **Expression Builder**, follow the pattern below for a result. See
examples for further clarity.

**Pattern**
**Result**
**Example**

[_THIS]

Text

[_THIS]

[{column_name}]

Number

[Project #]



## Related articles {.section}

  * [Lists expressions](Lists-expressions.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [Expressions](Expressions.md)
  * [Yes/No expressions](Yes-No-expressions.md)
  * [Time expressions](Time-expressions.md)

