#  Integrating with Google Apps (Sheets and Forms)


February 23, 2016 22:32

The easiest way to build AppSheet apps from Google Sheets and Forms is to use
the AppSheet add-ons found in the Google add-on gallery.


**Google Sheets**

The [Google Sheets AppSheet add-on](https://chrome.google.com/webstore/detail/appsheet/apemmfgpjhplakdihblplkjbakedfehh?hl=en-US) automatically converts a
Google Sheet to an AppSheet app. It does this in one step:

  1. **Go**: when you click "Go" from the AppSheet add-on pane in your Google Sheet, you are taken to www.appsheet.com to a working mobile app you can customize.

**Be aware**

Google Sheets allow you to create onEdit triggers-- these are code functions
that will run whenever a Google Sheet is edited via Google's web interface.
However, these onEdit triggers do not fire when data is edited and synced to
the spreadsheet via AppSheet. If you have important functionality that needs
to run on updated data, we suggest moving it to a timed trigger (a different
kind of trigger that Google supports). You can learn more about these
different trigger types via the Google Docs page.

Also, do not use filters on your Google Sheets --- it can make the filtered
rows invisible to updates. Instead, use filter views (this is a Google Sheets
feature that lets each user create and use their own filters without affecting
other users of the sheet).

**Google Forms**

The [Google Forms AppSheet add-on](https://chrome.google.com/webstore/detail/appsheet/hmmicpkfdjjchdajlldfckjaanfobjob?hl=en-US) automatically converts a
Google Form to an AppSheet app. It does this in two steps:

  1. **Prepare**: this analyzes the form, takes information from the form questions and adds it to the response spreadsheet in the form of notes on the column headers
  2. **Launch**: this creates an AppSheet app from the response spreadsheet.

It is important to understand that the AppSheet service cannot access the form
itself directly-- it is only the add-on (a web component running in your
browser) that can access the form. This is why the Prepare step is important.

This process has a few important caveats and limitations that you should be
aware of:

**Adding or moving questions**

If you add new questions or move questions around, the order of columns in the
response spreadsheet may no longer correspond to the latest form content. You
will need to create a new response spreadsheet (via the Responses menu),
Prepare, and then Launch again.

**Choosing AppSheet types**

You may want to use [AppSheet input types](Column-types.md) like Photos, Signatures, etc. Those cannot be specified in a
Google Form. So what can you do? The simple approach is to specify a question
as being of Text type and use a question title that is suggestive of the type
(eg" Customer Photo") or ("Manager Signature"), etc. AppSheet tries to
automatically guess the type based on these titles. You can also change the
type yourself in the Data / Column Structure tab of the AppSheet [Advanced
Editor](Advanced-app-customizations.md).

**Images and Videos**

Google Forms can contain embedded images and videos. Although AppSheet forms
can as well, the Forms add-on is unable to extract embedded image and video
data during the automatic app creation process. These fields will be given
placeholder URLs in the generated app that you should update in the AppSheet
[Advanced Editor](Advanced-app-customizations.md)
with correct URLs pointing to your image or video content.

**Form navigation**

Google Forms has a powerful mechanism to chain sections together using a "go-
to-next" navigation model tied to answers of specific questions. At the end of
every section, you can also specify to jump to another section or submit the
form.

AppSheet uses a different mechanism. In AppSheet, you can specify a
conditional expression that controls whether or not a form page should be
shown. The Forms add-on attempts to automatically generate the appropriate
expressions based on the structure of your form.

Most forms can now be correctly converted to AppSheet apps automatically, but
there are three main limitations:

  1. Reverse navigation is not supported by AppSheet. Try to arrange your form such that all navigation proceeds to higher section numbers.
  2. In Google Forms you can include a special "Other" option for Multiple choice questions and assign it specific navigation behavior. However, the navigation associated with this choice is not made available to the AppSheet add-on. We recommend avoiding use of "Other" on questions where "Go to section based on answer" is enabled.
  3. There is a practical limit to how much branching navigation can occur in a single form. Part of the process of converting to AppSheet's "Show If" navigation model requires building the set of all distinct paths through the form. The total number of paths through a form can quickly become unmanageable when there are many sections with redundant navigation options, such as multiple questions in the same section that can send the user to the same place. For this reason **we strongly recommend using at most one navigating question per section, and marking these required whenever possible**. Note that when more than one navigating question occurs in one section of a Google Form, only the last answered question will affect navigation anyway, and any others will be ignored.

For more information about building conditional branching forms in Google
Forms and in AppSheet, see [this article](/hc/en-us/articles/206435467).

**Advanced options**

Questions in Google Forms have Advanced options that let you constrain the
type of the response. This information is unfortunately not made available to
the add-on. However, you can explicitly set up equivalent behaviors in the
AppSheet Advanced Editor.

**Response summary**

Google Forms has a convenient feature that shows a statistical distribution of
responses. Unfortunately, this does not capture responses made via the
AppSheet app-- although the underlying response spreadsheet has all the
responses, the statistics are only measured on changes made through the Google
Form itself. However, Google Sheets now has a 
[great new feature](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CB8QFjAAahUKEwjaz8Hkv-_HAhWLOYgKHe0mARU&url=https%3A%2F%2Fsupport.google.com%2Fdocs%2Fanswer%2F6280499%3Fhl%3Den&usg=AFQjCNFqP92py3USUhu-2hodBYBZXvEmGg)
that serves a similar purpose --- it is called "Explore" and is found via a
plus button at the bottom right of the Google Sheet. Click on the Explore
button in your response sheet to automatically get insights into your form
responses.

**Username**

In a Google Form, you have an option at the top to collect the username
(actually the user email) of the respondent. This causes an extra column
'Username' to be added to the response spreadsheet. Unfortunately, this column
may be placed at any position within the spreadsheet and messes up the
AppSheet service. We recommend therefore that if you want this capability,
enable this option at the very end after completing the authoring of the rest
of the form. This adds the Username column at the end and therefore does not
cause any issues.

**Triggers**

If you have formSubmit triggers on the spreadsheet, they do not fire when
updates are made via AppSheet. As with onEdit triggers, we recommend moving
this logic to a timed trigger.



## Related articles {.section}

  * [Column types](Column-types.md)
  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching.md)
  * [Who should use AppSheet and what kind of apps can it create?](Who-should-use-AppSheet-and-what-kind-of-apps-can-it-create-.md)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-.md)
  * [Change alerts and workflows](Change-alerts-and-workflows.md)
