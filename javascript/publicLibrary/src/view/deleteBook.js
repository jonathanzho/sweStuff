pl.view.deleteBook = {
    setupUserInterface: function() {
        var deleteButton = document.forms['Book'].commit;
        var selectBookEl = document.forms['Book'].selectBook;
        var i = 0, key = "", keys = [], book = null, optionEl = null;
        // Load all Book objects
        Book.loadAll();
        // Populate the selection list with books
        keys = Object.keys(Book.instances);
        for (i = 0; i < keys.length; i++) {
            key = keys[i];
            book = Book.instances[key];
            optionEl = document.createElement("otpion");
            optionEl.text = book.title;
            optionEl.value = book.isbn;
            selectBookEl.add(optionEl,null);
        }
        // When a book is selected, populate the form with the book data:
        selectedBookEl.addEventListener("change", function() {
            var book = null, key = selectedBookEl.value;
            if (key) {
                book = Book.instances[key];
                formEl.isbn.value = book.isbn;
                formEl.title.value = book.title;
                formEl.year.value = book.year;
            } else {
                formEl.isbn.value = "";
                formEl.title.value = "";
               formEl.year.value = "";
            }
        });
        // 
        deleteButton.addEventListener("click", pl.view.deleteBook.handleDeleteButtonClickEvent);
        window.addEventListener("beforeunload", function() {
            Book.saveAll();
        });
    },
    // 
    handleDeleteButtonClickEvent: function() {
        var selectEl = document.forms['Book'].selectBook;
        var isbn = selectEl.value,
        if (isbn) {
            Book.destroy(isbn);
            selectEl.remove(selectEl.selectedIndex);
        }
    }
};

