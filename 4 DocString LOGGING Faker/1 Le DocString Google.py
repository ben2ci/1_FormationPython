# File -> Settings -> Tools -> Python Integrated Tolls -> DocString Format

def fonction_docString(description, auteur):
    """
    Args:
        description: documentation string
        auteur:      Python

    Returns:
        str: auteur and description
    """
    return f'{auteur}: {description}'


fonction_docString("Livre blanc", "Ben")

print(fonction_docString.__doc__)
help(fonction_docString)