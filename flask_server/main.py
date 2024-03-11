from azure_bindings import AzureDBconfig
from azuresqldb import AzureSqlDatabase, stored_procs
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Database setup
def initialize_database():
    azureconfig = AzureDBconfig().getconfig()
    azuresqldb = AzureSqlDatabase(server=azureconfig["server"],
                                database=azureconfig["database"],
                                username=azureconfig["username"],
                                password=azureconfig["password"],
                                driver=azureconfig["driver"])
    return azuresqldb

# Flask routes
@app.route("/api/locations", methods=["GET"])
def get_locations():
    azuresqldb = initialize_database()
    azuresqldb.connect()
    rows, columns = azuresqldb.execute_query(stored_procs["getJobCountByLocation"])
    azuresqldb.disconnect()
    # transform retrieved data into python readable format
    data = [tuple(row) for row in rows]
    columns = [column[0] for column in columns]
    df = pd.DataFrame(data, columns=columns)
    return jsonify(df[['lat', 'lng']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)