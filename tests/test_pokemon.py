import pytest

from pokemon import calcular_pontos_de_ataque, pokemon_evolui


def test_calcular_pontos_de_ataque():
    pokemon = {"forca_base": 10, "nivel": 1}
    assert calcular_pontos_de_ataque(pokemon) == 10
    pokemon = {"forca_base": 5, "nivel": 0} 
    assert calcular_pontos_de_ataque(pokemon) == 0
    pokemon = {"forca_base": 20, "nivel": 5} 
    assert calcular_pontos_de_ataque(pokemon) == 100

def test_pokemon_evolui():
    pokemon = {"nivel": 15} 
    nivel_evolucao = 20
    assert pokemon_evolui(pokemon, nivel_evolucao) == False
    pokemon = {"nivel": 20} 
    nivel_evolucao = 20
    assert pokemon_evolui(pokemon, nivel_evolucao) == True
    pokemon = {"nivel": 25} 
    nivel_evolucao = 20
    assert pokemon_evolui(pokemon, nivel_evolucao) == True