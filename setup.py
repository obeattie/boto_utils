from distutils.core import setup

setup(
    name='boto_ses_tools',
    version='0.1',
    description='Command-line tools based on Boto intended to replace the SES command-line tools provided by Amazon ' \
        '(which are just ridiculously complex to get installed under Debian)',
    author='Oliver Beattie',
    author_email='oliver@obeattie.com',
    url='https://github.com/obeattie/boto-ses-tools',
    packages=['boto_ses_tools'],
    scripts=[
        'boto_ses_tools/ses-send-email.py',
        'boto_ses_tools/ses-verify-email-address.py',
    ]
)
