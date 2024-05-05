- You need to install Js2Py (pip install js2py) and decouple (pip install python-decouple)

- Create ".env" file to store your credentials and IP / PORT

```ini
USERNAME=your_username
PASSWORD=your_password
IP=your_ip
PORT=your_port
```

- Create a file main_test.py

```py
from decouple import config
import js2py
import time
import re
from json import dumps
from synology_api import auth

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')
IP = config('IP')
PORT = config('PORT')

a = auth.Authentication(
IP,
PORT,
USERNAME,
PASSWORD,
secure=False,
cert_verify=False,
dsm_version=7,
debug=True,
otp_code=False
)

t0 = time.time()
context = js2py.EvalJs()
context.execute(a.load_UIString_file().decode('utf-8'))
context.execute(a.load_JSUIString_file().decode('utf-8'))

sds_file_content: str = a.load_error_codes_js().decode('utf-8')

# Regex pattern
pattern = r'function\s+n\(\)([\s\S]*?)(?=function\s+s\(\)|$)'

# Find all matches

matches = re.findall(pattern, sds_file_content, re.DOTALL)

if len(matches) == 1: ## This return e object with all error codes
sds_errors_code = "function n()"+matches[0]+"var errors = n()"
sds_errors_code = sds_errors_code.replace("SYNO.SDS.formatString", '"".concat')
context.execute(sds_errors_code)
errors = context.errors.to_dict()
with open('errors.json', 'w') as f:
    f.write(dumps(errors))

    t1 = time.time()
    total = t1-t0
    print(f"Time import errors list in: {total}s")
```
