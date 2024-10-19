"""
v0.0.1 

Not the best thing I have written, but it works
"""
import requests
import os
from flask import Flask


OUTPUT_DIR = 'generated'
IPO_PULSE_BASE_URL = os.environ["IPO_PULSE_BASE_URL"] 
API_URL = f"{IPO_PULSE_BASE_URL}/api/data"  # Using the provided API URL

def fetch_ipo_data():
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


def generate_html(ipo_data):
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google" content="notranslate"/>
    <meta name="google-adsense-account" content="ca-pub-4757594580756122">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IPO Pulse</title>
    <meta name="description" content="Welcome to IPO Pulse – Your comprehensive resource for the latest Initial Public Offering (IPO) information. Our platform provides detailed insights into upcoming IPOs, market trends, and performance analysis to help you make informed investment decisions. Stay updated with real-time alerts, expert analyses, and essential data that empower you to navigate the dynamic world of public offerings. Whether you're a seasoned investor or just starting out, IPO Pulse is your go-to hub for all things IPO.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.ipo.amgoyal.com/">
    <meta property="og:description" content="Welcome to IPO Pulse – Your comprehensive resource for the latest Initial Public Offering (IPO) information. Our platform provides detailed insights into upcoming IPOs, market trends, and performance analysis to help you make informed investment decisions. Stay updated with real-time alerts, expert analyses, and essential data that empower you to navigate the dynamic world of public offerings. Whether you're a seasoned investor or just starting out, IPO Pulse is your go-to hub for all things IPO.">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <style>
        .disclaimer {{
            font-size: 0.9rem;
            color: #888;
            margin-top: 20px;
            text-align: center;
        }}
        .table-container {{
            padding: 20px;
        }}
        .site-title {{
            text-align: center;
            margin-top: 20px;
        }}
    </style>
</head>
<body>

    <!-- Site Title -->
    <div class="container">
        <h1 class="site-title">IPO Pulse</h1>
    </div>

    <!-- Table -->
    <div class="container table-container">
        <div class="table-responsive">
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th>IPO</th>
                        <th>Status</th>

                        <th>Price</th>
                        <th>GMP (₹)</th>
                        <th>Est Listing</th>
                        
                        <th>Subscription</th>
                        
                        <th>Open</th>
                        <th>Close</th>
                        
                        <th>Allotment Dt</th>
                        <th>Listing Dt</th>
                        <th>Lot</th>
                        <th>IPO Size</th>
                        
                        <th>Last Updated</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    </div>

    <!-- Disclaimer -->
    <div class="container">
        <p class="disclaimer">
            Disclaimer: The information provided on this site is for informational purposes only, with no guarantee of accuracy or completeness. It may be incorrect or outdated.
        </p>
    </div>

    <!-- Bootstrap JS (Optional) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
    # Create table rows from the IPO data
    rows = ""
    for ipo in ipo_data:
        row = f"""
        <tr class="{ipo['meta']['row_class']}">

        
            <td>{ipo['IPO']}</td>
            <td>{ipo['status']}</td>
            
            <td>{ipo['Price']}</td>
            <td>{ipo['GMP(₹)']}</td>
            <td>{ipo['Est Listing']}</td>

            <td>{[str(ipo['subs'])+"x","NA"][ipo['subs']==None]}</td>
            
            
            <td>{ipo['Open']}</td>
            <td>{ipo['Close']}</td>
            <td>{ipo['BoA Dt']}</td>
            
            <td>{ipo['Listing']}</td>

            <td>{ipo['Lot']}</td>
            <td>{ipo['IPO Size']}</td>
            <td>{ipo['GMP Updated']}</td>
        </tr>
        """
        rows += row.strip() + "\n"

    # Fill the template with the rows
    html_content = html_template.format(rows=rows)
    return html_content


app = Flask(__name__)

@app.route('/api/html', methods=['GET'])
def get_data():
    ipo_data = fetch_ipo_data()
    return {"data": generate_html(ipo_data)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5679)
