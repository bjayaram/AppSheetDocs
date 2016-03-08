#  Locale support in AppSheet


January 30, 2016 00:23

**Locale vs Device Settings**

**Data Locale**

See the **Advanced Editor > Data > Tables > Data Locale** setting.** **This
setting is designed to align with the settings in your spreadsheet, so that
AppSheet reads the information in your spreadsheet correctly and so that
AppSheet returns data to your spreadsheet correctly. The focus is 1) parsing
numbers correctly with commas and decimals for Field Types of **Decimal,
Price, **and** Percent** and 2) reporting dates and times correctly for Field
Types of **Date, DateTime, **and** Time.**  You may have one locale setting
per spreadsheet and one Data Local setting per corresponding AppSheet table.

Note: **Data Locale** does not impact **Price Currency** settings and AppSheet
does not provide currency conversions. Data should be entered in your
spreadsheet/app according to the currency you would like displayed. See 
[How do I convert from US Dollars to my local Currency](How-do-I-convert-from-US-Dollars-to-my-local-Currency-.md).


**Locale for Google Sheets**

The Google Sheets Locale setting controls how Date, DateTime, Decimal, Price,
Percent, and Time values are entered into Google Sheets. For example, when the
Locale is United States, United Kingdom or Japan, you must enter a period as
the decimal separator between the whole and fractional parts of Decimal,
Price, and Percent values. Conversely, when the Locale is Germany, France, or
Brazil, you must enter a comma as the decimal separator.

If your AppSheet application uses Google Sheets or Google Forms and specifies
a Locale other than United States, you must specify the corresponding Locale
in AppSheet. This is necessary because when AppSheet adds or updates a Date,
DateTime, Decimal, Price, Percent, or Time value in a Google Sheet, it must
use the appropriate data format based upon the Google Sheets Locale setting.
Unfortunately, Google Sheets does not provide a way for AppSheet to retrieve
the Google Sheets Locale setting automatically. Instead, we ask you to specify
the Locale setting through the Advanced Editor.

You can check the Locale assigned to your Google Sheet by clicking the Google
Sheet File menu, selecting "Spreadsheet settings", and viewing the Locale
setting. If the Locale is anything other than United States, you must specify
a Locale in AppSheet.



**Configuring the Locale**

1\. Make certain that your Google Sheet specifies the appropriate locale. Do
this by opening the Google Sheet. From the "File" menu select the "Spreadsheet
settings". On the "Settings" dialog set "Locale" to your locale. For example,
in Thailand select "Thailand".

![locale settings](/article_attachments/203196118/Screen_Shot_2015-09-22_at_1.59.06_PM.png)

2. Make certain that each Date, Time, DateTime, Number, Currency, and Percent value in the Google Sheet is formatted appropriately. Do this by selecting all of the cells in the column containing the data values. From the "Format" menu select "Number" and then the appropriate formatting style. For example, for date values select "Date", for currency values select "Currency", for time values select "Time", and so forth. Do the same for each Date, Time, DateTime, Number, Currency, and Percent column.

3. Open your AppSheet app in the Advanced Editor and specify the locale for each table.

  * Open your app.
  * Go to the Advanced Editor>Data>Tables tab.
  * Click the 'Edit this table definition' button to the left of each table name.
  * In the Edit table definition dialog window, pick the appropriate Locale setting from the Locale dropdown. You should pick the Locale that most closely matches your Google Sheet Locale setting. For example, in Thailand select "Thai (Thailand)".
  * Click the Save button at the bottom of the Edit table definition dialog window.
  * Click the Save button at the top right of the Advanced Editor window.
  * If your application includes multiple tables, repeat this for each of your tables.

![Data locale](/article_attachments/205038477/Screen_Shot_2016-01-22_at_1.32.03_PM.png)

4. Make certain that your browser or device is set to use your locale. For example, in Thailand select the Thai locale. All data is sent between the AppSheet client and the AppSheet server in a common universal format. The browser or device setting completely determines how data values are displayed on your browser or device.

5. If you use a calendar other than the Gregorian calendar, make certain that your browser or device is set to use that calendar. For example, in Thailand select the "Buddist" calender. Many countries use the Gregorian calendar, so in many cases you can skip this step.

6. Click the "Sync" button in the application to read the latest values from the Google Sheet. See if the Date, DateTime, Decimal, Price, Percent, and Time values are displayed correctly in the AppSheet application. If not, verify your browser or device locale settings.

7. Try updating a Date, DateTime, Decimal, Price, Percent, or Time value and saving the changes to the server. See if the correct values appear in the Google Sheet and the AppSheet application.



** **Compatibility Locale**

One of the Locale values appearing in the Locale dropdown menu is the
Compatibility Locale. This value is present for backward compatibility only.
It preserves AppSheet’s existing but limited Locale behavior. If you choose
Compatibility Locale, we use a period as the decimal separator between the
whole and fractional parts of Decimal, Price, and Percent values. We use
simple rules for saving Date, DateTime, and Time values. We save formulas in
the United States Locale format, which works for many Locales that use a
period for the decimal separator. However, we recommend that you pick the
specific AppSheet Locale that matches your Google Sheet Locale. If you Google
Sheet does not specify a Locale, we recommend you specify AppSheet Locale
United States.

We currently support approximately 70 Locale values. We selected these locales
based upon the Locales that Google Sheets currently supports. Please let us
know if a Locale you need is missing from AppSheet.



**Locale for Excel**

It is not necessary to set the AppSheet Locale for AppSheet applications that
store data in Excel files on Box, Dropbox, Google Drive, Office365, or
OneDrive. This is a consequence of the way we add and update data and formula
values in Excel files. The AppSheet table Locale should be set to either
United States or Compatibility.  
  

**Locale for Smartsheet**

It is not necessary to set the AppSheet Locale for AppSheet applications that
store data in Smartsheet. This is a consequence of the way we add and update
data and formula values in Smartsheet. The AppSheet table Locale should be set
to either United States or Compatibility.



_Note: Changing the Locale in AppSheet doesn’t retroactively change the format
of previous entries, nor does it necessarily reflect accordingly in the app
emulator. What’s displayed in the app emulator is based on the locale settings
of your mobile phone or web browser. The Locale setting exists purely to
affect the data that’s pushed back to the spreadsheet._



## Related articles {.section}

  * [Column types](Column-types.md)
  * [App formulas](App-formulas.md)
  * [Change alerts and workflows](Change-alerts-and-workflows.md)
  * [Virtual columns](Virtual-columns.md)
  * [How do I change a Column Type?](How-do-I-change-a-Column-Type-.md)

