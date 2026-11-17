import json
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados.json"
ALUNO_DA_SESSAO = "M001"


def consultar_matricula():
    dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return dados[ALUNO_DA_SESSAO]


def solicitar_cancelamento():
    dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    matricula = dados[ALUNO_DA_SESSAO]
    if matricula["status"] != "ativa":
        return {"resultado": "A matrícula não está ativa."}
    if matricula["cancelamento_solicitado"]:
        return {"resultado": "Já existe uma solicitação de cancelamento registrada."}

    print(f"Solicitação: {matricula['aluno']} / {matricula['curso']}.")
    print(
        "Será registrada para análise da secretaria. Não cancela nem reembolsa "
        "automaticamente."
    )
    confirmacao = input("Digite CONFIRMAR para registrar, ou Enter para desistir: ")
    if confirmacao.strip() != "CONFIRMAR":
        return {"resultado": "Solicitação descartada, sem alteração nos dados."}

    matricula["cancelamento_solicitado"] = True
    ARQUIVO.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    return {
        "resultado": "Solicitação registrada para análise da secretaria.",
        "matricula": matricula,
    }
