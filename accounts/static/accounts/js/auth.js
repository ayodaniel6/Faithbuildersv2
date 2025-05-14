function flipCard(toBack) {
    const card = document.getElementById('flip-card');
    if (toBack) {
      card.classList.add('flipped');
    } else {
      card.classList.remove('flipped');
    }
  }