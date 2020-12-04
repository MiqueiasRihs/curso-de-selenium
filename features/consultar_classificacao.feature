#language: pt
Funcionalidade: Consultar classificacao do Brsileirao
    '''Eu como usuario quero acessar a pagina de classificação do campo Capeonato Brasileiro no globo esporte para consultar o primeiro colocado.'''

    Cenario: Consultar Primeiro Colocado no Brasileirão
    Dado acesso a pagina inicial do globo esporte
    Quando clico no menu do brasileirao
    E classificacao e exibida
    Então devo saber quem e o primeiro colocado