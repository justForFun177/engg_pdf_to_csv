import streamlit as st
import copy
import pandas as pd
from io import StringIO
import io
import processEnggResult
import tabula
import re
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, message=r"invalid escape sequence.*")

st.title("UPLOAD ENGINEERING RESULT PDF")

pdf = st.file_uploader("UPLOAD A FILE")

if pdf:
    pdf2 = copy.copy(pdf)
    check_table = tabula.read_pdf(pdf, pages="3-10", multiple_tables=True)
    name_pattern = r'Name:\s*([\w\s]+)'
    prn_pattern = r'PRN:\s*(\d+)'
    seat_pattern = r'Seat No:\s*(\d+)'
    flag = 0
    for i in range(len(check_table)):
        pattern = check_table[i].columns[0]
        if re.search(name_pattern, pattern) and re.search(prn_pattern, pattern) and re.search(seat_pattern, pattern):
            flag = 1
            break

    if flag==1:
        tables = tabula.read_pdf(pdf2, pages="all", multiple_tables=True)

        name_pattern = r'Name:\s*([\w\s]+)'
        prn_pattern = r'PRN:\s*(\d+)'
        seat_pattern = r'Seat No:\s*(\d+)'
        total_credit_pattern = r'Total Credit:\s*(\d+)'
        egp_pattern = r'EGP:\s*([\d.]+)'
        sgpa_pattern = r'SGPA:\s*([\d.]+)'
        status_pattern = r'Status:\s*([\w]+)'
        percentage_pattern = r'Percentage:\s*([\d.]+)\s*%'

        a = ["Exam Seat No.", "PRN No.", "Name of Student"] + ["BTN06301"] * 6 + ["BTN06302"] * 6 + ["BTN06303"] * 6 + [
            "BTN06304"] * 6 + ["BTN06305"] * 6 + [
                "BTN06306"] * 6 + [""] * 5
        b = ["", "", ""] + "ESE	ISE	ICA	POE	Total Sts".split() * 6 + [
            "Total Credit", "EGP", "SGPA", "Status", "Percentage"]
        c = pd.DataFrame(columns=[a, b])

        index = 0
        for i in range(len(tables) - 1):
            pattern = tables[i].columns[0]
            if re.search(name_pattern, pattern) and re.search(prn_pattern, pattern) and re.search(seat_pattern,
                                                                                                  pattern):
                # Search for matches using regex
                name_match = re.search(name_pattern, pattern)
                prn_match = re.search(prn_pattern, pattern)
                seat_match = re.search(seat_pattern, pattern)

                # Extract information if matches are found, else assign empty strings
                name = name_match.group(1)  # if name_match else ''
                prn = prn_match.group(1)  # if prn_match else ''
                seat_no = seat_match.group(1)  # if seat_match else ''

                c.at[index, 'Exam Seat No.'] = seat_no
                c.at[index, 'PRN No.'] = prn
                c.at[index, 'Name of Student'] = name
                print(i)
                c.iloc[index, 3] = tables[i].iloc[1, 3]
                c.iloc[index, 4] = tables[i].iloc[1, 5]
                c.iloc[index, 5] = tables[i].iloc[1, 7]
                c.iloc[index, 6] = tables[i].iloc[1, 9]
                c.iloc[index, 7] = tables[i].iloc[1, 12]
                c.iloc[index, 8] = tables[i].iloc[1, 16]

                c.iloc[index, 9] = tables[i].iloc[3, 3]
                c.iloc[index, 10] = tables[i].iloc[3, 5]
                c.iloc[index, 11] = tables[i].iloc[3, 7]
                c.iloc[index, 12] = tables[i].iloc[3, 9]
                c.iloc[index, 13] = tables[i].iloc[3, 12]
                c.iloc[index, 14] = tables[i].iloc[3, 16]

                c.iloc[index, 15] = tables[i].iloc[6, 3]
                c.iloc[index, 16] = tables[i].iloc[6, 5]
                c.iloc[index, 17] = tables[i].iloc[6, 7]
                c.iloc[index, 18] = tables[i].iloc[6, 9]
                c.iloc[index, 19] = tables[i].iloc[6, 12]
                c.iloc[index, 20] = tables[i].iloc[6, 16]

                c.iloc[index, 21] = tables[i].iloc[9, 3]
                c.iloc[index, 22] = tables[i].iloc[9, 5]
                c.iloc[index, 23] = tables[i].iloc[9, 7]
                c.iloc[index, 24] = tables[i].iloc[9, 9]
                c.iloc[index, 25] = tables[i].iloc[9, 12]
                c.iloc[index, 26] = tables[i].iloc[9, 16]

                c.iloc[index, 27] = tables[i].iloc[12, 3]
                c.iloc[index, 28] = tables[i].iloc[12, 5]
                c.iloc[index, 29] = tables[i].iloc[12, 7]
                c.iloc[index, 30] = tables[i].iloc[12, 9]
                c.iloc[index, 31] = tables[i].iloc[12, 12]
                c.iloc[index, 32] = tables[i].iloc[12, 16]

                c.iloc[index, 33] = tables[i].iloc[16, 3]
                c.iloc[index, 34] = tables[i].iloc[16, 5]
                c.iloc[index, 35] = tables[i].iloc[16, 7]
                c.iloc[index, 36] = tables[i].iloc[16, 9]
                c.iloc[index, 37] = tables[i].iloc[16, 12]
                c.iloc[index, 38] = tables[i].iloc[16, 16]

                input_string = tables[i].iloc[17, 0]
                total_credit_match = re.search(total_credit_pattern, input_string)
                egp_match = re.search(egp_pattern, input_string)
                sgpa_match = re.search(sgpa_pattern, input_string)
                status_match = re.search(status_pattern, input_string)
                total_credit = total_credit_match.group(1) if total_credit_match else ''
                egp = egp_match.group(1) if egp_match else ''
                sgpa = sgpa_match.group(1) if sgpa_match else ''
                status = status_match.group(1) if status_match else ''

                c.iloc[index, 39] = total_credit
                c.iloc[index, 40] = egp
                c.iloc[index, 41] = sgpa
                c.iloc[index, 42] = status

                input_string = tables[i].iloc[18, 0]
                percentage_match = re.search(percentage_pattern, input_string)
                percentage = percentage_match.group(1) if percentage_match else ''
                c.iloc[index, 43] = percentage

                index += 1

        a = c.to_csv().encode('utf-8')
        st.download_button("DOWNLOAD FILE",a, file_name="data.csv", mime="text/csv")

    else :
        try:
            data_list = processEnggResult.extract_data_from_pdf(pdf)

            html_head = """
            <thead>
                <tr>
                    <td rowspan="3">Exam Seat No.</td>
                    <td rowspan="3">PRN No.</td>
                    <td rowspan="3">Name of Student</td>
                    <td colspan="39">Sem 3</td>
                    <td colspan="42">Sem 4</td>
                    <td rowspan="3">Status</td>
                    <td rowspan="3">Percentage</td>
                </tr>
                <tr>
                    <td colspan="6">BTN06301</td>
                    <td colspan="6">BTN06302</td>
                    <td colspan="6">BTN06303</td>
                    <td colspan="6">BTN06304</td>
                    <td colspan="6">BTN06305</td>
                    <td colspan="6">BTN06306</td>
                    <td rowspan="2">Total Credit</td>
                    <td rowspan="2">EGP</td>
                    <td rowspan="2">SGPA</td>
                    <td colspan="6">BTN06401</td>
                    <td colspan="6">BTN06402</td>
                    <td colspan="6">BTN06403</td>
                    <td colspan="6">BTN06404</td>
                    <td colspan="6">BTN06405</td>
                    <td colspan="6">BTN06406</td>
                    <td colspan="3">BTNENV</td>
                    <td rowspan="2">Total Credit</td>
                    <td rowspan="2">EGP</td>
                    <td rowspan="2">SGPA</td>
                </tr>
                <tr>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>ICA</td>
                    <td>POE</td>
                    <td>Total</td>
                    <td>Sts</td>
                    <td>ESE</td>
                    <td>ISE</td>
                    <td>Total</td>
                </tr>
            </thead>
            """

            all_data = ""
            for student in data_list:
                one_row = ""
                one_row += f"<td>{student['Exam_Seat_No']}</td>"
                one_row += f"<td>{student['PRN_No']}</td>"
                one_row += f"<td>{student['Name']}</td>"

                for i in ["Sem3", "Sem4"]:
                    for data in student[i]:
                        # Check if the value is a dictionary before iterating over it
                        if isinstance(student[i][data], dict):
                            for abb in student[i][data]:
                                one_row += f"<td>{student[i][data][abb]}</td>"
                        else:
                            one_row += f"<td>{student[i][data]}</td>"

                one_row += f"<td>{student['Status']}</td>"
                one_row += f"<td>{student['Percentage']}</td>"
                all_data += f"<tr>{one_row}</tr>"

            table = f"<table>{html_head}<tbody>{all_data}</tbody></table>"
            result = pd.read_html(StringIO(table))


            a = result[0].to_csv().encode('utf-8')
            st.download_button("DOWNLOAD FILE",a, file_name="final.csv", mime="text/csv")
        except Exception as e:
            st.error(e)

