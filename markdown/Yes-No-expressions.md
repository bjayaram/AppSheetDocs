#  Yes/No expressions


February 22, 2016 15:17

Expressions may be used in various AppSheet features -- Initial Values, App
Formulas, Virtual Columns and Column Constraints (Valid_If, Show_If,
Required_If) -- to customize app behavior and provide your users with advanced
functionality. Expressions in this article align with the **Yes/No
Expressions** in the **Expression Builder** of the **Advanced Editor**. The
Expression Builder can be found anywhere you are able to enter a
formula/expression, noted by a little "flask" symbol next to it. Clicking on
the flask will bring up the Expression Builder. The Expression Builder is
"context-aware," i.e. it shows you expressions that are relevant to the
specific table you are editing. Also included in the builder is an "instant"
expression checker, to verify that the expression is valid.



**Expression components**

Use any of the following values as part of an expression:

**Constants**

  * Words, Dates, Times. Highlight all values with **"quotes"**, except for numeric values, e.g. **"Value"**,** "01/01/2016"**,** "12:00:00".**
  * Numeric values are noted just as they are, e.g **10**.

**Column Names**

  * Name any column using square brackets around the exact column name: **[ColumnName****]**. When combining a [ColumnName] with another value, put the expression in **(parentheses)**. May be used in any expression; however, when used in the Initial Value feature, it may only refer to a separate table.



**Yes/No conditions**

Yes/No Expressions utilize comparison operators that return a True or False
result displayed as a Yes or No in AppSheet. These Yes/No expressions are
composed of Comparison Operators, Composite Conditions, and Other
Conditions.** **AppSheet conditions are not a 1:1 match with Google Sheets
functions; however, in some cases the formatting similarity may help you
construct your expressions. Alternatively, if the formatting is not similar,
the Google Sheets function page may provide context for use of the function.
If available, see the Google Sheets function link in parentheses next to
applicable operators.

**Comparison operators**

AppSheet supports Comparison Conditions by using these comparison operators
with two expression parameters that have comparable types. For example, 5 > 2
is valid, but 5 > "Hello" is not valid.

  * Equals: =  ([EQ](https://support.google.com/docs/answer/3093593?hl=en&ref_topic=3105518))
  * Not Equals: <>  ([NE](https://support.google.com/docs/answer/3093981?hl=en&ref_topic=3105518))
  * Greater Than: >  ([GT](https://support.google.com/docs/answer/3098240?hl=en&ref_topic=3105518))
  * Greater Than or Equals: >=  ([GTE](https://support.google.com/docs/answer/3093975?hl=en&ref_topic=3105518))
  * Less Than: <  ([LT](https://support.google.com/docs/answer/3093596?hl=en&ref_topic=3105518))
  * Less Than or Equals: <=  ([LTE](https://support.google.com/docs/answer/3093976?hl=en&ref_topic=3105518))

**Composition operators**

AppSheet supports Composite Conditions by using composition operators with
comparison operators.

  * AND({cond_1},..,{cond_n}): returns true if all the sub-expressions are true  ([AND](https://support.google.com/docs/answer/3093301))
  * OR({cond_1},..,{cond_n}): returns true if any of the sub-expressions are true  ([OR](https://support.google.com/docs/answer/3093306?hl=en&ref_topic=3105413))
  * NOT({cond_1}): returns true if the sub-expression is false and vice-versa  ([NOT](https://support.google.com/docs/answer/3093305?hl=en&ref_topic=3105413))

**Other operators**

AppSheet supports the following additional operators:

  * ISBLANK({*}) returns true if an expression is empty  ([ISBLANK](https://support.google.com/docs/answer/3093290?hl=en))
  * CONTAINS({*},{*}): returns true if value contains
  * IN({*},{List}): returns true if a value is in a list



**Common and complex expressions**

**Common expressions**

  * AND([Color]="Green",[CompleteDate]>TODAY())
  * CONTAINS([Fruit],"Oranges")

**Complex expressions**

  * OR(([Price]*[Quantity])>$10,000.00,[Price]>$100.00) 
  * OR(CONTAINS([Fruit],"Oranges"),CONTAINS([Fruit],"Apples"),CONTAINS([Fruit],"Bananas"))



**Yes/No expression patterns and examples**

From the **Expression Builder, **follow the pattern below for a True/False,
i.e. Yes/No result. See examples for further clarity.

**Pattern**
**Example**

{value_1} = {value_2}

[Progress] = "Full"

{value_1} <> {value_2}

[File] <> "myfile.pdf"

{value_1} > {value_2}

[ChangeTimestamp] > "04/22/1970 12:15:44"

{value_1} >= {value_2}

[ChangeTimestamp] >= "04/22/1970 12:15:44"

{value_1} < {value_2}

[Percent] < 0.2

{value_1} <= {value_2}

[Decimal] <= 1.12

AND({cond_1}, .., {cond_n})

AND([ChangeTimestamp] >= "04/22/1970 12:15:44", [Percent] < 0.2)

OR({cond_1}, .., {cond_n})

OR([ChangeTimestamp] >= "04/22/1970 12:15:44", [Percent] < 0.2)

NOT({cond_1})

NOT([File] <> "myfile.pdf")

ISBLANK({*})

ISBLANK([Progress])

IN({*},{List})

IN([Progress],{"value_1", "value_2"})

CONTAINS({*},{*})

CONTAINS([Progress],"value_1")


## Related articles {.section}

  * [Math expressions](Math-expressions.md)
  * [Expressions](Expressions.md)
  * [Columns expressions](Columns-expressions.md)
  * [Other expressions](Other-expressions.md)
  * [App formulas](App-formulas.md)

