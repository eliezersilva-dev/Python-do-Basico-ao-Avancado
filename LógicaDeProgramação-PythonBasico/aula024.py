"""
Operador ternário em Python
"""
logged_user = False
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Precisa logar'
print(msg)

# Simplificando com operdor ternário
logged_user = False
msg = 'Usuário logado.' if logged_user else 'Precisa logar'
print(msg)

