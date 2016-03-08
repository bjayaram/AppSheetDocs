#  Extracting structure from cloud spreadsheets


January 05, 2016 22:40

Most interesting apps show and capture data. Traditionally, apps built by
software developers use proprietary mechanisms to store data in structured
databases. AppSheet avoids this approach for two reasons: (1) **our app
creators are not software developers**, (2) **we want our app creators to be
in full control of their data**.

Instead AppSheet apps use data from spreadsheets. Spreadsheets allow almost
anyone to organize and store data. In later sections, we'll describe how you
can also access data from other sources, but for now, let's focus on
spreadsheets.

**AppSheet cannot access data from a spreadsheet on your PC**, but it can access data from a spreadsheet stored in a cloud file system like Google Drive or Dropbox. To explain it really simply, AppSheet makes your cloud-hosted spreadsheet behave like a simple database. The power of using a cloud-hosted spreadsheet is that there are no copies of your data created, nor is the data 'uploaded' into AppSheet servers. Instead, AppSheet reads and writes directly to your spreadsheet.

AppSheet automatically infers the structure of your data from the spreadsheet
you provide. AppSheet models a data set as a 'table'-- i.e. a collection of
rows with uniformly structured columns. Each spreadsheet is treated as a
single 'table'.

For each column, AppSheet infers a data type, such as text, number, date, etc.
There are more than 20 data types recognized. AppSheet also automatically
groups related columns to form composite columns-- eg: \[FirstName and
LastName\], or \[Street, City, State\]. These inferences happen automatically but
of course, they may not always make the right decision, so you can always
override and fine tune these choices.


## Related articles {.section}

  * [Mobile apps 'driven' by the structure of data](Mobile-apps-driven-by-the-structure-of-data.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [AppSheet is NOT...](AppSheet-is-NOT-.md)
  * [Who should use AppSheet and what kind of apps can it create?](Who-should-use-AppSheet-and-what-kind-of-apps-can-it-create-.md)
  * [Mobile-specific features in my app](Mobile-specific-features-in-my-app.md)

