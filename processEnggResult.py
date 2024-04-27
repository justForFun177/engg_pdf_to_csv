# good for only input(engg) file
import re
import pandas as pd
import PyPDF2
from io import StringIO
import io
import tabula
import pdfplumber

def get_ese_marks(singlePage, sem: int, sub: int):
    # abb for Abbreviations
    abb_ese = re.compile(f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\d+\s*\|(\d+)")
    match = abb_ese.search(singlePage)

    if match:
        abb_ese_marks = match.group(1)
    else:
        abb_ese_marks = ""
    return abb_ese_marks


def get_ise_marks(singlePage, sem: int, sub: int):
    abb_ise = re.compile(f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)")
    match = abb_ise.search(singlePage)

    if match:
        abb_ise_marks = match.group(1)
    else:
        abb_ise_marks = ""
    return abb_ise_marks


def get_ica_marks(singlePage, sem: int, sub: int):
    abb_ica = re.compile(
        f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)"
    )
    match = abb_ica.search(singlePage)

    if match:
        abb_ica_marks = match.group(1)
    else:
        abb_ica_marks = ""
    return abb_ica_marks


def get_poe_marks(singlePage, sem: int, sub: int):
    abb_poe = re.compile(
        f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)"
    )
    match = abb_poe.search(singlePage)
    if match:
        abb_poe_marks = match.group(1)
    else:
        abb_poe_marks = ""
    return abb_poe_marks


def get_total_marks(singlePage, sem: int, sub: int):
    subject_total = re.compile(
        f"BTN06{sem}0{sub}\s*\|\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|(\d+)\s*\|--\s*\|(\d+)"
    )
    subMatch = subject_total.search(singlePage)
    if subMatch:
        sub_total_marks = subMatch.group(2)
    else:
        sub_total_marks = ""
    return sub_total_marks


def get_sts(singlePage, sem: int, sub: int):
    subject_sts = re.compile(
        f"BTN06{sem}0{sub}\s*\|\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|\d+\s*\|--\s*\|\d+\s*\|\S\s*\|\s*\d+\.\d+\|\s*\d+\.\d+\|\s*(\w)"
    )
    subMatch = subject_sts.search(singlePage)
    if subMatch:
        sub_sts_value = subMatch.group(1)
    else:
        sub_sts_value = ""
    return sub_sts_value


def sem3Data(singlePage):
    sub1_ese_marks = get_ese_marks(singlePage, 3, 1)
    sub2_ese_marks = get_ese_marks(singlePage, 3, 2)
    sub3_ese_marks = get_ese_marks(singlePage, 3, 3)
    sub4_ese_marks = get_ese_marks(singlePage, 3, 4)
    sub5_ese_marks = get_ese_marks(singlePage, 3, 5)
    sub6_ese_marks = get_ese_marks(singlePage, 3, 6)

    sub1_ise_marks = get_ise_marks(singlePage, 3, 1)
    sub2_ise_marks = get_ise_marks(singlePage, 3, 2)
    sub3_ise_marks = get_ise_marks(singlePage, 3, 3)
    sub4_ise_marks = get_ise_marks(singlePage, 3, 4)
    sub5_ise_marks = get_ise_marks(singlePage, 3, 5)
    sub6_ise_marks = get_ise_marks(singlePage, 3, 6)

    sub1_ica_marks = get_ica_marks(singlePage, 3, 1)
    sub2_ica_marks = get_ica_marks(singlePage, 3, 2)
    sub3_ica_marks = get_ica_marks(singlePage, 3, 3)
    sub4_ica_marks = get_ica_marks(singlePage, 3, 4)
    sub5_ica_marks = get_ica_marks(singlePage, 3, 5)
    sub6_ica_marks = get_ica_marks(singlePage, 3, 6)

    sub1_poe_marks = get_poe_marks(singlePage, 3, 1)
    sub2_poe_marks = get_poe_marks(singlePage, 3, 2)
    sub3_poe_marks = get_poe_marks(singlePage, 3, 3)
    sub4_poe_marks = get_poe_marks(singlePage, 3, 4)
    sub5_poe_marks = get_poe_marks(singlePage, 3, 5)
    sub6_poe_marks = get_poe_marks(singlePage, 3, 6)

    sub1_total_marks = get_total_marks(singlePage, 3, 1)
    sub2_total_marks = get_total_marks(singlePage, 3, 2)
    sub3_total_marks = get_total_marks(singlePage, 3, 3)
    sub4_total_marks = get_total_marks(singlePage, 3, 4)
    sub5_total_marks = get_total_marks(singlePage, 3, 5)
    sub6_total_marks = get_total_marks(singlePage, 3, 6)

    sub1_sts_value = get_sts(singlePage, 3, 1)
    sub2_sts_value = get_sts(singlePage, 3, 2)
    sub3_sts_value = get_sts(singlePage, 3, 3)
    sub4_sts_value = get_sts(singlePage, 3, 4)
    sub5_sts_value = get_sts(singlePage, 3, 5)
    sub6_sts_value = get_sts(singlePage, 3, 6)

    total_pattern = re.compile(
        r"Sem-III\s*Total Credit: (\d+\.\d+).*?EGP: (\d+\.\d+).*?SGPA: (\d+\.\d+)"
    )
    total_match = total_pattern.search(singlePage)

    if total_match:
        total_credit = float(total_match.group(1))
        egp = float(total_match.group(2))
        sgpa = total_match.group(3)
    else:
        total_credit = ""
        egp = ""
        sgpa = ""

    return {
        "BTN06301": {
            "ESE": sub1_ese_marks,
            "ISE": sub1_ise_marks,
            "ICA": sub1_ica_marks,
            "POE": sub1_poe_marks,
            "Total": sub1_total_marks,
            "Sts": sub1_sts_value,
        },
        "BTN06302": {
            "ESE": sub2_ese_marks,
            "ISE": sub2_ise_marks,
            "ICA": sub2_ica_marks,
            "POE": sub2_poe_marks,
            "Total": sub2_total_marks,
            "Sts": sub2_sts_value,
        },
        "BTN06303": {
            "ESE": sub3_ese_marks,
            "ISE": sub3_ise_marks,
            "ICA": sub3_ica_marks,
            "POE": sub3_poe_marks,
            "Total": sub3_total_marks,
            "Sts": sub3_sts_value,
        },
        "BTN06304": {
            "ESE": sub4_ese_marks,
            "ISE": sub4_ise_marks,
            "ICA": sub4_ica_marks,
            "POE": sub4_poe_marks,
            "Total": sub4_total_marks,
            "Sts": sub4_sts_value,
        },
        "BTN06305": {
            "ESE": sub5_ese_marks,
            "ISE": sub5_ise_marks,
            "ICA": sub5_ica_marks,
            "POE": sub5_poe_marks,
            "Total": sub5_total_marks,
            "Sts": sub5_sts_value,
        },
        "BTN06306": {
            "ESE": sub6_ese_marks,
            "ISE": sub6_ise_marks,
            "ICA": sub6_ica_marks,
            "POE": sub6_poe_marks,
            "Total": sub6_total_marks,
            "Sts": sub6_sts_value,
        },
        "Total_Credit": total_credit,
        "EGP": egp,
        "SGPA": sgpa,
    }


def sem4Data(singlePage):
    sub1_ese_marks = get_ese_marks(singlePage, 4, 1)
    sub2_ese_marks = get_ese_marks(singlePage, 4, 2)
    sub3_ese_marks = get_ese_marks(singlePage, 4, 3)
    sub4_ese_marks = get_ese_marks(singlePage, 4, 4)
    sub5_ese_marks = get_ese_marks(singlePage, 4, 5)
    sub6_ese_marks = get_ese_marks(singlePage, 4, 6)

    sub1_ise_marks = get_ise_marks(singlePage, 4, 1)
    sub2_ise_marks = get_ise_marks(singlePage, 4, 2)
    sub3_ise_marks = get_ise_marks(singlePage, 4, 3)
    sub4_ise_marks = get_ise_marks(singlePage, 4, 4)
    sub5_ise_marks = get_ise_marks(singlePage, 4, 5)
    sub6_ise_marks = get_ise_marks(singlePage, 4, 6)

    sub1_ica_marks = get_ica_marks(singlePage, 4, 1)
    sub2_ica_marks = get_ica_marks(singlePage, 4, 2)
    sub3_ica_marks = get_ica_marks(singlePage, 4, 3)
    sub4_ica_marks = get_ica_marks(singlePage, 4, 4)
    sub5_ica_marks = get_ica_marks(singlePage, 4, 5)
    sub6_ica_marks = get_ica_marks(singlePage, 4, 6)

    sub1_poe_marks = get_poe_marks(singlePage, 4, 1)
    sub2_poe_marks = get_poe_marks(singlePage, 4, 2)
    sub3_poe_marks = get_poe_marks(singlePage, 4, 3)
    sub4_poe_marks = get_poe_marks(singlePage, 4, 4)
    sub5_poe_marks = get_poe_marks(singlePage, 4, 5)
    sub6_poe_marks = get_poe_marks(singlePage, 4, 6)

    sub1_total_marks = get_total_marks(singlePage, 4, 1)
    sub2_total_marks = get_total_marks(singlePage, 4, 2)
    sub3_total_marks = get_total_marks(singlePage, 4, 3)
    sub4_total_marks = get_total_marks(singlePage, 4, 4)
    sub5_total_marks = get_total_marks(singlePage, 4, 5)
    sub6_total_marks = get_total_marks(singlePage, 4, 6)

    sub1_sts_value = get_sts(singlePage, 4, 1)
    sub2_sts_value = get_sts(singlePage, 4, 2)
    sub3_sts_value = get_sts(singlePage, 4, 3)
    sub4_sts_value = get_sts(singlePage, 4, 4)
    sub5_sts_value = get_sts(singlePage, 4, 5)
    sub6_sts_value = get_sts(singlePage, 4, 6)

    # calculation for BTNENV ese ise total
    subenv_ese = re.compile(f"BTNENV\s*\|\S\S\s*\|\d+\s*\|(\d+)")
    subenv_ese_match = subenv_ese.search(singlePage)

    if subenv_ese_match:
        subenv_ese_marks = subenv_ese_match.group(1)
    else:
        subenv_ese_marks = ""

    subenv_ise = re.compile(f"BTNENV\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)")
    subenv_ise_match = subenv_ise.search(singlePage)

    if subenv_ise_match:
        subenv_ise_marks = subenv_ise_match.group(1)
    else:
        subenv_ise_marks = ""

    subenv_total = re.compile(
        f"BTNENV\s*\|\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|(\d+)\s*\|--\s*\|(\d+)"
    )
    subenv_total_match = subenv_total.search(singlePage)

    if subenv_total_match:
        subenv_total_marks = subenv_total_match.group(2)
    else:
        subenv_total_marks = ""

    total_pattern = re.compile(
        r"Sem-IV\s*Total Credit: (\d+\.\d+).*?EGP: (\d+\.\d+).*?SGPA: (\d+\.\d+)"
    )
    total_match = total_pattern.search(singlePage)
    if total_match:
        total_credit = total_match.group(1)
        egp = total_match.group(2)
        sgpa = total_match.group(3)
    else:
        total_credit = ""
        egp = ""
        sgpa = ""

    return {
        "BTN06401": {
            "ESE": sub1_ese_marks,
            "ISE": sub1_ise_marks,
            "ICA": sub1_ica_marks,
            "POE": sub1_poe_marks,
            "Total": sub1_total_marks,
            "Sts": sub1_sts_value,
        },
        "BTN06402": {
            "ESE": sub2_ese_marks,
            "ISE": sub2_ise_marks,
            "ICA": sub2_ica_marks,
            "POE": sub2_poe_marks,
            "Total": sub2_total_marks,
            "Sts": sub2_sts_value,
        },
        "BTN06403": {
            "ESE": sub3_ese_marks,
            "ISE": sub3_ise_marks,
            "ICA": sub3_ica_marks,
            "POE": sub3_poe_marks,
            "Total": sub3_total_marks,
            "Sts": sub3_sts_value,
        },
        "BTN06404": {
            "ESE": sub4_ese_marks,
            "ISE": sub4_ise_marks,
            "ICA": sub4_ica_marks,
            "POE": sub4_poe_marks,
            "Total": sub4_total_marks,
            "Sts": sub4_sts_value,
        },
        "BTN06405": {
            "ESE": sub5_ese_marks,
            "ISE": sub5_ise_marks,
            "ICA": sub5_ica_marks,
            "POE": sub5_poe_marks,
            "Total": sub5_total_marks,
            "Sts": sub5_sts_value,
        },
        "BTN06406": {
            "ESE": sub6_ese_marks,
            "ISE": sub6_ise_marks,
            "ICA": sub6_ica_marks,
            "POE": sub6_poe_marks,
            "Total": sub6_total_marks,
            "Sts": sub6_sts_value,
        },
        "BTNENV": {
            "ESE": subenv_ese_marks,
            "ISE": subenv_ise_marks,
            "Total": subenv_total_marks,
        },
        "Total_Credit": total_credit,
        "EGP": egp,
        "SGPA": sgpa,
    }


def singlePageData(singlePage):
    # college_code_pattern = re.compile(r"College Code:\s*([^\s]+)")
    # college_code = college_code_pattern.search(singlePage).group(1)

    seat_no_pattern = re.compile(r"Seat No:\s*([^\s]+)")
    seat_match = seat_no_pattern.search(singlePage)
    if seat_match:
        seat_no = seat_match.group(1)
    else:
        seat_no = ""

    prn_no_pattern = re.compile(r"PRN:\s*(\d+)")
    prn_no_match = prn_no_pattern.search(singlePage)
    if prn_no_match:
        prn_no = prn_no_match.group(1)
    else:
        prn_no = ""

    name_pattern = re.compile(r"Name:\s*([^(\n]+)")
    name_match = name_pattern.search(singlePage)
    if name_match:
        name = name_match.group(1).strip()
    else:
        name = ""

    sem3_data = sem3Data(singlePage)
    sem4_data = sem4Data(singlePage)

    overall_status_pattern = re.compile(r"\|Status:\s*(\w+)\s*\|C")
    overall_status_match = overall_status_pattern.search(singlePage)
    if overall_status_match:
        overall_status = overall_status_match.group(1)
    else:
        overall_status = ""

    percentage_match = re.compile(r"\|Percentage:\s*(\d+\.\d+)\s*\%").search(singlePage)
    if percentage_match:
        percentage = percentage_match.group(1)
    else:
        percentage = ""

    return {
        "Exam_Seat_No": seat_no,
        "PRN_No": prn_no,
        "Name": name,
        "Sem3": sem3_data,
        "Sem4": sem4_data,
        "Status": overall_status,
        "Percentage": percentage,
    }


def extract_data_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    data_list = []
    for page_num in range(2, len(reader.pages)):
        single_page = reader.pages[page_num].extract_text()
        data = singlePageData(single_page)
        data_list.append(data)
    return data_list



def format2(pdf):

    tables = []
    with pdfplumber.open(pdf) as pdf:
        for page in pdf.pages:
            table = page.extract_tables()
            tables.extend(table)

    # Combine all tables into a single dataframe
    combined_table = None
    for table in tables:
        if combined_table is None:
            combined_table = table
        else:
            combined_table.extend(table)


    result = []
    for i in range(1, len(tables[0])):
        if "BTN" in tables[0][i][0]:
            result.append(tables[0][i][0])
        else:
            break
    subjectCode = sorted(list(set(result)))

    header = ["Exam Seat No.", "PRN No.", "Name of Student"]
    for i in subjectCode:
        for j in range(6):
            header.append(i)
    header.append("Total Credit")
    header.append("EGP")
    header.append("SGPA")
    header.append("Status")
    header.append("Percentage")
    b = ["", "", ""] + "ESE	ISE	ICA	POE	Total Sts".split() * len(
        subjectCode) + ["", "", "", "", ""]
    c = pd.DataFrame(columns=[header,b])

    index = 0

    for i in range(3, len(tables)):
        text = tables[i][0][0]
        seat_match = re.search(r'SeatNo:(\d+)', text)
        seat_match2 = re.search(r'Seat No:\s*(\d+)', text)
        prn_match = re.search(r'PRN:\s*(\d+)', text)
        name_match = re.search(r'Name:\s*([\w\s]+)', text)

        seat_no = seat_match.group(1) if seat_match else seat_match2.group(1)
        prn = prn_match.group(1) if prn_match else None
        name = name_match.group(1) if name_match else None

        c.at[index, 'Exam Seat No.'] = seat_no
        c.at[index, 'PRN No.'] = prn
        c.at[index, 'Name of Student'] = name

        codes = subjectCode.copy()
        for j in range(len(tables[i][3])):
            for code in codes:
                if tables[i][j][0] == code:
                    flag = subjectCode.index(code)
                    c.iloc[index, 3 + flag * 6] = tables[i][j][3]
                    c.iloc[index, 4 + flag * 6] = tables[i][j][5]
                    c.iloc[index, 5 + flag * 6] = tables[i][j][7]
                    c.iloc[index, 6 + flag * 6] = tables[i][j][9]
                    c.iloc[index, 7 + flag * 6] = tables[i][j][12]
                    c.iloc[index, 8 + flag * 6] = tables[i][j][16]
                    codes.remove(code)
                    break
        s = tables[i][len(tables[i]) - 2][0]

        total_credit_match = re.search(r'Total Credit:\s*(\d+)', s)
        total_credit_match2 = re.search(r'TotalCredit:(\d+)', s)
        egp_match = re.search(r'EGP:\s*([\d.]+)', s)
        sgpa_match = re.search(r'SGPA:\s*([\d.]+)', s)
        status_match = re.search(r'Status:\s*([\w]+)', s)

        total_credit = total_credit_match.group(1) if total_credit_match else total_credit_match2.group(1)
        egp = egp_match.group(1) if egp_match else None
        sgpa = sgpa_match.group(1) if sgpa_match else None
        status = status_match.group(1) if status_match else None

        c.at[index, 'Total Credit'] = total_credit
        c.at[index, 'EGP'] = egp
        c.at[index, 'SGPA'] = sgpa
        c.at[index, 'Status'] = status

        s = tables[i][len(tables[i]) - 1][0]
        percentage_match = re.search(r'Percentage:\s*([\d.]+)\s*%', s)
        percentage = percentage_match.group(1) if percentage_match else None
        c.at[index, 'Percentage'] = percentage

        index += 1

    return c
