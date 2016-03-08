#  Column types


February 21, 2016 01:55

Here is a list of available column/data types. We expect this list to grow
over time...

**Text types**

* **Text**: models a short piece of text (a few words) shown on single line.
* **Name**: special case of a Text type that represents the name of a person or place. 
* **LongText**: models longer text content shown across several lines.  
  

**Numeric types** - in the app, values of these types can be graphed.

  * **Number**: models an integer value.
  * **Decimal**: models a number with decimal precision.
  * **Price**: models currency values. The TypeQualifier field can be used to indicate a currency symbol ($ is the default).
  * **Percent**: represents percentage values.  
  

**Temporal types **- in the app, these values are shown utilizing the timezone and presentation format of the client device.

  * **Date**: models a day (day-month-year).
  * **Time**: models a time within a day (hour-minute-second).
  * **DateTime**: models the day and the time.
  * **Duration**: models a period of time.  
  

**Change types** - in some apps, it is important to record a timestamp or increment a counter 
automatically in a row when changes are made to other columns, and even _values_ within the 
columns. The change types provide this functionality. When the Type Qualifier is empty, these 
change types automatically update when _any_ other column value changes. However, they can be 
constrained to react to changes only on specific other columns by providing a Type Qualifier 
of the form: {"ChangeColumns":\["Column1", "Column2"\]}. Change types can be constrained to 
react to changes on certain values using this format in the Type Qualifier: 
{“ChangeColumns”:[“Column1”], “ChangeValues”:\[“failed”,”error”,”urgent”\]}.

  * **ChangeTimestamp**: shows when an entry was last edited. See how this works along with a Type Qualifier in the [Store Inventory sample.](https://www.appsheet.com/Template/ShowDef?appName=ProductInventory-10305)
  * **ChangeCounter**: shows how many times an entry has been edited. See how this works without a Type Qualifier in the [Interview Feedback sample.](https://www.appsheet.com/Template/ShowDef?appName=InterviewFeedback-10305)
  * **ChangeLocation**: will automatically populate with the current GPS location (where the change was made).  
  

**Enumerated types** - in the app, fields of these types are constrained to having one of a fixed list of allowed values.

  * **Yes/No**: also known as a 'Boolean' type, these values display as Y or N in the app and have a 'slider' choice mechanism in input forms.
  * **Enum**: models a text value that must belong to a specific list. The TypeQualifier contains the list of allowed values. This is typically generated automatically from data validation rules in your spreadsheet.  
  
You also have the ability to allow users to manually input data into dropdown
menus instead of only having the option to choose from the dropdown list. To
do this, choose the Enum type, and in the type qualifier, for example:  
`{"EnumValues":["One","Two","Three"],"AllowOtherValues":true}`  
  
When you have an enum that allows for the option "Other", typing in the box
will allow you to choose from a set of values in order to autocomplete the
entry. This allows users to choose from common entries that have already been
submitted, as well as to ensure all entries are submitted the same way,
avoiding typos.  
  

  * **EnumList**: allows the user to select multiple answers on a question. The TypeQualifier contains the list of allowed values. This is typically generated automatically from data validation rules in your spreadsheet.
  * **Ref**: an advanced feature that models a value that must be the key of another table or slice. The TypeQualifier contains the name of the referenced table or slice. See how table references work in the [Order Capture sample.](https://www.appsheet.com/Template/ShowDef?appName=OrderCapture-10305)
  * **Color**: color code entries in your app with a subset of 6 standard colors: Red, Yellow, Green, Orange,  Purple, and Blue.  
See how color coding works in the [Project Plan sample.](https://www.appsheet.com/Template/ShowDef?appName=MarketingPlan-10305)

  * **Progress**: show the progress of an entry by utilizing a ‘Harvey Ball’ ideogram. 
  See how the progress function works in the [Project Plan sample.](https://www.appsheet.com/Template/ShowDef?appName=MarketingPlan-10305)

**Communication types** - in the app, values of these types can be tapped to launch communication.

  * **Phone**: models a phone number -- gives you the option to both call and SMS text through the app.  
  * **Email**: models an email address -- gives you the ability to send emails by clicking the email address.   
  

**Geographic types** \- in the app, values of these types can be seen on a map.

  * **Address**: models a fully-specified postal address.  
  
You can store address information in AppSheet by creating adjacent columns in
your worksheet and naming them appropriately. When you do this, AppSheet
automatically recognized that the adjacent columns form an address. For
example, you can create adjacent columns in your worksheet, and name them
“Street”, “City”, “State”, “Zip”. In this case, AppSheet will recognize that
taken together these columns represent an address and it will create a
"Computed Address” field that concatenates the values in these address fields.  
  
AppSheet can also handle multi-line “Street” addresses, so you can name your
columns “Street1”, “Street2”, “Street3”, “City”, State”, Zip”, if your
application requires multiple lines of street information. This can be useful
if you need to extend the address information with apartment numbers, unit
numbers, attention, care of, or other such, address information.  
  
AppSheet is also capable of handling two or more addresses in the same
worksheet. For example, your worksheet might contain both a “Home Address” and
a “Work Address”. AppSheet recognizes the two addresses based upon a
combination of naming and adjacency. Keep the “Home Address” columns adjacent
to one another and likewise for the “Work Address” columns. Then name the
columns to help AppSheet group them appropriately. For example, you might name
the "Home Address" columns “Home Street”, “Home City”, “Home State”, “Home
Zip”. You might name the "Work Address" columns “Work Street1”, “Work
Street2”, “Work City”, “Work State”, “Work Zip”. You can use this approach to
include three or more addresses in your worksheet, if necessary.  
  

  * **LatLong**: models a latitude and a longitude (eg: '48.5564, -122.3421'). 
  Form fields for this data type can fill in the current location with a single 
  click. See how location capture works in the 
  [Site Inspection sample.](https://www.appsheet.com/Template/ShowDef?appName=SiteInspection-10305)

**Content types** - in the app, values of these types are shown as inline content, or open in an external content viewer.

  * **Drawing**: creates a drawing pad in the app. 
  * **Image**: models .jpg, .png and .gif images. The values may be image urls or names of files in the source file system of the spreadsheet. Please reference the section describing how to use files as images. Images are captured on the device using the camera or from the local camera roll.
  * **Thumbnail**: also models images, but instructs the app to expect small icons and thumbnails. Thumbnails are captured just like images.
  * **Signature**: models user signatures. These are captured using a touch-based signature pad and are stored as small inline images in the spreadsheet.
  * **File**: models any file content that can be viewed in a browser (typically used for PDF documents). There is no capture mechanism for files in the app.
  * **URL**: models any web address.
  * **Show**: empty columns in your spreadsheet that serve the sole purpose of improving the presentation of **data capture forms**. There are six categories of show types:  

    1. Page_Header: used to create a new page within the form
    2. Section_Header: used to create a new section within the same form page
    3. Text: used to show some descriptive text
    4. Url: used to show a clickable url
    5. Image: used to show a static image
    6. Video: used to show an MP4 video

**System types** \- these are meant for internal use only and should not be
explicitly assigned by AppSheet users in the current version.

  * **MultiColumnKey**: a composite field representing the combination of multiple fields for the purpose of a key.
  * **App**: represents an AppSheet app handle.


## Related articles {.section}

  * [App formulas](App-formulas.md)
  * [Slices](Slices.md)
  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)
  * [Presentation types](Presentation-types.md)
  * [How do I control the order of rows displayed in my app?](How-do-I-control-the-order-of-rows-displayed-in-my-app-.md)

