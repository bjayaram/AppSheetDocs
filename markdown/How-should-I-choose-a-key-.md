#  How should I choose a key?


January 09, 2016 01:28

In this article, we'll explain:

  * what a key is
  * why it matters
  * how keys are chosen and how you can influence the choice
  * how keys are displayed in your app
  * why RowNumber is bad for a key
  * how to generate unique key values

The example of an auto repair shop will be used to expand on these topics.  
  

  * **What is a key and why does it matter?**

A key **uniquely** identifies each individual row in the table. For example,
for a product catalog, the Product ID or Product Name are good keys since each
of those items will likely never repeat twice. Likewise, a First Name column
wouldn’t be a good key since first names are likely to repeat more than once.

The key may be a single column (such as Product ID) or a composite column
(such as FirstName and LastName). Many data sets naturally have a key.  
  

  * **How keys are chosen**

When you create an app from your spreadsheet, AppSheet intuitively assigns a
key by searching your data for columns without duplicate values. If AppSheet
can’t find a suitable key, it will combine two columns to create a “Computed
key.” If it _still_ can’t find a good key by combining two columns, row number
will become the key; but row number as a key is generally not a good idea--
we’ll talk more about that later in this section.

It’s a good practice to make your intended key the leftmost column in your
spreadsheet, if possible, since AppSheet reads the data from left to right.
That being said, AppSheet will still scan the data and assign a key it thinks
is best.

Let’s say I work for an auto repair shop and I’m keeping track of our weekly
services rendered and the total resulting profit. In my spreadsheet the _type_
of service is the leftmost column.

** ****

  * **How keys are displayed**

Although Type is my leftmost column, once I generated a mobile app from the
data (using the Google Sheets add-on) AppSheet chose Service as the key,
because there is repeating data in the Type column and unique data in the
Service column. AppSheet assumes the column with the key is the most important
and therefore displays it first, [according to Rule 1 of how columns are
displayed](How-do-I-control-the-order-of-columns-displayed-in-the-app-).  
  

** **Info** tab):  


  * **Why is RowNumber bad for a key?**

As stated before, if AppSheet cannot find an appropriate key within your
spreadsheet, it will default the key to row number. This isn’t a good key
however, because if entries are moved or deleted, or if users add or delete
entries simultaneously, the row number for each row then changes and there is
no way for AppSheet to uniquely identify the row. AppSheet will also give a
warning if you choose row number as the key:  
  

  * **How do I automatically assign unique key values to my data?**

In some cases, you may need entries to automatically generate their own unique
keys-- for example, in an app designed to capture product orders, each order
must contain a unique order ID that cannot and should not be manually
assigned. Our [Order Capture sample](https://www.appsheet.com/samples/An-app-for-a-salesperson-add-customers-orders-and-product-details?appGuidString=245700e5-9061-4045-843f-7850b5eb439a) shows you how to
do this.

You’ll see the app employs four different tables: Customers, Products, Order
Details, and Orders.  
  

******  
  
If you scroll through the table structures you’ll see that each table has its
own key. In the Orders table, Order Code has been made the key, but there’s
just one more step to ensure each Order ID will be unique. You’ll need to
scroll to the right and insert @(_UNIQUE) in the Default Value field.  
  

****  
  
Now, when I go back to the Orders view and add a new order, a unique order
code has been automatically generated by AppSheet.  
  

## Related articles {.section}

  * [Expressions](Expressions.md)
  * [Specifying a key](Specifying-a-key.md)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-.md)
  * [How can I receive (or send.md) an email alert when data changes?](How-can-I-receive-or-send-an-email-alert-when-data-changes-.md)
  * [Change alerts and workflows](Change-alerts-and-workflows.md)
