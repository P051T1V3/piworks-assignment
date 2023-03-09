from re import findall
import pandas as pd

"""
SELECT SUBSTR(Stats_Access_Link,INSTR('://',Stats_Access_Link)+3,INSTR('</',Stats_Access_Link)-INSTR('://',Stats_Access_Link)-3)
FROM DB;
"""

def main():
    filename = "example.xlsx"
    df = pd.read_excel(filename)
    prod_links = dict()
    pattern = "://.+</"

    for product, full_link in zip(df["Device_Type"],df["Stats_Access_Link"]):
        pure_link = findall(pattern, full_link)
        prod_links[product] = pure_link[0][3:-2]

    print(prod_links)

if __name__ == "__main__":
    main()