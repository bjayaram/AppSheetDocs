#  Errors accessing a spreadsheet


June 15, 2015 18:03

AppSheet can experience errors reading or writing spreadsheet data from any
cloud storage provider.

  * **Error 401** -- this occurs when AppSheet does not have permission to work on behalf of the user.
  * **Error 403** (permission denied) -- this occurs when AppSheet tries to access your spreadsheet, but the storage provider responds that AppSheet does not have the permission to access it. 
  * **Error 404** (cannot access the spreadsheet) -- this occurs when AppSheet tries to access your spreadsheet but the storage provider responds that no such document exists. Perhaps you have deleted the document? Perhaps you never had access to it?
  * **Timeout** -- occasionally, the remote storage provider has a timeout and fails to provide the spreadsheet data to AppSheet despite repeated retries. Although fewer than 1% of our requests encounter such issues, it is still significant enough that you may encounter such a problem. You may experience this problem as an unexpected delay during Sync, or even a sync failure. Typically a refresh or retry after a few seconds rectifies the problem.
  * **Error 500** (internal server error)  -- very occasionally, the remote storage provider has an internal error and fails to provide the spreadsheet data to AppSheet. Typically this is a transient problem and often is hidden from our users because we automatically retry the request. 


## Related articles {.section}

  * [Google Drive](Google-Drive.md)
  * [Make a spreadsheet](Make-a-spreadsheet.md)
  * [Plan upgrade required](Plan-upgrade-required.md)
  * [Deploy your app](Deploy-your-app.md)
  * [Using a scanner](Using-a-scanner.md)

