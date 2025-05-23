function sortBooks(order){
    const booksList = document.getElementById('books-list');
    const books = Array.from(booksList.getElementsByTagName('li'));

    books.sort((a, b) =>{
        const priceA = parseFloat(a.getAttribute('data-price'));
        const priceB = parseFloat(b.getAttribute('data-price'));

        if (order === 'asc'){
             return priceA - priceB;
        } else {
            return priceB - priceA;
        }
    });

    booksList.innerHTML = '';
    books.forEach(book => {
        booksList.appendChild(book);
    });
}