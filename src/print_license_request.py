import audible

auth = audible.Authenticator.from_file('../auth/burke_auth.py')
client = audible.Client(auth)

body = {
    "supported_drm_types" : [
        "Mpeg",
        "Adrm"
    ],
    "quality" : "High",
    "consumption_type" : "Download",
    "response_groups" : "last_position_heard,pdf_url,content_reference,chapter_info"
}

print(client.post('/content/B002V0GINK/licenserequest', body))