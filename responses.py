def sample_responses(input_text):
    user_message = input_text.lower()
    if 'hi' in user_message:
        return 'yo'
    if 'how are you' in user_message:
        return 'I am fine'
    return 'I dont know what are you talking'