from azure_bindings import AzureDBconfig
from azuresqldb import AzureSqlDatabase, stored_procs

azureconfig = AzureDBconfig().getconfig()
azuresqldb = AzureSqlDatabase(server=azureconfig["server"],
                            database=azureconfig["database"],
                            username=azureconfig["username"],
                            password=azureconfig["password"],
                            driver=azureconfig["driver"])
azuresqldb.connect()
rows, columns = azuresqldb.execute_query(stored_procs["getJobCountByLocation"])
azuresqldb.disconnect()

import pandas as pd

data = [tuple(row) for row in rows]
df = pd.DataFrame(data, columns=columns)

def strip_location_header(DataFrame : pd.DataFrame) -> list:
    header = []
    for i in DataFrame[['lat', 'lng']]:
        header.append(i[0])
    return header

def strip_location_data(DataFrame : pd.DataFrame) -> list:
    DataFrame.columns = [None] * len(DataFrame.columns)
    return DataFrame

df2 = pd.DataFrame(strip_location_data(df[['lat', 'lng']]), strip_location_header(df))
print(df2)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/locations")
def get_locations():
    return jsonify(df[['lat', 'lng']].to_dict(orient='records'))

#if __name__ == '__main__':


#    app.run(debug=True)