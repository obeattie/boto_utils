#!/usr/bin/env python
"""SES address verification tool. Closely mimicks the ses-verify-email-address.pl script provided by Amazon."""
import optparse
import sys

from boto_ses_tools.aws_credential_parser import get_ses_connection

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-k', dest='credential_file', help='A file containing your AWS credentials (required)',
                      metavar='FILE')
    parser.add_option('-e', dest='host', help='Use the specified Amazon SES endpoint',
                      default='email.us-east-1.amazonaws.com')
    parser.add_option('-v', dest='verify', help='Requests verification of an email address')
    parser.add_option('-l', dest='list', help='Lists the email addresses that you have already verified',
                      action='store_true')
    parser.add_option('-d', dest='delete', help='Deletes a verified email address')
    parser.add_option('--verbose', dest='verbose', help='Output debugging information', action='store_true')
    
    (options, args) = parser.parse_args()
    
    ses_connection = get_ses_connection(options, parser)
    
    if not (options.verify or options.list or options.delete):
        parser.error('You must specify one of -l, -d, or -v')
    
    # Do the work
    if options.verify:
        ses_connection.verify_email_address(options.verify)
    if options.list:
        response = ses_connection.list_verified_email_addresses()
        # How nasty is this?
        addresses = response['ListVerifiedEmailAddressesResponse']['ListVerifiedEmailAddressesResult']['VerifiedEmailAddresses']
        for address in addresses:
            print address
    if options.delete:
        ses_connection.delete_verified_email_address(options.delete)
    
    sys.exit(0)
