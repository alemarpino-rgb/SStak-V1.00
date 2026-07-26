import sys

def Stack(codice):
    stack=[]
    memoria={}
    Delete=False
    Duplica=False
    Prendi=False
    no_canc=False
    Commenti=False
    for token in codice.split():
        if Commenti==False:
            if token.isdigit():
                if Delete==False and Duplica==False and Prendi==False:
                    stack.append(int(token))
                elif Delete==True:
                    if 0 <= int(token) < len(stack):
                        stack.pop(int(token))
                    else:
                        print(f"Errore_6: impossibile eliminare l'elemento {token} perché inesistente")
                elif Duplica==True:
                    if 0 <= int(token) < len(stack):
                        elemento_duplo=stack[int(token)] 
                        stack.append(elemento_duplo) 
                    else:
                        print(f"Errore_6: impossibile duplicare l'elemento {token} perché inesistente")
                elif Prendi==True:
                    index=int(token)
                    if 0 <= index < len(stack):
                        elemento_preso=stack.pop(index)
                        stack.append(elemento_preso) 
                    else:
                        print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    
            elif token=="+":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif token=="++":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                while len(stack) > 1:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a+b)
            elif token=="*":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif token=="**":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                while len(stack) > 1:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
            elif token=="-":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                a=stack.pop()
                b=stack.pop()
                stack.append(a-b)
            elif token=="--":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                while len(stack) > 1:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a-b)
            elif token == "REP":
                if len(stack) < 2:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                
                a = stack.pop()
                b = stack.pop()
                
                for _ in range(b):
                    stack.append(a)
            elif token=="/":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                a=stack.pop()
                b=stack.pop()
                if b==0:
                    print(f"Errore_4: Divisione per zero, impossibile")
                    return
                stack.append(a/b)
            elif token=="//":
                if len(stack)<=1:
                    print(f"Errore_1: il token '{token}' deve essere utilizzato quando almeno due valori sono presenti nello stack")
                    return
                while len(stack) > 1:
                    a=stack.pop()
                    b=stack.pop()
                    if b==0:
                        print(f"Errore_4: Divisione per zero, impossibile")
                        return
                    stack.append(a/b)
            elif token=="DUP":
                if len(stack)<=0:
                    print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    return
                stack.append(stack[-1])
            elif token=="DEL":
                if len(stack)<=0:
                    print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    return
                stack.pop()
            elif token=="DEL(":
                if len(stack)<=0:
                    print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    return
                Delete=True
            elif token=="DUP(":
                if len(stack)<=0:
                    print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    return
                Duplica=True
            elif token=="PICK(":
                if len(stack)<=0:
                    print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    return
                Prendi=True
            elif token=="REM":
                nome_var = stack.pop()  
                valore = stack.pop()    
                memoria[nome_var] = valore
            elif token=="LOAD":
                nome_var = stack.pop()
                
                # Controlliamo se la variabile esiste nella nostra memoria
                if nome_var in memoria:
                    stack.append(memoria[nome_var])
                else:
                    print(f"Errore_7: la variabile '{nome_var}' non esiste in memoria!")
                    return
            elif token==")":
                if Delete==False and Duplica==False and Prendi==False:
                    print(f"Errore_5: il token '{token}' deve essere utilizzato solo dopo il token '('")
                    return
                Delete=False
                Duplica=False
                Prendi=False
            elif token=="DELALL":
                if len(stack)<=0:
                    print(f"Errore_3: il token '{token}' deve essere utilizzato quando almeno un valore è presente nello stack")
                    return
                stack=[]
            elif token=="SHOW":
                for numeri in stack:
                    print(f"{numeri}, ", end="")
                print("")
            elif token=="^^":
                Commenti=True
            
            else:
                if not token.isidentifier():
                    print(f"Errore_8: il token '{token}' non è valido")
                    return
                stack.append(token)
        else:
            if token=="^^":
                Commenti=False
        

    print("stack = "+ str(stack))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nome_file = sys.argv[1] # Prende il file passato da riga di comando (es. Fibonacci.SStak)
        try:
            with open(nome_file, "r") as file:
                codice = file.read()
            Stack(codice)
        except FileNotFoundError:
            print(f"Errore: il file '{nome_file}' non esiste!")
    else:
        print("Uso corretto: run <nome_file.SStak>")