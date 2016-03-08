#  How do I control the order of columns displayed in the app?


January 18, 2016 23:36

If you’re using the Tabular or Grouped List views, or the Table view, you
might want to control the order in which your data columns appear. AppSheet
does its best guessing which are most important to show, but you may need to
take actions if you’d like to see columns in a different order in your app.
We'll describe how to manually control column order later on in this article.

_Note: the size of your device’s screen determines __how many__ columns you
see represented in a given view.  
  
_

**How AppSheet automatically orders columns**

Here are the general rules for how AppSheet handles column ordering:

  * Rule 1. We always show the key because the key, by definition, uniquely identifies each row. Without the key, it is unclear which data entry is being shown. If the key is hidden (by checking the “Hidden” checkbox in the Advanced Editor), we don’t show the key and instead show the data left to right. [You can read more about how to pick an appropriate key here.](Specifying-a-key.md)
  * Rule 2. Next we add any fields that call for 'actionable' icons (eg: a phone number, email address, etc). AppSheet assumes these items are things you'd want a 'quick click' action on. If Explicit column headers are enabled (in the UX>Style tab of the Advanced Editor), we don’t show actionable icons.
  * Rule 3. Then we proceed left to right in spreadsheet column order-- if some columns are more important to you, please move them to the left in the spreadsheet.
  * Rule 4. Many spreadsheets have a rightmost column that is computed by a formula-- eg: cost of items. If we recognize this pattern, we make sure to include this column.

Let’s see how this works in a real app built with AppSheet: a cost estimator
put together by a fictional auto repair shop to calculate the resulting total
profit from jobs done in one week.

First, let’s take a look at the original spreadsheet-- there are four columns:
Service, Total, Cost, and Type.  
  

****** 
Once the app is created from the spreadsheet, either through AppSheet’s Google
Sheets add-on or straight from AppSheet.com, you can now view it live in the
app emulator.  
  

****** 
You’ll note that my leftmost column, Service, is showing first in the app.
Since the Service column is the first column in my spreadsheet _and_ the items
within the column don’t repeat twice, AppSheet chose Service as the [key](Specifying-a-key.md) for my app-- so that’s what shows
first.

If you click into any of the entries in the app, you’ll be able to see the
rest of the columns and data.

****** ****  
****

**Manually ordering columns**

Our goal is to do our best at guessing your preferred column order based on
how your spreadsheet is constructed. However, there may be some cases where
you wish to manually decide which columns are displayed in the main view. You
can manually reorder columns with the **Table UX view type**.

To do this, go to the Advanced Editor>UX>Views tab. Click the edit icon next
to the view whose columns you want to reorder.

Let's see how this works in the Profit Calculator app.

Originally, my columns were ordered according to my spreadsheet, with
"Service" first and then "Total" next. But let's say that I would like to
instead see "Type" and "Cost" first.

To do this, in the Advanced Editor>UX>Views tab, I'll first click the edit
icon next to the view I want to edit. Then, in the ColumnOrder field, I'll
click the "+" button for each column that I want to see in the main view.

** **Controlling column width**

AppSheet doesn't let app creators manually set column sizes due to the wide
variety of phone and tablet screen sizes. Instead we provide an option to
control how wide the columns are.

While editing a view in the Advanced Editor>UX>Views tab. There is an option
named ColumnWidth.:  
  
** **Default**\-- Columns will be automatically sized based on the size of the row content and column type.  
  
** **Wide**\-- Columns will be automatically sized but will be given some extra space. Use this option if you're having trouble with some columns being truncated.  
  
** **Narrow**\-- Columns will be automatically sized but will be smaller than they otherwise would be. Use this option to fit more columns onto small phone screens by truncating more text than normal.  
  
## Related articles {.section}

  * [Specifying a key](Specifying-a-key.md)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-.md)
  * [Choosing and adding data views](Choosing-and-adding-data-views.md)
  * [Reflecting your brand](Reflecting-your-brand.md)
  * [Change alerts and workflows](Change-alerts-and-workflows.md)

