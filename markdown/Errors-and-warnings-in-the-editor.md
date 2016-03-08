#  Errors and warnings in the editor


November 12, 2015 20:30

AppSheet automatically extracts structure from a spreadsheet so that your app
can be generated. While most spreadsheets are simple tabular structures, there
are also ways to use spreadsheets that are incompatible with AppSheet. So you
may see errors, warnings, and informaton messages in the app editor when
AppSheet reads your spreadsheet.

  1. Errors with spreadsheet structure \-- these errors typically occur when AppSheet is unable to properly identify the column headers. Often this is because the first worksheet in your spreadsheet has non-tabular data like charts or pictures.
  2. Errors when switching spreadsheets \-- when you switch to a different spreadsheet, AppSheet tries to retain as much as possible of your existing app. However, the new spreadsheet may have a totally different column structure. In this case, you may see errors that ask you to change the other parts of the app definition appropriately.
  3. Warnings about column structure mismatch \-- this is the most common warning seen during the app creation process. As users modify their spreadsheets, they add or remove columns. Each time you do this and tell AppSheet to refresh the column structure, you are warned if the old column structure and new structure do not align. AppSheet always adjusts to the new structure, so this is a warning, not an error.
  4. Warnings about formulas \-- we discuss formulas in a separate topic, but in brief, there are only certain kinds of spreadsheet formulas that make sense to use in your data.
  5. Information about the key column \-- as described earlier, this information tells you which column is chosen as the key. The key also plays an important part in the presentation of data as described in the UX section. If AppSheet cannot find a good key column, it tries to combine pairs of columns to find a composite key. If that also fails, it settles for the row number (an implicit column). This is typically not a good choice unless you have an app that is purely showing information and prevents all edits. The number of a row in a spreadsheet changes dynamically based on the rows above it, so clearly the row number identifies a row only as long as no rows are being added or deleted to the spreadsheet by the app, or directly.


## Related articles {.section}

  * [Reflecting your brand](Reflecting-your-brand)
  * [Plan upgrade required](Plan-upgrade-required)
  * [Offline behavior](Offline-behavior)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-)
  * [Making an "AppSheet-friendly" spreadsheet](Making-an-AppSheet-friendly-spreadsheet)

