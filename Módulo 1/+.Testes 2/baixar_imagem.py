import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Configuração da credencial (usando Secrets do GitHub)
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
# Aqui você puxa as credenciais da Service Account salvas no GitHub