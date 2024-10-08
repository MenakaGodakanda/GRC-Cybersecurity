# Comprehensive Governance, Risk, and Compliance (GRC) Tool for Cybersecurity
This project demonstrates a comprehensive understanding of Governance, Risk, and Compliance (GRC) in the field of cybersecurity. It includes scripts and tools to automate risk assessment and compliance checks, helping organizations manage risks and ensure adherence to regulatory requirements.<br>
<a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/Project_Description.md">Project Description</a>

## Overview
<img width="1106" alt="Screenshot 2024-08-08 at 11 20 28 PM" src="https://github.com/user-attachments/assets/fffd5168-dacd-4c4f-af38-e1692128b767">

### Explanation:

#### 1. Governance:
- `Governance.md` explains governance in cybersecurity and covers topics like policy creation, roles, and responsibilities.

#### 2. Risk Management:
- `Risk_Management.md` explains risk management frameworks and methodologies.

#### 3. Compliance:
- `Compliance.md` explains compliance standards (e.g., ISO 27001, GDPR).

#### 4. GRC Tool:
- `grc_tool.py` integrates risk assessment and compliance check functionalities.
- Produces final reports that cover both risk assessment and compliance.

## Step 1: Setting Up the Project

### 1. Clone the repository:
```bash
git clone https://github.com/MenakaGodakanda/GRC-Cybersecurity.git
cd GRC-Cybersecurity
```

### 2. Set Up Python Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
![Screenshot 2024-08-08 223802](https://github.com/user-attachments/assets/da58ec98-f923-47ca-9516-1fbc99c9b100)

### 3. Install Required Libraries:

**Pandas**:
- `pandas` is a powerful open-source data analysis and manipulation library for Python.
- It provides data structures like DataFrames and Series, which allow for efficient handling, cleaning, and analysis of structured data.
- In this GRC project, `pandas` is used to load, manipulate, and process data from Excel files.
- Specifically, it reads data from the Excel sheets, applies compliance checks, performs risk assessments, and generates reports in the form of new Excel files.
- The library's DataFrame structure is particularly useful for filtering and evaluating rows of data based on the compliance criteria defined in the configuration files.

**Openpyxl**:
- `openpyxl` is a Python library used to read and write Excel 2010 `.xlsx` files.
- It provides a flexible way to interact with Excel files, allowing for the creation, reading, editing, and formatting of spreadsheets.
- `openpyxl` is used by `pandas` under the hood to handle the reading and writing of Excel files.
- When the project scripts load data from an Excel file, `pandas` uses `openpyxl` to interface with the `.xlsx` format.
- Similarly, when generating reports (e.g., compliance and risk assessment reports), `pandas` leverages `openpyxl` to save the results back into an Excel format that can be easily shared and reviewed.

#### Install Libraries:
```
pip install -r tools/grc_tool/requirements.txt
```
![Screenshot 2024-08-08 223835](https://github.com/user-attachments/assets/eed8a68a-52a5-4586-888b-39b03b9c5ed1)

## Step 2: Usage
### 1. Running the Risk Assessment:
- To perform a risk assessment, run the following script:
```bash
python scripts/risk_assessment.py
```
- This will generate a report in `reports/risk_assessment_report.xlsx`.
![Screenshot 2024-08-08 223700](https://github.com/user-attachments/assets/cee19806-8d8c-490a-8e3b-44e4f4565d98)


### 2. Running the Compliance Check:
- To check compliance against the configuration, run the following script:
```bash
python scripts/compliance_check.py
```
- This will generate a report in `reports/compliance_report.xlsx`.
![Screenshot 2024-08-08 223707](https://github.com/user-attachments/assets/663e09ae-8e59-4516-b87f-3d88698a380a)

### 3. Running the Integrated GRC Tool:
- To run both the risk assessment and compliance check together, use the integrated tool:
```bash
python tools/grc_tool/grc_tool.py
```
- This will generate both reports in the `reports/` directory.
![Screenshot 2024-08-08 223712](https://github.com/user-attachments/assets/195abb28-65b4-4f36-9d53-5303d666255a) <br><br>
![Screenshot 2024-08-08 223733](https://github.com/user-attachments/assets/6468952c-5c39-4e1c-9939-932fbcb1f26e)

### 4. Demonstration
- A detail explanation of output is demonstrated in the <a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/Project_Description.md">Project Description</a> under `Input and Output` section.

## Example Files
- **Risk Assessment Data**: `examples/sample_risk_assessment.xlsx`
- **Compliance Data**: `examples/sample_compliance_data.xlsx`
- **Compliance Configuration**: `configs/grc_tool_config.xlsx`

## Documentation
- Detailed explanations and examples for each component are available in the `docs/` directory:
  - <a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/docs/Introduction.md">Introduction</a>
  - <a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/docs/Governance.md">Governance</a>
  - <a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/docs/Risk_Management.md">Risk Management</a>
  - <a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/docs/Compliance.md">Compliance</a>
  - <a href="https://github.com/MenakaGodakanda/GRC-Cybersecurity/blob/main/docs/Conclusion.md">Conclusion</a>

## Project Structure
```
GRC-Cybersecurity/
├── configs
│   └── grc_tool_config.xlsx      # Configuration file for compliance checks
├── docs
│   ├── Introduction.md           # Introduction to the project
│   ├── Governance.md             # Governance concepts and examples
│   ├── Risk_Management.md        # Risk management concepts and script explanation
│   ├── Compliance.md             # Compliance concepts and script explanation
│   └── Conclusion.md             # Conclusion and key takeaways
├── examples
│   ├── sample_risk_assessment.xlsx   # Example data for risk assessment
│   └── sample_compliance_data.xlsx   # Example data for compliance check
├── reports
│   ├── risk_assessment_report.xlsx   # Generated risk assessment report
│   └── compliance_report.xlsx        # Generated compliance report
├── scripts
│   ├── risk_assessment.py        # Script for risk assessment
│   └── compliance_check.py       # Script for compliance check
├── tools
│   └── grc_tool
│       ├── grc_tool.py           # Integrated tool to run risk assessment and compliance check
│       └── requirements.txt      # Python dependencies for the tool
└── README.md                     # Project overview and instructions
```

## License
This project is licensed under the MIT License.
