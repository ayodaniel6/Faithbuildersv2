document.getElementById('bookmark-btn').addEventListener('click', async function () {
    const postId = this.dataset.postId;

    const response = await fetch(`/posts/${postId}/bookmark/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),
      },
    });

    if (!response.ok) {
      console.error('Bookmark request failed:', response.statusText);
      return;
    }

    const data = await response.json();
    this.textContent = data.bookmarked ? 'Bookmarked' : 'Bookmark';
  });
  