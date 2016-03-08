#  What if I lose connectivity?


January 22, 2016 23:46

If you expect your app to be offline for any non-trivial period of time, we
strongly recommend configuring the app to indicate that it should work
offline. AppSheet has platform features that explicitly handle this scenario.

However, even for apps that have not enabled this feature, AppSheet is
designed to work through transient connectivity failures. Mobile apps work in
occasionally connected environments, and network failures do occur.

  * All changes are made locally and are queued up to send over the network when you choose to sync.
  * During Sync, if any changes fail to be propagated, they are retried. Our system is designed so that the changes are 'idempotent'-- this means that even if we mistakenly try to apply the same change repeatedly, the result is still sensible.
  * You can keep using the app until you get to a location with reliable connectivity and successfully sync your changes.


## Related articles {.section}

  * [Errors and retry](Errors-and-retry)
  * [Offline behavior](Offline-behavior)
  * [AppSheet is NOT...](AppSheet-is-NOT-)
  * [App formulas](App-formulas)
  * [Expressions](Expressions)

