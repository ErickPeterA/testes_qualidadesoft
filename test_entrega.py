from entrega import calcular_taxa_entrega


def test_ate_3km_cobra_taxa_fixa():
    assert calcular_taxa_entrega(2, 50.00) == 5.00


def test_acima_de_3km_cobra_adicional_por_km_excedente():
    assert calcular_taxa_entrega(4, 50.00) == 7.00


def test_pedido_a_partir_de_100_tem_entrega_gratis():
    assert calcular_taxa_entrega(5, 100.00) == 0.00
