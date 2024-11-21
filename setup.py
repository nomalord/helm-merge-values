from setuptools import setup

setup(
    name='HelmValuesMerge',
    version='',
    author='nomalord',
    install_requires=[
        'Click',
        'deepmerge',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'merge-values = helm_merge_values.main:merge_values',
        ],
    },
)
