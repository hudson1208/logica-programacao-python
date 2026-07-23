# ### Atividade 15 — Associação e ausência de valor

# Crie as variáveis:

# ```python
# curso = "Programação em Python"
# desconto = None
# ```

# Verifique:

# - se `"Python"` está presente em `curso`;
# - se `"Java"` não está presente em `curso`;
# - se `"programação"` está presente em `curso`;
# - se `desconto` é `None`;
# - se `desconto` não é `None`.

# Antes de executar, registre sua previsão para cada expressão.

curso = "Programação em Python"
desconto = None

print("Python está em curso?", "Python" in curso)
print("Java não está em curso?", "Java" not in curso)
print("programação está em curso?", "programação" in curso)
print("desconto é None?", desconto is None)
print("desconto não é None?", desconto is not None)