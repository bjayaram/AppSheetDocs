#  Make your list into an app


October 26, 2015 23:55

Everyone has a list in a spreadsheet-- a client list, an item list, etc. Here
are some suggestions for building useful list apps.

Consider multiple grouped list views instead of or in addition to the default
tabular view. Grouped views help you divide your data into different
categories.

If you have a list of people:

  * Their phone numbers should be touch-callable in the app. If not, it is probably because your telephone number format was not automatically recognized by AppSheet. No problem, you can explicitly set the type of this column to Phone.
  * If there are physical addresses for the entries in your list, consider adding a map view. Your addresses should be fully specified (i.e. if you live in Las Vegas and all your addresses are in Las Vegas, don't just leave out 'Las Vegas, NV, USA' from your addresses). While the shortened address clearly makes sense in your context, our mapping software does better with full addresses.

If you have a list of products:

  * Consider adding an image to each product and add an image gallery view. Images usually look beautiful. Play with the different image presentation sizes. They completely alter the feel of the app. Don't worry if you have high resolution images-- we downsize them appropriately for a mobile device.
  * If you want to steer users to an external e-commerce site, you can add an action button to each image. Take a look at the [ECommerce Store sample.](https://www.appsheet.com/Template/ShowDef?appName=ECommerceStore-10305)

If you have a list of numbers (sales reports, budgets, etc.):

  * Consider using one or more chart views-- they will help you visualize the data.
  * AppSheet supports different kinds of charts and we are adding more based on customer requests.

If you have a list of instructions:

  * Consider adding an image to each instruction and using a List view with a Deck presentation.
  * Take a look at the [Repair Manual sample.](https://www.appsheet.com/Template/ShowDef?appName=InstructionManual-10305)



## Related articles {.section}

  * [Apps using dates](Apps-using-dates)
  * [Displaying images and documents](Displaying-images-and-documents)
  * [Make a spreadsheet](Make-a-spreadsheet)
  * [How should I use multiple sheets in my app?](How-should-I-use-multiple-sheets-in-my-app-)
  * [Expressions](Expressions)

