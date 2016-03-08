#  Integrating with Excel and Office 365


October 27, 2015 20:53

An easy way to build AppSheet apps from Excel is to use the 
[AppSheet add-on](https://store.office.com/appsheet-mobile-apps-from-spreadsheets-WA104379644.aspx?assetid=WA104379644&sourcecorrid=75a881ae-d527-4cd9-bdc0-df51489c3996&searchapppos=0) found in the Office add-in store.

While this process is mostly seamless, there are some specific behaviors to be
aware of. With Office365, if one user has the spreadsheet open for editing,
other users and third party apps like AppSheet cannot make updates to the
spreadsheet. Consequently, if you intend to build an app that updates the data
(as most apps do!), please make sure to close the spreadsheet first. Otherwise, you will see conflict ("409") error messages and the app will not able to save changes to the spreadsheet.

## Related articles {.section}

  * [Integrating with Smartsheet](Integrating-with-Smartsheet.md)
  * [OneDrive](OneDrive.md)
  * [Integrating with Google Apps (Sheets and Forms.md)](Integrating-with-Google-Apps-Sheets-and-Forms-.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [References between tables](References-between-tables.md)

