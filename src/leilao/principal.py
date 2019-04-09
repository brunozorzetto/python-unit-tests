from src.leilao.dominio import Lance, Usuario, Leilao, Avaliador

bruno = Usuario('Bruno')
batman = Usuario('Batman')

lance_batman= Lance(batman, 2000.0)
lance_bruno = Lance(bruno, 500.0)

leilao = Leilao('Celular')
leilao.lances.append(lance_bruno)
leilao.lances.append(lance_batman)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} de um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
