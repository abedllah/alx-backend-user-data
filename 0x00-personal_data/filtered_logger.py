#!/usr/bin/env python3
""" Protecting PII """
import re

def filter_datum(fields, redaction, message, separator):
    """ returns the log message obfuscated """
    return re.sub(rf"({'|'.join(fields)})=.*?{separator}", rf"\1={redaction}{separator}", message)

