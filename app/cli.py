import requests
import sys
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

class SupportBotCLI:
    def __init__(self):
        self.api_url = "http://localhost:8000"
        self.console = Console()

    def display_welcome(self):
        welcome_text = """
        🤖 Welcome to Local AI Support Bot CLI! 🤖
        
        You can:
        - Ask questions using: ask <your question>
        - Upload documents using: upload <file_path>
        - Get help using: help
        - Exit using: exit
        
        Example commands:
        - ask What is the weather like?
        - upload documents/example.pdf
        - help
        - exit
        """
        self.console.print(Panel(welcome_text, title="Support Bot", border_style="blue"))

    def display_help(self):
        help_text = """
        Available Commands:
        - help: Show this help message
        - upload <file_path>: Upload a document
          Example: upload documents/example.pdf
        - ask <question>: Ask a question to the bot
          Example: ask What is the weather like?
        - exit: Exit the program
        """
        self.console.print(Panel(help_text, title="Help", border_style="green"))

    def upload_document(self, file_path):
        if not os.path.exists(file_path):
            self.console.print(f"[red]Error: File {file_path} does not exist[/red]")
            return

        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(f"{self.api_url}/upload", files=files)
                if response.status_code == 200:
                    self.console.print("[green]Document uploaded successfully![/green]")
                else:
                    self.console.print(f"[red]Error uploading document: {response.text}[/red]")
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def ask_question(self, question):
        if not question:
            self.console.print("[red]Error: Please provide a question[/red]")
            return

        try:
            response = requests.get(f"{self.api_url}/query", params={"question": question})
            if response.status_code == 200:
                result = response.json()
                if "error" in result:
                    self.console.print(f"[red]Error: {result['error']}[/red]")
                else:
                    answer = result.get("answer", "No answer received")
                    self.console.print(Panel(answer, title="Bot's Response", border_style="yellow"))
            else:
                self.console.print(f"[red]Error: {response.text}[/red]")
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def run(self):
        self.display_welcome()
        
        while True:
            try:
                user_input = Prompt.ask("\n[bold blue]Enter your command[/bold blue]")
                
                if user_input.lower() == 'exit':
                    self.console.print("[yellow]Goodbye! 👋[/yellow]")
                    break
                
                elif user_input.lower() == 'help':
                    self.display_help()
                
                elif user_input.lower().startswith('upload '):
                    file_path = user_input[7:].strip()
                    if not file_path:
                        self.console.print("[red]Error: Please provide a file path[/red]")
                        continue
                    self.upload_document(file_path)
                
                elif user_input.lower().startswith('ask '):
                    question = user_input[4:].strip()
                    if not question:
                        self.console.print("[red]Error: Please provide a question[/red]")
                        continue
                    self.ask_question(question)
                
                else:
                    self.console.print("[yellow]Unknown command. Type 'help' for available commands.[/yellow]")
            
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Goodbye! 👋[/yellow]")
                break
            except Exception as e:
                self.console.print(f"[red]Error: {str(e)}[/red]")

if __name__ == "__main__":
    cli = SupportBotCLI()
    cli.run() 