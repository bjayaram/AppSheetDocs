#  Displaying images and documents


February 21, 2016 08:28

Here are some guidelines on using images and documents in your app.

Many applications (e.g. a product catalog or a photo diary) use images. Use
the Image column type. Likewise, some apps use PDF documents. Use the File
column type.

There are two ways to represent an image or document in your spreadsheet-- as
a URL or as a filename.

**If you are providing a URL, please be careful to ensure that the URL is publicly accessible** Many users who choose this option provide image URLs that appear accessible to them, but are not really publicly accessible. Here are some examples of **bad** image URLs:

  * An image URL from your Facebook album-- you may be able to access the image because you are logged into Facebook, but when some other user tries to see the image, they will get an error. Whenever you are using an image from some kind of online storage provider, make sure that public access permissions are provided.
  * An image URL from your Dropbox or Google Drive-- most cloud file systems show you an image on a webpage, but the webpage itself is not actually an image. It is a page that _hosts_ an image. For example, : [https://drive.google.com/file/d/{fileId}/view](https://drive.google.com/file/d/0B6H-Xsozi7BgQU04RlVxSDR5VGs/view?usp=sharing) is an image hosting page on Google Drive, but the actual image URL is https://drive.google.com/uc?export=view&id={fileId}
  * An image URL from your local computer-- of the form file://MyImages/MyImage.jpg or C:/MyImages/MyImage.jpg. AppSheet has no access to your local computer, nor do you have the option to 'upload' an image to AppSheet. Instead, place your images in your cloud storage provider and use one of the mechanisms described above.

If you want to use a filename, it must be stored in your cloud file system,
not on your desktop** In the app editors, we provide a file selector widget that lets you browse your cloud file system to find an image.
  * If you are specifying an image or document file name in your spreadsheet, the file should be in the same folder location as your spreadsheet. For example, if you use Google Drive and your spreadsheet is in the /appsheet/data/MyApp folder, then if you have the image 'MyImage.jpg' in the same folder, you can just use the value 'MyImage.jpg' in the appropriate cell.
  * It is sometimes easier to organize images in their own folder. For that reason, we allow image file names to be specified relative to the location of the spreadsheet. For example, if your images are in a subfolder called 'Images', you can use the cell value 'Images/MyImage.jpg' or './Images/MyImage.jpg'.  
  

For apps that want to exclusively work with small thumbnail images, we also
provide a Thumbnail column type. However, AppSheet does not currently
automatically detect the difference between a regular image and a thumbnail.
To explicitly choose the Thumbnail type, please use our Advanced Editor, as
described in this document. To see an example of the use of thumbnails, look
at the [Marketing Docs sample](https://www.appsheet.com/samples/An-app-for-a-marketing-team-to-access-customer-case-studies-on-and-offline?appGuidString=2018fca7-8a19-49b9-a10b-7f53a05b7125).

See this [Google Sheets article](https://support.google.com/docs/answer/3093333) if you need
assistance with image sizing.



## Related articles {.section}

  * [Capturing images and documents](Capturing-images-and-documents.md)
  * [Reflecting your brand](Reflecting-your-brand.md)
  * [Column types](Column-types.md)
  * [Capturing GPS location](Capturing-GPS-location.md)
  * [Specifying a key](Specifying-a-key.md)

