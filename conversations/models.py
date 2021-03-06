from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    participants = models.ManyToManyField("users.User", related_name="conversation", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.message.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.message.count()

    count_messages.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="message", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name="message", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
