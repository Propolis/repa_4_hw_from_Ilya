from rich import print as rprint

def change_name(name):
    result = ""
    for i in range(len(name)):
        if i % 2 == 1:
            result += name[i].upper()
        else:
            result += name[i].lower()
    return result

def greet(name):
    rprint(f"[bold magenta]Hello[/bold magenta] [cyan]{name}[/cyan] :sparkles:")
