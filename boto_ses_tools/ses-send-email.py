#!/usr/bin/env python
"""SES email interface. Closely mimicks the interface of ses-send-email.pl provided by Amazon, but it should be noted
   that only raw mode is supported (not passing -r will result in an error just to be sure).
   
   Reads body from stdin."""
import optparse
import sys

from boto_ses_tools.aws_credential_parser import get_ses_connection

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-k', dest='credential_file', help='A file containing your AWS credentials (required)',
                      metavar='FILE')
    parser.add_option('-e', dest='host', help='Use the specified Amazon SES endpoint',
                      default='email.us-east-1.amazonaws.com')
    parser.add_option('-r', dest='raw', action='store_true', help='Specifies that this is a raw email message. You ' \
        'are responsible for ensuring that the raw message contains the correct email headers, and that it is ' \
        'properly (MANDATORY!)')
    parser.add_option('-f', dest='dest', help='The email address of the sender, followed immediately by the email ' \
        'address of the recipient. You can specify a list of recipients, separated by commas (MANDATORY)')
    parser.add_option('--from', dest='source', help='Sends the message from this sender')
    parser.add_option('--to', dest='destinations', help='Sends the message to these recipients (separate by a comma)')
    parser.add_option('--verbose', dest='verbose', help='Output debugging information', action='store_true')
    
    (options, args) = parser.parse_args()
    
    body = sys.stdin.read()
    ses_connection = get_ses_connection(options, parser)
    
    if not (options.dest or options.source or options.destinations):
        parser.error('-f is required (or --from and --to)')
    elif not options.raw:
        parser.error('-r is mandatory (non-raw mode is not supported)')
    elif options.dest and (options.source or options.destinations):
        parser.error('Cannot specify both -f and (--from or --to)')
    
    if options.dest:
        source, destinations = options.dest.split(' ', 1)
    else:
        source = options.source
        destinations = options.destinations
    
    # Process source/dest
    destinations = [i.strip() for i in destinations.split(',')]
    source = source.strip()
    
    ses_connection.send_raw_email(body, source=source, destinations=destinations)
    sys.exit(0)
