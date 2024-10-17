import os
from googletrans import Translator
import polib

# Directory containing the .po files
PO_DIR = "/mnt/c/Users/HP/Desktop/apimo_automation/languages"

# List of words or phrases to translate (in English)
target_phrases = ['hello']

# Initialize the translator
translator = Translator()

# Comprehensive language mapping
lang_mapping = {
    'ar': 'ar',       # Arabic
    'bg_BG': 'bg',    # Bulgarian
    'ca_ES': 'ca',    # Catalan
    'co': 'co',       # Corsican
    'cs_CZ': 'cs',    # Czech
    'da_DK': 'da',    # Danish
    'de_CH': 'de',    # German (Switzerland)
    'de_DE': 'de',    # German (Germany)
    'el_GR': 'el',    # Greek
    'en_GB': 'en',    # English (UK)
    'en_US': 'en',    # English (US)
    'es_CL': 'es',    # Spanish (Chile)
    'es_CR': 'es',    # Spanish (Costa Rica)
    'es_ES': 'es',    # Spanish (Spain)
    'es_PE': 'es',    # Spanish (Peru)
    'es_VE': 'es',    # Spanish (Venezuela)
    'fa_IR': 'fa',    # Persian
    'fi_FI': 'fi',    # Finnish
    'fr_BE': 'fr',    # French (Belgium)
    'fr_CH': 'fr',    # French (Switzerland)
    'fr_FR': 'fr',    # French (France)
    'he_IL': 'he',    # Hebrew
    'hu_HU': 'hu',    # Hungarian
    'it_IT': 'it',    # Italian
    'ja_JP': 'ja',    # Japanese
    'km_KH': 'km',    # Khmer
    'lb_LU': 'lb',    # Luxembourgish
    'lo_LA': 'lo',    # Lao
    'mn_MN': 'mn',    # Mongolian
    'ms_MY': 'ms',    # Malay
    'nb_NO': 'no',    # Norwegian Bokmål
    'nl_BE': 'nl',    # Dutch (Belgium)
    'nl_NL': 'nl',    # Dutch (Netherlands)
    'pl_PL': 'pl',    # Polish
    'pt_BR': 'pt',    # Portuguese (Brazil)
    'pt_PT': 'pt-pt', # Portuguese (Portugal)
    'ro_RO': 'ro',    # Romanian
    'ru_RU': 'ru',    # Russian
    'sv_SE': 'sv',    # Swedish
    'ta_IN': 'ta',    # Tamil
    'th_TH': 'th',    # Thai
    'tr_TR': 'tr',    # Turkish
    'uk_UA': 'uk',    # Ukrainian
    'zh_CN': 'zh-cn', # Chinese (Simplified)
}

def translate_phrase(phrase, target_lang):
    try:
        translation = translator.translate(phrase, dest=target_lang)
        return translation.text
    except Exception as e:
        print(f"Error translating '{phrase}' to {target_lang}: {e}")
        return phrase

def process_po_file(po_file_path):
    print(f"Processing {po_file_path}...")
    
    # Determine the target language from the filename
    file_name = os.path.basename(po_file_path)
    lang_code = file_name.split('-')[1].split('.')[0]
    
    # Get the target language code
    target_lang = lang_mapping.get(lang_code, lang_code.split('_')[0])

    # Load the .po file
    po = polib.pofile(po_file_path)

    # Add translations
    for phrase in target_phrases:
        if not any(entry.msgid == phrase for entry in po):
            translation = translate_phrase(phrase, target_lang)
            entry = polib.POEntry(
                msgid=phrase,
                msgstr=translation
            )
            po.append(entry)

    # Save the updated .po file
    po.save()

    # Compile .po to .mo
    mo_file_path = po_file_path.replace('.po', '.mo')
    po.save_as_mofile(mo_file_path)
    print(f"Compiled {po_file_path} to {mo_file_path}")

def main():
    for file_name in os.listdir(PO_DIR):
        if file_name.endswith('.po'):
            po_file_path = os.path.join(PO_DIR, file_name)
            process_po_file(po_file_path)

    print("All translations added and files compiled.")

if __name__ == "__main__":
    main()