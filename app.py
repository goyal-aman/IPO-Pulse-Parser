"""
v0.0.1 

Not the best thing I have written, but it works
"""
import requests


# API URL
api_url = "http://192.168.1.2:5678/api/data"  # Using the provided API URL

def fetch_ipo_data():
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


def generate_html(ipo_data):
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IPO Pulse</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
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
                        <th>GMP (₹)</th>
                        <th>Price</th>

                        <th>Est Listing</th>
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
        print(ipo)
        row = f"""
                  
        <tr>
            <td>{ipo['IPO']}</td>
            <td>{ipo['GMP(₹)']}</td>
            
            <td>{ipo['Price']}</td>
            <td>{ipo['Est Listing']}</td>
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

    # Write to an HTML file
    with open("ipo_pulse.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    try:
        ipo_data = fetch_ipo_data()
        generate_html(ipo_data)
        print("HTML file generated successfully: ipo_pulse.html")
    except Exception as e:
        print(f"An error occurred: {e}")
