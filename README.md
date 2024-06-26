# Evil Eval

This script can be used to fuzz potentially vulnerable eval() functions when present as a `POST` request.

## Usage

~~~bash
python3 evil_eval.py --url http://example.com --error 'some error message' --json-key key_name
~~~

## Payloads

The payload list is not exhaustive and more can be added. Comments start with `#` and empty lines will be ignored in the `payloads.txt` file.

## TODO

TODO | Description
---- | -----------
1 | Add more payloads to the payloads.txt file
2 | Implement `GET` request compatibility

## Disclaimer

This tool, Evil Eval is intended for security testing and educational purposes only. It is designed to help security professionals and developers identify and address vulnerabilities related to the use of eval() functions in JavaScript applications.

The authors and contributors of this tool do not condone or support any illegal or unethical activities, including unauthorized access, exploitation, or damage to computer systems or networks. The use of this tool must comply with all applicable laws, regulations, and ethical standards.

The authors and contributors of this tool disclaim any responsibility or liability for any misuse or illegal use of this tool by users. Users assume full responsibility for their actions and the consequences thereof.
Remember, responsible and ethical security testing is essential for improving the security posture of applications and protecting against real-world threats. Use this tool responsibly, and always prioritize the safety and integrity of systems and data.
