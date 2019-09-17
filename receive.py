# Importing libraries 
import imaplib, email 
from algo import decrypt_msg

user = 'example@gmail.com'
password = 'password'
imap_url = 'imap.gmail.com'
  
# Function to get email content
def get_body(msg): 
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True) 
  
# Function to search emails
def search(key, value, con):  
    result, data = con.search(None, key, '"{}"'.format(value)) 
    return data 
  
# Function to get emails
def get_emails(result_bytes): 
    msgs = []
    for num in result_bytes[0].split(): 
        typ, data = con.fetch(num, '(RFC822)') 
        msgs.append(data) 
    return msgs 

con = imaplib.IMAP4_SSL(imap_url)  
con.login(user, password)  
con.select('Inbox')  

# Fetching emails from user
msgs = get_emails(search('FROM', user, con))   


# Finding the required content from our msgs  
for msg in msgs[::-1]:  
    for sent in msg: 
        if type(sent) is tuple:  
            # encoding set as utf-8 
            content = str(sent[1], 'utf-8')  
            data = str(content) 

            # Handling errors related to unicodenecode 
            try:
                indexstart = data.find("ltr") 
                data2 = data[indexstart + 5: len(data)] 
                indexend = data2.find("</div>") 

                # printtng the required content which we need 
                # to extract from our email i.e our body 
                print("Raw email content")
                print("\n-----------------------------")
                print(data2[0: indexend])
                print("-----------------------------")

                content = data2.split("\n")[-2]
                print("\nEncrypted message")
                print(content)

                print("\nDecrypting ...")
                print("Decrypted message", u'\u2713')
                print(decrypt_msg(content))
                break
            
            except UnicodeEncodeError as e: 
                pass
