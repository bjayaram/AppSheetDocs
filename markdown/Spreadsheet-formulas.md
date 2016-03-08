#  Spreadsheet formulas


January 08, 2016 02:31

Spreadsheets have very rich and expressive formula capabilities. These are
well-documented by the spreadsheet providers like Excel and Google Sheets.
When the mobile app reads data from the spreadsheet, the formula values are
computed. Likewise, when data is updated and synced back to the spreadsheet,
the appropriate formulas are computed again.

**There are two kinds of spreadsheet formulas:**

  1. In-row formulas: these are formulas that only use values from other cells in the same row. For example, if the formula for cell C2 = A2 + B2
  2. Multi-row formulas: these are formulas that use values from cells in other rows. For example, if the formula for cell C2 = C1 + 1

Columns with spreadsheet formulas are treated as Read-Only by AppSheet. This
is because spreadsheet formulas cannot be evaluated in the mobile app.
However, they are evaluated when data is sent to or from the backend
spreadsheet.

**  Formula consistency**

If all the cells in a column have the same formula, AppSheet recognizes that
the intent is for all new rows to also have that formula. As a result, new
rows inserted will include the formula.

On the other hand, if some cells in a column have a formula and other cells
have either no formula or a different formula, AppSheet will issue a warning
to the app creator. The column will be marked Read-Only but new rows will not
be assigned a formula in this column (because it is not clear what the desired
intent is).  
  

**Multi-row formulas with aggregates**

A common use of multi-row formulas in a spreadsheet is to compute aggregate
functions (totals, averages, etc). For example, a spreadsheet with individual
order items followed by a row with the order total. AppSheet apps require that
the rows in the same table be all of a similar nature --- i.e. all order items
--- because clearly there are different app behaviors expected with order
items and order totals.

AppSheet ignore rows with aggregate multi-row formulas after issuing a warning
to the app creator. This applies to both "totals rows" and "sub-totals" rows.



Note: spreadsheet formulas are distinct from [App Formulas](App-formulas.md). 
The two mechanisms are complementary and
both add value to your app. App Formulas run while the user is updating data
in the app, and will work even when the app is offline.


## Related articles {.section}

  * [App formulas](App-formulas.md)
  * [Expressions](Expressions.md)
  * [Specifying a key](Specifying-a-key.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [Slices](Slices.md)

