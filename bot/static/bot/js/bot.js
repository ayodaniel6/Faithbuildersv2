// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Toggle chatbot visibility
document.getElementById('chatbot-button').addEventListener('click', function () {
    const chatbot = document.getElementById('chatbot-box');
    chatbot.classList.toggle('hidden');
});

// Handle predefined bot questions
function askBot(question) {
    appendUserMessage(question);
    processBotRequest(question);
}

// Handle free text input
function sendBotMessage() {
    const input = document.getElementById('bot-input');
    const message = input.value.trim();
    if (!message) return;

    appendUserMessage(message);
    input.value = '';
    processBotRequest(message);
}

// Append user message to chat area
function appendUserMessage(message) {
    const chatArea = document.getElementById('chat-area');
    const userMessage = document.createElement('div');
    userMessage.className = 'bg-blue-100 p-2 rounded text-right';
    userMessage.textContent = message;
    chatArea.appendChild(userMessage);
    chatArea.scrollTop = chatArea.scrollHeight;
}

// Append bot reply
function appendBotMessage(message) {
    const chatArea = document.getElementById('chat-area');
    const botMessage = document.createElement('div');
    botMessage.className = 'bg-gray-100 p-2 rounded';
    botMessage.innerHTML = message;
    chatArea.appendChild(botMessage);
    chatArea.scrollTop = chatArea.scrollHeight;
}

// Handle bot logic
function processBotRequest(message) {
    if (message.toLowerCase().includes('request a counsellor')) {
        const requestUrl = document.getElementById('chatbot-box').dataset.requestUrl;
        window.location.href = requestUrl;
        return;
    }

    fetch("/bot/reply/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken')
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        if (data.response) {
            appendBotMessage(data.response);
        } else {
            appendBotMessage("Sorry, I didn't understand that.");
        }
    })
    .catch(error => {
        console.error("Bot error:", error);
        appendBotMessage("Something went wrong. Please try again.");
    });
}

// Script to toggle mobile menu 
  document.getElementById('mobile-menu-btn').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
  });
