// Fetch and insert the navbar into the current page
fetch('navbar.html')
    .then(response => response.text())
    .then(navbarHtml => {
        // Insert the navbar at the beginning of the body
        document.body.insertAdjacentHTML('afterbegin', navbarHtml);

        // Highlight the current page in the navbar
        const currentPath = window.location.pathname.split('/').pop();
        const currentPageLink = document.querySelector(`.nav-item[href="${currentPath}"]`);
        if (currentPageLink) {
            currentPageLink.classList.add('active'); // Add a class for styling the active link
        }
    })
    .catch(error => console.error('Error fetching navbar:', error));
