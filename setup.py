"""
Setup configuration for python-transform package.
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-transform',
    version='0.1.0',
    description='Convert documents and images to Markdown format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/python-transform',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=[
        'python-docx>=0.8.11',
        'PyPDF2>=3.0.1',
        'pdfplumber>=0.9.0',
        'pdf2image>=1.16.3',
        'Pillow>=10.0.0',
        'pytesseract>=0.3.10',
        'pillow-heif>=0.13.0',
        'markdown>=3.5.0',
    ],
    entry_points={
        'console_scripts': [
            'python-transform=main:main',
        ],
    },
)
