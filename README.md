## Email Encryption using Blowfish Algorithm
### Introduction


### Project
##### Structure
```
.
├── algo.py
├── blowfish_algo.py
├── README.md
├── receive.py
└── send.py
```

##### File description
| File       | Description                                             |
|------------|---------------------------------------------------------|
| algo.py    | Methods to Encrypt and Decrypt using Blowfish algorithm |
| send.py    | Encrypt message and Send email                          |
| receive.py | Receive email and Decrypt message                       |

### Algorithm
##### Blowfish
Blowfish is a symmetric block cipher that can be used as a drop-in replacement for DES or IDEA. It takes a variable-length key, from 32 bits to 448 bits, making it ideal for both domestic and exportable use.

### Setup

##### Cipher key
`Admin key` is the symmetrical cipher key used by Blowfish algorithm for both Encryption and Decryption. Set a custom admin_key in the [algo.py](./algo.py) file.
```python
# Replace admin_key with string
# Size > 4 bytes
cipher = blowfish.Cipher(b"admin_key")
```
##### Testing
Testing Blowfish algorithm

```python
python algo.py
```
Must generate the following output
```
JuxX3vmzzDqblD/SZJyJ8PICXrVfzcBWZZBX6Kk=
Testing Blowfish: Success ✓
```
##### Email (Gmail)
###### Sending email
Replace values with sender Email ID and Password and receiver Email ID in the [send.py](./send.py) file.
```python
fromx = "example@gmail.com"
to = "donjoe@gmail.com"
password = "password"
```
[Additional Setup](https://www.lifewire.com/allow-email-programs-access-to-gmail-with-password-1171875) for sending email using Gmail.

###### Receiving email
Replace values with sender Email ID and Password [receive.py](./receive.py) file.
```python
user = 'example@gmail.com'
password = 'password'
```
[Additional setup](https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/amp/) for receiving email from Gmail.

##### Run
```python
# Encryption message and
# Sending email
python send.py

# Receiving email and
# Decryption message
python receive.py
```

### Result
###### Encode and Send E-mail
```
Enter message to send: Testing email encryption using Blowfish algorithm.

Sending email ...
----------------------------
From:    example@gmail.com
To:      donjoe@gmail.com
Subject: ENC: Sample mail
Message:
 CCn4VdEuE33qHpW197H+5+sBTcKO/7vvIllr9eE4MGnx4cYlH8VISLAvBp3+fYEkoZk=
----------------------------

Message sent ...  ✓
```

###### Receive and Decode E-mail
```
Raw email content
-----------------------------
...
Subject: ENC: Sample mail
From: example@gmail.com
To: donjoe@gmail.com

CCn4VdEuE33qHpW197H+5+sBTcKO/7vvIllr9eE4MGnx4cYlH8VISLAvBp3+fYEkoZk=
-----------------------------

Encrypted message
CCn4VdEuE33qHpW197H+5+sBTcKO/7vvIllr9eE4MGnx4cYlH8VISLAvBp3+fYEkoZk=

Decrypting ...
Decrypted message ✓
Testing email encryption using Blowfish algorithm.
```