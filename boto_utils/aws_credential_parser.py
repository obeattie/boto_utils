import re

from boto.ses.connection import SESConnection

LINE_RE = re.compile(r'^\s*(.*?)=(.*?)\s*$')

def parse_aws_credentials_file(fp):
    """Return a dictionary containing aws_access_key_id and aws_secret_access_key, given a file to a credentials file
       in the format expected by AWS tools (as described at http://j.mp/qGGHNp).
       
       This is a port of the Perl code in SES.pm, so should behave identically."""
    
    result = {}
    
    for line in fp:
        match = LINE_RE.match(line)
        if not line:
            continue
        elif not match:
            raise ValueError, 'Cannot parse credentials file entry <%s>' % line
        elif match.group(1) == 'AWSAccessKeyId':
            result['aws_access_key_id'] = match.group(2)
        elif match.group(1) == 'AWSSecretKey':
            result['aws_secret_access_key'] = match.group(2)
        else:
            raise ValueError, 'Unrecognized credential <%s>' % match.group(1)
    
    return result

def get_ses_connection(options, parser):
    """Given parsed command line options, returns an SESConnection object from the parameters."""
    if not options.credential_file:
        parser.error('You must specify a credentials file')
    
    credentials = parse_aws_credentials_file(open(options.credential_file))
    return SESConnection(
        aws_access_key_id=credentials['aws_access_key_id'],
        aws_secret_access_key=credentials['aws_secret_access_key'],
        host=options.host,
        debug=(1 if options.verbose else 0)
    )
