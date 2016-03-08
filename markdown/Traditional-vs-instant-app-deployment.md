#  Traditional vs. instant app deployment


January 20, 2016 19:44

We do NOT follow the traditional app deployment model because it is too
cumbersome.

The traditional 'heavyweight' app deployment model is to create and submit
each app separately to an app store (iTunes Store for iOS and Google Play
Store for Android). And then your users find and download the app from the app
store. This is mechanically complex-- a software developer needs to package
code together and submit it. It is procedurally complex-- there are forms to
fill out and an approval process. It is time consuming, especially as this is
the process every time you make a small change to your app.

These processes make sense if you are building a unique app for consumers or a
broad audience. In the future, we may offer a 'whitelabel' service for this
scenario, but it does not make sense if you are building an app for your team
or employees. That's why we have created an instant app deployment mechanism
for AppSheet. Deploying an AppSheet app is as simple as clicking on a link in
an email and following a couple of instructions.

**AppSheet's deployment model**

AppSheet runs on iOS and Android (4.2 and above) devices.

Instant app deployment is possible because all AppSheet apps (the apps you
build) are "hosted" by the AppSheet mobile app.

The essential idea behind AppSheet is that your apps are driven by data and
configuration settings. The only unique aspect of each app is its data and its
configuration. And everything else that is _common_ across apps is collected
together into a single 'hosting' environment called the AppSheet mobile app.

The AppSheet app already available for download in each mobile appstore. When
you deploy and run your app, it will appear to run on its own, but is actually
'hosted' by the AppSheet app. While this is not a perfectly accurate analogy,
it may be useful to think of your app hosted in the AppSheet app in just the
same way that web pages are hosted in a web browser.

You can distribute your app [by sending your users an install link by
email](Deployment-from-an-install-link.md). When
they click on the link from a mobile device, they are asked to install
AppSheet on their device (AppSheet is already available in the app stores) and
then to install the app icon on their homescreen. Clicking on the icon
launches the app.

Your app is hosted and rendered on the mobile device using AppSheet as a
'runtime', just the same way different web pages are hosted in a browser.

Beyond the obvious simplicity of this approach, there are a few other
benefits:

  * Your apps are instantly available-- there is no delay between app creation and app deployment.
  * Changes to your apps are instantly available too.
  * Any system-wide changes (new features we provide, issues we fix, performance improvements) automatically appear in all apps.

In some cases, you might really want to build a traditional app like a
software developer. White-label is a possibility for AppSheet apps, we are
currently working on a solution for stand-alone apps that go in the store but
the option is currently unavailable. While this choice is not common, you
might consider it if:

  * The discovery and distribution model of the appstore is important in your use case.
  * You are aiming for large scale consumer adoption of your app.

When you choose to submit an app to the iTunes or Google Play app stores, you
need to ensure that it conforms to the policies of those app stores, and the
approval process that goes along with it.

We will update this entry with more details about White-Label in the future.


## Related articles {.section}

  * [Mobile-specific features in my app](Mobile-specific-features-in-my-app)
  * [AppSheet is NOT...](AppSheet-is-NOT-)
  * [Who should use AppSheet and what kind of apps can it create?](Who-should-use-AppSheet-and-what-kind-of-apps-can-it-create-)
  * [Advanced app customizations](Advanced-app-customizations)
  * [Create an app](Create-an-app)

