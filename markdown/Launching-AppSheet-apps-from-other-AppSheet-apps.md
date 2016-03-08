#  Launching AppSheet apps from other AppSheet apps


January 23, 2016 01:50

If you have ever used AppSheet's App Gallery in your mobile device, you'll
realize the value of having a list of apps that you an easily access from a
single App.

You can create an AppSheet app that can link to other AppSheet apps, helping
you create suites of solutions that fits the needs of your users, this also
simplifies the deployment process for multiple apps as you can now send one
app and simply change the back-end spreadsheet to update to a new version of
the app or add a new service.



** **Introducing app launchers (beta)**

An app Launcher has a very similar behavior as the App Gallery in the AppSheet
mobile app. To achieve this you need to follow a few instructions:



1\. Structure the table

The App Launcher is based on a table that looks like this:



App Name

Image

App Link

Consultant

Sample app Launcher_Images/Consultant.Image.121017.png

Consultant-10305

Reporter

Sample app Launcher_Images/Reporter.Image.121109.png

Journalist-10305

Assignment Manager

Sample app Launcher_Images/Assignment Manager.Image.120718.png

SchoolWorkManager-71626

Class Assignments

Sample app Launcher_Images/Class Assignments.Image.120811.png

ClassAssignments-71626

Extracurricular Schedule

Sample app Launcher_Images/Extracurricular Schedule.Image.121042.png

ExtracurricularSchedule-71626



  * App Name: You can give any name to the app
  * Image: It has to be a public url for the image or enter a reference to a file in your cloud provider. [How to add Images](Images-and-documents)
  * App Link: Follow the instructions below





2\. In the app link field, enter the app name.

Each app has a unique App Name, you can find it in the link to the app. For
example:

[https://www.appsheet.com/template/showdef?appName=ClassAssignments-71626](htt
ps://www.appsheet.com/template/showdef?appName=ClassAssignments-71626)

In this case, the App Name is: ClassAssignments-71626





3\. Create the app

Add it via one of our add-ons or directly from My Apps > Make New App.





4\. Make sure the field types are as follows:

Change the field type by going to Advanced Editor > Data > Column Structure

App Name: Name

Image: Image or Thumbnail

App Link: App.



The last field to change is App.





5\. Make the available view a gallery

That's it, the linked apps should load when you click/tap on the image.

This is pre-beta so we might still have lots of behaviors to hone.


## Related articles {.section}

  * [Expressions](Expressions)
  * [Column types](Column-types)
  * [Information for an IT department](Information-for-an-IT-department)
  * [Managing App Versions](Managing-App-Versions)
  * [Pricing, billing, and subscription plans](Pricing-billing-and-subscription-plans)

