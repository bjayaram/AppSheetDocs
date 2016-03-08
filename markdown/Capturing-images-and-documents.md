#  Capturing images and documents


February 23, 2016 22:30

Documents (PDF files) can be captured by an app only when it is run in a
desktop browser. Documents require a column of type File that is editable.
Mobile devices do not have a standard file system, which is why file upload is
not supported on mobile devices at the moment.

Many applications (e.g. a vehicle inspection app) need to capture an image in
a column of a data row. If your app has a column of type Image or Thumbnail,
and you have enabled data Edit or Add, then the app can capture images when
editing or adding a data row.

On Android devices, by default, the user is prompted with the choice to take a
new photo or use the camera roll. On iOS devices, by default, the camera is
launched. If you want to optionally browse the photos in your camera roll, you
should enable a setting for the AppSheet app on the device.

Here's how AppSheet processes the photos taken with the camera:

  * Any photo taken on a device with your app is saved in full resolution in the camera roll on the device. [See how the camera function works in our Site Scout sample app.](https://www.appsheet.com/samples/An-app-for-construction-site-inspections-with-GPS-and-images?appGuidString=a7058530-b6d1-4dcd-a819-6000e7bbe6c1) Note: if you use the app on the desktop, the image capture function only allows you to open an image file. Using the image function on a mobile device will allow you to either upload an image from your device's gallery or to manually take a photo.
  * When the user presses the Sync button, the photo is downloaded at a reduced resolution (to conserve network bandwidth) and is saved in the same folder location as the spreadsheet (all images are saved into a subfolder). The image resolution used is controllable via an app setting in the Advanced Editor>Settings>Content tab.
  * If you run into issues with uploading images, and if your phone has a high-resolution camera, consider reducing its capture resolution within the camera app.  
** The row in the spreadsheet includes the name of the image file just created, so that all subsequent accesses work smoothly. The image file name includes the row key as well as the column name so that it can easily be correlated to the corresponding row.



If you would like to have URLs to view these images, you should add an
additional URL column and use the following spreadsheet formula (on Google
Sheets) to construct image urls from the image file names:

_**Format:**_

`=SUBSTITUTE(CONCATENATE("https://www.appsheet.com/template/gettablefileurl?app
Name=","**[AppName-Account#]**","&tableName=","**[TableName]**","&fileName=",+
**[ImageColumnCell]**), " ", "%20")`

_**Sample:**_

`=SUBSTITUTE(CONCATENATE("https://www.appsheet.com/template/gettablefileurl?appName=","**Inventory-114348**","&tableName=","**Orders**","&fileName=",+**B2**)
, " ", "%20")`

**Note: Your image folder must be publicly accessible.**

Now that you have the correct URL format, you may also embed the image inline
within your spreadsheet (on Google Sheets). To do so, wrap the URL formula in
an IMAGE() expression.

**_Format:_**

`=IMAGE(SUBSTITUTE(CONCATENATE("https://www.appsheet.com/template/gettablefileu
rl?appName=","**[AppName-Account#]**","&tableName=","**[TableName]**","&fileNa
me=",+**[ImageColumnCell]**), " ", "%20"))`

**_Sample:_**

`=IMAGE(SUBSTITUTE(CONCATENATE("https://www.appsheet.com/template/gettablefileu
rl?appName=","**Inventory-114348**","&tableName=",**"Orders"**,"&fileName=",+*
*B2**), " ", "%20"))`



## Related articles {.section}

  * [Displaying images and documents](Displaying-images-and-documents.md)
  * [Capturing signatures and drawings](Capturing-signatures-and-drawings.md)
  * [Capturing GPS location](Capturing-GPS-location.md)
  * [Reflecting your brand](Reflecting-your-brand.md)
  * [Errors and warnings in the editor](Errors-and-warnings-in-the-editor.md)

