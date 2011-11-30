import re

from boto.ses.connection import SESConnection
from boto.ses import get_region
from boto_utils.common import parse_aws_credentials_file

def get_ses_connection(args):
	"""Given a set of parsed arguments, returns an SESConnection."""
	credentials = parse_aws_credentials_file(args.credentials_file)

	region = None

	if args.region:
		region_name = re.search('email\.(.+)\.amazonaws\.com', args.region).group(1)
		region_info = get_region(region_name)
	
	return SESConnection(region=region_info, debug=(2 if args.verbose else 0),
		**credentials)
