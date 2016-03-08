#  Column structure


January 07, 2016 20:44

Every table has a column structure which is a list of column definitions. All
the rows of the table conform to this structure.

Each column definition has these attributes:

  * Name: this correlates to the column header in the spreadsheet
  * Description: a verbose description suitable for the application end-user
  * Type: one of the column types supported by AppSheet (for example, Number or Text)
  * Type Qualifier: optional further information to specialize the type
  * App Formula: an expression used to compute the value of the column
  * Column behaviors: 
    * Is it part of a key?
    * Is it a hidden or visible in the app?
    * Is it read-only in the app?
    * Is it searchable in the app?
    * Is it scannable in the app?
    * What default value should be assigned to this column in a new row?

The type is the most important component of the column definition and has a
significant impact on the behavior of the app.  


**Regenerating the column structure**

If you have already created an app from your spreadsheet and you go back and
make changes to the spreadsheet's column structure, you will need to
regenerate the column structure in the AppSheet Editor so AppSheet can
recognize the new structure. You can do this in both the Basic and Advanced
Editors.

In the **Basic Editor**, click the Data tab. Click "Regenerate column
structure" at the bottom.

![basic editor](../article_attachments/204790027/Screen_Shot_016-01-07_at_1.40.44_PM.png)

In the **Advanced Editor**, click the Data>Column Structure tab. If you have
multiple spreadsheets, find the one you're looking for and click "Regenerate".  
  
![advanced editor](../article_attachments/204790057/Screen_Shot_016-01-07_at_1.4.34_PM.png)


## Related articles {.section}

  * [Column types](Column-types.md)
  * [Modifying column structure in the editor](Modifying-column-structure-in-the-editor.md)
  * [Tables](Tables.md)
  * [Slices](Slices.md)
  * [Making an "AppSheet-friendly" spreadsheet](Making-an-AppSheet-friendly-spreadsheet.md)

