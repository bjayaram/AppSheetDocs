#  Working with maps


January 27, 2016 23:46

Whenever you have address or lat/long geocoded data, AppSheet provides the
ability to see it on a map. Columns of the Address or LatLong data types can
be shown on maps. We utilize the Bing maps platform to handle addresses and
mapping.

We rely on **Google Maps** to provide driving directions. If you are using an
iPhone or iPad device, you must install Google maps on that device to obtain
driving directions.

[See how the map function works in our Service Log sample
app.](https://www.appsheet.com/samples/An-app-for-field-service-technicians-to-log-customer-visits?appGuidString=083269d9-34b7-467a-bb14-bcad351adcbc)

**[Read a detailed blog post about using the map feature.](http://blog.appsheet.com/2014/11/19/use-the-map-view-feature-to-visualize-addresses-in-your-app/)**

Here are some other tips to make sure maps work well for you:

  * **If you use the LatLong data type**
    * the data values should be of the form "44.2456, -122.3348", i.e. comma-separated latitude and longitude values.
    * LatLong data can also be captured in a form field when editing entries or adding new entries. This uses high-accuracy GPS location capture on your device, which is potentially a time-consuming and battery-intensive operation. This function should therefore be used only in appropriate situations.
  * **When using addresses**
    * try to provide complete addresses (including city and country). This may seem redundant. For example, a local business in one city may record addresses without a City, State, Country, and ZipCode. While this makes sense to the customer, Bing maps does not have the context to know to which city '100 Main Street' refers. Always try to provide as much information as possible.
    * if you find that your addresses are not being mapped correctly, try to look up the address at maps.bing.com to see if there is a problem with the way the address is written.

## Related articles {.section}

  * [Capturing GPS location](Capturing-GPS-location.md)
  * [Conditional formatting](Conditional-formatting.md)
  * [Capturing images and documents](Capturing-images-and-documents.md)
  * [Working with charts](Working-with-charts.md)
  * [Expressions](Expressions.md)

