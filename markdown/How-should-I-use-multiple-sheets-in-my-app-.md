#  How should I use multiple sheets in my app?


January 22, 2016 23:04

You might want to use data from more than one spreadsheet in your AppSheet
app. There are two ways to do this. [You can add multiple standalone
spreadsheet files as AppSheet tables.](Using-
multiple-spreadsheets) It is also possible to create AppSheet tables from
different worksheets within the same workbook.

To be clear on terminology, a single dataset used by AppSheet is called a
**table**. The source of a table is a single spreadsheet. A **workbook** is a
file that contains one or more worksheets; a **worksheet** is a single
spreadsheet that contains cells organized by rows and columns.

Either approach works just fine, depending on your circumstances. The
performance of the two options may differ based on the specific content. The
intuition is simple-- the AppSheet backend has to download the entire
spreadsheet file but if the same file (workbook) is referenced multiple times
(via multiple tables referencing individual worksheets in the workbook), the
backend can be efficient and download it just once. On the other hand,
multiple small files can be fetched and processed efficiently in parallel.

In most cases, you should pick whichever approach is convenient for you to
manage. However, if you use only two worksheets out of a spreadsheet file with
a hundred large worksheets in it, you'd be better off splitting those two off
into their own single files.


## Related articles {.section}

  * [Using multiple spreadsheets](Using-multiple-spreadsheets)
  * [How do I control the order of columns displayed in the app?](How-do-I-control-the-order-of-columns-displayed-in-the-app-)
  * [Multi-page forms with conditional branching](Multi-page-forms-with-conditional-branching)
  * [Who should use AppSheet and what kind of apps can it create?](Who-should-use-AppSheet-and-what-kind-of-apps-can-it-create-)
  * [How do I design a secure app?](How-do-I-design-a-secure-app-)

