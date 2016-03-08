#  Is it possible to create an incrementing number for each record?


February 27, 2016 05:58

Lots of customer ask for the ability to create monotonically increasing record
number keys that accurately reflects the order in which the records were
created. This is a natural desire, but it is technically impossible in a
system that combines multiple distributed clients, who are allowed to
concurrently add records, and who can add records while offline.

It is possible, but can be expensive, if you are willing to relax one or more
of these requirements.  
  
1\. Monotonically increasing key, such as 1, 2, 3 ... or 1000, 1001, 1002, ...  
2\. Keys accurately reflect the order the records were first created by the
client.  
3\. Two or more clients can add records concurrently.  
4\. Clients can add records while offline.  
  
For example, you can achieve a monotonically increasing key through a central
locking scheme if you are willing to give up doing adds while offline.  
  
If you are willing to give up having the record number increase strictly
monotonically and to reflect the exact order the records were created, you can
give each client a block of numbers that only that client uses for its newly
added record key values. The block of numbers reserved for each client must be
large enough so that no client runs out of preassigned numbers while it is
working offline. Obviously, the record number keys are no longer strictly
monotonically increasing and they don't strictly reflect the order of
creation, but they roughly reflect the order the records were added.  
  
You can assign monotonically increasing number keys to newly added records, by
having the server assign the record number keys after the client synchronizes.
The resulting record number keys reflect the order in which the newly added
record first reached the server, rather than the absolute time they were
created by each client. This can lead to some complications because the client
only knows the record's "real key" after it synchronizes with the server. If
the client adds a set of records that are related by key value, the client
must assign the actual key values to each of the newly created records, and
ensure they the references between these records reflect the actual key
values. The client can only do this after the actual key values are returned
by the server.  
  
There are other design alternatives, but all of them involve tradeoffs
regarding which requirements you relax and how much cost you are willing to
bear to achieve nearly monotonically increasing record number keys.


## Related articles {.section}

  * [Keys](Keys.md)

