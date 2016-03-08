#  Using formats and data validation rules


January 08, 2016 02:28

Spreadsheets have a built-in mechanism called 'formats' to indicate the type
of data in a cell. Especially when using dates and times with custom formats,
please assign spreadsheet formats.

Spreadsheets allow you to pick a format for each cell. However, AppSheet is
deducing a data type for every column, not every cell. So make sure to apply
the same format to all non-header cells in a column. This is the most normal
use of formats anyway. In the case below I'm making sure to set my Date column
to the Date format under the Format menu.

**Specifying data validation rules (dropdown menus, or enums) in the spreadsheet**

Spreadsheets have a built-in mechanism called data validation rules to
constrain the allowed values in a cell. Utilize this mechanism if you want a
column to have an 'enumeration' type, i.e. a dropdown list of allowed values.
You can either do this by manually typing in the allowed values into the
validation list (not recommended), or selecting a predefined set of cells that
already contain the allowed values (recommended).

When you have lots of legal enum values, we suggest creating an additional
worksheet in your workbook to contain all of these enum values. The
alternative, manually typing in the allowed values into the validation list,
imposes a limit of 256 characters for the entire list. For clarity, we will
refer to the original worksheet containing your application data as the
“DataSheet”. We will refer to the legal enum values worksheet as the
“EnumSheet”.

**Do the following:**

  1. Add a new worksheet to your Google workbook to contain your legal enum values. 
  I am referring to this as the “EnumSheet”.  
  
## Related articles {.section}

  * [Column types](Column-types.md)
  * [Spreadsheet formulas](Spreadsheet-formulas.md)
  * [App formulas](App-formulas.md)
  * [Conditional formatting](Conditional-formatting.md)
  * [Modifying column structure in the editor](Modifying-column-structure-in-the-editor.md)

