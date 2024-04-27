import streamlit as st
import pandas as pd
from io import StringIO
import io
import pdfplumber
import processEnggResult
import re
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, message=r"invalid escape sequence.*")
st.set_page_config(page_title="PDF to EXCEL")
st.title("UPLOAD ENGINEERING RESULT PDF")
try:
    result = subprocess.run(['nvidia-smi', '--query-gpu=index,name,utilization.gpu,memory.total,memory.used,memory.free', '--format=csv,noheader,nounits'], capture_output=True, text=True, check=True)
    gpu_stats = result.stdout.strip().split('\n')
    for stat in gpu_stats:
        print(stat)
except subprocess.CalledProcessError as e:
     st.write(e)
try:
    pdf = st.file_uploader("UPLOAD A FILE")

    if pdf:
        tables = []

        with pdfplumber.open(pdf) as a:
            for i, page in enumerate(a.pages):
                if i >= 2:
                    break
                table = page.extract_tables()
                tables.extend(table)

        if tables != []:
            data = processEnggResult.format2(pdf)
            a = data.to_csv().encode('utf-8')
            st.download_button("DOWNLOAD FILE", a, file_name="data.csv", mime="text/csv")

        else:
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
                st.download_button("DOWNLOAD FILE", a, file_name="final.csv", mime="text/csv")
            except Exception as e:
                st.error(e)
except Exception as e:
    st.error("PLEASE CHECK FORMAT OF GIVEN FILE!!!")
