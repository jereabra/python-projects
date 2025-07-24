import pytest
import src.logic as logic

def test_agregar_mostrar(monkeypatch, capsys):
    turnos=[]
    respuestas = iter(["María", "150", "25", "H", "B"])
    monkeypatch.setattr('builtins.input', lambda prompt=None: next(respuestas))

    resultado=logic.agregar_turnos(turnos)

    assert len(resultado)==1

    nuevo = resultado[0]
    assert nuevo["nombre"] == "María"
    assert nuevo["edad"] == 25
    assert nuevo["especialidad"] == "Cardiología"

    logic.mostrar_turnos(turnos)

    #lee consola
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert any("Estos son los turnos que hay en el momento:" ==line for line in output_lines), output_lines
    assert any("1 . María 25 Cardiología" ==line for line in output_lines), output_lines
    return

def test_filtrar(monkeypatch, capsys):
    turnos = [
        {"nombre": "Ana", "edad": 30, "especialidad": "Clínica"},
        {"nombre": "Luis", "edad": 45, "especialidad": "Cardiología"}
    ]

    respuestas1 = iter(["d", "B"])
    monkeypatch.setattr('builtins.input', lambda prompt=None: next(respuestas1))
    logic.filtrar_por_especialidad(turnos)
    resultado1=capsys.readouterr()
    output_lines1=resultado1.out.strip().splitlines()

    assert any("Seleccione una letra entre la lista" ==line for line in output_lines1), output_lines1

    respuestas2 = iter(["150", "40", "d", "a"])
    monkeypatch.setattr('builtins.input', lambda prompt=None: next(respuestas2))
    logic.filtrar_mayores(turnos)
    resultado2=capsys.readouterr()
    output_lines2=resultado2.out.strip().splitlines()

    assert any("1 . Luis 45 Cardiología" ==line for line in output_lines2), output_lines2


