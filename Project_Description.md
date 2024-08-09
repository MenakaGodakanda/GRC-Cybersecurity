# GRC Tool - Version 1

This project demonstrates a comprehensive understanding of Governance, Risk, and Compliance (GRC) in the field of cybersecurity. It includes scripts and tools to automate risk assessment and compliance checks, helping organizations manage risks and ensure adherence to regulatory requirements.

## Features

### 1. Risk Assessment
- **Data Loading**: The project provides a feature to load risk assessment data from Excel files. This allows the user to input a variety of data points related to potential risks, including factors like impact and likelihood.
- **Risk Evaluation**: The project calculates a risk level for each entry in the dataset based on the product of the impact and likelihood values. This simple yet effective risk scoring mechanism helps to prioritize risks.
- **Report Generation**: After assessing the risks, the project can save the evaluated data back into an Excel file. This report can then be used by stakeholders to understand and mitigate identified risks.

### 2. Compliance Check
- **Configuration Loading**: The project can load configuration data from a Excel file, which specifies the compliance requirements that must be checked. This makes the compliance checks adaptable to different regulatory frameworks and standards.
- **Compliance Verification**: The project verifies whether the data entries meet the specified requirements by comparing the actual values against the expected values in the configuration file.
- **Compliance Reporting**: Similar to the risk assessment, the project generates a compliance report in an Excel format. This report indicates which entries are compliant or non-compliant, making it easier to address gaps in compliance.

### 3. Modular Design
- **Script Modularity**: The project is designed with modularity in mind. Separate scripts (`risk_assessment.py`, `compliance_check.py`) handle different aspects of the GRC process. This not only makes the project easier to maintain but also allows for the addition of new features without disrupting existing functionalities.
- **Main Orchestrator**: The `grc_tool.py` script serves as the main orchestrator, coordinating the execution of both risk assessment and compliance checks. This design ensures a streamlined workflow for the user, where both tasks can be performed with a single command.

### 4. Customizable and Extendable
- **Customizable Configurations**: Through the use of Excel configuration files, the project allows users to define their own compliance requirements. This makes the tool adaptable to different organizations or regulatory standards.
- **Easy to Extend**: Given the modular nature of the project, new features or checks can be easily added. For instance, additional risk factors or compliance checks could be implemented without needing to rewrite the core functionality.

### 5. User-Friendly Output
- **Excel Reports**: The project outputs its results in widely-used Excel formats. This makes it easy for non-technical stakeholders to review and understand the results.
- **Clear Console Messages**: The project provides clear console messages indicating where the results have been saved. This immediate feedback is useful for ensuring that the process has completed successfully.


### 6. Open-Source Libraries
- **Pandas**: Used for handling data manipulation and analysis, making it easier to work with tabular data.
- **OpenPyXL**: Facilitates the reading and writing of Excel files, enabling the project to generate reports that are easy to share and understand.

### 7. Ease of Use
- **Minimal Setup**: The project is easy to set up and use, with clear instructions provided in the README.md file. The use of a virtual environment ensures that dependencies are managed correctly, reducing the risk of conflicts.
- **Automation**: The entire GRC process (risk assessment and compliance check) can be run with a single command, making it highly efficient and user-friendly.

### 8. Educational Value
- **Code Explanation**: Each script in the project is clearly explained, making it an excellent learning resource for those new to GRC in cybersecurity.
- **Step-by-Step Workflow**: The project guides the user through the entire GRC process, from data loading to report generation, providing a comprehensive understanding of how these concepts are applied in real-world scenarios.

## Coding

### Risk Assessment (`scripts/risk_assessment.py`)

#### 1. Imports
- **pandas**: The script starts by importing the `pandas` library, which is essential for data manipulation. In this script, `pandas` is used to read data from Excel files into DataFrames, perform operations on this data, and then save the modified data back to an Excel file.

#### 2. Function: `load_data`
- **Purpose**: This function reads data from an Excel file into a pandas DataFrame.
- **Parameters**:
  - **`file_path`**: The path to the Excel file to be loaded.
- **Functionality**:
  - **`pd.read_excel(file_path)`**: This pandas function reads the Excel file specified by `file_path` and returns its contents as a DataFrame.
- **Returns**: The DataFrame containing the data from the Excel file.
- If `file_path` is `'examples/sample_risk_assessment.xlsx'`, this function loads the data from this file into a DataFrame.

#### 3. Function: assess_risks
- **Purpose**: This function performs a basic risk assessment by calculating a "Risk_Level" for each item in the dataset.
- **Parameters**:
  - `data`: A pandas DataFrame containing the data to be assessed. The DataFrame is expected to have columns named `Impact` and `Likelihood`.
- **Functionality**:
  - `data['Risk_Level'] = data['Impact'] * data['Likelihood']`: This line creates a new column in the DataFrame called `Risk_Level`. It calculates the value of `Risk_Level` for each row by multiplying the `Impact` and `Likelihood` columns. This is a simple risk assessment method where risk is determined by the product of impact and likelihood.
- **Returns**: The DataFrame with the new `Risk_Level` column added.
- If a row in the DataFrame has `Impact = 3` and `Likelihood = 4`, the `Risk_Level` will be calculated as `12` (i.e., `3 * 4`).

#### 4. Function: save_report
- **Purpose**: This function saves the assessed DataFrame to an Excel file.
- **Parameters**:
  - `data`: The pandas DataFrame to be saved.
  - `output_path`: The path where the Excel file will be saved.
- **Functionality**:
  - `data.to_excel(output_path, index=False)`: This pandas function saves the DataFrame to an Excel file at the specified `output_path`. The `index=False` argument ensures that the row indices are not written to the file.
- If `output_path` is `'reports/risk_assessment_report.xlsx'`, this function saves the DataFrame to that file.

#### 5. Main Execution Block
- **Purpose**: This block is executed when the script is run directly (not imported as a module). It orchestrates the loading, assessing, and saving of the risk data.
- **Steps**:
  - **Load Data**:
    - `data = load_data('examples/sample_risk_assessment.xlsx')`
    - The script loads the data from the Excel file `'examples/sample_risk_assessment.xlsx'` into the `data` DataFrame.
  - **Assess Risks**:
    - `assessed_data = assess_risks(data)`
    - The script applies the risk assessment logic to the `data` DataFrame and stores the result in `assessed_data`.
  - **Save Report**:
    - `save_report(assessed_data, 'reports/risk_assessment_report.xlsx')`
    - The script saves the `assessed_data` DataFrame, including the newly added `Risk_Level` column, to `'reports/risk_assessment_report.xlsx'`.
  - **Print Confirmation**:
    - `print("Results saved in reports/risk_assessment_report.xlsx")`
    - A message is printed to the console to confirm that the results have been saved successfully.

### Compliance Check (`scripts/compliance_check.py`)

#### 1. Imports
- **pandas**: The script also imports `pandas`, which is used for data manipulation. In this script, `pandas` is used to read data from Excel files, perform compliance checks, and save the results back to an Excel file.

#### 2. Function: load_config
- **Purpose**: This function reads a Excel configuration file and returns its contents as a Python dictionary.
- **Parameters**:
  - `file_path`: The path to the Excel configuration file.
- **Functionality**:
  - The function opens the specified file in read mode.
  - `yaml.safe_load(file)`: This line parses the YAML file content and converts it into a Python dictionary.
- **Returns**: The configuration data as a dictionary.
- If file_path is `'configs/grc_tool_config.yaml'`, the function will return the contents of this YAML file as a dictionary.

#### 3. Function: load_data
- **Purpose**: This function reads data from an Excel file into a pandas DataFrame.
- **Parameters**:
  - `file_path`: The path to the Excel file to be loaded.
- **Functionality**:
  - `pd.read_excel(file_path)`: This pandas function reads the Excel file specified by `file_path` and returns its contents as a DataFrame.
- **Returns**: The DataFrame containing the data from the Excel file.
- If file_path is 'examples/sample_compliance_data.xlsx', this function loads the data from this file into a DataFrame.

#### 4. Function: check_compliance
- **Purpose**: This function checks each row in the data against the compliance criteria specified in the YAML configuration.
- **Parameters**:
  - `data`: A pandas DataFrame containing the data to be assessed. The DataFrame is expected to have columns named `Requirement` and `Value`.
  - `config`: A dictionary containing the compliance criteria, loaded from the YAML file.
- **Functionality**:
  - **Column Check**:
    - The script first checks if the DataFrame contains the necessary columns: `Requirement` and `Value`.
    - If either column is missing, a `KeyError` is raised with a relevant message.
  - **Compliance Check**:
    - The script adds a new column called `Compliant` to the DataFrame.
    - It uses the `apply` function to evaluate each row, checking if the `Value` in that row matches the expected value from the `config` dictionary for the corresponding `Requirement`.
    - `config.get(row['Requirement'], None)` retrieves the expected value for the `Requirement` from the `config` dictionary. If the requirement is not found in the dictionary, it defaults to `None`.
    - If the `Value` matches the expected value, the `Compliant` column is set to `True`; otherwise, it is set to `False`.
- **Returns**: The DataFrame with an additional `Compliant` column indicating whether each requirement is compliant.
- If a row has `Requirement = "Requirement1"` and `Value = "Yes"`, and the `config` dictionary specifies that `Requirement1` should have the value "Yes", the `Compliant` column for that row will be `True`.

#### 5. Function: save_report
- **Purpose**: This function saves the DataFrame (with compliance results) to an Excel file.
- **Parameters**:
  - `data`: The pandas DataFrame to be saved.
  - `output_path`: The path where the Excel file will be saved.
- **Functionality**:
  - `data.to_excel(output_path, index=False)`: This pandas function saves the DataFrame to an Excel file at the specified `output_path`. The `index=False` argument ensures that row indices are not written to the file.
- If `output_path` is `'reports/compliance_report.xlsx'`, this function saves the DataFrame to that file.

#### 6. Main Execution Block
- **Purpose**: This block is executed when the script is run directly (not imported as a module). It orchestrates the loading of configuration and data, checking of compliance, and saving of results.
- **Steps**:
  - **Load Configuration**:
    - `config = load_config('configs/grc_tool_config.yaml')`
    - The script loads the compliance criteria from the YAML file `'configs/grc_tool_config.yaml'`.
  - **Load Data**:
    - `data = load_data('examples/sample_compliance_data.xlsx')`
    - The script loads the data from the Excel file `'examples/sample_compliance_data.xlsx'` into a DataFrame.
  - **Check Compliance**:
    - `compliant_data = check_compliance(data, config)`
    - The script checks the compliance of each row in the DataFrame against the criteria in the configuration file and adds a `Compliant` column.
  - **Save Report**:
    - `save_report(compliant_data, 'reports/compliance_report.xlsx')`
    - The script saves the compliance results to `'reports/compliance_report.xlsx'`.
  - **Print Confirmation**:
    - `print("Results saved in reports/compliance_report.xlsx")`
    - A message is printed to the console to confirm that the results have been saved successfully.

### GRC Tool (`tools/grc_tool/grc_tool.py`)

The grc_tool.py script acts as the main orchestrator for running both risk assessment and compliance check processes within the GRC (Governance, Risk, and Compliance) project.

#### 1. Imports
- **sys**: This module provides access to some variables used or maintained by the Python interpreter. It is being used here to manipulate the Python path.
- **os**: This module provides a way of using operating system-dependent functionality like reading or writing to the file system. In this script, it is used to navigate and manage file paths.

#### 2. Adding the Root Directory to the Python Path
- **Purpose**: This line ensures that the root directory of the project is added to the Python path.
- **Explanation**:
  - `os.path.dirname(__file__)`: Gets the directory where `grc_tool.py` is located.
  - `os.path.join(os.path.dirname(__file__), '../../')`: Goes up two levels from the current directory (where `grc_tool.py` is located) to reach the root directory of the project.
  - `os.path.abspath()`: Converts the resulting path to an absolute path.
  - `sys.path.append()`: Adds the absolute path of the root directory to the Python path, allowing the script to import modules from anywhere within the project.
  - By adding the root directory to the Python path, the script ensures that it can import other modules (`risk_assessment.py` and `compliance_check.py`) from the `scripts` directory, no matter where the script is executed from.

#### 3. Importing Functions from Other Scripts
- **Purpose**: The script imports specific functions from the `risk_assessment.py` and `compliance_check.py` scripts.
- **Details**:
  - **From `risk_assessment.py`**:
    - `load_data`: Loads data from an Excel file.
    - `assess_risks`: Assesses risks based on the data.
    - `save_report`: Saves the assessed risk data to an Excel file. It is imported with an alias `save_risk_report` to differentiate it from the `save_report` function in `compliance_check.py`.
  - **From `compliance_check.py`**:
    - `load_config`: Loads the YAML configuration file.
    - `check_compliance`: Checks compliance based on the data and configuration.
    - `save_report`: Saves the compliance results to an Excel file, imported with an alias `save_compliance_report`.

#### 4. Main Function: main()
- **Purpose**: This function coordinates the execution of both risk assessment and compliance checks.
- **Steps**:
  - **Risk Assessment**:
    - **Load Risk Data**:
      - `risk_data = load_data('examples/sample_risk_assessment.xlsx')`
      - Loads data from an Excel file containing sample risk assessment data.
    - **Assess Risks**:
      - `assessed_risk_data = assess_risks(risk_data)`
      - Assesses the risks based on the loaded data by calculating a risk level.
    - **Save Risk Report**:
      - `save_risk_report(assessed_risk_data, 'reports/risk_assessment_report.xlsx')`
      - Saves the assessed risk data to an Excel file.
    - **Print Confirmation**:
      - `print("Results saved in reports/risk_assessment_report.xlsx")`
      - Prints a message to confirm that the risk assessment report has been saved.
  - **Compliance Check**:
    - **Load Compliance Configuration**:
      - `compliance_config = load_config('configs/grc_tool_config.yaml')`
      - Loads the YAML configuration file containing compliance requirements.
    - **Load Compliance Data**:
      - `compliance_data = load_data('examples/sample_compliance_data.xlsx')`
      - Loads data from an Excel file containing sample compliance data.
    - **Check Compliance**:
      - `compliant_data = check_compliance(compliance_data, compliance_config)`
      - Checks the compliance of the data against the requirements specified in the YAML file.
    - **Save Compliance Report**:
      - `save_compliance_report(compliant_data, 'reports/compliance_report.xlsx')`
      - Saves the compliance check results to an Excel file.
    - **Print Confirmation**:
      - `print("Results saved in reports/compliance_report.xlsx")`
      - Prints a message to confirm that the compliance report has been saved.

#### 5. Execution Block
- **Purpose**: This block ensures that the `main()` function is executed when the script is run directly (as opposed to being imported as a module).
- **Functionality**:
  - When the script is executed, it calls the `main()` function, which in turn performs the entire workflow of loading data, performing risk assessments, checking compliance, and saving the results to Excel files.
 
## Input and Output

### 1. Risk Assessment Script Output
- Below are the input and output of running the `scripts/risk_assessment.py` script.

- **Input File**: `examples/sample_risk_assessment.xlsx`
  ![Screenshot 2024-08-09 225654](https://github.com/user-attachments/assets/ac082d6f-bea6-458d-8429-05ec3bdd4eb0)

- **Output File**: `reports/risk_assessment_report.xlsx`
  ![Screenshot 2024-08-09 225720](https://github.com/user-attachments/assets/cdb52f89-3d63-485f-ac12-4fb0ee9cc90d)

- **Explanation**: The `Risk_Level` column is calculated as `Impact * Likelihood`. For `Risk 1`, the risk level is `5 * 2 = 10`, and for `Risk 2`, it is `3 * 4 = 12`.

### 2. Compliance Check Script Output
- Below are the input and output of running the `scripts/compliance_check.py` script.

- **Input File**: `examples/sample_compliance_data.xlsx`
  ![Screenshot 2024-08-09 224135](https://github.com/user-attachments/assets/e349c4ea-c461-4117-899e-acdb5ddcd4ec)

- **Input File**: `configs/grc_tool_config.xlsx`
  ![Screenshot 2024-08-09 224149](https://github.com/user-attachments/assets/9a6a4ed5-9cce-45ae-bd80-b69963a2572e)

- **Output File**: `reports/compliance_report.xlsx`
  ![Screenshot 2024-08-09 224215](https://github.com/user-attachments/assets/b72e6846-cab7-481c-89df-32497afde0dc)

- **Explanation**:
  - The `Compliant` column is calculated based on whether the `Value` matches the expected value in the configuration file.
  - Both `Requirement1` and `Requirement2` meet their compliance criteria.
  - However, Requirement3` and `Requirement4` do not meet their compliance criteria.

### 3. Integrated GRC Tool Output
- `tools/grc_tool/grc_tool.py` combines the functionalities of both risk assessment and compliance check.
- `grc_tool.py` will generate `risk_assessment_report.xlsx` and `compliance_report.xlsx` as above.
- **Final Output**:
  - **Risk Assessment Report**: Contains the results of the risk assessment, including calculated risk levels.
  - **Compliance Report**: Contains the results of the compliance check, indicating whether each requirement is met.
- **Output Files**:
  - `reports/risk_assessment_report.xlsx`
    ![Screenshot 2024-08-09 225720](https://github.com/user-attachments/assets/1943c889-eabb-4dcd-81ca-27a299c25a31)

  - `reports/compliance_report.xlsx`
    ![Screenshot 2024-08-09 224215](https://github.com/user-attachments/assets/c421ad66-b991-447d-99bd-c99cf9677f62)

- This integrated approach provides a comprehensive view of both risk and compliance, generating the necessary reports to assist in governance, risk management, and compliance tasks.
