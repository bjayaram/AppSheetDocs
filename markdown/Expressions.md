#  Expressions


February 03, 2016 14:29

Please see the [Expressions section](Expressions.md)
for further details.

Expressions allow you to calculate new values from existing values. Most
advanced apps utilize expressions to customize behavior. If you are familiar
with spreadsheet formulas, you will find AppSheet expressions to be similar in
syntax and meaning. At the moment, AppSheet supports a very small subset of
the functions supported by Excel or Google Sheets. However, we are adding new
functions every week.

Expressions are utilized in a variety of AppSheet features-- App Formulas,
Default Values, Column Constraints, and Virtual Columns. The sample app [Rate 
Calculator](https://www.appsheet.com/Template/SimpleDef?appName=RateCalculator-71626) 
shows the use of various expressions in App Formulas.

AppSheet checks all expressions to ensure that they are correctly formed and
are being used in an appropriate manner. For example, if an expression is
being used to assign a default value to a column of type Number, AppSheet
checks that the result of the expression is indeed a number.

Although not an exact 1:1 match to AppSheet Expressions, these [Google
Functions](https://support.google.com/docs/table/25273?hl=en) may provide
assistance with syntax.

An expression is built by utilizing any combination of the following:   

**Constants**

Use any of the following values as part of a formula:

  * **Numbers**:** **You can use any number as part of the formula
  * **Dates**: Use format MM/DD/YYYY
  * **Words**: Use quotation marks around the word --> e.g. "Word"  
  

**Columns**

Name any column using square brackets around the exact column name: **[Column]  
  
**

**De-references  
**

If a field in the column structure has a reference to a row in another table,
you can use a DE-REFERENCE expression to get the value of another column in
that row of the referenced table. The format to do this is `[Column With
Reference].[Column in Referenced Table]`

Check out the [Order Capture](https://www.appsheet.com/samples/An-app-for-a-salesperson-add-customers-orders-and-product-details?appGuidString=245700e5-9061-4045-843f-7850b5eb439a) sample app to see
how the Order Details table uses DE-REFERENCING to get the price of a product
with the expression: `[Product].[Price]`

`[Product]` Is the name of the column that has a reference to the Products table.

`[Price]` Is the name of the column in the Products table that contains the price.

In the Order Capture app, there is also a formula that multiplies
`[Product]`.`[Price]` with another column called `[Quantity]`. **This is
an example of a complex expression.  
  

**Built-in functions**

AppSheet's list of built-in function expressions is growing every week:

  * NOW() for the current DateTime
  * TODAY() for the current Date
  * TIMENOW() for the current Time
  * HERE() for LatLong of the current Location
  * USERNAME() for the Name of the current user
  * USEREMAIL() for the Email of the current user
  * UNIQUEID() to create unique Text values for keys
  * ISBLANK(<expression>) to check if an expression is empty
  * CONCATENATE(<text-expression1>, <text-expression2>, ...) to combine two or more text values
  * LEN(<text-expression>) to get the length of a text value
  * IF(<condition>,<then-expression>,<else-expression>) 

Other Functions

  * SECOND(duration) for the Second component of a Specific Time
  * MINUTE(duration) for the Minute component of a Specific Time
  * HOUR(duration) for the Hour component of a Specific Time
  * DAY(date) for the Day of the Month
  * WEEKDAY(date) for the Day Number from a Date
  * WEEKNUM(date,[type]) for the Week Number from a Date
  * MONTH(date) for the Month Number from a Date
  * YEAR(date) for the Year from a Date

For backwards compatibility, we also support the function syntax below for a
set of functions that have been supported from the earliest AppSheet release.

  * @(_TODAY) for Date
  * @(_TIMENOW) for Time
  * @(_NOW) for DateTime
  * @(_HERE) for LatLong
  * @(_USERNAME) for Name
  * @(_USEREMAIL) for Email
  * @(_UNIQUE) for unique Text values  
  

**Arithmetic**

Use any of the arithmetic operators below to build arithmetic expressions:

  * **Add**: +
  * **Subtract**: -
  * **Multiply**: *
  * **Divide**: /

Each of these operators is used with two numeric expression parameters: 3+2,
5.0/2.3, etc. Add and Subtract can also be used with dates and datetime types
to add or subtract days:

  * TODAY() + 1 adds a day to the current Date 
  * TIMENOW() - 1 subtracts a day from the current DateTime
  * TODAY() - "12/12/2001" gets a Duration between the two dates
  * TIMENOW() + "003:03:00" adds a 3 hours and 3 minutes to the current DateTime

Combine arithmetic expressions with parentheses to form complex expressions
like: (`[ColumnA]*2) + ([ColumnB]*3)` or `@(_TODAY)+([ColumnA]+1)  `
  
**Comparison conditions**

AppSheet also supports comparison operators in expressions that return true or
false.

  * **Equals**: =
  * **Not Equals**: <>
  * **Greater Than**: >
  * **Greater Than or Equals**: >=
  * **Less Than**: <
  * **Less Than or Equals**: <=

Each of these operators is used with two expression parameters that have
comparable types. For example, `5 > 2` is valid, but `5 > "Hello"` is not.  
  

**Composite conditions**

These expression combine comparison expressions utilizing three composition
operators:

  * AND(expr1, expr2, ...) : returns true if all the sub-expressions are true
  * OR(expr1, expr2, ...): : returns true if any of the sub-expressions are true
  * NOT(expr): returns true if the sub-expression is false and vice-versa


## Related articles {.section}

  * [App formulas](App-formulas.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [Virtual columns](Virtual-columns.md)
  * [Slices](Slices.md)
  * [Modifying column structure in the editor](Modifying-column-structure-in-the-editor.md)

