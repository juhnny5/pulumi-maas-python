# coding=utf-8

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "1.0.0"
PLUGIN_VERSION = "1.0.0"

class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'maas', PLUGIN_VERSION, '--server', 'https://github.com/juhnny5/pulumi-maas/releases/download/v${VERSION}'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print(f"""
                There was an error installing the maas resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource maas {PLUGIN_VERSION}`
                """)
            else:
                raise


def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "maas Pulumi Package - Development Version"


setup(name='pulumi-maas',
      python_requires='>=3.7',
      version=VERSION,
      description="A Pulumi package for creating and managing Canonical Metal-As-A-Service (MAAS) resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi maas category/cloud',
      url='https://www.pulumi.com',
      project_urls={
          'Repository': 'https://github.com/juhnny5/pulumi-maas-python'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'pulumi-maas': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
