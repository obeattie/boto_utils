from distutils.core import setup

setup(
    name='boto_utils',
    version='0.1',
    description='Command-line tools based on Boto',
    long_description=open('description.rst', 'r').read(),
    author='Oliver Beattie',
    author_email='oliver@obeattie.com',
    url='https://github.com/obeattie/boto-ses-tools',
    packages=['boto_utils'],
    scripts=[
        'boto_utils/ses-send-email',
        'boto_utils/ses-verify-email-address',
        'boto_utils/s3-put',
    ]
)
