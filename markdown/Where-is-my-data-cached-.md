#  Where is my data cached?


January 22, 2016 23:37

**Caching on the mobile device**

By default, AppSheet does not cache spreadsheet data on the server. However,
for read-only apps, server-side data caching significantly improves the speed
perceived by app users during a Sync-- explained in simple terms, the mobile
app can get the data directly from AppSheet's servers without having to wait
for the data to be fetched from the backend cloud storage platform (Google
Drive, Dropbox, etc).

By default, AppSheet does cache spreadsheet data on the mobile client in order
to allow continued app usage despite transient loss of network connectivity
(for example-- getting into an elevator).

However, full and seamless offline behavior needs to be explicitly enabled in
the app definition, and these features require the Premium subscription plan.
By default, AppSheet does not cache images and documents that are referenced
by the spreadsheet data for offline access. You can explicitly require
AppSheet to cache images and documents by setting the appropriate option in
your app definition. After you do so, image downloads will happen
asynchronously during initial app load, and subsequently the entire app and
its image/document content is available offline.

By default, your device needs to be online to launch an AppSheet app from the
homescreen icon. Of course, it can then function despite transient loss of
connectivity. If you need the app to launch when offline, this is an option
you can explicitly set.

**These features are set from the Advanced Editor>Settings>Content. **

**Caching on the AppSheet Servers**

Your data is never stored on AppSheet's servers.

The AppSheet web service is an intermediary between the mobile app and the
backend spreadsheet. Importantly, it does NOT have a persistent copy of the
spreadsheet so there is no danger of your data being compromised via the
AppSheet web service. There are two caveats to this statement:

  * You can optionally ask AppSheet to cache spreadsheet data in our service in order to improve performance. If so, this data is cached in-memory in our server for up to five minutes at a time.
  * AppSheet caches resized copies of images used by the apps. Image resizing is important to conserve network bandwidth to mobile devices.


## Related articles {.section}

  * [Can I have my app update automatically?](Can-I-have-my-app-update-automatically-)
  * [Displaying images and documents](Displaying-images-and-documents)
  * [Data access for different classes of users](Data-access-for-different-classes-of-users)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)
  * [Content caching on the AppSheet server](Content-caching-on-the-AppSheet-server)

