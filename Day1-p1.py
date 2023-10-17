import pandas as pd

data = {
    "DEPARTMENT_ID": [
        10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270
    ],
    "DEPARTMENT_NAME": [
        "Administration", "Marketing", "Purchasing", "Human Resources", "Shipping",
        "IT", "Public Relations", "Sales", "Executive", "Finance", "Accounting",
        "Treasury", "Corporate Tax", "Control And Credit", "Shareholder Services",
        "Benefits", "Manufacturing", "Construction", "Contracting", "Operations",
        "IT Support", "NOC", "IT Helpdesk", "Government Sales", "Retail Sales", "Recruiting", "Payroll"
    ]
}

df = pd.DataFrame(data)

distinct_department_ids = df['DEPARTMENT_ID'].unique()

print(distinct_department_ids)

DEPARTMENT_ID
0              10
1              20
2              30
3              40
4              50
5              60
6              70
7              80
8              90
9             100
10            110
11            120
12            130
13            140
14            150
15            160
16            170
17            180
18            190
19            200
20            210
21            220
22            230
23            240
24            250
25            260
26            270
