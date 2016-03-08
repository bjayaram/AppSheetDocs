#  Slices


January 22, 2016 00:32

A 'Slice' is a subset-- or filter-- of the rows and columns of a table. As the
definition suggests, it has three components:

  1. The table it is based on
  2. The (optional) subset of columns it retains
  3. The (optional) subset of rows it retains

A slice does not need to subset both the columns and the rows-- in fact, it is
common to subset just the rows or just the columns as appropriate.

When a slice subsets the rows in a table, it uses a 'Filter Condition' to
express the subset. A filter condition is a simple expression that can be
evaluated on a single row and return true (yes, include in the slice) or false
(no, exclude from the slice). For example, a filter condition 'Price > $1000'
might be used to define a slice of high priced products.

The use of filter conditions makes a slice a very powerful and dynamic
mechanism to model the data used in an app. While the slice definition stays
fixed, the actual rows that participate in the slice change as the underlying
table data changes.

Here's more about [how to implement slices](Defining-and-using-slices.md).

## Related articles

  * [Defining and using slices](Defining-and-using-slices.md)
  * [Advanced app customizations](Advanced-app-customizations.md)
  * [Expressions](Expressions.md)
  * [Spreadsheet formulas](Spreadsheet-formulas.md)
  * [Keys](Keys.md)

