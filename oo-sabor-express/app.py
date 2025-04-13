from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'gourmet')
restaurante_praca.receber_avaliacao('Edson', 10)

def main():
    Restaurante.listar_restaurantes()
    Restaurante.receber_avaliacao

if __name__ == '__main__':
    main()
