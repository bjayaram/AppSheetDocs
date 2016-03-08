#  Making an "AppSheet-friendly" spreadsheet


January 07, 2016 21:20

You can control column structure by changing your spreadsheet.

  * Use the first worksheet-- by default, AppSheet only uses the first worksheet of your spreadsheet file. 
  And it only extracts one structured 'table' of data from that spreadsheet. So it is important that you 
  put the appropriate data in the first worksheet. Note that AppSheet apps can utilize multiple spreadsheet 
  files, a feature described in the Advanced Editor section. Also as described in that section, you can 
  explicitly specify a worksheet other than the first worksheet, if necessary.  
  

  * Just header + data please-- you could put almost any content in a spreadsheet, including charts, 
  pictures, free form text, etc. However, if the data isn't obviously tabular, AppSheet will probably 
  fail to extract a tabular column structure. Ideally make the first row contain column headers and the 
  rest of the rows contain data.  
  

  * Provide data for column type deduction-- if possible, provide at least 5-10 rows of actual data 
  in the spreadsheet. This allows AppSheet to look at the data and deduce their types. For example, 
  if every row of a column had an entry that looks like 'something.jpg', AppSheet can recognize that 
  this is an Image. However, users sometimes start with a blank spreadsheet and that leads AppSheet 
  to make poor guesses.  
  

  * Use data formats consistently, as described in [the next article](Effective-use-of-column-headers.md).   
  

  * Use spreadsheet data validation rules where appropriate, as described in 
  [a later article](Using-formats-and-data-validation-rules.md).  
  

  * Provide data for key identification, as described in [a separate article](Specifying-a-key.md).  
  

  * If AppSheet still doesn't quite get the column structure right, you can tweak it in the [Advanced Editor](/hc/en-us/articles/206559378.md).

[ Read a detailed blog post about structuring your spreadsheets.](http://blog.appsheet.com/2014/12/03/5-tips-for-building-better-spreadsheets-for-your-appsheet-mobile-apps/.md)



## Related articles {.section}

  * [Specifying a key](Specifying-a-key.md)
  * [Advanced app customizations](Advanced-app-customizations.md)
  * [App formulas](App-formulas.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-.md)

