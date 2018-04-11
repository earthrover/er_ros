
"""
from: https://gist.github.com/dennislwy/0194036234445776d48ad2fb594457d4

With thanks to Dennis Lee
"""

from base64 import b64encode, b64decode

from urlparse import urlparse
import urllib
import random

import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random


ALPHA_NUMERIC = "abcdefghijklmnopqrstuvwxyz0123456789"

def generateNewRandomAlphaNumeric(length):
    random.seed()
    values = []
    for i in range(length):
        values.append(random.choice(ALPHA_NUMERIC))
    return "".join(values)

hash = "SHA-256"

def newkeys(keysize):
    random_generator = Random.new().read
    key = RSA.generate(keysize, random_generator)
    private, public = key, key.publickey()
    return public, private

def importKey(externKey):
    return RSA.importKey(externKey)

def getpublickey(priv_key):
    return priv_key.publickey()

def encrypt(message, pub_key):
    #RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    #RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)

def sign(message, priv_key, hashAlg="SHA-256"):
    global hash
    hash = hashAlg
    signer = PKCS1_v1_5.new(priv_key)
    if (hash == "SHA-512"):
        digest = SHA512.new()
    elif (hash == "SHA-384"):
        digest = SHA384.new()
    elif (hash == "SHA-256"):
        digest = SHA256.new()
    elif (hash == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.sign(digest)

def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    if (hash == "SHA-512"):
        digest = SHA512.new()
    elif (hash == "SHA-384"):
        digest = SHA384.new()
    elif (hash == "SHA-256"):
        digest = SHA256.new()
    elif (hash == "SHA-1"):
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.verify(digest, signature)

def sign_url(url, private_pem, salt=""):
    private_key = importKey(private_pem)
    msg = "%s%s" % (url, salt)
    return b64encode(sign(msg, private_key, "SHA-256"))

def verify_sig(url, signature, public_openssh, salt=""):

    public_key = importKey(public_openssh)
    msg = "%s%s" % (url, salt)
    return verify(msg, b64decode(signature), public_key)


def config_url(creds, cpu_serial):
    return _signed_url(creds, creds["url"], query_attrs={"serial": cpu_serial})


def firebase_token_url(creds, custom_token_url):
    return _signed_url(creds, custom_token_url)


def _signed_url(creds, url, query_attrs=None):
    private_pem = creds["private_key"]
    parsed = urlparse(url)
    nonced_path = "%s/%s" % (parsed.path, generateNewRandomAlphaNumeric(20))
    sig = sign_url(nonced_path, private_pem)
    attrs = {"sig": sig}
    if query_attrs is not None:
        attrs.update(query_attrs)
    query = urllib.urlencode(attrs)
    url = "%s://%s%s?%s" % (parsed.scheme, parsed.netloc, nonced_path, query)
    return url


def firebase_url(host, path, access_token):
    query = urllib.urlencode({"access_token": access_token})
    return "https://%s%s?%s" % (host, path, query)


def get_config(creds, serial):
    url = config_url(creds, serial)
    rsp = requests.get(url)

    if rsp.status_code == 200:
        return rsp.json()

    if rsp.status_code == 409:
        print "Error: another device is using this key already"

    return None


def get_firebase_custom_token(creds, custom_token_url):
    url = firebase_token_url(creds, custom_token_url)
    rsp = requests.get(url)

    if rsp.status_code == 200:
        return rsp.json()

    if rsp.status_code == 409:
        print "Error: another device is using this key already"

    return None