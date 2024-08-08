import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Now you can import from the scripts directory
from scripts.risk_assessment import load_data, assess_risks, save_report as save_risk_report
from scripts.compliance_check import load_config, check_compliance, save_report as save_compliance_report

def main():
    risk_data = load_data('examples/sample_risk_assessment.xlsx')
    assessed_risk_data = assess_risks(risk_data)
    save_risk_report(assessed_risk_data, 'reports/risk_assessment_report.xlsx')
    print("Results saved in reports/risk_assessment_report.xlsx")
    
    compliance_config = load_config('configs/grc_tool_config.yaml')
    compliance_data = load_data('examples/sample_compliance_data.xlsx')
    compliant_data = check_compliance(compliance_data, compliance_config)
    save_compliance_report(compliant_data, 'reports/compliance_report.xlsx')
    print("Results saved in reports/compliance_report.xlsx")
    
if __name__ == "__main__":
    main()
