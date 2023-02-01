from django.shortcuts import render


def profiles(request):
    """
    Display the users profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)