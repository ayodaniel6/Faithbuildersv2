from .models import FAQ

def get_bot_response(user_input):
    input_lower = user_input.lower()
    faqs = FAQ.objects.all()
    for faq in faqs:
        if any(keyword in input_lower for keyword in faq.question.lower().split()):
            return faq.answer
    return "Sorry, I don't understand. Please try rephrasing or contact a counselor."
