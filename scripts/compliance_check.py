import yaml
import pandas as pd

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def load_data(file_path):
    return pd.read_excel(file_path)

def check_compliance(data, config):
    # Ensure the required columns exist
    if 'Requirement' not in data.columns or 'Value' not in data.columns:
        raise KeyError("The input data must contain 'Requirement' and 'Value' columns.")
    
    # Add a new 'Compliant' column based on whether each requirement meets the config criteria
    data['Compliant'] = data.apply(lambda row: row['Value'] == config.get(row['Requirement'], None), axis=1)
    return data

def save_report(data, output_path):
    data.to_excel(output_path, index=False)

if __name__ == "__main__":
    config = load_config('configs/grc_tool_config.yaml')
    data = load_data('examples/sample_compliance_data.xlsx')
    compliant_data = check_compliance(data, config)
    save_report(compliant_data, 'reports/compliance_report.xlsx')
    print("Results saved in reports/compliance_report.xlsx")
