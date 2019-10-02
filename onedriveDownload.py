import onedrivesdk
import os.path
import sys

input = getattr(__builtins__, 'raw_input', input)

# list of files to download
downloadList = ['smartzap4-diagram.html',
                'BTC-2Transf.png'
    ]
# Directory to list
#directory_id = "DED4CB994E09B102!42674"
directory_id = "root"

def navigate(client, item_id):
    items = client.item(id=item_id).children.get()
    return items

def listDirectory(client,download):
  items = navigate(client, directory_id)
  count = 0

  for count, item in enumerate(items):
    if download == 0:
      print(f'count={count}\tid="{items[count].id}"\tfilename="{item.name}"')
    else: # Download 
      if item.name in downloadList:
        print(f'Download {items[count].id} filename="{item.name}"')
        client.item(id=items[count].id).download(item.name)

redirect_uri = 'http://localhost:8080/'
client_secret = 'BqaTYqI0XI7wDKcnJ5i3MvLwGcVsaMVM'
client_id='00000000481695BB'
api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(http_provider=http_provider,client_id=client_id,scopes=scopes)

client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)

## Check sesseion files
if os.path.isfile('session.pickle'): 
  client.auth_provider.load_session()
  client.auth_provider.refresh_token()
else:
  auth_url = client.auth_provider.get_auth_url(redirect_uri)
  # Ask for the code
  print("You don't have session stored, please follow the instructions bellow:" )
  print('Paste this URL into your browser, approve the app\'s access.')
  print('Copy everything in the address bar after "code=", and paste it below.')
  print(auth_url)
  code = input('Paste code here: ')
  client.auth_provider.authenticate(code, redirect_uri, client_secret)
  client.auth_provider.save_session()

if len(sys.argv) <=1:
  print(f'usage: {sys.argv[0]} -l | -d')
  print('-l = List | -d download')
  exit(0)

cmd = sys.argv[1]

if cmd == '-l':
  download=0
  listDirectory(client,download)
elif cmd == '-d':
  download=1
  listDirectory(client,download)
  


