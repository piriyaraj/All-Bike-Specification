data = """{"installed":{"client_id":"214907560505-q9f9eq8j9pin59b0l4u1us37buma6331.apps.googleusercontent.com","project_id":"all-bike-specifi-1629717026903","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"NkFzLVH9By5zJVroO8CdZHer","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}"""
open("client_secrets.json", 'w').write(data)
