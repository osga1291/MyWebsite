from .models import post
from .signals import message_responded, message_confirmed
from django.core.exceptions import ValidationError

class MessagingService(object):
    def send_post(self,sender,recipient,switch,shift,recipient_shift,comment):

        if sender == recipient:
            raise ValidationError("You can't send messages to yourself.")

        post_sent = post(sender=sender, recipient=recipient, switch= switch, shift= shift, recipient_shift= recipient_shift, 
        comment = comment)
        post_sent.save()

        post_sent.send(sender = post, from_user = post.sender, to = message.recipient)


        # The second value acts as a status value
        return post, 200