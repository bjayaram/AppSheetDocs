#  Mobile-specific features in my app


October 26, 2015 22:55

You should not expect to see a spreadsheet in your app. Your spreadsheet is
only a data source. You are creating an app optimized for a mobile device in
four ways: data presentation, data capture, offline use, and branding.

  1. Mobile devices have limited screen sizes, so each data row is presented using mobile-optimized patterns.
    * Most data views are summary views that expand to show the full details when an entry is clicked/tapped.
    * In summary views, we always show the key value and as many other columns as possible.
    * Actionable values (that launch actions when you tap them) like phone numbers and emails are preferentially shown.
    * Columns on the left of the spreadsheet are considered more important than columns on the right.
  2. Mobile-appropriate input controls are provided for different column data types.
    * If there is an Image column, it is populated by taking a photo with the camera.
    * Signatures can be captured on the touch screen. [See how the signature feature works in our Delivery Tracking sample app.](https://www.appsheet.com/Template/SimpleDef?appName=DeliveryTrack-10305)
    * Enumerated types (defined by data validation lists in the spreadsheet) get a dropdown list to choose from.
  3. Each app can be branded in a variety of ways, including with a logo. When you distribute your app to your users, you will control the brand experience for your users.
  4. Apps that require connectivity and constantly utilize the network significantly reduce battery life. AppSheet apps are designed for offline access with only occasional synchronization over the network. The data used by the app therefore is cached locally on the device. This does constrain the volume of data that can be used in an app-- for this reason, in the current version of AppSheet, avoid extremely large spreadsheets. All updates on the device are made locally and pushed to the backend spreadsheet only during synchronization.



## Related articles {.section}

  * [AppSheet is NOT...](AppSheet-is-NOT-.md)
  * [Create an app](Create-an-app.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [Extracting structure from cloud spreadsheets](Extracting-structure-from-cloud-spreadsheets.md)
  * [Controlling data updates](Controlling-data-updates.md)

