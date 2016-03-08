#  Math expressions


February 22, 2016 15:17

Expressions may be used in various AppSheet features -- Initial Values, App
Formulas, Virtual Columns and Column Constraints (Valid_If, Show_If,
Required_If) -- to customize app behavior and provide your users with advanced
functionality. Expressions in this article align with the **Math Expressions**
in the **Expression Builder** of the **Advanced Editor**. The Expression
Builder can be found anywhere you are able to enter a formula/expression,
noted by a little "flask" symbol next to it. Clicking on the flask will bring
up the Expression Builder. The Expression Builder is "context-aware," i.e. it
shows you expressions that are relevant to the specific table you are editing.
Also included in the builder is an "instant" expression checker, to verify
that the expression is valid.



**Expression components**

Use any of the following values as part of an expression:

**Constants**

  * Words, Dates, Times. Highlight all values with **"quotes"**, except for numeric values, e.g. **"Value"**, **"01/01/2016"**, **"12:00:00"**.
  * Numeric values are noted just as they are, e.g **10**.

**Column Names**

  * Name any column using square brackets around the exact column name: **[ColumnName]**. When combining a [ColumnName] with another value, put the expression in **(parentheses)**. May be used in any expression; however, when used in the Initial Value feature, it may only refer to a separate table.



**Math conditions**

Math Expressions utilize arithmetic operators to return a numeric value. All
operators, except Unary Minus, are used with two numeric expression
parameters, e.g. (3+2), (5.0/2.3), etc. AppSheet conditions are not a 1:1
match with Google Sheets functions; however, in some cases the formatting
similarity may help you construct your expressions. Alternatively, if the
formatting is not similar, the Google Sheets function page may provide context
for use of the function. If available, see the Google Sheets function link in
parentheses next to applicable operators.

**Math operators**

Use any of the arithmetic operators below to build arithmetic expressions:

  * Add: +  ([ADD](https://support.google.com/docs/answer/3093590))
  * Subtract: -  ([MINUS](https://support.google.com/docs/answer/3093977?hl=en&ref_topic=3105518))
  * Multiply: *  ([MULTIPLY](https://support.google.com/docs/answer/3093978?hl=en&ref_topic=3105518))
  * Divide: /  ([DIVIDE](https://support.google.com/docs/answer/3093973?hl=en&ref_topic=3105518))
  * Mod: %  ([MOD](https://support.google.com/docs/answer/3093497?hl=en))
  * Unary Minus: -  ([UMINUS](https://support.google.com/docs/answer/3093606?hl=en&ref_topic=3105518))



**Common and complex expressions**

**Common expressions**

  * (1+[Number])
  * ([Decimal]-4.5)
  * ([Price]*[Quantity])
  * 10/2

**Complex expressions**

  * ([Number]*2) + ([Number]*3)



**Math expression patterns and examples**

From the **Expression Builder**, follow the pattern below for a numeric
result. See examples for further clarity.

**Pattern**
**Example**

({value_1} + {value_2})

([Decimal] + 1.12)

({value_1} - {value_2})

([Percent] - 0.2)

({value_1} * {value_2})

([Price] * 19.99)

({value_1} / {value_2})

([Number] / 1)

({value_1} % {value_2})

([Percent] % 0.2)

(- {value_1})

(- [Decimal])



## Related articles {.section}

  * [Time expressions](Time-expressions.md)
  * [Yes/No expressions](Yes-No-expressions.md)
  * [Expressions](Expressions.md)
  * [Columns expressions](Columns-expressions.md)
  * [Lists expressions](Lists-expressions.md)

