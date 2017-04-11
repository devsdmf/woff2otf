
from setuptools import setup, find_packages

setup(
    # module name and version
    name = 'woff2otf',
    version = '1.0.0',

    # useful information
    description = 'Python library to convert WOFF fonts to OTF format',
    url = 'https://github.com/devsdmf/woff2otf',
    author = 'devsdmf',
    author_email = 'devsdmf@gmail.com',
    license='MIT',

    # module index
    classifiers = [
        # current project status
        'Development Status :: 5 - Production/Stable',

        # topics
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',

        # license
        'License :: OSI Approved :: MIT License',

        # compatibility
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords = 'woff woff2 otf converter font webfont',

    # module packages
    packages = find_packages(),

    # module requirements
    install_requires=[]
)
