from flask import Flask,request,render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
fernet_key = Fernet(key)

#Route encrypt returns encrypted string
@app.route("/encrypt")
def encrypt():
    string = request.args.get('string','Test')
    #Encrypting our string
    token = f.encrypt(bytes(string, 'utf-8'))

    is_encrypt = True
    return render_template('index.html', encrypted_string = str(token), is_encrypt = is_encrypt)

#Route decrypt returns decrypted string
@app.route("/decrypt")
def decrypt():
    try:
        string = request.args.get('string',None)
        if not string:
            return 'Invalid'
        #Decrypting our string    
        token = f.decrypt(bytes(string, 'utf-8'))
        is_encrypt = False
        return render_template('index.html', decrypted_string = str(token),is_encrypt = is_encrypt)
    except:
        return "Invalid"


if __name__ == "__main__":
    app.run(debug = True)
