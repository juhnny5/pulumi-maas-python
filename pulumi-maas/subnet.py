# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SubnetArgs', 'Subnet']

@pulumi.input_type
class SubnetArgs:
    def __init__(__self__, *,
                 cidr: pulumi.Input[str],
                 allow_dns: Optional[pulumi.Input[bool]] = None,
                 allow_proxy: Optional[pulumi.Input[bool]] = None,
                 dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 fabric: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rdns_mode: Optional[pulumi.Input[int]] = None,
                 vlan: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Subnet resource.
        :param pulumi.Input[str] cidr: The subnet CIDR.
        :param pulumi.Input[bool] allow_dns: Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        :param pulumi.Input[bool] allow_proxy: Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[str] fabric: The fabric identifier (ID or name) for the new subnet.
        :param pulumi.Input[str] gateway_ip: Gateway IP address for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]] ip_ranges: A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] name: The subnet name.
        :param pulumi.Input[int] rdns_mode: How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
               created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
               the appropriate CNAME resource records for the network, if the network is small enough to require the support described
               in RFC2317.
        :param pulumi.Input[str] vlan: The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
               required.
        """
        pulumi.set(__self__, "cidr", cidr)
        if allow_dns is not None:
            pulumi.set(__self__, "allow_dns", allow_dns)
        if allow_proxy is not None:
            pulumi.set(__self__, "allow_proxy", allow_proxy)
        if dns_servers is not None:
            pulumi.set(__self__, "dns_servers", dns_servers)
        if fabric is not None:
            pulumi.set(__self__, "fabric", fabric)
        if gateway_ip is not None:
            pulumi.set(__self__, "gateway_ip", gateway_ip)
        if ip_ranges is not None:
            pulumi.set(__self__, "ip_ranges", ip_ranges)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rdns_mode is not None:
            pulumi.set(__self__, "rdns_mode", rdns_mode)
        if vlan is not None:
            pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[str]:
        """
        The subnet CIDR.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="allowDns")
    def allow_dns(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        """
        return pulumi.get(self, "allow_dns")

    @allow_dns.setter
    def allow_dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_dns", value)

    @property
    @pulumi.getter(name="allowProxy")
    def allow_proxy(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        """
        return pulumi.get(self, "allow_proxy")

    @allow_proxy.setter
    def allow_proxy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_proxy", value)

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        """
        return pulumi.get(self, "dns_servers")

    @dns_servers.setter
    def dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_servers", value)

    @property
    @pulumi.getter
    def fabric(self) -> Optional[pulumi.Input[str]]:
        """
        The fabric identifier (ID or name) for the new subnet.
        """
        return pulumi.get(self, "fabric")

    @fabric.setter
    def fabric(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fabric", value)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway IP address for the new subnet. This argument is computed if it's not set.
        """
        return pulumi.get(self, "gateway_ip")

    @gateway_ip.setter
    def gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_ip", value)

    @property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]]]:
        """
        A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
        [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        return pulumi.get(self, "ip_ranges")

    @ip_ranges.setter
    def ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]]]):
        pulumi.set(self, "ip_ranges", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The subnet name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rdnsMode")
    def rdns_mode(self) -> Optional[pulumi.Input[int]]:
        """
        How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
        created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
        the appropriate CNAME resource records for the network, if the network is small enough to require the support described
        in RFC2317.
        """
        return pulumi.get(self, "rdns_mode")

    @rdns_mode.setter
    def rdns_mode(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rdns_mode", value)

    @property
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[str]]:
        """
        The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
        required.
        """
        return pulumi.get(self, "vlan")

    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vlan", value)


@pulumi.input_type
class _SubnetState:
    def __init__(__self__, *,
                 allow_dns: Optional[pulumi.Input[bool]] = None,
                 allow_proxy: Optional[pulumi.Input[bool]] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 fabric: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rdns_mode: Optional[pulumi.Input[int]] = None,
                 vlan: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Subnet resources.
        :param pulumi.Input[bool] allow_dns: Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        :param pulumi.Input[bool] allow_proxy: Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        :param pulumi.Input[str] cidr: The subnet CIDR.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[str] fabric: The fabric identifier (ID or name) for the new subnet.
        :param pulumi.Input[str] gateway_ip: Gateway IP address for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]] ip_ranges: A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] name: The subnet name.
        :param pulumi.Input[int] rdns_mode: How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
               created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
               the appropriate CNAME resource records for the network, if the network is small enough to require the support described
               in RFC2317.
        :param pulumi.Input[str] vlan: The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
               required.
        """
        if allow_dns is not None:
            pulumi.set(__self__, "allow_dns", allow_dns)
        if allow_proxy is not None:
            pulumi.set(__self__, "allow_proxy", allow_proxy)
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if dns_servers is not None:
            pulumi.set(__self__, "dns_servers", dns_servers)
        if fabric is not None:
            pulumi.set(__self__, "fabric", fabric)
        if gateway_ip is not None:
            pulumi.set(__self__, "gateway_ip", gateway_ip)
        if ip_ranges is not None:
            pulumi.set(__self__, "ip_ranges", ip_ranges)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rdns_mode is not None:
            pulumi.set(__self__, "rdns_mode", rdns_mode)
        if vlan is not None:
            pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter(name="allowDns")
    def allow_dns(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        """
        return pulumi.get(self, "allow_dns")

    @allow_dns.setter
    def allow_dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_dns", value)

    @property
    @pulumi.getter(name="allowProxy")
    def allow_proxy(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        """
        return pulumi.get(self, "allow_proxy")

    @allow_proxy.setter
    def allow_proxy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_proxy", value)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The subnet CIDR.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        """
        return pulumi.get(self, "dns_servers")

    @dns_servers.setter
    def dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_servers", value)

    @property
    @pulumi.getter
    def fabric(self) -> Optional[pulumi.Input[str]]:
        """
        The fabric identifier (ID or name) for the new subnet.
        """
        return pulumi.get(self, "fabric")

    @fabric.setter
    def fabric(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fabric", value)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway IP address for the new subnet. This argument is computed if it's not set.
        """
        return pulumi.get(self, "gateway_ip")

    @gateway_ip.setter
    def gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_ip", value)

    @property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]]]:
        """
        A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
        [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        return pulumi.get(self, "ip_ranges")

    @ip_ranges.setter
    def ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetIpRangeArgs']]]]):
        pulumi.set(self, "ip_ranges", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The subnet name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rdnsMode")
    def rdns_mode(self) -> Optional[pulumi.Input[int]]:
        """
        How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
        created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
        the appropriate CNAME resource records for the network, if the network is small enough to require the support described
        in RFC2317.
        """
        return pulumi.get(self, "rdns_mode")

    @rdns_mode.setter
    def rdns_mode(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rdns_mode", value)

    @property
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[str]]:
        """
        The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
        required.
        """
        return pulumi.get(self, "vlan")

    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vlan", value)


class Subnet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_dns: Optional[pulumi.Input[bool]] = None,
                 allow_proxy: Optional[pulumi.Input[bool]] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 fabric: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetIpRangeArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rdns_mode: Optional[pulumi.Input[int]] = None,
                 vlan: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Subnet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_dns: Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        :param pulumi.Input[bool] allow_proxy: Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        :param pulumi.Input[str] cidr: The subnet CIDR.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[str] fabric: The fabric identifier (ID or name) for the new subnet.
        :param pulumi.Input[str] gateway_ip: Gateway IP address for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetIpRangeArgs']]]] ip_ranges: A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] name: The subnet name.
        :param pulumi.Input[int] rdns_mode: How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
               created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
               the appropriate CNAME resource records for the network, if the network is small enough to require the support described
               in RFC2317.
        :param pulumi.Input[str] vlan: The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
               required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Subnet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SubnetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_dns: Optional[pulumi.Input[bool]] = None,
                 allow_proxy: Optional[pulumi.Input[bool]] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 fabric: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetIpRangeArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rdns_mode: Optional[pulumi.Input[int]] = None,
                 vlan: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubnetArgs.__new__(SubnetArgs)

            __props__.__dict__["allow_dns"] = allow_dns
            __props__.__dict__["allow_proxy"] = allow_proxy
            if cidr is None and not opts.urn:
                raise TypeError("Missing required property 'cidr'")
            __props__.__dict__["cidr"] = cidr
            __props__.__dict__["dns_servers"] = dns_servers
            __props__.__dict__["fabric"] = fabric
            __props__.__dict__["gateway_ip"] = gateway_ip
            __props__.__dict__["ip_ranges"] = ip_ranges
            __props__.__dict__["name"] = name
            __props__.__dict__["rdns_mode"] = rdns_mode
            __props__.__dict__["vlan"] = vlan
        super(Subnet, __self__).__init__(
            'maas:index/subnet:Subnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_dns: Optional[pulumi.Input[bool]] = None,
            allow_proxy: Optional[pulumi.Input[bool]] = None,
            cidr: Optional[pulumi.Input[str]] = None,
            dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            fabric: Optional[pulumi.Input[str]] = None,
            gateway_ip: Optional[pulumi.Input[str]] = None,
            ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetIpRangeArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rdns_mode: Optional[pulumi.Input[int]] = None,
            vlan: Optional[pulumi.Input[str]] = None) -> 'Subnet':
        """
        Get an existing Subnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_dns: Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        :param pulumi.Input[bool] allow_proxy: Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        :param pulumi.Input[str] cidr: The subnet CIDR.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[str] fabric: The fabric identifier (ID or name) for the new subnet.
        :param pulumi.Input[str] gateway_ip: Gateway IP address for the new subnet. This argument is computed if it's not set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetIpRangeArgs']]]] ip_ranges: A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] name: The subnet name.
        :param pulumi.Input[int] rdns_mode: How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
               created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
               the appropriate CNAME resource records for the network, if the network is small enough to require the support described
               in RFC2317.
        :param pulumi.Input[str] vlan: The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
               required.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SubnetState.__new__(_SubnetState)

        __props__.__dict__["allow_dns"] = allow_dns
        __props__.__dict__["allow_proxy"] = allow_proxy
        __props__.__dict__["cidr"] = cidr
        __props__.__dict__["dns_servers"] = dns_servers
        __props__.__dict__["fabric"] = fabric
        __props__.__dict__["gateway_ip"] = gateway_ip
        __props__.__dict__["ip_ranges"] = ip_ranges
        __props__.__dict__["name"] = name
        __props__.__dict__["rdns_mode"] = rdns_mode
        __props__.__dict__["vlan"] = vlan
        return Subnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowDns")
    def allow_dns(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value that indicates if the MAAS DNS resolution is enabled for this subnet. Defaults to `true`.
        """
        return pulumi.get(self, "allow_dns")

    @property
    @pulumi.getter(name="allowProxy")
    def allow_proxy(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value that indicates if `maas-proxy` allows requests from this subnet. Defaults to `true`.
        """
        return pulumi.get(self, "allow_proxy")

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[str]:
        """
        The subnet CIDR.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> pulumi.Output[Sequence[str]]:
        """
        List of IP addresses set as DNS servers for the new subnet. This argument is computed if it's not set.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter
    def fabric(self) -> pulumi.Output[Optional[str]]:
        """
        The fabric identifier (ID or name) for the new subnet.
        """
        return pulumi.get(self, "fabric")

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> pulumi.Output[str]:
        """
        Gateway IP address for the new subnet. This argument is computed if it's not set.
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetIpRange']]]:
        """
        A set of IP ranges configured on the new subnet. Parameters defined below. This argument is processed in
        [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        return pulumi.get(self, "ip_ranges")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The subnet name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rdnsMode")
    def rdns_mode(self) -> pulumi.Output[Optional[int]]:
        """
        How reverse DNS is handled for this subnet. Defaults to `2`. Valid options are: * `0` - Disabled, no reverse zone is
        created. * `1` - Enabled, generate reverse zone. * `2` - RFC2317, extends `1` to create the necessary parent zone with
        the appropriate CNAME resource records for the network, if the network is small enough to require the support described
        in RFC2317.
        """
        return pulumi.get(self, "rdns_mode")

    @property
    @pulumi.getter
    def vlan(self) -> pulumi.Output[Optional[str]]:
        """
        The VLAN identifier (ID or traffic segregation ID) for the new subnet. If this is set, the `fabric` argument is
        required.
        """
        return pulumi.get(self, "vlan")

