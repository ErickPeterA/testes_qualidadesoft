TAXA_BASE = 5.00
DISTANCIA_INCLUIDA_KM = 3
VALOR_POR_KM_EXCEDENTE = 2.00
PEDIDO_MINIMO_ENTREGA_GRATIS = 100.00


def calcular_taxa_entrega(distancia_km, total_pedido):
    """Calcula a taxa de entrega.

    Regras:
    1. Até 3 km, a taxa é de R$ 5,00.
    2. Acima de 3 km, acrescenta R$ 2,00 por km excedente.
    3. Pedidos a partir de R$ 100,00 têm entrega gratuita.
    """
    if total_pedido >= PEDIDO_MINIMO_ENTREGA_GRATIS:
        return 0.00

    km_excedente = max(0, distancia_km - DISTANCIA_INCLUIDA_KM)
    return TAXA_BASE + km_excedente * VALOR_POR_KM_EXCEDENTE
