document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const resultsDiv = document.getElementById('search-results');

    searchInput.addEventListener('keyup', function () {
        const query = searchInput.value;
        if (query.length > 1) {
            fetch(`/blog/search/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);  // Log the response to verify the structure
                    resultsDiv.innerHTML = '';
                    if (data.length > 0) {
                        data.forEach(item => {
                            if (item.slug && item.title) {  // Ensure slug and title exist
                                const div = document.createElement('div');
                                div.innerHTML = `<a href="/posts/${item.slug}/" class="block px-4 py-2 hover:bg-gray-100 text-gray-800 text-sm">${item.title}</a>`;
                                resultsDiv.appendChild(div);
                            } else {
                                console.error("Invalid data: ", item);  // Log invalid data
                            }
                        });
                    } else {
                        resultsDiv.innerHTML = '<div>No results found</div>';
                    }
                })
                .catch(error => {
                    console.error('Error fetching search results:', error);
                    resultsDiv.innerHTML = '<div>Error fetching results</div>';
                });
        } else {
            resultsDiv.innerHTML = '';
        }
    });
});

document.addEventListener("click", function (e) {
    const input = document.getElementById("search-input");
    const results = document.getElementById("search-results");
    if (!input.contains(e.target) && !results.contains(e.target)) {
        results.classList.add("hidden");
    }
});


