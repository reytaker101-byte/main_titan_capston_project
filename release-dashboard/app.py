from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="AI-SRE Release Dashboard")


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI-SRE Release Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f5f6f8;
            }

            h1 {
                margin-bottom: 5px;
            }

            .subtitle {
                color: #666;
                margin-bottom: 30px;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                background: white;
            }

            th, td {
                padding: 16px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }

            th {
                background: #222;
                color: white;
            }

            .healthy {
                color: green;
                font-weight: bold;
            }

            .active {
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <h1>AI-SRE Release Dashboard</h1>

        <div class="subtitle">
            Kubernetes Release & Blue/Green Deployment Status
        </div>

        <table>
            <tr>
                <th>Service</th>
                <th>Environment</th>
                <th>Blue</th>
                <th>Green</th>
                <th>Active</th>
                <th>Status</th>
            </tr>

            <tr>
                <td>payment-service</td>
                <td>DEV</td>
                <td>v1.0.0</td>
                <td>-</td>
                <td class="active">Blue</td>
                <td class="healthy">HEALTHY</td>
            </tr>

            <tr>
                <td>payment-service</td>
                <td>STAGE</td>
                <td>v1.0.0</td>
                <td>v1.1.0</td>
                <td class="active">Blue</td>
                <td class="healthy">HEALTHY</td>
            </tr>

            <tr>
                <td>payment-service</td>
                <td>PROD</td>
                <td>v1.0.0</td>
                <td>-</td>
                <td class="active">Blue</td>
                <td class="healthy">HEALTHY</td>
            </tr>

        </table>

    </body>
    </html>
    """


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "release-dashboard"
    }
