from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.decorators.http import require_POST
import json
import re
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import CounsellorRequestForm
from blog.models import Post


# 🔹 Counsellor Request View (Login Required)
@login_required(login_url='/accounts/auth/')
def request_counsellor(request):
    if request.method == 'POST':
        form = CounsellorRequestForm(request.POST)
        if form.is_valid():
            form.save()

            # Send email to the user
            send_mail(
                'Counsellor Request Submitted',
                f'Thank you {request.user.username}, your request for a counsellor has been received.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],  # Send to the user's email
                fail_silently=False,
            )
            messages.success(request, "Your request has been submitted. A confirmation email has been sent.")

            # email = EmailMessage(
            #     'Counsellor Request Received',
            #     '<h2>Thank you for your request</h2><p>Your request is being processed.</p>',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [user_email],
            # )
            # email.content_subtype = 'html'  # To send HTML email
            # email.send()

            return redirect('bot:thank_you')

    else:
        initial_data = {
            'email': request.user.email,
            'name': request.user.get_full_name() or request.user.username
        }
        form = CounsellorRequestForm(initial=initial_data)

    return render(request, 'bot/request.html', {'form': form})


@csrf_exempt
@require_POST
def bot_reply(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    data = json.loads(request.body)
    message = data.get('message', '').lower()

    # === 1. FAQ-like fixed responses ===
    faq_responses = {
        "what is this site about": "This is a student support platform where you can read blog posts and request to meet a counselor.",
        "how to request a counsellor": "Click the 'Request a Counsellor' button above to get started.",
        "how to post": "Only authors can post content via the dashboard.",
    }

    for keyword, response in faq_responses.items():
        if keyword in message:
            return JsonResponse({'response': response})

    # === 2. Keyword extraction for post search ===
    search_keywords = re.findall(r'\w+', message)
    if search_keywords:
        query = Q()
        for word in search_keywords:
            query |= Q(title__icontains=word) | Q(content__icontains=word) | Q(tags__name__icontains=word)

        matching_posts = Post.objects.filter(query).distinct()[:5]

        if matching_posts.exists():
            response = "Here are some posts you might find helpful:<br><ul>"
            for post in matching_posts:
                post_url = post.get_absolute_url()
                response += f'<li><a href="{post_url}" class="text-blue-600 hover:underline" target="_blank">{post.title}</a></li>'
            response += "</ul>"
            return JsonResponse({'response': response})

    return JsonResponse({'response': "Sorry, I couldn't find anything related to that."})