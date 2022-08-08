
from datetime import datetime
from django.views import View
from django.core.mail import EmailMultiAlternatives
from .models import Appointment
from django.shortcuts import redirect, render
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'appointment/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            client_name=request.POST['client_name'],
            date=datetime.strptime(request.POST['date'], '%Y-%M-%d'),
            message=request.POST['message'],
        )
        appointment.save()

        html_content = render_to_string(
            'appointment/appointment_created.html',
            {'appointment': appointment}
        )

        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%m-%d")}',
            body=appointment.message,
            from_email='seleznevaiu86@yandex.ru',
            to=['caha150886@gmail.com'],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return redirect('/appointments/')