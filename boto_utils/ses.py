from boto.ses.connection import SESConnection

from boto_utils.common import parse_aws_credentials_file

def get_ses_connection(args):
    """Given a set of parsed arguments, returns an SESConnection."""
    credentials = parse_aws_credentials_file(args.credentials_file)
    return SESConnection(
        host=args.host,
        debug=(2 if args.verbose else 0),
        **credentials
    )
