#  How can I receive (or send) an email alert when data changes?


January 19, 2016 00:36

You can opt to receive an email each time data is added, updated, or deleted
in the app. The emails fire when the updates are synced from the mobile
device.

For example, let’s say I’ve created a Project Management app I’m sharing with
the rest of my team to track our projects, assigned tasks, and progress to
goal. I’d like to receive an email each time someone adds a new task to the
app so I am always up to date with new assignments.

I’ll need to go to the Advanced Editor>Settings>Workflow.

****** 
When I click +Workflow Rule, a dialog box appears called “Edit workflow rule”.
There are [several fields](Change-alerts-and-workflows.md) to fill out:

****** 
For the email subject and the attachment template, I can use placeholders that
will populate with the correct information in the email. The placeholders must
directly correspond to the column names in my spreadsheet or to AppSheet’s
built-in placeholders, case included, with the following format:
<<ColumnName>>. (To see the complete list of allowed placeholders, 
[click here](/hc/en-us/articles/205860137)). You’ll see I’ve done this in the Email
subject field:

****** ****Instead of having the update in the body of the email, I instead want a PDF attached to the email that contains the updates. I will need to specify a Google Doc template with the corresponding placeholders in the document. Here’s what my Google Doc template looks like:****  
****

******  
When I click into the “Attachment template” field, I will get the option to
choose my corresponding document from my Google Drive.****  
****

****** ****Once I hit Save I can see my new rule has been added:

****** 
Let’s see this in action. In the mobile app, my colleague Mark just added a
new task: Print Ad Sketches.

****                                               ** 
When Mark synced the device, I received the workflow email:

****** 
Attached to the email is the PDF with the appropriate data replacing the
placeholders:

****** 
We’ve focused on email in this article. Going forward, AppSheet will support a
variety of other actions for workflow rules-- including text messages, push
notifications, webhooks and more.

Please note that while the app is in test mode (i.e. it has not passed a
[Deployment Check](Check-your-app-for-deployment.md)), any messages sent from workflow actions will go only to the app
creator.



## Related articles {.section}

  * [Change alerts and workflows](Change-alerts-and-workflows.md)
  * [How should I choose a key?](How-should-I-choose-a-key-.md)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-.md)
  * [Expressions](Expressions.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)

