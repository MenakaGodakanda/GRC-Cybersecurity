import pandas as pd

def load_config(file_path):
    return pd.read_excel(file_path)

def load_data(file_path):
    return pd.read_excel(file_path)

def check_compliance(data, config):
    # Ensure the required columns exist
    if 'Requirement' not in data.columns or 'Value' not in data.columns:
        raise KeyError("The input data must contain 'Requirement' and 'Value' columns.")
    
    # Add a new 'Compliant' column based on whether each requirement meets the config criteria
    data['Compliant'] = data.apply(lambda row: row['Value'] == config.loc[config['Requirement'] == row['Requirement'], 'Value'].values[0] 
                                   if not config.loc[config['Requirement'] == row['Requirement'], 'Value'].empty 
                                   else False, axis=1)
    return data

def save_report(data, output_path):
    data.to_excel(output_path, index=False)

if __name__ == "__main__":
    # Load configuration and data
    config = load_config('configs/grc_tool_config.xlsx')
    data = load_data('examples/sample_compliance_data.xlsx')
    
    # Check compliance
    compliant_data = check_compliance(data, config)
    
    # Save and print the compliance report
    save_report(compliant_data, 'reports/compliance_report.xlsx')
    print("Results saved in reports/compliance_report.xlsx")
