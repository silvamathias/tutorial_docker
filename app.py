# %%
import brazilian_register as br

# %%
def decorador(func):
    def validacao(tipo,doc):
        f = func(tipo,doc)

        if f == False:
           return print('O documento {} informado é inválido'.format(doc))
        
        else:           
           return print('O documento {} informado é válido'.format(doc))
    
    return validacao

# %%
@decorador
def valida_doc(tipo, doc):
    
    if tipo == 0:
        r = br.cpf(doc)

        return r.cpf_status()
    
    elif tipo == 1:
        r = br.cnpj(doc)

        return r.cnpj_status()


# %%
tipo = input('digite 0 para CPF e 1 para CNPJ:')

doc = input('digite documento:')

d = valida_doc(tipo, doc)
d


