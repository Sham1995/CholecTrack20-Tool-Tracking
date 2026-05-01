# -*- coding: utf-8 -*-
"""
Download CholecTrack20 Dataset
"""

import requests
import synapseutils
import synapseclient

def main():

    print("Authenticating user ...")
    syn = synapseclient.login(email=email, authToken=authToken)

    print("Authenticating access key permission to download dataset ...")
    API_URL = "https://synapse-response.onrender.com/validate_access"
    USER_ID = syn.getUserProfile()['ownerId']

    response = requests.post(API_URL, json={
        "access_key": accesskey,
        "synapse_id": USER_ID
    })

    if response.status_code == 200:
        entity_id = response.json()['entity_id']
    else:
        print("❌ Failed to request access:", response.text)
        exit(1)

    print("Downloading dataset...")
    synapseutils.syncFromSynapse(syn, entity=entity_id, path=local_folder)
    print("✅ Download complete!")

if __name__ == "__main__":

    email = "stanleyosuozah@gmail.com"

    # 🔐 Paste your token HERE locally (not here in chat)
    authToken = "eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIiwibW9kaWZ5Il0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTc3NzU2Mzg4OSwiaWF0IjoxNzc3NTYzODg5LCJqdGkiOiIzNjY0MyIsInN1YiI6IjM1ODc2NjYifQ.qxDIaxErU3C58fMkFrOiNAeh-7re5ADZvXfZ488ggd9e-BBCmboLYbiotgQyrM_mtzt_p-cTnfvwca_9yCsWwrNh_LNWK_vwxuV5zoJ4L6-Qvnjdq4TVbcGcuCIVi8YdJpEx1JcFDCvxQtJR1CqHeHeGMdRY38iShVg_a0KFCOcen0DxCpeQKPg9sRgYFU7hqZRtVBkqtjOEpISE1RO8dYnjsStAdrYWqg4etau3fD-zDB_aNkg78hTfIB6O_2j9mSW6zbNmMi2xzEz1wQf8I4Hjp3gOgMxeN5oe2mSl-1SUGmsztOy_AyLr3GtKHi6TgNHGj2drRRFxwqEbcNkCXg"

    accesskey = "ZAHJTF.4656753"

    local_folder = r"C:\Users\shamsa\Desktop\StrongSORT\datasets\CholecTrack20"

    main()