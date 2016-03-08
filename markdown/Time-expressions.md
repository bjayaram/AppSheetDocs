#  Time expressions


February 22, 2016 15:18

Expressions may be used in various AppSheet features -- Initial Values, App
Formulas, Virtual Columns and Column Constraints (Valid_If, Show_If,
Required_If) -- to customize app behavior and provide your users with advanced
functionality. Expressions in this article align with the **Time Expressions**
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



**Time conditions**

Time Expressions utilize Dates or Durations to return a DateTime, Date, Time,
Duration or Number value. AppSheet conditions are not a 1:1 match with Google
Sheets functions; however, in some cases the formatting similarity may help
you construct your expressions. Alternatively, if the formatting is not
similar, the Google Sheets function page may provide context for use of the
function. If available, see the Google Sheets function link in parentheses
next to applicable operators.

**Current operators**

  * NOW() for the current DateTime  ([NOW](https://support.google.com/docs/answer/3092981?hl=en&ref_topic=3105385))
  * TODAY() for the current Date  ([TODAY](https://support.google.com/docs/answer/3092984))
  * TIMENOW() for the current Time  ([TIME](https://support.google.com/docs/answer/3093056?hl=en&ref_topic=3105385))
  * HOUR({Duration}) for the Hour component of a Specific Time  ([HOUR](https://support.google.com/docs/answer/3093045?hl=en&ref_topic=3105385))
  * MINUTE({Duration}) for the Minute component of a Specific Time  ([MINUTE](https://support.google.com/docs/answer/3093048?hl=en&ref_topic=3105385))
  * SECOND({Duration}) for the Second component of a Specific Time  ([SECOND](https://support.google.com/docs/answer/3093054?hl=en&ref_topic=3105385))
  * DAY({Date}) for the Day of the Month  ([DAY](https://support.google.com/docs/answer/3093040?hl=en&ref_topic=3105385))
  * MONTH({Date}) for the Month Number from a Date  ([MONTH](https://support.google.com/docs/answer/3093052?hl=en&ref_topic=3105385))
  * YEAR({Date}) for the Year from a Date  ([YEAR](https://support.google.com/docs/answer/3093061?hl=en&ref_topic=3105385))
  * WEEKDAY({Date}) for the Day Number from a Date  ([WEEKDAY](https://support.google.com/docs/answer/3092985?hl=en&ref_topic=3105385))
  * WEEKNUM({Date}) for the Week Number from a Date  ([WEEKNUM](https://support.google.com/docs/answer/3294949?hl=en))

**Legacy operators**

For backwards compatibility, we also support the function syntax below for a
set of functions that have been supported from the earliest AppSheet release.

  * @(_NOW) for the current DateTime  ([NOW](https://support.google.com/docs/answer/3092981?hl=en&ref_topic=3105385))
  * @(_TODAY) for the current Date  ([TODAY](https://support.google.com/docs/answer/3092984))
  * @(_TIMENOW) for the current Time  ([TIME](https://support.google.com/docs/answer/3093056?hl=en&ref_topic=3105385))


**Common and complex expressions**

**Common expressions**

  * TODAY() + 1: adds 1 day to the current Date 
  * NOW() - 1: subtracts 1 day from the current DateTime
  * TODAY() - "12/12/2001": returns a Duration between the two dates
  * TIMENOW() + "03:03:00": adds 3 hours and 3 minutes to the current Time

**Complex expressions**

  * @(_TODAY)>([TargetDate]+1)



**Time expression patterns, results and examples**

From the **Expression Builder**, follow the pattern below for a DateTime,
Date, Time, Duration or Number result. See the results and examples for
further clarity.

**Pattern**
**Result**
**Example**

NOW()

DateTime

NOW()

TODAY()

Date

TODAY()

TIMENOW()

Time

TIMENOW()

HOUR({Duration})

Number

HOUR([Duration])

MINUTE({Duration})

Number

MINUTE([Duration])

SECOND({Duration})

Number

SECOND([Duration])

DAY({Date})

Number

DAY([Date])

MONTH({Date})

Number

MONTH([Date])

YEAR({Date})

Number

YEAR([Date])

WEEKDAY({Date})

Number

WEEKDAY([Date])

WEEKNUM({Date})

Number

WEEKNUM([Date])

{value_1} + {number}

Date

[Date] + 1

{value_1} - {value_2}

Duration

[Date] - (TODAY() + 1)

{value_1} - {duration}

Date

[Date] - "002:00:00"

{value_1} - {number}

DateTime

[DateTime] - 1

{value_1} - {value_2}

Duration

[DateTime] - (NOW() + 1)

{value_1} + {duration}

DateTime

[DateTime] + "002:00:00"

{value_1} + {number}

Duration

[Duration] + 1

{value_1} - {value_2}

Duration

[Duration] - (0:00:00 + 1)

{value_1} - {duration}

Duration

[Duration] - "002:00:00"

{value_1} - {number}

Time

[Time] - 1

{value_1} - {value_2}

Duration

[Time] - (TIMENOW() + 1)

{value_1} + {duration}

Time

[Time] + "002:00:00"



## Related articles {.section}

  * [Columns expressions](Columns-expressions.md)
  * [Expressions](Expressions.md)
  * [Math expressions](Math-expressions.md)
  * [Lists expressions](Lists-expressions.md)
  * [Yes/No expressions](Yes-No-expressions.md)

