#  Offline behavior


January 22, 2016 21:56

AppSheet apps are designed for offline function. There are four elements to
offline behavior as described below, and they are controlled by the app
creator. AppSheet apps can work offline because the information needed to run
the app (the app definition, the data, and optionally images) is maintained
locally on the mobile device.

**One important pre-condition for all offline access is that the app must initially be launched on the device when it is online.** The process of launching the app on the device causes the appropriate information to be downloaded and cached locally.

Offline behavior is controlled via the Advanced Editor>Settings>Content tab.
The use of these features does require the Premium subscription plan.  
  

**Delayed sync**: 'Sync' is the step that sends data updates from the device to the backend and brings back the latest app definition and data from the backend. If you choose Delayed Sync for your app, it indicates that the app will not sync data immediately when a new edit/delete/add occurs. Rather, it will just be queued up until you explicitly choose to sync. You should select this option for apps that are expected to work in offline environments or where you want to control the use of data bandwidth on the device.

**Intermittent connectivity**: Apps that don't enable Delayed Sync will synchronize changes every time that data changes on the device. However, there may be connectivity issues that prevent this from happening. Even in a mostly connected environment, there can be intermittent network outages. If such failures occur, AppSheet automatically queues up the changes that fail to send-- in other words, the app will default to a delayed sync behavior if the attempt to sync fails. This is the default behavior and prevents loss of data. Furthermore, repeated retries will not cause any duplication or corruption of data (except for the special case where you use RowNumber as your key-- please read our warning article about that).

**Viewing content offline**:** **All spreadsheet/table data content is always copied locally on the device so that it is available offline by default. However, the images and documents associated with the app and data are not (these are typically much larger and so we need do not maintain a local copy). You can explicitly enable a setting that instructs AppSheet to make an offline copy of all image and document content. As with all other offline data caching, this copy occurs when the app is initially run on the mobile device (online) and is subsequently checked and refreshed as needed when Sync occurs.

**Launching offline**: If you have used the lightweight deployment mechanism, you are familiar with launching apps from their homescreen icons. By default, a mobile device needs to be online in order to launch an app from its homescreen icon. Once launched, the app can then function offline or with intermittent connectivity. However, if you need the app to launch when the device is offline, this is an option you must explicitly set in the app definition.

To do this, go to the Settings tab in either of the editors and choose the
'launch offline' option. If you have already installed your app to your home
screen, you will then need to uninstall and reinstall the app in order to
launch it from the home screen icon. Otherwise you'll need to launch it from
the AppSheet app itself.

## Related articles {.section}

  * [Plan upgrade required](Plan-upgrade-required.md)
  * [Reflecting your brand](Reflecting-your-brand.md)
  * [Displaying images and documents](Displaying-images-and-documents.md)
  * [Advanced app customizations](Advanced-app-customizations.md)
  * [Check your app for deployment](Check-your-app-for-deployment.md)
