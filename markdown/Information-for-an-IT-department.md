#  Information for an IT department


January 23, 2016 01:39

If you are an AppSheet innovator at a larger company with an IT department,
you may need to provide some information about AppSheet as you progress
towards deploying your apps to others within the company. In this document,
we've put together an "FAQ for IT". Many of the topics have more detailed
information via separate articles in our Zendesk documentation site.

**  
Architecture questions  
  
How are AppSheet apps created?**

Apps are created on the AppSheet website. Each app is based on one or more
'tables'. Typically each table is a spreadsheet, but in general, each table is
linked to a source of [structured data](Mobile-
apps-driven-by-the-structure-of-data). The rest of the app is defined via
configuration options. There is no code involved, so apps can be created in
minutes.  
  
**How are AppSheet apps distributed?**

Apps are distributed by sending an [install email to desired users with an
install link](Sharing-and-distributing-your-app).
Users open the install email on a mobile device, click on the install link,
and can install the apps instantly.  
  
**What is the high-level architecture of AppSheet?**

Each mobile app is derived from and based on backend data, typically a
spreadsheet hosted on a cloud storage system like Google Drive, Dropbox, or
Office365. On the mobile device, a copy of the data is cached locally, in
order to permit offline operation. Whenever changes are made in the app, or
when the users explicitly choose to sync the app, the [changes from the app
are moved to the backend spreadsheet, and vice versa](/hc/en-
us/articles/206366667-Sync-between-the-app-and-the-backend). All communication
between the app and the backend data happens through the cloud-hosted AppSheet
web service.  
  
**Where is AppSheet hosted?**

AppSheet's web service is hosted on Microsoft's Azure web hosting
infrastructure.  
  
**Can AppSheet be hosted on-premise within the company?**

No, AppSheet is hosted in the cloud. It is not an on-premise service.  
  
**Is AppSheet reliable?**

The AppSheet web service is highly reliable with 99.99% monthly uptime. The
reliability derives from both the redundant cloud architecture as well as the
reliability of the underlying cloud infrastructure services like Microsoft
Azure. The greatest source of reliability concerns for a mobile app stem from
[connectivity issues](What-if-I-lose-
connectivity-). AppSheet is explicitly designed for environments with bad or
intermittent connectivity, and the data synchronization technology handles
various kinds of failures seamlessly without data loss.  
  
**Is each app separately deployed via the iOS or Android app store?**

No. Mobile apps run on the device within a common 'host' app called AppSheet.
This host app is already available in the iOS and Android app stores. This
allows any new app to be [instantly deployable](/hc/en-us/articles/205111288
-Traditional-vs-instant-app-deployment).

**  
Data architecture questions  
  
What sources of data can AppSheet access?**

AppSheet apps can access spreadsheet data from Google Drive, Office365,
Dropbox, Box, and Smartsheet. More data sources are being added actively.
Connectors to Salesforce and SQL databases will shortly be available for early
adopters.  
  
**Do we _have_ to use data in a spreadsheet?**

AppSheet is meant for non-developers to easily build apps, which is why we
have emphasized access to spreadsheets. Over the next few months, we will also
be supporting more traditional enterprise data sources as well.  
  
**Can you connect to our corporate database or resources behind a firewall?**

Not directly. The AppSheet architecture permits our service to interact with
data sources via a web service that acts as a proxy to the actual data. If the
actual data is behind a firewall, you (or your IT department) will need to
create a web service that acts as a proxy for the data. This is a relatively
straightforward task for a web developer and we can help enterprise customers
with sample code for this proxy service.

**  
Mobile platform questions  
  
What mobile platforms do you support?**

AppSheet apps run on iOS and Android devices. We encourage iOS version 8.0 and
higher, and Android version 4.3 and higher. Lower versions of these operating
systems can cause subtle bugs or performance problems in certain scenarios.  
  
**Can the apps run in a browser?**

Yes. While we primarily focus on mobile devices, many AppSheet customers also
run their apps in a web browser, usually within an iframe. In fact, on
unsupported mobile platforms like Windows Phone, we recommend running within a
browser. Most of the app functionality is supported in a browser (except
offline image caching and bar code scanning). We recommend a modern browser
and the apps work best on Chrome. AppSheet does not work on IE versions lower
than V10.0.

**  
Functionality questions  
  
Do you support feature X?**

We add features to AppSheet at a rapid rate-- it is not uncommon for us to
unblock a customer by adding a new feature in a couple of weeks. There is an
active [user community](http://community.appsheet.com) that drives and
prioritizes our feature investments. All features are initially announced via
the community for trial and then promptly added to the Zendesk documentation.

**  
Security questions  
  
Where can I learn about the security model?**

We have written a short article describing different aspects of [the AppSheet
security model](How-do-I-design-a-secure-app-).
We are happy to share further detail with IT experts.  
  
**What data does AppSheet store on its servers?**

The AppSheet service records user signup information and access tokens in
order to be able to access backend spreadsheet data. The definition of each
app is also stored. [The actual data used by each app is not copied to the
AppSheet service](Where-is-my-data-cached-)\--
instead it passes through the AppSheet service as it flows between the mobile
device and the backend cloud storage system chosen by the customer.

AppSheet does record usage events and also logs data updates in order to
support diagnostics, debugging, analytics, and billing. We are introducing an
option for customers to limit the duration for which this information stays in
the system logs.  
  
**Has AppSheet passed security and/or privacy audits?**

As a startup company, we have focused for the last year on building a secure
and scalable architecture. We have designed for security and for data privacy.
Over the next year, we will be working with established auditors to gain
official compliance certifications.

**  
Support and services questions  
  
What is the response time for product support questions?**

Our user community forum is the venue for most support questions. Not only is
every member of our team actively engaged with user questions, we also have
power users who are community moderators who also help all members of the
AppSheet community with questions and issues. Most issues are responded to
within hours and resolved within the day. We also offer premium support for
customers in higher subscription plans.  
  
**Do you provide professional services for app development?**

We try to focus on core platform development. For some key strategic
engagements, we can help customers with app development. The preferred model
is for our customers to work with one of our solution partners-- these are
professionals who are experts on the AppSheet platform. Depending on your
needs, we can identify suitable solution partners.


## Related articles {.section}

  * [Pricing, billing, and subscription plans](Pricing-billing-and-subscription-plans)
  * [Launching AppSheet apps from other AppSheet apps](Launching-AppSheet-apps-from-other-AppSheet-apps)
  * [Check your app for deployment](Check-your-app-for-deployment)
  * [Application crashes/errors](Application-crashes-errors)
  * [Automated usage summary emails](Automated-usage-summary-emails)

