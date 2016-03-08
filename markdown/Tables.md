#  Tables


February 09, 2016 03:26

The first step for your data to become an AppSheet app is to be added as a
table to the template of the app. It means the data is still going to be in
your spreadsheet, the table is simply a "model" of the rows and columns in it.
This is the first step in creating an App Definition.

**This is how we see columns and rows in AppSheet:**

**Columns:** AppSheet reads each column header to define the Column Structure of the app. Every time you change the columns in the spreadsheet, then you need to regenerate the column structure in the app or AppSheet won't know how to locate the columns to read/write data. Column headers are essential to your app, you need column headers for each column where you want to collect data

**Rows:** Every time you add new data, a new row will be added to the spreadsheet. This is very important to understand. You want the columns in your table to never or rarely change while the rows can change as needed by adding, deleting or updating new data. 

**Adding Multiple Tables**

To add multiple tables after you created your app, go to Advanced Edit > Data > Tables and add a new table:

![New table](../article_attachments/205257818/Tables1.png)

AppSheet will ask you to select a new file, if you have multiple data sources, it will prompt you to select a new data source; it can be the same spreadsheet or a completely new one from a different data source. Great for data mashups!

When you add a new table - or when you are editing an existing table - you can choose how data is accessed in the app. You can allow people to Add, Update, Delete or any combination of those three. 
![Table definition](../article_attachments/205290917/Tables2.png)

You can also choose a specific tab inside the table by adding its exact name in the Worksheet Qualifier field. 

Tables are the first step for a solid AppSheet app. And you can bring a lot of richness 
with multiple tables and data access levels.  

** A few tips for tables:**

  * You can add the same spreadsheet any times you need. This is useful if you want to use one table for read only (show data) and the same data table to capture data in a different view. 
  * Even though AppSheet can see the row number in a spreadsheet, it doesn't locate the row by it's number but rather by a data point in one of the columns. That's where the concept of [Keys](Specifying-a-key.md) become essential in an AppSheet app
  * Using keys as a way to locate rows in the spreadsheet also allows for multiple users adding data at the same time. AppSheet will "serialize" the data going back to the spreadsheet from the app, letting the last person to write in a cell to "win".

## Related articles {.section}

  * [Column structure](Column-structure.md)
  * [References between tables](References-between-tables.md)
  * [Column types](Column-types.md)
  * [Slices](Slices.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)

