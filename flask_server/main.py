from azure_bindings import AzureDBconfig
from azuresqldb import AzureSqlDatabase, stored_procs
from gcp_bindings import ApiServiceKeys
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes - allows react frontend to access API endpoints (note - in production this would need better handling for security)
CORS(app)

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
    try:
        azuresqldb = initialize_database()
        azuresqldb.connect()
        rows, columns = azuresqldb.execute_query(stored_procs["getJobCountByLocation"])
        azuresqldb.disconnect()
        # transform retrieved data into python readable format
        data = [tuple(row) for row in rows]
        columns = [column[0] for column in columns]
        df = pd.DataFrame(data, columns=columns)
        return jsonify(df[['job_count', 'lat', 'lng']].to_dict(orient='records'))
    except Exception as e:
        print(f"An error occured at /api/locations: {e}")
        return jsonify("An error occured at /api/locations")

# treat API key as data that is encapsulated within the flask backend
@app.route("/api/gmaps-api-key", methods=["GET"])
def get_gmaps_api_key():
    gmaps_api_key = ApiServiceKeys().get_service_key()["googlemaps"]
    return jsonify({'gmaps-api-key':gmaps_api_key})

@app.route("/", methods=["GET"])
def index():
    try: 
        print("loading index...")
        azuresqldb = initialize_database()
        print("initialised db")
        azuresqldb.connect()
        print("connected db")
        rows, columns = azuresqldb.execute_query(stored_procs["getJobCountByLocation"])
        print(rows, columns)
        azuresqldb.disconnect()
        print("disconnected from db")
        return "Hello World!"
    except:
        if azuresqldb:
            return "azuresqldb initialised"
        else:
            return "Goodbye World!"

if __name__ == '__main__':
    # the client-side fetch requests should match this port (at least for development purpose)
    app.run(debug=True, host='0.0.0.0' ,port=5000)