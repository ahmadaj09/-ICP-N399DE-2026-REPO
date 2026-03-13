
import json, csv, os
from datetime import datetime
from jinja2 import Template

class ReportGenerator:

    def __init__(self,target):
        self.target = target
        self.time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.dir = "reports"
        os.makedirs(self.dir,exist_ok=True)

    def path(self,ext):
        safe=self.target.replace(".","_")
        return f"{self.dir}/scan_{safe}_{self.time}.{ext}"

    def txt(self,data,duration):
        p=self.path("txt")
        with open(p,"w") as f:
            f.write("PortSleuth Scan Report\n")
            f.write(f"Target: {self.target}\n")
            f.write(f"Duration: {duration}\n\n")
            for r in data:
                f.write(f"{r['port']} {r['service']} {r['risk']} {r['banner']}\n")
        return p

    def json(self,data,duration):
        p=self.path("json")
        with open(p,"w") as f:
            json.dump(data,f,indent=2)
        return p

    def csv(self,data,duration):
        p=self.path("csv")
        with open(p,"w",newline="") as f:
            w=csv.writer(f)
            w.writerow(["Port","Service","Risk","Banner"])
            for r in data:
                w.writerow([r['port'],r['service'],r['risk'],r['banner']])
        return p

    def html(self,data,duration):
        p=self.path("html")
        template="""
        <html>
        <head>
        <title>PortSleuth Report</title>
        <style>
        body{font-family:Arial}
        table{border-collapse:collapse;width:80%}
        td,th{border:1px solid #333;padding:8px}
        </style>
        </head>
        <body>
        <h1>Port Scan Report</h1>
        <p>Target: {{target}}</p>
        <table>
        <tr><th>Port</th><th>Service</th><th>Risk</th><th>Banner</th></tr>
        {% for r in data %}
        <tr>
        <td>{{r.port}}</td>
        <td>{{r.service}}</td>
        <td>{{r.risk}}</td>
        <td>{{r.banner}}</td>
        </tr>
        {% endfor %}
        </table>
        </body>
        </html>
        """
        html=Template(template).render(target=self.target,data=data)
        open(p,"w").write(html)
        return p
