from .forms import InvestmentForm, ContactForm
from .investment import Investment
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def calculate_investment(request):
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            contribution = form.cleaned_data['contribution']
            time = form.cleaned_data['time']
            interest_rate = form.cleaned_data['interest_rate']

            investment = Investment()
            investment._principal = principal
            investment._contribution = contribution
            investment._time = time
            investment._interest_rate = interest_rate / 100  # Convert percentage to decimal
            investment.calculate_future_values()

            graph_json = investment.get_plot()
            table_data = investment.get_table_data()

            return render(request, 'investment_result.html', {
                'graph_json': graph_json,
                'table_data': table_data
            })
        else:
            # Form is invalid; render form with errors
            return render(request, 'investment_form.html', {'form': form})
    else:
        form = InvestmentForm()
    return render(request, 'investment_form.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose email
            subject = f'New Contact Form Submission from {name}'
            full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]

            # Send email
            send_mail(subject, full_message, from_email, recipient_list)

            # Redirect to success page
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'calculator/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'calculator/contact_success.html')
