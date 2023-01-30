from django.http import HttpResponse


class stripeWH_handler:
    """ handles stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handles unknown/unexpected event
        """
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200
        )
