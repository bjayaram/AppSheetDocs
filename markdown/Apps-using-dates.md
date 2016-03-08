#  Apps using dates


February 02, 2016 19:55

If your data uses dates or timestamps, there are some special considerations
to keep in mind.



**Dates in spreadsheets**

Date formats vary widely across languages and locales. So it is really
important that you use the cell formatting capability of the spreadsheet to
indicate that all the cells of a column are Date values. You can utilize dates
and times in your local format.

If your data column in the source spreadsheet is formatted as a Date or Time
with a specific format (eg: DD/MM/YYYY) we respect that format when your
changes are stored back in the spreadsheet.

Many spreadsheets use automatic mechanisms to add a timestamp in the first
column. A timestamp is generally a poor choice for a key-- though it uniquely
identifies the row, the timestamp isn't really meaningful to the rest of the
app. So if the timestamp is chosen as your key, you may need to change that
explicitly.



**Dates in apps**

Dates and times in AppSheet apps are shown in the appropriate locale-specific
format.

If you're seeing the wrong date format on your mobile device or browser, make
sure your system and browser language is correct. US English date format is
different than non-US English format.

Change your language on Android: [https://support.google.com/accounts/answer/3
2047?source=gsearch&hl=en](https://support.google.com/accounts/answer/32047?so
urce=gsearch&hl=en)

Change your language on iPhone / iPad: <https://support.apple.com/en-
us/HT204031>

Change your language on Chrome:
<https://support.google.com/chrome/answer/173424?hl=en>


## Related articles {.section}

  * [Using formats and data validation rules](Using-formats-and-data-validation-rules)
  * [Expressions](Expressions)
  * [Locale support in AppSheet](Locale-support-in-AppSheet)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints)
  * [Presentation types](Presentation-types)

