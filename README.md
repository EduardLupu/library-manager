# library-manager
Application of a library (books, clients, rentals), built in Python.
* The user can add, remove, update, and list both clients and books.
* A client can rent an available book. A client can return a rented book at any time. Only available books (those which are not currently rented) can be rented.
* Search for clients or books using any one of their fields (e.g. books can be searched for using id, title or author).
* The search works using case-insensitive and partial string matching.
* Create statistics: most rented books, most active clients, most rented author (will be provided in descending order)
* Unlimited undo/redo functionality (implemented using reverse operation)
* The repository can be selected by the user (in-memory, files, binary-files, json, sqlite).