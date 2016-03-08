#  Limits on data size


February 16, 2016 01:53

AppSheet is meant for mobile apps that are designed to work seamlessly despite
intermittent connectivity or completely offline. As a result, all data used by
the app must be cached locally on the mobile device. This is an important
factor to consider when designing your app.

Ideally, you should make your data set as small as possible to achieve the
desired functionality.



**Actual limits**

Do not build an AppSheet app against a huge data set. What is "huge"? For an
AppSheet app, the compressed data size limit is 5MB or 10MB (depending on the
device) for all the data in one app. It is difficult to translate this
accurately into a specific number of rows or columns because compressed data
size depends on how much repetition there is in the data. For example, a large
spreadsheet with a lot of empty cells will probably compress better than a
smaller spreadsheet with no empty cells. In general, the fewer cells in the
sheet, the better.

In the future, we may increase the 5MB/10MB limit.

"External" data like images and documents are not included in this data size
limit. You can definitely have applications with many rows and an image in
every row. Images and documents are not cached locally on the device by
default. If you do enable the option to cache images for offline access, they
are stored in a different location on the device that does not have the same
size limitations.



**Performance concerns**

In practice today, this is not a meaningful limit, because system performance
degrades well before you reach the limit. This happens for three reasons:

  1. Slow iterative development-- the data set is checked repeatedly during app development to ensure that the app is consistent with the data
  2. Long sync times-- when data is synchronized between the device and the backend, the delay depends on the size of the data set. 
  3. Sluggish app behavior-- large data sets can make the app itself sluggish in its interactions like scrolling, search, etc.



**Mitigations**

Always check if your sheets have empty rows in them. In particular, some
sheets have hundreds of empty rows at the bottom. Removing these rows will
improve performance.

Also check if your sheets have many extra worksheets that are not being used
by the app at all. Removing extra worksheets will improve performance.

In some circumstances though, the underlying dataset is large and just cannot
be changed. If so, consider using either of these options:

  1. Use a Security Filter to forcibly limit the data sent to the mobile app.
  2. use a slice to subset the data and strictly use only the slice in your app. This allows AppSheet to send just that subset of data to the device.

It is often the case that even if an app requires large data sets, much of the
data is read-only. In this situation, you can improve some aspects of app
performance by separating the read-only data sets into a separate table or
tables from those that are writeable/updateable.


## Related articles {.section}

  * [Expressions](Expressions.md)
  * [Slices](Slices.md)
  * [Including PDF's in your application](Including-PDF-s-in-your-application.md)
  * [Virtual columns](Virtual-columns.md)
  * [Conditional formatting](Conditional-formatting.md)

