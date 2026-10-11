# Esse é um sistema de gerenciamento de Pokémons, a Pokedex.
# Onde o usúario(adestrador), adiciona o nome, tipo(elemento), e nível do seu pokémon.
# Consegue listar o nome, tipo e nível dentro da pokedex
# Se em alguma batalha acaba perdendo o pokémon, consegue remove-lo da pokedex
# Atualizar o nível se houver alguma evolução
# Registra quantas capturas houve explorando o mundo pokémon ou em batalhas
# E se precisar dos registros de captura de cada pokémon, é só solicitar a pokedex.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import datetime

app = FastAPI(
    title="Pokedex API",
)

# "Banco" em memória
pokedex = {}


# ---------- Schemas Pydantic ----------

class PokemonCreate(BaseModel):
    nome: str
    elemento: str
    nivel: int = Field(ge=1, le=100)   # valida 1 a 100 automaticamente


class NivelUpdate(BaseModel):
    novo_nivel: int = Field(ge=1, le=100)


class CapturaCreate(BaseModel):
    quantidade: int = Field(gt=0)      # tem que ser maior que zero


# ---------- Rotas ----------

@app.get("/health", tags=["Sistema"])
def health():
    """Verifica se a API está no ar."""
    return {"status": "ok"}


@app.post("/pokemon", tags=["Pokémon"])
def adicionar_pokemon(obj: PokemonCreate):
    nome = obj.nome.strip()
    if nome in pokedex:
        raise HTTPException(status_code=400, detail="Pokémon já cadastrado.")

    pokedex[nome] = {
        "elemento": obj.elemento,
        "nivel": obj.nivel,
        "total_capturas": 0,
        "capturas_historico": [],
    }
    return {"mensagem": f"Pokémon {nome} cadastrado com sucesso!"}


@app.get("/pokemon", tags=["Pokémon"])
def listar_pokemon():
    if not pokedex:
        return {"total": 0, "pokemons": []}

    lista = [
        {"nome": nome, "elemento": info["elemento"], "nivel": info["nivel"]}
        for nome, info in sorted(pokedex.items())
    ]
    return {"total": len(lista), "pokemons": lista}


@app.delete("/pokemon/{nome}", tags=["Pokémon"])
def remover_pokemon(nome: str):
    nome = nome.strip()
    if nome not in pokedex:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado.")
    del pokedex[nome]
    return {"mensagem": f"Pokémon '{nome}' removido com sucesso!"}


@app.put("/pokemon/{nome}/nivel", tags=["Pokémon"])
def atualizar_nivel(nome: str, obj: NivelUpdate):
    nome = nome.strip()
    if nome not in pokedex:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado.")
    pokedex[nome]["nivel"] = obj.novo_nivel
    return {"mensagem": f"Pokémon '{nome}' evoluiu para o nível {obj.novo_nivel}."}


@app.post("/pokemon/{nome}/captura", tags=["Capturas"])
def registrar_captura(nome: str, obj: CapturaCreate):
    nome = nome.strip()
    if nome not in pokedex:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado.")

    pokedex[nome]["total_capturas"] += obj.quantidade
    pokedex[nome]["capturas_historico"].append({
        "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "quantidade": obj.quantidade,
    })
    return {
        "mensagem": f"{obj.quantidade} captura(s) de {nome} registrada(s).",
        "total_capturas": pokedex[nome]["total_capturas"],
    }


@app.get("/pokemon/{nome}/historico", tags=["Capturas"])
def exibir_historico(nome: str):
    nome = nome.strip()
    if nome not in pokedex:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado.")

    historico = pokedex[nome]["capturas_historico"]
    if not historico:
        return {"pokemon": nome, "historico": []}

    return {"pokemon": nome, "historico": historico}