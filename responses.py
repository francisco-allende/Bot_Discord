import random

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hola':
        return 'como andas?'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'Escribi "pic" para recibir una foto random de Bolivia'

    if p_message == "pete":
        return "pete tu vieja"
    
    if p_message=="lila":
        return "la capri"
    
    if p_message=="pic":
        num = random.randint(1, 10)
        if num == 1:
            return "https://www.linkpicture.com/q/a_59.jpg"
        if num == 2:
            return "https://www.linkpicture.com/q/b_51.jpg"
        if num == 3:
            return "https://www.linkpicture.com/q/c_18.jpg"
        if num == 4:
            return "https://www.linkpicture.com/q/d_19.jpg"
        if num == 5:
            return "https://www.linkpicture.com/q/e_21.jpg"
        if num == 6:
            return "https://www.linkpicture.com/q/f_22.jpg"     
        if num == 7:
            return "https://www.linkpicture.com/q/g_15.jpg"
        if num == 8:
            return "https://www.linkpicture.com/q/h_1.jpg"
        if num == 9:
            return "https://www.linkpicture.com/q/i_16.jpg"
        if num == 10:
            return "https://www.linkpicture.com/q/j_9.jpg"
