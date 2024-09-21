#!/usr/bin/env python

import argparse
from paperqa import Settings, ask, settings
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_answer_details(answer, verbosity=0):

    # Print the Question header in bold blue and the question text in blue
    print(Fore.CYAN + Style.BRIGHT + "Question:")
    print(Fore.BLUE + Style.NORMAL + answer.answer.question)

    # Print the Answer header in bold green and the answer text in green
    print(Fore.CYAN + Style.BRIGHT + "\nAnswer:")
    print(Fore.WHITE + Style.NORMAL + answer.answer.answer)

    if verbosity > 0:
        print(Fore.CYAN + Style.BRIGHT + "\nContexts Used:")
        for context in answer.answer.contexts:
            print(Fore.YELLOW + f"- {context.context} " + Fore.MAGENTA + f"(from {context.text.name})")

    # Print References header in bold magenta and the references text in magenta
    print(Fore.CYAN + Style.BRIGHT + "\nReferences:")
    print(Fore.MAGENTA + Style.NORMAL + answer.answer.references)

    print(Fore.CYAN + Style.BRIGHT + "\nToken Counts:")
    for model, tokens in answer.answer.token_counts.items():
        print(Fore.YELLOW + f"- {model}: " + Fore.GREEN + f"{tokens} tokens")

    print(Fore.CYAN + Style.BRIGHT + "\nCost:")
    print(Fore.GREEN + Style.NORMAL + f"${answer.answer.cost:.6f}")

    print(Fore.CYAN + Style.BRIGHT + "\nLLM Model Used:")
    print(Fore.GREEN + Style.NORMAL + ", ".join(answer.answer.token_counts.keys()))

    print(Fore.CYAN + Style.BRIGHT + "\nAgent Status:")
    print(Fore.GREEN + Style.NORMAL + answer.status.value)

    if answer.timing_info:
        print(Fore.CYAN + Style.BRIGHT + "\nTiming Information:")
        print(Fore.GREEN + Style.NORMAL + f"Duration: {answer.duration} seconds")



def main():
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description="Run a query with Paper-QA2")
    
    # Positional argument for the query
    parser.add_argument(
        'query', 
        type=str, 
        help='The query string to ask the model'
    )
    
    # Optional arguments with short and long forms
    parser.add_argument(
        '-p', '--paper_directory', 
        type=str, 
        default='.', 
        help='Directory containing the papers to be queried (default: current directory)'
    )
    
    parser.add_argument(
        '-l', '--llm', 
        type=str, 
        default='gpt-4o-mini', 
        choices=['gpt-4o', 'gpt-4o-mini', 'o1-preview', 'o1-mini'], 
        help='Select the language model to use:\n'
             '  gpt-4o: Our high-intelligence flagship model for complex, multi-step tasks. gpt-4o is cheaper and faster than gpt-4-turbo.\n'
             '  gpt-4o-mini (default): Our affordable and intelligent small model for fast, lightweight tasks. It is cheaper and more capable than gpt-3.5-turbo.\n'
             '  o1-preview: A reasoning model designed to solve hard problems across domains.\n'
             '  o1-mini: A faster and cheaper reasoning model particularly good at coding, math, and science.'
    )
    
    parser.add_argument(
        '-s', '--summary_llm', 
        type=str, 
        default='gpt-4o-mini', 
        choices=['gpt-4o', 'gpt-4o-mini', 'o1-preview', 'o1-mini'], 
        help='Select the summary language model to use:\n'
             '  gpt-4o: Our high-intelligence flagship model for complex, multi-step tasks. gpt-4o is cheaper and faster than gpt-4-turbo.\n'
             '  gpt-4o-mini (default): Our affordable and intelligent small model for fast, lightweight tasks. It is cheaper and more capable than gpt-3.5-turbo.\n'
             '  o1-preview: A reasoning model designed to solve hard problems across domains.\n'
             '  o1-mini: A faster and cheaper reasoning model particularly good at coding, math, and science.'
    )
    
    parser.add_argument(
        '-t', '--temperature', 
        type=float, 
        default=0.0, 
        help='Temperature setting for the model (controls creativity; default: 0.0)'
    )
    
    parser.add_argument(
        '-i', '--index_directory', 
        type=str, 
        default=None, 
        help='Directory for storing index files (default: uses built-in directory)'
    )
    
    parser.add_argument(
        '-r', '--index_recursively', 
        action='store_true', 
        default=False, 
        help='Index papers recursively in subdirectories (default: False)'
    )
    
    parser.add_argument(
        '-v', '--verbosity', 
        type=int, 
        default=0, 
        help='Verbosity level of the output (default: 0)'
    )
    
    parser.add_argument(
        '-e', '--evidence_summary_length', 
        type=str, 
        default='about 100 words', 
        help='Length of the evidence summary (default: "about 100 words")'
    )
    
    parser.add_argument(
        '-m', '--answer_max_sources', 
        type=int, 
        default=5, 
        help='Maximum number of sources for the answer (default: 5)'
    )
    
    parser.add_argument(
        '-a', '--answer_length', 
        type=str, 
        default='about 200 words, but can be longer', 
        help='Length of the generated answer (default: "about 200 words, but can be longer")'
    )
    
    args = parser.parse_args()

    # Set up the settings object
    ask_settings = Settings(
        llm=args.llm,
        summary_llm=args.summary_llm,
        temperature=args.temperature,
        index_directory=args.index_directory,
        index_recursively=args.index_recursively,
        verbosity=args.verbosity,
        paper_directory=args.paper_directory,
        answer=settings.AnswerSettings(
            evidence_summary_length=args.evidence_summary_length,
            answer_max_sources=args.answer_max_sources,
            answer_length=args.answer_length,
        )
    )

    # Run the query with the specified settings
    answer = ask(
        args.query,
        settings=ask_settings
    )

    # Print the answer
    print_answer_details(answer, args.verbosity)

if __name__ == '__main__':
    main()

