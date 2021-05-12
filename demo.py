from Google import Create_Service

CLIENT_SECRET_FILE = 'Client_Secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

national_parks = ['Krl', 'Teste', 'Animal']

for national_park in national_parks:
  file_metadata = {
    'name': national_park,
    'mimeType': 'application/vnd.google-apps.folder'
    # 'parents': []
  }
  
  service.files().create(body=file_metadata).execute()