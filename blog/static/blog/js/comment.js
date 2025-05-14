document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('comment-form');
    const commentList = document.getElementById('comment-list');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const formData = new FormData(form);

        fetch(window.location.pathname + 'add-comment/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            
            if (data.comment) {
                const p = document.createElement('p');
                p.innerHTML = `<strong>${data.comment.username}</strong>: ${data.comment.content}`;
                commentList.prepend(p);
                
                form.reset();
            } else if (data.errors) {
                alert(Object.values(data.errors).join("\n"));
            }
        })
        .catch(err => {
            console.error('Error:', err);
            alert("Failed to add comment.");
        });
    });
});

