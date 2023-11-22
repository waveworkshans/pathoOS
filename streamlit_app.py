
import streamlit as st

import re
import time


def reformat_data(input_str):

    dates = re.findall(r'\d{2}-[A-Za-z]{3}-\d{2}', input_str)
    substring = input_str
    pattern = re.compile(r'(\d{1,3}\.\d|\d{1,3}|--)\s?(H|L)?\s?')
    output_data = []
    input_str = re.sub(r'\([^)]*\)', '', input_str)
    input_str = re.sub(r'Vitamin B12', 'Vitamin B', input_str)
    # print(input_str)
    if 'Haemoglobin' in input_str:
        names = []
        names.append(['Hb',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	155]) if 'Haemoglobin' in input_str else None
        names.append(['WCC',	r'(\d{1,2}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	12]) if 'White Cell Count' in input_str else None
        names.append(['PltC',	r'(\d{3}|--|See Below|HAEM)(\s(H|L))?\s?',	400]) if 'Platelet Count' in input_str else None
        names.append(['MCV',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	99]) if 'MCV' in input_str else None
        names.append(['RCC',	r'(\d{1}\.\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	5.2]) if 'RCC' in input_str else None
        names.append(['Hct',	r'(\d{1}\.\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	0.45]) if 'Hct' in input_str else None
        names.append(['MCH',	r'(\d{2}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	34]) if 'MCH' in input_str else None
        names.append(['MCHC',	r'(\d{3}|--|See Below|HAEM)(\s(H|L))?\s?',	365]) if 'MCHC' in input_str else None
        names.append(['RDW',	r'(\d{1,2}\.\d{1}|--)(\s(H|L))?\s?',	14]) if 'RDW' in input_str else None
        names.append(['Neut',	r'(\d{1,2}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	8]) if 'Neutrophils' in input_str else None
        names.append(['Lymph',	r'(\d{1}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	3.5]) if 'Lymphocytes' in input_str else None
        names.append(['Monocytes',	r'(\d{1}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	1]) if 'Monocytes' in input_str else None
        names.append(['Eosinophils',	r'(\d{1}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	0.5]) if 'Eosinophils' in input_str else None
        names.append(['Basophils',	r'(\d{1}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	0.2]) if 'Basophils' in input_str else None
        if 'HaemoglobinWhite' not in input_str:
            names.reverse()
        start_index = 0
        if 'HaemoglobinWhite' in input_str:
            start_index = input_str.find('HaemoglobinWhite')
        substring = input_str[start_index:]
        output_data1 = []
        output_data2 = []
        for i,j in enumerate(names):
            if j[0] == 'Folate' and 'HaemoglobinWhite' in input_str:
                start_index = input_str.find('Folate')
            output_data1.append([])
            for k in range(len(dates)):
                match = re.compile(j[1]).search(input_str, start_index)
                if match is None:
                    break
                # print(input_str[start_index:])
                start_index = match.span()[1]
                match_output = match.group(1)
                try:
                    if float(match.group(1)) > j[2] and match.group(2) is None and '.' not in match.group(1):
                        start_index -= 1
                        match_output = match.group(1)[:-1]
                except:
                    match_output = f'({match.group(1)})'
                    if match.group(1) == '--':
                        match_output = ''
                match_output = match_output + (match.group(2)[1:] + "*") if match.group(2) is not None else match_output
                output_data1[i].append(match_output)
            if 'HaemoglobinWhite' not in input_str:
                output_data1[i].reverse()
            output_data2.append(output_data1[i])
            # print(names[i][0] + str(output_data1[i]))
    elif 'Sodium' in input_str:
        names = []
        names.append(['Na',	r'(\d{3}|--|See Below|HAEM)(\s(H|L))?\s?',	145]) if 'Sodium' in input_str else None
        names.append(['K',	r'(\d{1}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	5.2]) if 'Potassium' in input_str else None
        names.append(['Cl',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	110]) if 'Chloride' in input_str else None
        names.append(['Bicarbonate',	r'(\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	32]) if 'Bicarbonate' in input_str else None
        names.append(['Ur',	r'(\d{1,2}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	9]) if 'Urea' in input_str else None
        names.append(['Cr',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	90]) if 'Creatinine' in input_str else None
        names.append(['eGFR',	r'(\d{2,3}|--|HAEM)(\s(H|L))?\s?',	999]) if 'eGFR' in input_str else None
        names.append(['Ca',	r'(\d{1}\.\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	2.6]) if 'Calcium' in input_str else None
        names.append(['CaCorrected',	r'(\d{1}\.\d{2}|--)(\s(H|L))?\s?',	2.6]) if 'Calcium Corrected' in input_str else None
        names.append(['Mg',	r'(\d{1}\.\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	1.1]) if 'Magnesium' in input_str else None
        names.append(['Phos',	r'(\d{1}\.\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	1.5]) if 'Phosphate' in input_str else None
        names.append(['Protein',	r'(\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	80]) if 'Total Protein' in input_str else None
        names.append(['Alb',	r'(\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	52]) if 'Albumin' in input_str else None
        names.append(['Glo',	r'(\d{2}|--|See Below|HAEM)(\s(H|L))?\s?',	40]) if 'Globulin' in input_str else None
        names.append(['Bil',	r'(\d{1,2}|--|See Below|HAEM)(\s(H|L))?\s?',	21]) if 'Bilirubin' in input_str else None
        names.append(['ALT',	r'(\d{1,2}|--|See Below|HAEM)(\s(H|L))?\s?',	35]) if 'ALT' in input_str else None
        names.append(['AST',	r'(\d{1,2}|--|See Below|HAEM)(\s(H|L))?\s?',	30]) if 'AST' in input_str else None
        names.append(['GGT',	r'(\d{1,2}|--|See Below|HAEM)(\s(H|L))?\s?',	35]) if 'GGT' in input_str else None
        names.append(['ALP',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	110]) if 'ALP' in input_str else None
        names.append(['CRP',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	999]) if 'CRP' in input_str else None
        names.append(['Fer',	r'(\d{2,3}|--|See Below|HAEM)(\s(H|L))?\s?',	300]) if 'Ferritin' in input_str else None
        names.append(['Iron',	r'(\d{1,3}|--|See Below|HAEM)(\s(H|L))?\s?',	32]) if 'Iron' in input_str else None
        names.append(['Transferrin',	r'(\d{1}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	3.6]) if 'Transferrin' in input_str else None
        names.append(['TransferrinSaturation',	r'(\d{1,2}|--|See Below|HAEM)(\s(H|L))?\s?',	45]) if 'Transferrin saturation' in input_str else None
        names.append(['VitB12',	r'(\d{3,4}|--|See Below|HAEM)(\s(H|L))?\s?',	698]) if 'Vitamin B' in input_str else None
        names.append(['Holotranscobalamin',	r'(\d{3}|--|See Below|HAEM)(\s(H|L))?\s?',	165]) if 'Holotranscobalamin' in input_str else None
        names.append(['Folate',	r'(\d{1,2}\.\d{1}|--|See Below|HAEM)(\s(H|L))?\s?',	99]) if 'Folate' in input_str else None
        if 'SodiumPotassium' not in input_str:
            names.reverse()
        start_index = 0
        if 'SodiumPotassium' in input_str:
            start_index = input_str.find('SodiumPotassium')
        substring = input_str[start_index:]
        output_data1 = []
        output_data2 = []
        for i,j in enumerate(names):
            if j[0] == 'Folate' and 'SodiumPotassium' in input_str:
                start_index = input_str.find('Folate')
            output_data1.append([])
            for k in range(len(dates)):
                match = re.compile(j[1]).search(input_str, start_index)
                if match is None:
                    break
                # print(input_str[start_index:])
                start_index = match.span()[1]
                match_output = match.group(1)
                try:
                    if float(match.group(1)) > j[2] and match.group(2) is None and '.' not in match.group(1):
                        start_index -= 1
                        match_output = match.group(1)[:-1]
                except:
                    match_output = f'({match.group(1)})'
                    if match.group(1) == '--':
                        match_output = ''
                match_output = match_output + (match.group(2)[1:] + "*") if match.group(2) is not None else match_output
                output_data1[i].append(match_output)
            if 'SodiumPotassium' not in input_str:
                output_data1[i].reverse()
            output_data2.append(output_data1[i])
            # print(names[i][0] + str(output_data1[i]))

    else:
        print('UNRECOGNIZED FORMATTING')
        exit(1)
    for i, j in enumerate(output_data2):
        output_data.append([names[i][0],j])
    if 'SodiumPotassium' not in input_str:
        dates.reverse()
        output_data.reverse()
    return dates, output_data

# Replace your main function with this
def main():
    st.title('Data Reformatter')
    # Sample input data
    input_data = st.text_area("Pathology input:", "Paste your data here...")
    
    # Check if input_data is not the placeholder
    if input_data and "Paste your data here..." not in input_data:
        # Reformat the data
        dates, output_data = reformat_data(input_data)
        if len(output_data) < 1:
            st.write("No data to display.")
            return
        results = ''
        for i, date in enumerate(dates):
            output_data_sub = ''
            for x in output_data:
                if x[1][i] != '':
                    output_data_sub += f"{x[0]}{x[1][i]}/"
            output_data_sub = f"({date})\n{output_data_sub[:-1]}\n"
            results += output_data_sub
        st.text('Output:')
        st.write(results)
    else:
        st.write("Please paste your data in the text area above.")

# Use Streamlit's way of running the app
if __name__ == "__main__":
    main()
