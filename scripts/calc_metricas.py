"""Script auxiliar para cálculo de métricas de eficiência em partidas de futebol.

Calcula pontaria, taxa de conversão e estimativa de Gols Esperados (xG) simplificada.
"""

from typing import Dict, Any


def calcular_metricas(
    gols: int,
    chutes_totais: int,
    chutes_no_alvo: int,
    posse_pct: float
) -> Dict[str, Any]:
    """Calcula indicadores derivados de desempenho ofensivo.

    Args:
        gols: Quantidade de gols marcados.
        chutes_totais: Número total de finalizações tentadas.
        chutes_no_alvo: Número de chutes direcionados à meta.
        posse_pct: Percentual de posse de bola (0 a 100).

    Returns:
        Dicionário com pontaria (%), conversao (%) e estimativa de xG.
    """
    chutes_fora = max(0, chutes_totais - chutes_no_alvo)

    # Cálculo da pontaria (% de chutes certos em relação ao total)
    pontaria = (chutes_no_alvo / chutes_totais * 100) if chutes_totais > 0 else 0.0

    # Eficiência de conversão (% de chutes certos que viraram gol)
    conversao = (gols / chutes_no_alvo * 100) if chutes_no_alvo > 0 else 0.0

    # Estimativa empírica simplificada de xG:
    # ~0.30 por chute no alvo + ~0.05 por finalização fora do alvo
    xg_estimado = (chutes_no_alvo * 0.30) + (chutes_fora * 0.05)

    return {
        "gols": gols,
        "chutes_totais": chutes_totais,
        "chutes_no_alvo": chutes_no_alvo,
        "posse_pct": round(posse_pct, 1),
        "pontaria_pct": round(pontaria, 1),
        "conversao_pct": round(conversao, 1),
        "xg_estimado": round(xg_estimado, 2)
    }


if __name__ == "__main__":
    # Teste rápido
    time_a = calcular_metricas(gols=2, chutes_totais=14, chutes_no_alvo=6, posse_pct=58.0)
    time_b = calcular_metricas(gols=1, chutes_totais=8, chutes_no_alvo=3, posse_pct=42.0)

    print("--- Time A ---")
    print(time_a)
    print("--- Time B ---")
    print(time_b)

