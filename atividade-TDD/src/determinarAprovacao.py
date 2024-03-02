
def determinarAprovação (frequencia, notaFinal, notaEspecial):
    if (frequencia >= 0) and  (notaFinal >= 0) and (notaEspecial  >= 0): 
        if (frequencia >= (75)) and (((notaFinal + notaEspecial)/2) >= 60) and (notaFinal>=60):
            return  "aprovado"
        else:
            return "reprovado"
    else: 
        return "reprovado"
