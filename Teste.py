import recomendacao as f
'''Recomendação baseada em usuários'''
valor = f.getRecomendacoesUsuario(f.avaliacoesUsuario, 'Leonardo')
#print(valor)

listaitens = f.calculaItensSimilares(f.avaliacoesFilme)
#print(f'{listaitens}')


'''Recomendação baseada em itens'''
recomendacao = f.getRecomendacoesItens(f.avaliacoesUsuario, listaitens, 'Leonardo')
print(recomendacao)