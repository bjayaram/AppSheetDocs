#  Including PDF's in your application


December 15, 2015 00:01

**There are a three ways you can include PDF's in your application. **

**1\. Link to the PDF using a relative path**

Using relative paths, you can create links to files relative to the
spreadsheet that your app is using. This works in a similar way to links to
image. For example, if the PDF is in the same directory as your spreadsheet,
you can create a link to it just by putting in its name in your spreadsheet,
eg. ‘foo.pdf’.

**2\. Link to the PDF using a direct URL**

Using direct Url’s you can link to a pdf that is somewhere on the internet.
Just like you would link to an image, you can link to a pdf, for example.
‘http://www.mywebsite.com/path/super_pdf.pdf’

**3\. Use a Google Drive URL**

These are url’s that you copy from your address bar in your browser when you
are previewing a pdf in google drive, eg.
‘<https://drive.google.com/view?id=1234>’

Note that these are not direct or relative links, which means you are not
supplying us with the actual PDF file. This means that you won’t be able to
take full advantage of AppSheet’s PDF support.

**How does it work?**

**iOS - **Regardless of the type of URL, the pdf will be opened in Safari. However, only relative and direct URL’s are guaranteed to be cached for offline use.

**Android -** If you link to the PDF using a direct URL or relative path, the PDF will be downloaded to your phone, and you will be able to choose a viewer with which to view it. If you do not have a PDF viewer installed on your phone, we’ll give you a link to the recommended viewer.

## Related articles {.section}

  * [ Viewing external content](-Viewing-external-content)
  * [Printing your data](Printing-your-data)
  * [Advanced app customizations](Advanced-app-customizations)
  * [Limits on data size](Limits-on-data-size)
  * [Using spreadsheets with pivoted data](Using-spreadsheets-with-pivoted-data)

