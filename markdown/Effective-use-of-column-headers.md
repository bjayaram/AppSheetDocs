#  Effective use of column headers


January 07, 2016 21:52

AppSheet infers the types of columns from the column header names as well as
from the content of the rows. Especially in cases where there are no existing
rows, it is important to pay attention to the column header names.

There are special words in column headers that 'trigger' AppSheet to infer
specific column types. For example, a column header name 'Web Site' suggests
that the data is of the URL type. Currently, this only works with English but
we intend to add similar capabilities for other languages in the future.

There are a few special cases to be aware of:

  * A column header ending with a question mark is inferred as a Yes/No data type. 
  * A column header ending with an exclamation mark is inferred as an action Url
  * A column header whose name is similar to another table already in the app may 
  be inferred as a table Ref type. For example, if there is a table called Products 
  and a new spreadsheet is added with a column called 'Product' or 'Products', 
  AppSheet will infer that it is a Ref type.

If you are building an app from a Google Form and your question is marked as
Text, a similar inference process occurs on the question title.  
  

**Here is a complete list of field types, what they do, and the trigger words that activate them:  **


* **Address **

What it does: Identifies the content of the field as a full postal address
that can be mapped. The completeness of the address will increase the accuracy
of the map location.**  
**Trigger words: "address", "where"**  
****  
**

* **ChangeCounter**

**What it does:** Shows how many times an entry has been edited.   
**Trigger words:** No trigger words. Must be selected in the Advanced Editor.  
  

* **ChangeLocation**

**What it does:** Automatically populates the GPS location where the change was made.  
**Trigger words:** No trigger words. Must be selected in the Advanced Editor.  
  

* **ChangeTimestamp**

**What it does:** Shows when an entry was last edited.  
**Trigger words:** No trigger words. Must be selected in the Advanced Editor.  
  

* **Color**

**What it does:** Displays a color entry in the app from a subset of 6 standard color names. Use IF Conditions in the spreadsheet to populate the color name based on a specific field.  
**Trigger words:** "blue", "green", "orange", "purple", "red", "yellow"  
  

* **Date**

**What it does:** Models a day (day-month-year).  
**Trigger words:** "birthday", "dob", "day", "month", "year"  
  

* **DateTime** 

**What it does:** Models the date and the time (day-month-year hour-minute-second).  
**Trigger words:** "date", "dates", "day", "days", "month", "months", "year", "years", "timestamp"  
  

* **Decimal**   

**What it does:** Models a number with decimal precision.  
**Trigger words:** "altitude", "altitudes", "amount", "amounts", "amt", "amts", "age", "ages", "capacity", "capacities", "depth", "depths",  "displacement", "displacements", "height", "heights", "hours", "latitude", "latitudes", "length", "lengths", "longitude", "longitudes",  "magnitude", "magnitudes", "mass", "masses", "population", "populations", "pop", "qty", "qtys", "quantity", "quantities", "size", "sizes", "sum", "sums", "total", "totals", "units", "weight", "weights", "width", "widths", "volume", "volumes"  
  

* **Drawing**

**What it does:** Enables a large field to make a simple drawing or capture notes. Choose from a set of seven colors.   
**Trigger words:** "depiction", "diagram", "drawing", "illustration", "layout", "likeness", "rendering", "sketch"  
  

* **Duration**

**What it does:** Models a period of time. Data should be in the format HH:MM:SS.   
**Trigger words:** "duration", "timespan", "period", "elapsed"  
  

  * **Email**

**What it does:** Enables to send an email using the default email app in the mobile device.  
**Trigger words:** "email", "e-mail"  
  

  * **Enum**

**What it does:** Picks up data validation from the spreadsheet and displays the list in the app. The list is picked only the first time the app is created and is not dynamically refreshed.  
Trigger words: No trigger words. Automatic if there is a validation list in
the column.  
  

  * **EnumList**

**What it does:** Allows multiple choice selection from a validation list.  
**Trigger words:** No trigger words. Must be selected in the Advanced Editor.  
  

  * **File**

**What it does:** You can reference files in your cloud drive (PDFs and similar documents) By adding a string indicating the location of the file in relation to the spreadsheet. For example. Reference/guide.pdf ß AppSheet will locate the file and add a link to it from the app.  
**Trigger words:** "file", "files"  
  

  * **Image**

**What it does:** Displays .jpg, .png, and .gif it also allows to capture images using the phone’s camera.  
**Trigger words:** "image", "images", "picture", "pictures", "photograph", "photographs", "photo", "photos", "figure", "figures", "fig", "figs", "icon", "icons", "illustration", "illustrations", "snapshot", "snapshots"  
  

  * **LatLong**

**What it does:** Reads latitude and longitude data (e.g. 48.5564, -122.3421) It can place the location on a map or use the mobile device location to populate the field.   
**Trigger words:** "latlong", "geolocation"  
  

  * **LongText**

**What it does:** Shows a large text box.  
**Trigger words:** "notation", "notations", "note", "notes", "desc", "description", "descriptions", "comment", "comments"  
  

  * **Name**

**What it does:** Text type that represents the name of a person of place. Shown as Text.  
**Trigger words:** "first", "givenname", "given-name", "last", "middle", "mi", "name", "names", "surname", "surnames"  
  

  * **Number**

**What it does:** Models an integer value.  
**Trigger words:** "altitude", "altitudes", "amount", "amounts", "amt", "amts", "age", "ages", "capacity", "capacities", "depth", "depths", "displacement", "displacements", "height", "heights", "hours", "latitude", "latitudes", "length", "lengths", "longitude", "longitudes",  "magnitude", "magnitudes", "mass", "masses", "population", "populations", "pop", "qty", "qtys", "quantity", "quantities", "size", "sizes", "sum", "sums", "total", "totals", "units", "weight", "weights", "width", "widths", "volume", "volumes"  
  

  * **Percent**

**What it does:** Shows percentage symbol.  
**Trigger words:** "%", "discount", "discounts", "interest", "percent", "percentage", "chance", "percentages", "probability", "probabilities", "quota", "quotas", "split"  
  

  * **Phone **

**What it does:** Enables calling or texting a phone number listed in the field directly from the app.  
**Trigger words:** "cell", "cellphone", "fax", "mobile", "pager", "phone", "phonenumber", "tdd", "tel", "telephone", "telex", "tty"  
  

  * **Postal Code**

**What it does:** This helps AppSheet detect an address when an address spans multiple columns. For example, a "Street" column, "City" column, and "Postal Code" column.  
**Trigger words:** "zip", "zipcode", "postalcode"  
  

  * **Price**

**What it does:** Shows a currency symbol. Use the **TypeQualifier** field to indicate anything different than **$.**  
**Trigger words:** "amount", "amounts", "amt", "amts", "balance", "balances", "bonus", "bonuses", "cash", "commission", "commissions", "compensation", "contribution", "contributions", "cost", "costs",  "discount", "discounts", "dividend", "dividends", "donation", "donations", "dues", "duty", "duties", "earnings", "excise", "expense", "expenses", "fee", "fees", "fine", "fines",   "gain", "gains", "gross", "indemnity", "income", "levy", "levies", "loss", "losses", "pay", "payment", "payments", "payoff", "pension", "pledge", "pledges", "premium", "premiums", "price", "prices",  "proceeds", "profit", "profits","receipts", "reimbursement", "reimbursements", "remittance", "remittances", "remuneration", "remunerations", "rent", "rents", "revenue", "revenues", "royality", "royalities", "salary", "salaries", "sales", "stipend", "stipends", "subtotal", "subtotals", "tariff", "tariffs", "tax", "taxes", "tip", "tips", "tithe", "tithes", "toll", "tolls", "total", "totals","value", "values", "wage", "wages", "winnings"  
  

  * **Ref**

**What it does:** Models a list picked from another table. The **TypeQualifier** must contain the name of the referenced table. Tables can be added in the Advanced Editor>Data>Tables section.  
**Trigger words:** No trigger words. Must be selected in the Advanced Editor.  
  

  * **Signature **

**What it does:** Enables a signature capture field. The signature is saved in the app creator’s Google Drive.  
**Trigger words:** "signature", "signatures"  
  

  * **Thumbnail**

**What it does:** Models images but instructs the app to expect small icons and thumbnails. They are captured just like images.  
**Trigger words:** "thumbnail", "thumbnails", "logo", "logos"  
  

  * **Time**

**What it does:** Models a time within a day (hour-minute-second).  
**Trigger words:** "hour", "hours", "mins", "minute", "minutes", "second", "seconds", "secs", "time", "times"  
  

  * **URL**

**What it does:** Displays a URL, when clicking on it, the default device browser will load the page.  
**Trigger words:** "site", "sites", "url", "urls", "web", "website", "websites"  
  

  * **Yes/No**

**What it does:** Also known as “Boolean”. It displays a Y or N or N/A option.  
**Trigger words:** Starts with "has" or "is" or ends with "?".



**Displaying column headers in the app**

You can choose to display your spreadsheet's column headers in your app using
the Advanced Editor. Go to UX>Options and click the 'Explicit column headers'
check box.  
  
![column header](/article_attachments/204791417/Screen_Shot_2016-01-07_at_1.50.36_PM.png)
## Related articles {.section}

  * [Column types](Column-types.md)
  * [Specifying a key](Specifying-a-key.md)
  * [Using formats and data validation rules](Using-formats-and-data-validation-rules.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [Create an app](Create-an-app.md)

