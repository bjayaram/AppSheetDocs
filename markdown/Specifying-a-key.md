#  Specifying a key


January 08, 2016 00:17

It is very important that AppSheet pick a good key for your dataset. AppSheet
needs to be able to uniquely identify each row of data in the spreadsheet. The
'key' is a single column that provides this unique identity. This helps
AppSheet synchronize changes made in the app back to the spreadsheet.

Many data sets naturally have a key, i.e. a column whose value does not change
and that uniquely identifies the row. For a product catalog, the product ID or
the product name are good keys. For a customer database, the customer name or
ID makes a good key. Make your key column the leftmost column if possible.
AppSheet processes the data left to right looking for a key column. Key
columns should not have duplicate values. AppSheet checks the data to see if
there are duplicates, and ignores some column types that are typically not
good keys (e.g. a URL or a timestamp). If no obvious unique key is found,
AppSheet tries to combine columns to form a 'computed' key. And if no other
option exists, the rownumber is picked as the key, but this has various
limitations so try to avoid this if possible.



**Generating a random key**

You have the option of generating a random text key for each entry to uniquely
identify it. This is useful for forms inputs that need to generate a key
field. To do this, use the Advanced Editor. Click the Data tab, and then the
Column Structure tab. Scroll to the field name you would like to have a random
text key, then scroll to the right, and in the Default Value field, type
_@(_UNIQUE)_.  
  

**AppFormulas and keys**

AppFormulas may be used in key fields provided the AppFormula always yields
the same result over time. That ensures that the key value remains consistent
over the life of the row. We examine the contents of the key field's
AppFormula to ensure that it yields the same result over time. We display an
error if it does not. For example, an AppFormula that includes the current
date or time might yield different results over time, so it would be
prohibited in a key field's AppFormula.  
  

**Using multi-column keys**

You can also specify more than one column as the key in your app. This will
combine the columns you choose, showing all chosen columns' values next to
each other in the app. You would do this to create a more refined key. From
the Advanced Editor, click the Data tab, then 'Column Structure.' Under
'Primary key?' check any number of boxes to form a multi-column key-- this
will appear at the bottom as the '_ComputedKey'.


## Related articles {.section}

  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-)
  * [Column types](Column-types)
  * [Keys](Keys)
  * [Spreadsheet formulas](Spreadsheet-formulas)
  * [How do I control the order of rows displayed in my app?](How-do-I-control-the-order-of-rows-displayed-in-my-app-)

