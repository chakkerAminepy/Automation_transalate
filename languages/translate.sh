#!/bin/bash

# Directory containing the .po files
PO_DIR="/mnt/c/Users/HP/Desktop/languages"



declare -A TRANSLATIONS_SELECT_CITY=(
    ["apimo-ar.po"]="اختر المدينة"
    ["apimo-bg_BG.po"]="Изберете град"
    ["apimo-ca_ES.po"]="Seleccionar ciudad"
    ["apimo-co.po"]="Selezionà cità"
    ["apimo-cs_CZ.po"]="Vyberte město"
    ["apimo-da_DK.po"]="Vælg by"
    ["apimo-de_CH.po"]="Stadt auswählen"
    ["apimo-de_DE.po"]="Stadt auswählen"
    ["apimo-el_GR.po"]="Επιλέξτε πόλη"
    ["apimo-en_GB.po"]="Select city"
    ["apimo-en_US.po"]="Select city"
    ["apimo-es_CL.po"]="Seleccionar ciudad"
    ["apimo-es_CR.po"]="Seleccionar ciudad"
    ["apimo-es_ES.po"]="Seleccionar ciudad"
    ["apimo-es_PE.po"]="Seleccionar ciudad"
    ["apimo-es_VE.po"]="Seleccionar ciudad"
    ["apimo-fa_IR.po"]="انتخاب شهر"
    ["apimo-fi_FI.po"]="Valitse kaupunki"
    ["apimo-fr_BE.po"]="Sélectionner la ville"
    ["apimo-fr_CH.po"]="Sélectionner la ville"
    ["apimo-fr_FR.po"]="Sélectionner la ville"
    ["apimo-he_IL.po"]="בחר עיר"
    ["apimo-hu_HU.po"]="Város kiválasztása"
    ["apimo-it_IT.po"]="Seleziona città"
    ["apimo-ja_JP.po"]="都市を選択"
    ["apimo-km_KH.po"]="ជ្រើសរើសទីក្រុង"
    ["apimo-nl_BE.po"]="Stad selecteren"
    ["apimo-nl_NL.po"]="Stad selecteren"
    ["apimo-pl_PL.po"]="Wybierz miasto"
    ["apimo-pt_BR.po"]="Selecionar cidade"
    ["apimo-pt_PT.po"]="Selecionar cidade"
    ["apimo-ro_RO.po"]="Selectați orașul"
    ["apimo-ru_RU.po"]="Выберите город"
    ["apimo-sv_SE.po"]="Välj stad"
    ["apimo-th_TH.po"]="เลือกเมือง"
    ["apimo-tr_TR.po"]="Şehir seçin"
    ["apimo-uk_UA.po"]="Виберіть місто"
    ["apimo-zh_CN.po"]="选择城市"
)

# Function to add translations and compile
process_po_file() {
    local po_file=$1
    
    echo "Processing $po_file..."

    # Add translations to the .po file if not already present
    
     if ! grep -q 'msgid "Select city"' "$po_file"; then
        echo -e '\nmsgid "Select city"\nmsgstr "'"${TRANSLATIONS_SELECT_CITY[$po_file]}"'"' >> "$po_file"
    fi

    # Compile .po to .mo
    local mo_file="${po_file%.po}.mo"
    msgfmt "$po_file" -o "$mo_file"
    echo "Compiled $po_file to $mo_file"
}

# Loop through all .po files in the directory
for po_file in "$PO_DIR"/*.po; do
    process_po_file "$(basename "$po_file")"
done

echo "All translations added and files compiled."