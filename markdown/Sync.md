#  Errors during Sync


February 19, 2016 00:50

As described earlier, Sync has three stages:

  1. Send changes from the device to the backend. When this stage starts, the Sync progress bar is about 1/4 complete.
  2. Fetch the latest app definition from the backend. After this stage, the Sync progress bar moves to 3/4 complete.
  3. Fetch the latest data from the backend.

Most errors in Sync are observed in the first stage (i.e. when the progress
bar is 1/4 complete).

  1. If there are network errors, the step is retried a few times, and if the failure persists, the Sync is halted. The solution is to retry later when connectivity is better.
  2. If you have poor connectivity or if large images have to be sent as part of the Sync, this step can take a long time and can potentially timeout. The solution is to retry later when connectivity is better.

If the app definition has changed on the backend (for example, new columns
have been added to the data), the local changes from the device may no longer
be executable. In this case, an error message is shown to the app user during
Sync. It usually takes the form of an error indicating that a value being
inserted is incompatible with the type of data expected (because the columns
have changed

## Related articles {.section}

  * [Application crashes/errors](Application-crashes-errors)
  * [Sync-- between the app and the backend](Sync-between-the-app-and-the-backend)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints)
  * [How should I choose a key?](How-should-I-choose-a-key-)
  * [App formulas](App-formulas)

