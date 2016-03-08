#  Capturing GPS location


January 13, 2016 22:00

Use a column of type LatLong to capture GPS locations.

There are three ways to capture the GPS location in a form:

  1. If you give the column a default value of '@(_HERE)' (using the advanced editor) then every time a new entry is added, the value of this column is auto-populated with the current location.
  2. The input field for a LatLong column has a clickable icon that lets you capture the current GPS location of the device. This is useful particularly when you want to update the value of a field to a new current location.
  3. You can explicitly type in a LatLong value-- eg: '46.34,-32.34'

As a special case, you can also use a column of type ChangeLocation to capture
GPS locations. Such a column captures the location when some other value in
the record changes. A separate article discusses Change types.

Whether on a mobile device or in a browser, the system will probably ask you
to give AppSheet permission to access your current location. If you are
running your app within a browser, this permission request may not be very
prominent (some browsers bring up a subtle request near the address bar and it
can be easy to overlook).


## Related articles {.section}

  * [Working with maps](Working-with-maps.md)
  * [Capturing images and documents](Capturing-images-and-documents.md)
  * [Tracking changes using 'Change' column types](Tracking-changes-using-Change-column-types.md)
  * [Column types](Column-types.md)
  * [Displaying images and documents](Displaying-images-and-documents.md)

