In order to use this project, you must have a private key generated from the Firebase Admin SDK.

Go to the project's Firebase page (you only have access if you worked on this project!), go to settings, then
service accounts, then Firebase Admin SDK. Scroll to the bottom and click on "Generate new private key". Firebase
should then generate a JSON file and download it through your browser. Place that JSON file here, in this folder,
and rename it to "iliketrains_firebase_key.json" (or change the line of code referencing it in app.py). Then
you should be good to go.

https://firebase.google.com/docs/admin/setup
https://console.firebase.google.com/project/iliketrains-1919/settings/serviceaccounts/adminsdk
