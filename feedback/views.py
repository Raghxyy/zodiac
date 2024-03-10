from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.core.mail import send_mail
from .models import Feedback
import plotly.graph_objs as go

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()

            # Send email notification
            subject = 'Feedback Submitted'
            message = f"Hi {feedback.name},\n\nThank you for your feedback. Your feedback content:\n\n{feedback.content}\n\nWe appreciate your input!"
            from_email = ''
            to_email = [feedback.email]
            send_mail(subject, message, from_email, to_email, fail_silently=True)

            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')

def feedback_graph(request):
    # Fetch feedback data
    feedback_data = Feedback.objects.all()

    # Extract data for visualization
    names = [feedback.name for feedback in feedback_data]
    feedback_count = len(names)

    # Create a pie chart
    fig = go.Figure(data=[go.Pie(labels=names, values=[1]*feedback_count)])
    graph_json = fig.to_json()

    return render(request, 'feedback_graph.html', {'graph_json': graph_json})