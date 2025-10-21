import os

def converti_poesia():
    # Percorso della cartella dove si trova lo script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "text.txt")
    output_file = os.path.join(script_dir, "texthtml.txt")

    # Controlla se text.txt esiste
    if not os.path.isfile(input_file):
        print(f"❌ Errore: il file 'text.txt' non è stato trovato in {script_dir}")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()  # Mantiene gli a capo come righe separate
    except Exception as e:
        print(f"❌ Errore durante la lettura di 'text.txt': {e}")
        return

    # Genera un <p> per OGNI riga (anche vuota)
    html_lines = []
    for line in lines:
        # Escapa caratteri speciali per sicurezza HTML
        safe_line = (
            line
            .replace("&", "&amp;")
            .replace("<", "<")
            .replace(">", ">")
        )
        html_lines.append(f"<p>{safe_line}</p>")

    html_output = '<div id="allinea">\n' + "\n".join(html_lines) + '\n</div>'

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_output)
    except Exception as e:
        print(f"❌ Errore durante la scrittura di 'texthtml.txt': {e}")
        return

    print(f"✅ File HTML generato con successo!")
    print(f"📁 Percorso: {output_file}")
    print(f"📄 Numero di righe (inclusi spazi vuoti): {len(html_lines)}")

if __name__ == "__main__":
    converti_poesia()