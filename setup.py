from setuptools import setup

setup(
    name='boto_utils',
    version='0.2',
    description='Command-line tools based on Boto',
    long_description=open('README.rst', 'r').read(),
    author='Oliver Beattie',
    author_email='oliver@obeattie.com',
    url='https://github.com/obeattie/boto_utils',
    packages=['boto_utils'],
    install_requires=['boto>=2.2.0'],
    scripts=[
        'boto_utils/ses-send-email',
        'boto_utils/ses-verify-email-address',
        'boto_utils/s3-put',
        'boto_utils/s3-geturl',
        'boto_utils/s3-copy',
        'boto_utils/s3-delete',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ]
)
