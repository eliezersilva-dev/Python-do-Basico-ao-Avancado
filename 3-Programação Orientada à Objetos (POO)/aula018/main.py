"""
Em Python tudo é um objeto: incluindo classes;
Metaclasses são as 'classes' que criam classes;
Type é uma metaclasse!
"""

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        # if 'b_fala' not in namespace:
        #     print(f'Oi, você precisa criar o método b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um método, não atributo em {name}.')

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


b = B()

print(b.attr_classe)

