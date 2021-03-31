def sample_response(input_text):
    user_message=str(input_text).lower()
    if user_message in("stupid"):
        return "hahha lol"
    if user_message in("fat"):
         return "dont call me fat"
    if user_message in("dump"):
        return "what are u saying?"
    return "i dont unserstand"
