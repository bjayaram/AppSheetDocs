#  Other expressions


February 22, 2016 16:26

Expressions may be used in various AppSheet features -- Initial Values, App
Formulas, Virtual Columns and Column Constraints (Valid_If, Show_If,
Required_If) -- to customize app behavior and provide your users with advanced
functionality. Expressions in this article align with the **Other Expressions
**in the **Expression Builder** of the **Advanced Editor**. The Expression
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

  * Name any column using square brackets around the exact column name: **[ColumnName]**. When combining a [ColumnName] with another value, put the expression in **(parentheses)**. May be used in any expression; however, when used in the Initial Value feature, it may only refer to a separate table.



**Other conditions**

Other expressions impact a range of scenarios and don't fit into any of the
previous Yes/No, Math, Time, Columns, or Lists expression categories. AppSheet
conditions are not a 1:1 match with Google Sheets functions; however, in some
cases the formatting similarity may help you construct your expressions.
Alternatively, if the formatting is not similar, the Google Sheets function
page may provide context for use of the function. If available, see the Google
Sheets function link in parentheses next to applicable operators.

**Current operators**

  * LEN(<text-expression>) to get the length of a text value  ([LEN](https://support.google.com/docs/answer/3094081))
  * CONCATENATE(<text-expression1>, <text-expression2>, ...) to combine two or more text values  ([CONCATENATE](https://support.google.com/docs/answer/3094123?hl=en))
  * LEFT({Text},{Number}) Returns a substring from the beginning of a specified string.  ([LEFT](https://support.google.com/docs/answer/3094079?hl=en&ref_topic=3105625))
  * RIGHT({Text},{Number}) Returns a substring from the end of a specified string.  ([RIGHT](https://support.google.com/docs/answer/3094087?hl=en))
  * FIND({Text},{Text}) Returns the position at which a string is first found within text, case-sensitive.  ([FIND](https://support.google.com/docs/answer/3094126?hl=en))
  * IF({condition},{then-expression},{else-expression})  ([IF](https://support.google.com/docs/answer/3093364?hl=en))  The last two values (then, else) of the expression, must be of the same type, i.e. text, number, etc.
  * UNIQUEID() to create unique Text values for Keys
  * HERE() for LatLong of the current user
  * USEREMAIL() for the Email of the current user
  * USERNAME() for the Name of the current user

**Legacy operators**

For backwards compatibility, we also support the function syntax below for a
set of functions that have been supported from the earliest AppSheet release.

  * @(_UNIQUE) to create unique Text values for Keys
  * @(_HERE) for LatLong of the current user
  * @(_USEREMAIL) for the Email of the current user
  * @(_USERNAME) for the Name of the current user

**Common and complex expressions**

**Common expressions**

  * LEN("AppSheet"): Returns 8.
  * CONCATENATE([First Name]," ",[Last Name]): Returns a Full Name.
  * IF([Status]="Open"."Green","Red"): Returns "Green" when Status equals Open; otherwise, returns "Red".

Example: Column called [AppName] with a value of "Sales-10305"

  * `LEFT[AppName, 5]`: Returns "Sales".
  * `RIGHT[AppName, 5]`: Returns "10305"
  * `LEFT([AppName], FIND("-",[AppName]))` gives you "Sales"

Use the following expressions in the Initial Value feature of the **Advanced
Editor**:

  * `UNIQUEID()`: Use to generate a unique Text value, e.g. a unique Invoice ID.
  * `HERE()`:  Use to identify the user's current LatLong.
  * `USEREMAIL()`: Use to populate record value based on user login
  * `USERNAME()`: This value is not reliably populated by cloud providers, please defer to USEREMAIL(). To obtain USERNAME() in this case, utilize a reference table based on the USEREMAIL(). See [References between tables](References-between-tables).

**Complex expressions**

  * `LEN([_THIS])<=10`: Use this expression in the Valid_If Constraint to restrict form field input to a maximum of 10 characters.
  * `IF([Status]="Open","Green",IF([Status]="Closed","Red",IF([Status]="Not Started","Blue","Purple")))`: Returns "Green" when Status equals Open; returns "Red" when Status equals Closed; returns "Blue" when status equals Not Started; otherwise, returns "Purple".



**Other expression patterns and examples**

From the **Expression Builder**, follow the pattern below for a null, numeric,
text, email, name, or LatLong result. See examples for further clarity.

Pattern

Result

Example

[{ref_column}].[{lookup_column}]

null

[Ref].[Ref]

`LEN({*})`

Number

LEN([ChangeTimestamp])

`CONCATENATE({*},{*})`

Text

`CONCATENATE([ChangeTimestamp],"value_1")`

LEFT({Text},{Number})

Text

`LEFT([Text],1)`

RIGHT({Text},{Number})

Text

`RIGHT([Text],1)`

FIND({Text},{Text})

Number

`FIND([Text],"text value")`

IF({Yes/No},{*},{*})

`IF([Yes/No],"value_1","value_2")`

USERNAME()`

Name

`USERNAME()`

`USEREMAIL()`

Email

`USEREMAIL()`

`UNIQUEID()`

Text

`UNIQUEID()`

`HERE()`

LatLong

`HERE()`


## Related articles {.section}

  * [Time expressions](Time-expressions.md)
  * [Lists expressions](Lists-expressions.md)
  * [Expressions](Expressions.md)
  * [Required_If](Required-If.md)
  * [Yes/No expressions](Yes-No-expressions.md)

