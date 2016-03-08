#  Working with charts


February 20, 2016 21:19

We support a number of different chart presentations. In general, charting is
a complex topic. As the designer of a chart, you typically have to make three
choices:

  * How many individual series 'lines' do you draw?
  * What values are on the X and Y axes?
  * What chart display type do you use-- line, bar chart, etc.

We have tried to keep it simple by limiting the possible answers for each of
these choices:

  * **Histogram **\-- this is the ideal chart type to segment and drilldown a dataset. A histogram is a special kind of bar chart to show aggregate distributions. For example, if you want to see the number of customers who purchased each automobile model, you specify the column whose values will be aggregated. The X axis gets one entry for each unique value in this column and the Y axis shows the count of the number of rows that have that value in that column. You can specify multiple levels of drilldown by specifying multiple columns. 
  * **Row Series chart**\-- this is appropriate for spreadsheet data where most of the data is numeric on a uniform scale (eg: monthly sales data). Every row forms a series, each of which is identified by the row key. You choose a subset of the column names that will be charted on the X axis. The Y axis is based on the numeric values in the row cells. You can choose a line chart, a bar chart, or a stacked bar chart as the display type. A good example of a Row Series chart is the 'By Month' view in the [Sales Report sample.](https://www.appsheet.com/samples/A-car-sales-reporting-app-with-helpful-visual-graphs-driven-by-sales-data-?appGuidString=033f7ab1-4f16-4adb-8bd9-0dd6a7433bb5)
  * **Column Series chart**\-- this is appropriate for spreadsheet data with just a few rows corresponding to items to compare (eg: monthly sales data by category). Every column forms a series, each of which is identified by the column name. Each row (using its row key column) forms one entry on the X axis. The Y axis is based on the numeric values in the row cells. You can choose a line chart, a bar chart or a stacked bar chart as the display type. A good example of a Column Series chart is the 'By Type' view in the [Sales Report sample.](https://www.appsheet.com/samples/A-car-sales-reporting-app-with-helpful-visual-graphs-driven-by-sales-data-?appGuidString=033f7ab1-4f16-4adb-8bd9-0dd6a7433bb5)

Over time, we will add more chart types, while trying to keep the concepts
simple.



## Related articles {.section}

  * [Presentation types](Presentation-types.md)
  * [Customizing input forms](Customizing-input-forms.md)
  * [Conditional formatting](Conditional-formatting.md)
  * [Expressions](Expressions.md)
  * [ Viewing external content](-Viewing-external-content.md)

