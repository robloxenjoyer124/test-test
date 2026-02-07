from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from contextlib import contextmanager

console = Console()

def print_header(title: str, subtitle: str = ""):
    """Prints a styled header."""
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_row(
        Panel(
            Text(title, justify="center", style="bold cyan"),
            subtitle=Text(subtitle, style="italic magenta"),
            style="blue",
            border_style="bright_blue",
        )
    )
    console.print(grid)
    console.print()

def print_success(message: str):
    """Prints a success message."""
    console.print(f"[bold green]✔[/bold green] {message}")

def print_error(message: str):
    """Prints an error message."""
    console.print(f"[bold red]✖[/bold red] {message}")

def print_warning(message: str):
    """Prints a warning message."""
    console.print(f"[bold yellow]![/bold yellow] {message}")

def print_info(message: str):
    """Prints an info message."""
    console.print(f"[bold blue]ℹ[/bold blue] {message}")

def create_table(title: str, columns: list[str]) -> Table:
    """Creates a configured Rich Table."""
    table = Table(title=title, show_header=True, header_style="bold magenta")
    for col in columns:
        table.add_column(col, style="cyan")
    return table

def print_table(table: Table):
    """Prints a Rich Table."""
    console.print(table)

@contextmanager
def status_spinner(text: str):
    """Context manager for a spinner."""
    with console.status(f"[bold green]{text}[/bold green]", spinner="dots"):
        yield
