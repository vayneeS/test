
def add(a, b):  # E231 : espace manquant après la virgule
    return a + b  # E225 : espaces manquants autour de l'opérateur

def subtract(a, b):  # E201/E202 : espaces parasites
    result= a - b  # E225
    return result


class Calculator:  # N801 : nom de classe doit être en PascalCase
    def multiply(self, x, y):  # E231
        return x * y 
    