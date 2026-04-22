from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .content import get_home_page_context
from .forms import ContactRequestForm
from .services.notifications import send_contact_request_notification


def home(request):
    return render(request, "gym/home.html", _build_home_context(ContactRequestForm()))


def submit_contact_request(request):
    if request.method != "POST":
        return redirect("home")

    form = ContactRequestForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Проверьте форму и попробуйте еще раз.")
        return render(
            request,
            "gym/home.html",
            _build_home_context(form),
            status=400,
        )

    contact_request = form.save()
    send_contact_request_notification(contact_request)
    messages.success(
        request,
        "Заявка отправлена. Мы свяжемся с вами в ближайшее время.",
    )
    return redirect(f"{reverse('home')}#contact")


def _build_home_context(contact_form):
    context = get_home_page_context()
    context["contact_form"] = contact_form
    return context


def health_check(request):
    return JsonResponse({"status": "ok", "service": "hammergym"})
