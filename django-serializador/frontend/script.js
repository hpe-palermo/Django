const apiUrlBooks = 'http://localhost:8000/api/books/';
const apiUrlAuthors = 'http://localhost:8000/api/authors/';

// Função para listar todos os autores
async function fetchAuthors() {
    const response = await fetch(apiUrlAuthors);
    const authors = await response.json();
    const authorsList = document.getElementById('authors');
    const authorSelect = document.getElementById('author-select');
    authorsList.innerHTML = '';
    authorSelect.innerHTML = '';

    authors.forEach(author => {
        const li = document.createElement('li');
        li.textContent = `${author.name} (Born: ${author.birthdate})`;
        authorsList.appendChild(li);

        const option = document.createElement('option');
        option.value = author.id;
        option.textContent = author.name;
        authorSelect.appendChild(option);
    });
}

// Função para listar todos os livros
async function fetchBooks() {
    const response = await fetch(apiUrlBooks);
    const books = await response.json();
    const booksList = document.getElementById('books');
    booksList.innerHTML = '';

    books.forEach(book => {
        const li = document.createElement('li');
        li.innerHTML = `
            ${book.title} by ${book.author.name} (Published: ${book.published_date})
            <div>
                <button onclick="editBook(${book.id})">Edit</button>
                <button onclick="deleteBook(${book.id})">Delete</button>
            </div>
        `;
        booksList.appendChild(li);
    });
}

// Função para adicionar ou atualizar um livro
async function saveBook(event) {
    event.preventDefault();

    const bookId = document.getElementById('book-id').value;
    const title = document.getElementById('title').value;
    const authorId = document.getElementById('author-select').value;
    const publishedDate = document.getElementById('published_date').value;

    const book = {
        title,
        author: { id: authorId },
        published_date: publishedDate
    };

    const response = bookId
        ? await fetch(`${apiUrlBooks}${bookId}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(book)
        })
        : await fetch(apiUrlBooks, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(book)
        });

    if (response.ok) {
        document.getElementById('form').reset();
        fetchBooks();
    }
}

// Função para editar um livro
async function editBook(id) {
    const response = await fetch(`${apiUrlBooks}${id}/`);
    const book = await response.json();

    document.getElementById('book-id').value = book.id;
    document.getElementById('title').value = book.title;
    document.getElementById('author-select').value = book.author.id;
    document.getElementById('published_date').value = book.published_date;
}

// Função para deletar um livro
async function deleteBook(id) {
    const response = await fetch(`${apiUrlBooks}${id}/`, {
        method: 'DELETE'
    });

    if (response.ok) {
        fetchBooks();
    }
}

document.getElementById('form').addEventListener('submit', saveBook);

// Inicializa a lista de livros e autores ao carregar a página
fetchBooks();
fetchAuthors();
