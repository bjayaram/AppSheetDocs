#  Sync-- between the app and the backend


January 13, 2016 21:52

Apps built with AppSheet are designed to handle intermittent connectivity
loss, or full offline operation. This is achieved by maintaining a copy of the
relevant data locally on the mobile device (securely, of course!)

As a side-effect of this design, we have to consider when and how the local copy of the data stays in sync with the backend spreadsheet.

There are three cases to consider:

1. Changes are made in the app and need to be propagated to the backend.
2. Changes are made to the backend data (either directly, or by other users of the AppSheet app) and these need to be propagated to the app.
3. Changes are made to the app definition itself and need to be propagated to the app.

All of these occur as part of "Sync". There are four ways in which Sync may be invoked:

1. If this is the first time the app is being invoked on a specific device, Sync is automatically invoked when the app is started. This fetches the latest app definition along with the data needed to run the app.
2. For apps that work primarily online and want close to synchronous behavior, the app creator should disable the "Delayed Sync" setting. Every time the app user saves any edit, add, or delete action, this not only makes the change locally on the device but also immediately invokes Sync.   
3. If the app has local changes that have not been propagated to the backend, the Sync button (at the bottom right) is highlighted. Clicking on Sync will manually invoke the Sync function. For apps that work primarily offline, the app creator should enable the "Delayed Sync" setting, and the app users will explicitly invoke Sync when they have network connectivity.
4. The app creator can also enable the "Sync on Start" option. When this is enabled, the app syncs every time it is started by the user.

Each Sync action itself has three steps that occur sequentially:

1. Any local changes are sent to the backend and applied to the backend data in the order they were originally executed.
2. The latest app definition is fetched down to the mobile device. If no change has occurred since the last Sync, this step is optimized.
3. The latest backend data is fetched down to the mobile device. If no change has occurred since the last Sync, this step is optimized.

## Related articles {.section}

  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)
  * [Customizing input forms](Customizing-input-forms.md)
  * [Plan upgrade required](Plan-upgrade-required.md)
  * [Mobile-specific features in my app](Mobile-specific-features-in-my-app.md)
  * [Can I have my app update automatically?](Can-I-have-my-app-update-automatically-.md)

