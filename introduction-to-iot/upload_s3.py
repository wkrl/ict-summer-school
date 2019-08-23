from boto.s3.key import Key
from boto.s3.connection import S3Connection
import string
import time
import random

def gen_url(bucket, key):
  return 'https://%s.s3.amazonaws.com/%s' % (bucket, key)

def gen_hash():
	lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(5)]
	str = "".join(lst)
	return str

AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_KEY'
BUCKET = 'YOUR_BUCKET'
KEY = gen_hash()

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
print "Connection made"
b = conn.get_bucket(BUCKET)

uploadfile = "face.jpg" 
k = Key(b)
k.key = KEY
k.set_contents_from_filename(uploadfile)
print "Uploaded file"
k.make_public()

# Save URL to local text file 
URL = gen_url(BUCKET, KEY)
f = open("faces.txt", "a+")
f.write("\n" + URL)
f.close()
