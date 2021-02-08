import plivo


def sendsms_on_completion(completiom_time):
    client = plivo.RestClient("MAZJZLYTFIMDDHMJZMYZ", "NWMzZTBiZWFjYTMyYTNkNjFkZTI4MTU5ZDIwNzIx")
    message_created = client.messages.create(
        src='+15709985164',
        dst=f'+15712911193',
        text=f'Your completion time was {str(completiom_time)}.'
    )