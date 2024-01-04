//fetch & insert navbar into current page
fetch('navbar1.html')
    .then(response => response.text())
    .then(navbarHtml => {
        //insert navbar at the beginning of body
        document.body.insertAdjacentHTML('afterbegin', navbarHtml);

        //highlight current page in the navbar when in homepage or resource page
        const currentPath = window.location.pathname.split('/').pop();
        const currentPageLink = document.querySelector(`.nav-item[href="${currentPath}"]`);
        if (currentPageLink) {
            currentPageLink.classList.add('active'); //add a class for styling active link
        }
    })
    .catch(error => console.error('Error fetching navbar:', error));
