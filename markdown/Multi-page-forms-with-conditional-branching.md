#  Multi-page forms with conditional branching


January 13, 2016 21:59



You might want to break up a long input form into several pages for
convenience. In some apps, it makes sense to conditionally show or hide a
specific page based on choices made earlier. For example, in a form for a
vehicle inspection report, you may have an initial question asking if there is
damage. If the answer is Yes, you may want to show a Form page that has
specific questions about the damage. If the answer is No, you would want to
skip that page.



**Conditional branching in Google Forms**

When you are building your app from a Google Form, use **Add Item -> Page
break** to split the form into multiple pages (Note: You can optionally
provide a page header or description. This is helpful to remember where you're
directing respondents and helping respondents understand your form's
structure). You can then add **Multiple choice** or **Choose from a list**
items with the option "Go to page based on answer" and choose different
navigation paths for each option. _Often you will also want these "conditional
branching" questions be be marked as required._

At each page break, you can also choose where the form should go next. Keep in
mind that the page break navigation will only take effect under certain
circumstances:

  1. When the page has no conditional branching questions
  2. When conditional branching questions are not required and no answer is given
  3. When "Continue to next page" is chosen for specific answers to branching questions

After setting up your form, start the [AppSheet add-on](https://chrome.google.com/webstore/detail/appsheet/hmmicpkfdjjchdajlldfckjaanfobjob?hl=en-US) and
click "Prepare". The AppSheet add-on creates "Page Header" columns in your
response spreadsheet to represent each page break and automatically converts
the form's "go-to-page" navigation into AppSheet's "show if" expression model.
The Page Header columns appear in AppSheet as "[Show](Column-types)" type columns, meaning they affect the
visual presentation of forms. The Type Qualifier for these columns specifies
the Category as 'Page_Header'. You can examine the column structure in the
[Advanced Editor](Advanced-app-customizations.md)>Data>Column Structure.

Most forms can now be correctly converted to AppSheet apps automatically, but
there are two main limitations:

  1. Reverse navigation is not supported by AppSheet. Try to arrange your form such that all navigation proceeds to higher page numbers.
  2. In Google Forms you can include a special "Other" option for Multiple choice questions and assign it specific navigation behavior. However, the navigation associated with this choice is not made available to the AppSheet add-on. We recommend avoiding use of "Other" on questions where "Go to page based on answer" is enabled.

For more information about the conversion from Google Forms to AppSheet, see
[this article](Integrating-with-Google-Apps-Sheets-and-Forms-.md).



**Conditional branching in your spreadsheet and the Advanced Editor**

When you are building your form app from a spreadsheet, insert an empty column
at each point where you'd like a page break in the form.

While conditional branching in Google Forms is based on a "go-to-page"
navigation model, AppSheet uses a "show if" model to describe whether a given
page should be shown or hidden. By default, pages are always shown. To make a
page appear conditionally,

  1. Find the corresponding Page Header at Advanced Editor>Data>Column Structure (the empty page-break columns in the spreadsheet are treated within AppSheet as "[Show](Column-types)"-type fields with Category "Page_Header").
  2. Click the "edit" icon on the left side and scroll down to the Type Qualifier settings.
  3. Create an [expression](Expressions.md) in the "Show_If" field that defines when the page should be shown.

**Example**

Suppose you have an Enum (dropdown) on the first page called "Cat or dog
person?" with choices "Cat" and "Dog", and you have page breaks for an "About
Cats" page and an "About Dogs" page.

The "About Cats" page can be shown only when "Cat" is chosen by setting the
Show_If field of the Page Header to the expression **[Cat or dog
person?]="Cat"**.

Likewise the "About Dogs" page can be shown only when "Dog" is chosen by using
the Show_If expression **[Cat or dog person?]="Dog"**.



**Which should I use?**

Auto-generating your app from a Google Form with the 
[AppSheet add-on](https://chrome.google.com/webstore/detail/appsheet/hmmicpkfdjjchdajlldfckjaanfobjob?hl=en-US) is often easier and more convenient, since the add-on takes care of
building the Show_If expressions for you. However, if your form requires
complex navigation conditions that depend on multiple fields, you may not be
able to represent it with Google's "go-to-page" model.

Creating your own Show_If expressions in the Advanced Editor gives you more
freedom to define complex composite or comparison conditions that can't be
represented in Google Forms using functions like AND, OR, NOT, etc.

## Related articles {.section}

  * [Customizing input forms](Customizing-input-forms.md)
  * [Controlling data inputs with column constraints](Controlling-data-inputs-with-column-constraints.md)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-.md)
  * [Conditional formatting](Conditional-formatting.md)
  * [Capturing GPS location](Capturing-GPS-location.md)

