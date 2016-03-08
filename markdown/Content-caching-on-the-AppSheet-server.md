#  Content caching on the AppSheet server


January 22, 2016 22:01

You can modify the way AppSheet caches content on both server and mobile
device.

By default, AppSheet does not cache spreadsheet data on the server. However,
server-side data caching can significantly improve the speed perceived by app
users during a Sync. Explained in simple terms, the mobile app can get the
data directly from AppSheet's servers without having to wait for the data to
be fetched from the backend cloud storage platform (Google Drive, Dropbox,
etc).

You can explicitly enable server-side data caching via an optional setting in
the Advanced Editor>Settings>Content:  
  
![Enable cacheing](../article_attachments/205038957/Screen_Shot_2016-01-22_at_2.00.16_PM.png)
  
## Related articles {.section}

  * [Offline behavior](Offline-behavior.md)
  * [Plan upgrade required](Plan-upgrade-required.md)
  * [Choosing and adding data views](Choosing-and-adding-data-views.md)
  * [Slices](Slices.md)
  * [App formulas](App-formulas.md)

