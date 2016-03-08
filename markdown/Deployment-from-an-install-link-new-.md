#  Deployment from an install link (new)


February 26, 2016 04:10

How does a user install your app with the install link? The link points to a
page with instructions depending on the combination of platform and web
browser that they are using.

**Chrome and Firefox on Android:  
**Chrome has features which allow us to detect whether or not AppSheet is installed on a user’s device, which greatly simplifies the installation process. First, they are taken to a page that looks like this:

** **Chrome Fallback to Old Install Experience**

On some older phones, AppSheet cannot automatically create shortcuts for you,
so you have the option to create it using a different approach. On the install
page, in the bottom right, tap on the gray text that says "Having issues with
creating shortcuts?" (outlined in red below)

** **Any other browser on Android:  
**Browsers other than Chrome are less sophisticated, so this process is a bit more complicated. Once the user you shared your app with opens the link, they will be taken to a page that looks like this:

** **Safari on iOS  
**On iOS, Safari is the only supported browser at the moment. When the user opens the share link sent to them, they will see the following page:

**  
  
**

Tapping the first button will install AppSheet. Then they have to come back
and tap the “Install Driver Dispatch” button, which will then instruct them to
create a shortcut on their homescreen. It will look like this:

  
** **Any other browser on iOS**

Only Safari is currently supported on iOS. The following page is the one that
opens up when you open the page in a browser other than iOS:

## Related articles {.section}

  * [Deploy your app](Deploy-your-app)
  * [Advanced app customizations](Advanced-app-customizations)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints)
  * [Expressions](Expressions)
  * [Deployment from an install link (old)](Deployment-from-an-install-link-old-)

