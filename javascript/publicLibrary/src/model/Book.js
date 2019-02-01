// Book class
function Book(slots) {
    this.isbn = slots.isbn;
    this.title = slots.title;
    this.year = slots.year;
};

// Collection of all Book instances
Book.instances = {};

// Convert row to object
Book.convertRow2Obj = function(bookRow) {
    var book = new Book(bookRow);
    return book;
};

// Load all Book instances
Book.loadAll = function() {
    var i = 0, key = "", keys = [], bookTableString = "", bookTable = {};

    try {
        if (localStorage["bookTable"]) {
            bookTableString = localStorage["bookTable"];
        }
    } catch (e) {
        alert("Error when reading from local storage\n" + e);
    }

    if (bookTableString) {
        bookTable = JSON.parse(bookTableString);
        keys = Object.keys(bookTable);
        console.log(keys.length + " books loaded.");
        for (i = 0; i < keys.length; i++) {
            key = keys[i];
            Book.instances[key] = Book.convertRow2Obj(bookTable[key]);
        }
    }
};

// Save all book instances to local storage
Book.saveAll = function() {
    var bookTableString = "", error = false, nmrOfBooks = Object.keys(Book.instances).length;

    try {
        bookTableString = JSON.stringify(Book.instances);
        localStorage["bookTable"] = bookTableString;
    } catch (e) {
        alert("Error when writing to Local Storage\n" + e);
        error = true;
    }

    if (!error) console.log(nmbOfBooks + " books saved.");
};

// Add a Book
Book.add = function(slots) {
   var book = new Book(slots);
   Book.instances[slots.isbn] = book;
   console.log("Book " + slots.isbn + " create!");
};

// Update a Book
Book.update = function(slots) {
    var book = Book.instances[slots.isbn];
    var year = parseInt(slots.year);
    if (book.title !== slots.title) { book.title = slots.title;}
    if (book.year !== year) { book.year = year;}
    console.log("Book " + slots.isbn + " modified!");
};

// Destroy a Book
Book.destroy = function(isbn) {
    if (Book.instances[isbn]) {
        console.log("Book " + isbn + " deleted!");
        delete Book.instances[isbn];
    } else {
        console.log("There is no book with ISBN " + isbn + " in the database!");
    }
};

// Create test data for Book
Book.createTestData = function() {
    console.log("Book.createTestData");

    Book.instances["01wtw"] = new Book({isbn:"01wtw", title:"Weaving the Web", year:2000});
    Book.instances["02geb"] = new Book({isbn:"02geb", title:"Godel, Escher, Bach", year:1999});
    Book.instances["03iaa"] = new Book({isbn:"03iaa", title:"I Am A Strange Loop", year:2008});

    Book.saveAll();
};

// Clear data for Book from local storage
Book.clearData = function() {
    console.log("Book.clearData");

    if (confirm("Do you really want to delete all book data?")) {
        localStorage["bookTable"] = "{}";
    }
};

