import pandas as pd

data = {
    "JOB_ID": ["AD_PRES", "AD_VP", "AD_ASST", "FI_MGR", "FI_ACCOUNT", "AC_MGR", "AC_ACCOUNT",
               "SA_MAN", "SA_REP", "PU_MAN", "PU_CLERK", "ST_MAN", "ST_CLERK", "SH_CLERK",
               "IT_PROG", "MK_MAN", "MK_REP", "HR_REP", "PR_REP"],
    "JOB_TITLE": ["President", "Administration Vice President", "Administration Assistant", "Finance Manager",
                  "Accountant", "Accounting Manager", "Public Accountant", "Sales Manager", "Sales Representative",
                  "Purchasing Manager", "Purchasing Clerk", "Stock Manager", "Stock Clerk", "Shipping Clerk",
                  "Programmer", "Marketing Manager", "Marketing Representative", "Human Resources Representative",
                  "Public Relations Representative"],
    "MIN_SALARY": [20080, 15000, 3000, 8200, 4200, 8200, 4200, 10000, 6000, 8000, 2500, 5500, 2008, 2500,
                   4000, 9000, 4000, 4000, 4500],
    "MAX_SALARY": [40000, 30000, 6000, 16000, 9000, 16000, 9000, 20080, 12008, 15000, 5500, 8500, 5000, 5500,
                   10000, 15000, 9000, 9000, 10500]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by='JOB_TITLE', ascending=False)

print(df_sorted)

        JOB_ID                        JOB_TITLE  MIN_SALARY  MAX_SALARY
11      ST_MAN                    Stock Manager        5500        8500
12    ST_CLERK                      Stock Clerk        2008        5000
13    SH_CLERK                   Shipping Clerk        2500        5500
8       SA_REP             Sales Representative        6000       12008
7       SA_MAN                    Sales Manager       10000       20080
9       PU_MAN               Purchasing Manager        8000       15000
10    PU_CLERK                 Purchasing Clerk        2500        5500
18      PR_REP  Public Relations Representative        4500       10500
6   AC_ACCOUNT                Public Accountant        4200        9000
14     IT_PROG                       Programmer        4000       10000
0      AD_PRES                        President       20080       40000
16      MK_REP         Marketing Representative        4000        9000
15      MK_MAN                Marketing Manager        9000       15000
17      HR_REP   Human Resources Representative        4000        9000
3       FI_MGR                  Finance Manager        8200       16000
1        AD_VP    Administration Vice President       15000       30000
2      AD_ASST         Administration Assistant        3000        6000
5       AC_MGR               Accounting Manager        8200       16000
4   FI_ACCOUNT                       Accountant        4200        9000

