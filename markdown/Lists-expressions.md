#  Lists expressions


February 22, 2016 15:20

Expressions may be used in various AppSheet features -- Initial Values, App
Formulas, Virtual Columns and Column Constraints (Valid_If, Show_If,
Required_If) -- to customize app behavior and provide your users with advanced
functionality. Expressions in this article align with the **Lists
Expressions** in the **Expression Builder **of the **Advanced Editor**. The
Expression Builder can be found anywhere you are able to enter a
formula/expression, noted by a little "flask" symbol next to it. Clicking on
the flask will bring up the Expression Builder. The Expression Builder is
"context-aware," i.e. it shows you expressions that are relevant to the
specific table you are editing. Also included in the builder is an "instant"
expression checker, to verify that the expression is valid.



**Expression components**

Use any of the following values as part of an expression:

**Constants**

  * Words, Dates, Times. Highlight all values with "quotes", except for numeric values, e.g. **"Value"**, **"01/01/2016"**, **"12:00:00"**.
  * Numeric values are noted just as they are, e.g **10**.

**Column Names**

  * Name any column using square brackets around the exact column name: **[ColumnName]**. When combining a [ColumnName] with another value, put the expression in **(parentheses)**. May be used in any expression; however, when used in the Initial Value feature, it may only refer to a separate table.



**Lists conditions**

Lists Expressions utilize operators that return a list or numeric value.
AppSheet conditions are not a 1:1 match with Google Sheets functions; however,
in some cases the formatting similarity may help you construct your
expressions. Alternatively, if the formatting is not similar, the Google
Sheets function page may provide context for use of the function. If
available, see the Google Sheets function link in parentheses next to
applicable operators.

**Lists operators**

  * LIST({*},{*})  
  * SELECT({List}),{Yes/No}) 
  * COUNT({List})  ([COUNT](https://support.google.com/docs/answer/3093620?hl=en))
  * SUM({List})  ([SUM](https://support.google.com/docs/answer/3093669))
  * ANY({List})



**Context**

In addition to basic column types, we have a meta-type List_Of_X (eg: List Of
Number, List Of Enum, etc) that represents a (potentially empty) list of
unique values. This becomes really important for more powerful expressions.

There are functions to construct lists and functions that use lists:

**Construct a list:**

  * The simplest way to construct such a list is by explicitly writing it  {1, 2, 3} or {[ColumnA], [ColumnB]}
  * The **LIST** function is syntactically equivalent to an explicit list --- **LIST**(1,2,3) is the same as {1, 2, 3}
  * A table column list – the values are constructed from the unique values in a specific column of a specific table. Eg: Customers[Phone Number] returns a list of unique phone numbers in the Customers table
  * **SELECT** is a more powerful way to construct a list from another table. It is  a stylized SQL select-from-where query. It returns a single list of values from one column of a table. However, a filter can be applied to eliminate some of the rows.  
    * `SELECT(Customers[Phone Number], [State] = “WA”)`  --- returns a list of phone numbers of WA customers



**Use a list (however it is constructed):**

The most common use case is to check if a value is in a list:

  * IN([ColumnName], {1, 2, 3})
  * IN([_THIS], {1, 2, 3})  --- a special case used for column constraints like Valid_If and Show_If
  * For column constraints, we accept a short form of the previous expression which is just the list… so {1, 2, 3} is treated as IN([_THIS], {1, 2, 3})

 Aggregate functions

  * **COUNT**(<list of anything>)
  * **SUM**(<list of numeric type>)
  * **ANY**(<list of anything>)



The behavior of COUNT() and SUM() are self-evident. ANY() picks a single value
from a list of values. For example, if there is a table called Customers, each
of whom has a Name and a Phone Number, the expression
ANY(SELECT(Customers[Phone], [Name] = "John Doe")) gets the phone number of a
specific customer.

In many usage scenarios, a** SELECT** expression is used in the context of a
particular column (eg: in a Valid_If or a Show_If ) in a particular row. In
these contexts, the condition used in the **SELECT** function can utilize not
just the columns of the table (Customer) but also the column values from the
context in which it is used. **[_THIS]** refers to the cell/column from the
context and **[_THISROW]** refers to the row from the context. See [Column
Constraints](Controlling-data-inputs-with-column-
constraints).

    * A sample Valid_If condition for a column that accepts a State:   COUNT(SELECT(Customers[Phone Number], [State] = [_THIS])) > 100  --- this says the State is valid only if the number of customers in that state > 100 
    * A sample Show_If condition for a subsequent column in a form that first asks for a State: COUNT(SELECT(Customers[Phone Number], [State] = [_THISROW].[State])) > 1000  --- ask this question only for states with a lot of customers



**Common and complex expressions**

**Common expressions**

  * `Customers[Phone Number]`: returns a list of unique phone numbers in the Customers table
  * `LIST(1,2,3)`: returns 1,2,3
  * `SELECT(Customers[Phone Number], [State] = “WA”)`: returns a list of phone numbers of WA customers
  * `COUNT({Dogs,Cats,Birds})`: returns the number 3.
  * `COUNT({3,4,9,15,32})`: returns the number 5.
  * `SUM({3,4,9,15,32})`: returns the number 63.

**Complex expressions**

  * for Valid_If: `COUNT(SELECT(Customers[Phone Number], [State] = [_THIS])) > 100` : the State is valid only if the number of customers in that state > 100
  * for Show_If: `COUNT(SELECT(Customers[Phone Number], [State] = [_THISROW].[State])) > 1000` : ask this question only for states with a lot of customers



**Lists expression patterns and examples**

From the **Expression Builder,** follow the pattern below for a list or
numeric result. See examples for further clarity.

**Pattern**
**Result**
**Example**

table_name[{column_name}]

List

Field Types[Address]

`LIST({*},{*})`

List

`LIST([ChangeTimestamp],"value_1")`

`SELECT({List},{Yes/No})`

List

`SELECT({"value_1", "value_2"},[Price] = 19.99)`

`COUNT({List})`

Number

`COUNT({"value_1", "value_2"})`

SUM({List})`

Number

SUM({"value_1", "value_2"})`

ANY({List})`

Number

ANY({"value_1", "value_2"})`



## Related articles {.section}

  * [Expressions](Expressions.md)
  * [Other expressions](Other-expressions.md)
  * [Columns expressions](Columns-expressions.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [Column types](Column-types.md)

