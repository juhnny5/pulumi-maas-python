# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('maas')


class _ExportableConfig(types.ModuleType):
    @property
    def api_key(self) -> Optional[str]:
        """
        The MAAS API key
        """
        return __config__.get('apiKey')

    @property
    def api_url(self) -> Optional[str]:
        """
        The MAAS API URL (eg: http://127.0.0.1:5240/MAAS)
        """
        return __config__.get('apiUrl')

    @property
    def api_version(self) -> Optional[str]:
        """
        The MAAS API version (default 2.0)
        """
        return __config__.get('apiVersion')
