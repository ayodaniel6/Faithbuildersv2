const getCSRFToken = () => {
  return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
};

document.getElementById('like-btn').addEventListener('click', async function () {
  const postId = this.dataset.postId;

  const response = await fetch(`/posts/${postId}/like/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
  });

  if (!response.ok) {
    console.error('Request failed', response.statusText);
    return;
  }

  const data = await response.json();
  document.getElementById('like-count').textContent = data.like_count;
  this.textContent = data.liked ? `Unlike (${data.like_count})` : `Like (${data.like_count})`;
});