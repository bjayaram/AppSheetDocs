#  Using the app editor and a spreadsheet


January 09, 2016 00:37

AppSheet extracts tabular column structure from your spreadsheet, and works
best when the spreadsheet has regular tabular data-- the first row has column
headers and the remaining rows are data. Extraneous data, drawings, charts,
etc. may cause problems. Here's how you understand and control the process.

In the **Data** section of the Basic Editor, you see a few simple controls.
The **Browse Data** link opens the spreadsheet in a separate browser tab. If
you are using Google Sheets, this allows you to edit the Google sheet in one
tab while you see the effects on your app in the AppSheet tab.  
  

** **Preview Data** link, you see the first few rows of the
spreadsheet conforming to the column structure that AppSheet has extracted.
Each column has a header name and a data type. Also, one of the columns has
been identified as the [unique key](Keys). [This choice](How-should-I-choose-a-key-.md) is very
important-- the unique key helps AppSheet synchronize changes made in the app
back to the spreadsheet.  
  

** **Regenerate Column Structure**.  
  

** **switch to another spreadsheet**. There are two
reasons to do this-- perhaps you started with an example to play with and now
you want to switch to a 'real' spreadsheet with a very different structure, or
perhaps you want to switch to a different spreadsheet that has the identical
structure (eg: switching from test data to production data). In both cases,
AppSheet detects the new column structure and reacts appropriately to it.


## Related articles {.section}

  * [Create an app](Create-an-app.md)
  * [How should I choose a key?](How-should-I-choose-a-key-.md)
  * [Column types](Column-types.md)
  * [Modifying column structure in the editor](Modifying-column-structure-in-the-editor.md)
  * [Controlling data updates](Controlling-data-updates.md)

