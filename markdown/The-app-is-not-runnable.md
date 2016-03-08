#  The app is not runnable


June 15, 2015 18:05

You may see this error in the app emulator (in the editor web page) or your
users may see this error on a mobile device.

It indicates that the app definition is invalid (most likely) or corrupt
(rare).

The most likely reason for an app definition to become invalid is that the
structure of the spreadsheet used to create the app changed. For example,
someone added or deleted a column. Now the spreadsheet is no longer compatible
with the app. Every time you open the app in the app editor, or refresh the
app editor web page, AppSheet rechecks this and alerts you with error messages
if the app definition is invalid. In many cases, AppSheet wil automatically
adjust the app to make it runnable again. However, this does not happen unless
the app creator actually opens the app editor --- i.e. it requires an
intentional action by the app creator.

AppSheet will also consider an app definition as invalid if the underlying
spreadsheets are no longer readable (if the data cannot be read, then clearly
the app cannot be verified let alone run).

On a mobile device, an app definition may be corrupted if a network error
occurs while the app definition is being downloaded (initially or during a
sync). This is a relatively rare event and usually is resolved with a restart
or resync. In rare cases, you may need to uninstall and reinstall AppSheet.


## Related articles {.section}

  * [Application crashes/errors](Application-crashes-errors)
  * [Errors accessing a spreadsheet](Errors-accessing-a-spreadsheet)
  * [Plan upgrade required](Plan-upgrade-required)
  * [Deploy your app](Deploy-your-app)
  * [Make a spreadsheet](Make-a-spreadsheet)

