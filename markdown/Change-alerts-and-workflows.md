#  Change alerts and workflows


February 21, 2016 01:21

You might want to take actions when data updates occur. Change workflows are
the mechanism to do this. Change workflow rules (emails) fire at the AppSheet
backend when data changes are made and synced through the AppSheet app running
on the mobile device or the desktop browser.

Every change workflow rule is structured as follows:

  1. When does the rule fire? 
    * On specific actions: you can choose Adds, Deletes, Updates or any combination of them.
    * On specific tables or slices: if you have an app with multiple tables or slices, you can choose a subset of these to trigger the workflow rule.
    * Only _after_ the modification has been saved to the spreadsheet, so any formulas in the spreadsheet will be computed on the row before the update email is sent.  
  

  2. What action should be performed? 
    * At the moment, the only action supported is to send an email. You can customize many aspects of that email as we'll describe below.

This feature set will grow further in functionality over time. The rules can
be authored in the Advanced Editor>Settings>Content. Please note that while
the app is in test mode (i.e. it has not passed a [Deployment Check](/hc/en-
us/articles/205803947-Check-your-app-for-deployment)), any messages sent from
workflow actions will go only to the app creator.

Let's look closer at each of the components of a workflow rule.  
  

**Controlling when a workflow rule fires  
**A workflow rule can be triggered when:

  * A new row is added to a table.
  * A row is updated in a table.
  * A row is deleted from a table.

You may wish to further restrict when a workflow rule is triggered. For
example, maybe the workflow rule should only be triggered when a row is
changed and the row satisfies a specific condition. For example:

  * When a new row is added to the Inspections table, and the value in the InspectionPassed field is false.
  * When a row is updated in the Orders slice, and the value in the OrderAmount field is over $500.

We enable this via slices. Typically, you define slices in order to show
filtered views of the data. This is a very different use of slices. You can
choose to trigger a rule only if the changed row is included in a slice. So in
the first example above, you would define a slice that includes only rows
where the InspectionPassed field is false. You would then configure your
workflow rule to refer to this slice and only take effect when a row is added.

Note that since you can specify multiple change actions and multiple tables or
slices in each rule, it is a very powerful mechanism to specify the rule
firing condition.  
  

**When are workflow rules invoked?  
**The AppSheet workflow rules are evaluated on the AppSheet server when a user does an add, update, or delete through the AppSheet client and then syncs these changes back to the server. When the client syncs the changes to the server, the server first makes the appropriate changes to the spreadsheet and then checks whether any workflow rules should be invoked.

The AppSheet server invokes the workflow rule action if all of the following
conditions are satisfied.

  1. It first checks whether any workflow rules have been specified for the updated table or slice. 
  2. If workflow rules are specified for the table or slice, the server checks whether the workflow rule's "Update event" type matches the action the user performed, that is Add, Update, or Delete. 
  3. Finally, if the workflow rule is specified for a Slice, the server checks whether the slice filter condition is true. The server skips this step, if the workflow rule is associated with a table rather than a slice.

Changes you make directly to the spreadsheet do not go through the AppSheet
server, so they do not trigger the AppSheet workflow rules. For example, if
you update a Google Sheet directly, Google Sheets does not notify the AppSheet
server about the change, so the AppSheet server is completely unaware of the
change. When your AppSheet client performs a sync, the AppSheet server will
read the Google Sheet and return the updated data values to the client, but
AppSheet server is unaware that you updated the Google Sheet directly.  
  

**What action is performed?  
**At the moment, the only action supported is sending email. You can configure the following aspects of the email:

  * **Send to:** This is a comma-separated list of email addresses or expressions that yield email addresses.
  1. You can enter specific email addresses, such as **JohnHughes@gmail.com**. If you enter an email address that contains special characters such as hyphen or plus, you must enclose the email address in quotes, such as "**John-L-Hughes@gmail.com".**
  2. You can specify that the email address be taken from a field in the record that is being updated. For example, when a new order is captured, you may wish to send email to the customer who created the order. You can do this by entering an expression specifying the field name containing the customer's email address. For example, if there is a field called "CustomerEmail" in the updated record, you can specify **[CustomerEmail]** in the email address list.
  3. You can specify that the email address be taken from a field in a record that is referenced by the record being updated. For example, each of your Order records might contain a reference to a Customer record. Each Customer record might contain the customer's email address. When a new order is captured, you can send email to the customer who created the order. You can do this by entering the name of the Order record field that references the customer record, followed by the name of the Customer record field containing the customer's email address. For example, assume the name of the Order record field that references the customer record is **CustRef**, Assume the name of the Customer record field containing the customer's email address is **CustEmail**. You can specify the customer's email address by entering the expression **[CustRef].[CustEmail]** in the email address list.
  4. You can specify that the email addresses be taken from an entire column in another table. For example, you could create a table called **PeopleToInform** having two columns, **Name** and **EmailAddress**. Each time a new order is captured, you can send email to all of the people in the **PeopleToInform** table. Do this by entering the expression **PeopleToInform****[EmailAddress]** in the email address list.
  5. When you specify multiple email addresses, you can include any combination of specific email addresses and expressions in the email address list. For example, you could specify the following email address list. **JohnHughes@gmail.com,"**John-L-Hughes@gmail.com",[CustomerEmail],[CustRef].[CustEmail],PeopleToInform**[EmailAddress]******
  * **Email Subject:** AppSheet uses a default subject, but you can override that with your own subject text. Here, you can define placeholders that are filled in by the values in the updated entry. Here is an example of a subject line: 'Thanks <<CustomerName>> for your order** 
  **Email body:** You have three options when it comes to the body of the email. You can customize the email body field or add a body template (as described below), or simply do nothing and receive a default email that contains **all** of the values for the updated row. Here's what it looks like if you do not choose to customize the email body or provide a body template:  
![Email](../article_attachments/202926318/Screen_Shot_2015-08-28_at_5.08.47_PM.png)
** **Email body: **May contain template variables. Use this field when you have a simple email body.

  * **Body template: **For more complex workflow emails, you can specify a Google doc that may contain text, images, and placeholders (see next section about placeholders). After the placeholders are replaced the resulting document becomes the email body. Use this field when you have a more complex email body. When a Body template is present, it is used in lieu of the “Email body”.
  * **Attachment template:** You can optionally specify a template file to use as an email attachment. The file itself is chosen from your cloud file system (at the moment, we only support Google Drive for this feature and the template file is a Google Doc). In your document, or in the subject line, for example, you may want to include placeholders that correspond to your column headers, and that will be replaced when actual data updates are made i.e. "<<CustomerName>> has been added to your app". When an email is actually sent, it will carry a PDF attachment that is a copy of this file with the placeholders replaced by actual values from the updated entry.
  * **Attachment Name: **The name given to the email attachment. The default AttachmentName is “ChangeReport”. You may specify a different name and may include placeholders in the AttachmentName.
  * **CC:** Email "CC value. May contain one or more email addresses. Multiple addresses must be separated by commas. You can enter both specific email addresses and expressions as described with "Send to". 
  * **BCC:** Email "BCC" value. May contain one or more email addresses. Multiple addresses must be separated by commas. You can enter both specific email addresses and expressions as described with "Send to". 
  * **Reply to:** Email "reply to" value. May contain one email address. You can enter either a specific email address or an expression as described with "Send to". 
  * ****PreHeader: ****The default PreHeader value is "'<<_UPDATEMODE>> to application '<<_APPNAME>>' table '<<_TABLENAME>>' by '<<_USERNAME>>' at '<<_NOW>>'". This would yield a PreHeader such as "Update to application 'Workflow' by 'Julie Morgan' at 8/26/2015 6:12:28 PM". You may customize the PreHeader and may include placeholders.   

Over time, we intend to provide a richer set of actions including the ability
to post to external systems, to utilize other communication channels, and to
make other data updates. In particular, this could trigger a chain of workflow
rules leading to rich, multi-step behaviors.  
**  
Placeholders  
**You can specify a variety of placeholders in your email subject, body, PreHeader, attachment name, and templates that will populate with the correct corresponding data when the email is fired. Here's a list of AppSheet's built-in placeholders-- note that each one carries a preceding mandatory underscore. 

  * **<<_APPID>>:** Application GUID (Globally Unique Identifier) that identifies the AppTemplate e.g. “8c26466f-1db0-4032-9c0f-40c2a588cf50”.
  * **<<_APPNAME>>: **The name of the AppSheet application e.g. “Workflow-10301”.
  * **<<_APPOWNER>>:** The Owner Id of the AppSheet application e.g. “10301”.
  * **<<_ATTACHMENTNAME>>:** The name given to the attachment.
  * **<<_NOW>>:** The current date and time e.g. "6/15/2009 1:45:30 PM".
  * **<<_ROWKEY>>:** The key value of the added, deleted, or updated record.
  * **<<_ROW_WEB_LINK>>:** URL that opens the added or updated record in AppSheet. The record key is displayed as the link name.
  * **<<_ROW_WEB_URL>>:** URL that opens the added or updated record in AppSheet. The full URL is displayed. Customers will probably use <<_ROW_WEB_LINK>> more commonly.
  * **<<_RULENAME>>:** Name of the workflow rule e.g. “My Update Rule”.
  * **<<_TABLENAME>>:** Name of the table e.g. “Orders”.
  * **<<_TIMENOW>>:** The current time e.g. "1:45:30 PM"
  * **<<_TODAY>>:** The current date e.g. "6/15/2009".
  * **<<_UPDATEMODE>>:** The name of the operation that triggerred the workflow rule. Namely, “Add”, “Delete” or “Update”.
  * **<<_USEREMAIL>>:** The current user’s email address e.g. “jmorgan@google.com”.
  * **<<_USERNAME>>:** The current user’s name e.g. “Julie Morgan”.

We also allow you to use placeholders that correspond to your column
headers.The placeholders must exactly correspond to the column names in your
spreadsheet, case included, with the following format: <<ColumnName>>. Do not
include underscores as with AppSheet's built-in placeholders.

You can also use any [AppSheet expression](Expressions.md) in a placeholder. This allows you to
customize your templates with powerful data-driven logic.

[Click here to see an example of how workflow emails work.](How-can-I-receive-or-send-an-email-alert-when-data-changes-.md)


## Related articles {.section}

  * [Advanced app customizations](Advanced-app-customizations.md)
  * [Printing your data](Printing-your-data.md)
  * [Slices](Slices.md)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-.md)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-.md)

