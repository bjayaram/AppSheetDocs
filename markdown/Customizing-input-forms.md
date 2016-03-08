#  Customizing input forms


February 11, 2016 07:36

You can control the presentation of data input forms.

If you choose to allow users to add or edit data from within the Data pane,
your app will give users the ability to create or modify a data row using a
form. The form is a sequence of labels (column names) and input fields
(specific to the column data type). You can customize the form in the
following ways:

  * Column descriptions-- you might want to provide a verbose description of each column for the user. If a comment is found, it is used in the label instead of the column name.
  * Form style-- from the Advanced Editor>UX.Options tab, you can configure the layout of the form and whether the individual fields are numbered.
  * Using "Show"-type columns.

Show-type columns are empty columns in your spreadsheet that serve the sole
purpose of improving the presentation of data capture forms. There are six
Categories of Show types. Use the Type Qualifier to tell the Editor what to
show.

Categories:

  1. Page_Header: used to create a new page within the form
  2. Section_Header: used to create a new section within the same form page
  3. Text: used to show some descriptive text
  4. Url: used to show a clickable url  
**Here's an example of the Url Type Qualifier format: **  
**{"Category":"Url", "Content":"http://www.your-url.com"}**
  5. Image: used to show a static image  
**Here's an example of the Image Type Qualifier format:   
{"Category":"Image","Content":"http://www.your-url.com/your-image.png"}**

  6. Video: used to show an MP4 video or Youtube video (For MP4 videos, use the hosted link. For Youtube videos, use the embed link.)  
  
** **Here's an example of the Video Type Qualifier format: **  
** {"Category":"Video","Content":"https://www.youtube.com/watch?v=IdwbSNJwLAk"}**  

Check out our [Movie Survey sample](https://www.appsheet.com/samples/An-app-designed-to-collect-information-from-moviegoers-for-a-marketing-promotion?appGuidString=436c1296-5ac7-4c96-9df1-22a36d984af4) to see a video
embedded into a form using the 'Show' type.

[ Read a detailed blog post about customizing input
forms.](http://blog.appsheet.com/2014/12/18/use-appsheet-forms-to-get-mobile-data-back-home/)



**Input form as the only view in the app**

You can choose to make your input form the only view in your app, so new users
are not able to see past submitted data.

To do this, simply remove any data view from the UX tab of either Editor
(Advanced Editor>UX>Views, only keeping the form view.


## Related articles {.section}

  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-.md)
  * [Sync-- between the app and the backend](Sync-between-the-app-and-the-backend.md)
  * [Change alerts and workflows](Change-alerts-and-workflows.md)
  * [Who can discover and install your app?](Who-can-discover-and-install-your-app-.md)

