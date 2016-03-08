#  References between tables


January 16, 2016 21:25

Once you have an app with [multiple spreadsheets](Using-multiple-spreadsheets.md) it's useful to create connections or
"References" between the sheets and slices.

Columns with a Ref column type always point to the **_Key_** field in the
table they are referencing. If you need other columns besides the reference
key field, consider using a De-reference (See [Expressions](Expressions.md)).

A reference example, the [Order Capture sample
app](https://www.appsheet.com/samples/An-app-for-a-salesperson-add-customers-orders-and-product-details?appGuidString=245700e5-9061-4045-843f-7850b5eb439a)
has a spreadsheet of products in inventory and a separate spreadsheet of
orders. The products spreadsheet is kept up to date with all the products in
the warehouse and when someone buys a product a new row is added to the orders
spreadsheet.

The problem is when a new order is created, the product information from the
products spreadsheet has to be manually copied into the orders spreadsheet.

This is a great place to use References. Since each row in the orders
spreadsheet has one product, we can add a column with the product id to the
orders spreadsheet. This connection between the spreadsheets will be used a in
few different areas of AppSheet to make your app much more convenient and
powerful.

![Table ref](../article_attachments/202449887/2015-07-21_11_51_18-erd.html_-_draw.io_-_Firefox_Developer_Edition.png)

**Creating references**

AppSheet will automatically create references between tables if there is a
column name that contains the name of another table in your app, followed by
the name of a column in that table. For example if you have a Customers table
that has a Name column, another sheet that has a column named Customer Name
will automatically be a Reference when the row is added.


Otherwise, you can create and modify references manually using the Advanced
Editor by setting the Field Type of a column to Ref and putting the name of
the spreadsheet to reference in the ReferencedType field.  
  

**Using references**

Appsheet will automatically turn References into links that you can select to
navigate to the referenced record.


![order capture Ref link](../article_attachments/203928847/Screen_Shot_2015-11-11_at_5.27.36_PM.png)

Additionally any record that is linked to will have a View and Add button.

![order capture Ref nav](../article_attachments/203928867/Screen_Shot_2015-11-11_at_5.28.15_PM.png)

**Refs as views in the app**

If you'd like to see a graph, map, or customize the view that you are taken to
when selecting View, you can create a new View in the Advanced Editor>UX.Views
tab and set the Position to ref.


## Related articles {.section}

  * [Expressions](Expressions.md)
  * [App formulas](App-formulas.md)
  * [Using a specific worksheet](Using-a-specific-worksheet.md)
  * [Presentation types](Presentation-types.md)
  * [Conditional formatting](Conditional-formatting.md)

