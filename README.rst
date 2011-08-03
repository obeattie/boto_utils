Command-line tools for interacting with Amazon Web Services, based on `Boto <http://pypi.python.org/pypi/boto/>`_.

Currently included are:

* ``s3-put``: Upload file(s) to S3. Built to replace Boto's ``s3put`` command, allowing placement of files inside
  directories within buckets.
* ``ses-send-email``: Send an email via `SES <http://aws.amazon.com/ses/>`_. Replacement for the ``ses-send-email.pl`` 
  script provided `by Amazon <http://aws.amazon.com/developertools/Amazon-SES/8945574369528337>`_, which is a (ahem) a
  total nightmare to get running; and installing unpackaged source code manually just makes me uncomfortable.
  
  This tool supports the interface necessary to submit raw mail only; that is, you will have to give the script
  a raw email as input over stdin. This means it is ideally suited to use along a pipeline, for instance as a mail
  transport under Postfix (using ``PIPE``)
* ``ses-verify-email-address``: Manage verified SES email addresses. Pretty much a drop-in replacement for the tool
  provided by Amazon in the SES developer tools.

All scripts are made to parse a credentials file, which will be in the same format as that expected by some AWS tools.
Details `here <http://docs.amazonwebservices.com/ses/latest/DeveloperGuide/index.html?InitialSetup.Scripts.html>`_. By 
default, this is expected to be available at ``/etc/aws-credentials.txt``, but can be overridden by passing the path to
your credentials file with `-k`.
