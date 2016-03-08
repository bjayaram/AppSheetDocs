#  Google Drive


February 27, 2016 18:05

Users of Google Drive can sometimes see Error 403 (permission denied) or Error
404 (not found). There are a few common reasons for this:

  1. You are not the owner of the document but this is a shared document owned by a different Google account. Check your document sharing permissions on Google.
  2. You have multiple Google accounts (let's call them Acct1 and Acct2); your spreadsheet is owned by Acct1 but you sign into AppSheet using Acct2 to access the spreadsheet. Either use the same account, or share the document across accounts. 
  3. You had access to the file at one point, but the access has been removed.
  4. This can sometimes occur if you have a corporate Google Docs account that has an admin policy that prohibits all users from enabling third party software like AppSheet (so you may need to talk to your account admin).

[Click here to learn more about enabling Google permissions.](https://support.
google.com/a/answer/3187191?topic=1714320&ctx=topic)

If you use on of the AppSheet add-ons to integrate with Google Forms, Sheets,
or Docs, please also read [this article](/hc/en-us/articles/205612728
-Integrating-with-Google-Apps-Sheets-and-Forms-) to learn more about specific
limitations in those integrations.

In particular, if you utilize Google AppScript onEdit triggers on your Google
Sheet, or a third-party addon that utilizes these triggers, those triggers are
not fired when AppSheet makes a change to the data in the spreadsheet. This is
an unfortunate limitation imposed by Google on all third-party solutions like
AppSheet. The best workaround is to utilize a timed AppScript trigger rather
than an onEdit trigger.

The Google onChange "Simple Trigger" is fired when AppSheet makes a change to
the spreadsheet. When Google Sheets fires the onChange trigger, it passes an
"event object" to the invoked onChange script that contains information
regarding the onChange event. See the Google documentation for "App Scripts"
for more information regarding scripting.

Also, do not use filters on your Google Sheets --- it can make the filtered
rows invisible to updates. Instead, use filter views (this is a Google Sheets
feature that lets each user create and use their own filters without affecting
other users of the sheet).

## Related articles {.section}

  * [Plan upgrade required](Plan-upgrade-required)
  * [Customizing input forms](Customizing-input-forms)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)
  * [Dropbox](Dropbox)
  * [Deployment from an install link (new)](Deployment-from-an-install-link-new-)

