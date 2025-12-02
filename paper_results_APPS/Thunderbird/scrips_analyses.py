import re
import os

def analyze_test_script(file_path, core_function_keywords=None):

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    loc_total = len(lines)
    loc_executable = sum(1 for line in lines if line.strip() and not line.strip().startswith('//'))

    content = ''.join(lines)

    # Regex patterns
    test_pattern = re.compile(r'@Test\b')
    onview_pattern = re.compile(r'onView\s*\(')
    perform_pattern = re.compile(r'\.perform\s*\(')

    # Count elements
    num_tests = len(test_pattern.findall(content))
    num_onview = len(onview_pattern.findall(content))
    num_perform = len(perform_pattern.findall(content))

    # Check if functionality keyword appears (optional)
    covers_functionality = False
    if core_function_keywords:
        covers_functionality = any(kw.lower() in content.lower() for kw in core_function_keywords)

    # Results
    results = {
        "Test Cases (@Test)": num_tests,
        "UI Interactions (onView)": num_onview,
        "User Actions (perform)": num_perform,
        "Total Lines (LOC)": loc_total,
        "Executable LOC": loc_executable,
        "Covers Main Functionality": covers_functionality
    }

    return results


def analyze_all_scripts_in_folder(folder_path, core_keywords):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Ajuste para outras extensões se necessário
            file_path = os.path.join(folder_path, filename)

            # Analisar script
            results = analyze_test_script(file_path, core_keywords)

            # Criar nome do arquivo de saída baseado no script
            name_base = os.path.splitext(filename)[0]
            output_filename = f"script_analysis_{name_base}.txt"
            output_path = os.path.join(folder_path, output_filename)

            # Salvar resultado
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"=== GUI Test Script Analysis for {filename} ===\n")
                for key, value in results.items():
                    f.write(f"{key}: {value}\n")

            print(f"✅ Saved analysis: {output_path}")


if __name__ == "__main__":
    # Caminhos das pastas dos modelos (altere conforme seus diretórios)
    folders = [
    #r"C:\Users\nayse\Downloads\experiments\ARTIGO\Thunderbird\results\PRONTO\ChatGPT\script_promt",
    #r"C:\Users\nayse\Downloads\experiments\ARTIGO\Thunderbird\results\PRONTO\Claude\script_promt",
    #r"C:\Users\nayse\Downloads\experiments\ARTIGO\Thunderbird\results\PRONTO\Gemini\script_promt"
    r"C:\Users\nayse\Downloads\experiments\ARTIGO\Thunderbird\results\PRONTO\gemma12b\script_promt"
]

    core_keywords = [
    "open navigation drawer",
    "search for email",
    "filter or sort emails",
    "load more emails",
    "compose new email",
    "open overflow menu"
]


    for folder in folders:
        analyze_all_scripts_in_folder(folder, core_keywords)
