import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)

def assess_risks(data):
    # Simple risk assessment logic
    data['Risk_Level'] = data['Impact'] * data['Likelihood']
    return data

def save_report(data, output_path):
    data.to_excel(output_path, index=False)

if __name__ == "__main__":
    data = load_data('examples/sample_risk_assessment.xlsx')
    assessed_data = assess_risks(data)
    save_report(assessed_data, 'reports/risk_assessment_report.xlsx')
    print("Results saved in reports/risk_assessment_report.xlsx")
