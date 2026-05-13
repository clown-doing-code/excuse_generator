import random

excuses_list = [
    "My goldfish has separation anxiety and needs me home",
    "I accidentally became nocturnal and just now woke up",
    "My WiFi is haunted and won't let me leave the house",
    "I have a medical condition called 'chronic Monday-itis'",
    "My cat is holding my car keys hostage",
    "I'm allergic to Mondays (it says so on my certificate)",
    "I forgot how to human today, trying again tomorrow",
    "My houseplant told me it needs emotional support",
    "I can't find matching socks and it's a crisis",
    "My brain is in sleep mode and needs a reboot",
    "My productivity level is at 0% and it's not coming back today",
    "I accidentally ate a magic cookie and now I'm legally unavailable",
    "My boss left me on read and I'm taking it personally",
    "I'm currently in a committed relationship with my bed",
    "My calendar says 'do nothing' and I'm honoring that commitment",
    "I'm not lazy, I'm on energy-saving mode",
    "My left eyebrow has an existential crisis and I need to help it",
    "I have a prior engagement with my Netflix queue",
    "My phone charger only works when I stay home",
    "I'm experiencing technical difficulties with my motivation",
]


def main():
    print(f"Sorry, I can't go to work today.\n{random.choice(excuses_list)}")


main()
