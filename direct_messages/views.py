from django.shortcuts import render, redirect
from .models import DirectMessage

# Create your views here.
def direct_message(request):
    if request.method == 'POST':
        message = DirectMessage.objects.create(
            sender=request.user.user_profile,
            content = request.POST.get('message-content') # <textarea name="message-content"
        )

        # Date gets set automatically
        message.save()

        return redirect(direct_message)

    if request.GET:
        my_messages = DirectMessage.objects.filter(
            Q(sender=request.user.user_profile) | Q(recipient=request.user.user_profile)
        )

        # Dictionary of the form
        # {
        #     'other_person1s_username': [message1, message2, ...],
        #     'other_person2s_username': [message1, message2, ...],
        # }
        messages_dict = dict()


        # Group all the messages by conversation.
        for message in my_messages:
            # Go through all the messages and group them by other person (who could either be the sender or recipient)

            other_person = message.sender if message.recipient == request.user.user_profile else message.recipient

            if other_person.username in messages_dict:

                messages_dict[other_person.username].append(message)

            else:
                messages_dict[other_person.username] = [message]

