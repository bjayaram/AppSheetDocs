#  Presentation types


January 13, 2016 02:33

AppSheet supports five presentation views--** list, image gallery, map, chart,
**and** form**.  
  
All of the views show a 'summary' view of the data with the ability to drill
into a 'detailed' view of one specific entry. As with other aspects of
AppSheet, the platform automatically generates most of the UX and the app
creator guides the outcome primarily be changing the structure of the data.

  * **List**\-- this is the default view of tabular data. There are three display styles to choose from:  
  

  * Tabular: each row is showed in a compact representation. Tapping or clicking on a row expands it to show all the details. An extra option specifies the column to sort the data on. You can choose to sort the data in ascending or descending order.
  * Grouped: rows are grouped together based on the value in the grouping column specified. Within each group, the data is shown using the tabular view and sorted based on the order of data in the underlying spreadsheet.
  * Deck: this is a special presentation for data that has an image column. The data is displayed as a stack of 'cards', and clicking on any of them expands the card and its image. The deck view allows for round and square image presentations. 

[See how lists work in our Recruiting sample
app.](https://www.appsheet.com/Template/SimpleDef?appName=Recruiting-10305)

2\. **Gallery**\-- this is the default view of data that has an image or
thumbnail image column. The content is shown in a 'summary' view as an image
gallery where each image is annotated with the row key. Clicking on any image
opens up a full screen 'details' view of the image along with the other row
columns. Once in the full screen details view, the user can swipe left or
right to move to adjacent rows. This presentation has three sub-options that
control the size of the images shown in the summary view:

  * Small: appropriate for thumbnail images.
  * Medium: fits two images side by side on a phone screen.
  * Large: shows large images full-width with a vertical scroll.

As with the List view, you can choose a column to sort the order of
presentation of the data. [See how the gallery works in our Product Catalog
sample app.](https://www.appsheet.com/Template/SimpleDef?appName=ProductCatalo
g-10305)

3\. **Map**\-- the map view only makes sense if you have an Address column.
When you choose the Map view, AppSheet automatically picks up the data from
your Address column, geocodes those addresses, and shows them on a map. [See
how maps work in our Contact Directory sample
app.](https://www.appsheet.com/Template/AppDef?appName=ContactDirectory-10305)

[ Read a detailed blog post about the map
feature.](http://blog.appsheet.com/2014/11/19/use-the-map-view-feature-to-
visualize-addresses-in-your-app/)

4\. **Chart**\-- we support a number of different chart presentations. In
general, charting is a complex topic. As the designer of a chart, you
typically have to make three choices:

  * How many individual series 'lines' do you draw?
  * What values are on the X and Y axes?
  * What chart display type do you use-- line, bar chart, etc.

We have tried to keep it simple by limiting the possible answers for each of
these choices:

  * Row Series chart-- this is appropriate for spreadsheet data where most of the data is numeric on a uniform scale (eg: monthly sales data). Every row forms a series, each of which is identified by the row key. You choose a subset of the column names that will be charted on the X axis. The Y axis is based on the numeric values in the row cells. You can choose a line chart, a bar chart, or a stacked bar chart as the display type. A good example of a Row Series chart is the 'By Month' view in the [Sales Report sample.](https://www.appsheet.com/Template/ShowDef?appName=DataInsight-10305)
  * Column Series chart-- this is appropriate for spreadsheet data with just a few rows corresponding to items to compare (eg: monthly sales data by category). Every column forms a series, each of which is identified by the column name. Each row (using its row key column) forms one entry on the X axis. The Y axis is based on the numeric values in the row cells. You can choose a line chart, a bar chart or a stacked bar chart as the display type. A good example of a Column Series chart is the 'By Type' view in the [Sales Report sample.](https://www.appsheet.com/Template/ShowDef?appName=DataInsight-10305)
  * Histogram-- this is a special kind of bar chart to show aggregate distributions. For example, if you want to see the number of customers who purchased each automobile model, you specify the column whose values will be aggregated. The X axis gets one entry for each unique value in this column and the Y axis shows the count of the number of rows that have that value in that column.

5: **Form**\-- Your apps give you the ability to capture signatures, photos,
and location services.You can use AppSheet for Google Forms to both distribute
forms through a mobile app as well as use a mobile app to view and interact
with form responses. But if you're only using your app to distribute forms,
you probably don't want your app showing each user's response, and instead
have each new user simply be able to fill out a new form with the app.

To do this, click the UX tab in either editor. In the Basic Editor, choose
'form' from the dropdown list of presentation view types. In the Advanced
Editor, click the UX tab, then 'Controls'. From there choose 'form' from the
dropdown list of presentation view types under the Action field.

New guests to the form will only be able to fill out a new form and will not
see entries made by previous users.

AppSheet also helps you unlock mobile-specific features for your Forms that
the web cannot capture. Your apps give you the ability to capture signatures,
photos, and location services.

6\. **Deck**\-- A view that displays a large image on the left, in your choice
of either a round, square, or full presentation, with the most important
information on the right and any action buttons that correspond to your field
types.

7\. **Table**\-- This presentation is best with handling large data sets with
many rows.

Over time, we will add more chart types, while trying to keep the concepts
simple.

[ Read a detailed blog post about presentation types.](http://blog.appsheet.com/2014/12/10/4-types-of-views-to-enhance-your-appsheet-apps/)


## Related articles {.section}

  * [How do I control the order of rows displayed in my app?](How-do-I-control-the-order-of-rows-displayed-in-my-app-.md)
  * [Expressions](Expressions.md)
  * [Conditional formatting](Conditional-formatting.md)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-.md)
  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)

