import virustotal2
import os
import sys
import time
import json
from fpdf import FPDF

class vt_scan:

    def __init__(self, apikey, filepath):
        self.apikey = apikey
        self.filepath = filepath
        self.vt = virustotal2.VirusTotal(apikey)
        self.vt.set_verbose(False)

    def scan(self):
        try:
            self.vt.scan_file(self.filepath)
            time.sleep(60)
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['scans']
            self.report = self.report['Kaspersky']['result']
            if self.report == 'clean':
                return True
            else:
                return False
        except:
            return False
        
    def get_report(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['scans']
            self.report = self.report['Kaspersky']['result']
            return self.report
        except:
            return False
        
    def get_scan_id(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['scan_id']
            return self.report
        except:
            return False
        
    def get_scan_status(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['response_code']
            return self.report
        except:
            return False
        
    def get_scan_date(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['scan_date']
            return self.report
        except:
            return False
        
    def get_permalink(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['permalink']
            return self.report
        except:
            return False
        
    def get_verbose(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['verbose_msg']
            return self.report
        except:
            return False
        
    def get_sha256(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['sha256']
            return self.report
        except:
            return False
        
    def get_md5(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['md5']
            return self.report
        except:
            return False
        
    def get_sha1(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            self.report = self.report['sha1']
            return self.report
        except:
            return False

    def save_report(self, filepath):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            with open(filepath, 'w') as f:
                json.dump(self.report, f)
            return True
        except:
            return False
    
    def get_report_from_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.report = json.load(f)
            return self.report
        except:
            return False
        
    def print_json(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            print(json.dumps(self.report, indent=4, sort_keys=True))
        except:
            return False

    def print_report(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            print('\n\n\n')
            print('-'*40)
            print('VT Report for file: ' + self.filepath)
            print('-'*40)
            print('Scan ID: ' + self.report['scan_id'])
            print('Scan Date: ' + self.report['scan_date'])
            print('Report Link: ' + self.report['permalink'])
            print('Report Status: ' + self.report['response_code'])
            print('Report Verbose: ' + self.report['verbose_msg'])
            print('SHA256: ' + self.report['sha256'])
            print('MD5: ' + self.report['md5'])
            print('SHA1: ' + self.report['sha1'])
            print('Kaspersky: ' + self.report['Kaspersky']['result'])
            print('-'*40)
            print('\n\n\n')
        except:
            return False
    
    def print_report_pdf(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(40, 10, 'VT Report for file: ' + self.filepath)
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(40, 10, 'Scan ID: ' + self.report['scan_id'])
            pdf.cell(40, 10, 'Scan Date: ' + self.report['scan_date'])
            pdf.cell(40, 10, 'Report Link: ' + self.report['permalink'])
            pdf.cell(40, 10, 'Report Status: ' + self.report['response_code'])
            pdf.cell(40, 10, 'Report Verbose: ' + self.report['verbose_msg'])
            pdf.cell(40, 10, 'SHA256: ' + self.report['sha256'])
            pdf.cell(40, 10, 'MD5: ' + self.report['md5'])
            pdf.cell(40, 10, 'SHA1: ' + self.report['sha1'])
            pdf.cell(40, 10, 'Kaspersky: ' + self.report['Kaspersky']['result'])
            pdf.output('vt_report.pdf')
        except:
            return False
        
    def print_report_csv(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            with open('vt_report.csv', 'w') as f:
                f.write('VT Report for file: ' + self.filepath + '\n')
                f.write('Scan ID: ' + self.report['scan_id'] + '\n')
                f.write('Scan Date: ' + self.report['scan_date'] + '\n')
                f.write('Report Link: ' + self.report['permalink'] + '\n')
                f.write('Report Status: ' + self.report['response_code'] + '\n')
                f.write('Report Verbose: ' + self.report['verbose_msg'] + '\n')
                f.write('SHA256: ' + self.report['sha256'] + '\n')
                f.write('MD5: ' + self.report['md5'] + '\n')
                f.write('SHA1: ' + self.report['sha1'] + '\n')
                f.write('Kaspersky: ' + self.report['Kaspersky']['result'] + '\n')
        except:
            return False
        
    def print_report_html(self):
        try:
            self.report = self.vt.get_file_report(self.filepath)
            self.report = json.loads(self.report)
            with open('vt_report.html', 'w') as f:
                f.write('<html>\n')
                f.write('<head>\n')
                f.write('<title>VT Report for file: ' + self.filepath + '</title>\n')
                f.write('</head>\n')
                f.write('<body>\n')
                f.write('<h1>VT Report for file: ' + self.filepath + '</h1>\n')
                f.write('<h2>Scan ID: ' + self.report['scan_id'] + '</h2>\n')
                f.write('<h2>Scan Date: ' + self.report['scan_date'] + '</h2>\n')
                f.write('<h2>Report Link: ' + self.report['permalink'] + '</h2>\n')
                f.write('<h2>Report Status: ' + self.report['response_code'] + '</h2>\n')
                f.write('<h2>Report Verbose: ' + self.report['verbose_msg'] + '</h2>\n')
                f.write('<h2>SHA256: ' + self.report['sha256'] + '</h2>\n')
                f.write('<h2>MD5: ' + self.report['md5'] + '</h2>\n')
                f.write('<h2>SHA1: ' + self.report['sha1'] + '</h2>\n')
                f.write('<h2>Kaspersky: ' + self.report['Kaspersky']['result'] + '</h2>\n')
                f.write('</body>\n')
                f.write('</html>\n')
        except:
            return False
"""
EXAMPLE:

if __name__ == '__main__':
    apikey = os.environ['VT_API_KEY']
    filepath = sys.argv[1]
    vt = vt_scan(apikey, filepath)
    print(vt.scan())
    print(vt.get_report())
    print(vt.get_scan_id())
    print(vt.get_scan_status())
    print(vt.get_scan_date())
    print(vt.get_permalink())
    print(vt.get_verbose()) 
    print(vt.get_sha256())
    print(vt.get_md5())
    print(vt.get_sha1())
    print(vt.save_report('report.json'))
    print(vt.get_report_from_file('report.json'))
    print(vt.print_json())
    print(vt.print_report())
    print(vt.print_report_pdf())
    print(vt.print_report_csv())
    print(vt.print_report_html())
"""
