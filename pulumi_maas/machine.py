# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MachineArgs', 'Machine']

@pulumi.input_type
class MachineArgs:
    def __init__(__self__, *,
                 power_parameters: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 power_type: pulumi.Input[str],
                 pxe_mac_address: pulumi.Input[str],
                 architecture: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 min_hwe_kernel: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Machine resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] power_parameters: A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
               for a list of the available power parameters for each power type.
        :param pulumi.Input[str] power_type: A power management type (e.g. `ipmi`).
        :param pulumi.Input[str] pxe_mac_address: The MAC address of the machine's PXE boot NIC.
        :param pulumi.Input[str] architecture: The architecture type of the machine. Defaults to `amd64/generic`.
        :param pulumi.Input[str] domain: The domain of the machine. This is computed if it's not set.
        :param pulumi.Input[str] hostname: The machine hostname. This is computed if it's not set.
        :param pulumi.Input[str] min_hwe_kernel: The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
               set.
        :param pulumi.Input[str] pool: The resource pool of the machine. This is computed if it's not set.
        :param pulumi.Input[str] zone: The zone of the machine. This is computed if it's not set.
        """
        pulumi.set(__self__, "power_parameters", power_parameters)
        pulumi.set(__self__, "power_type", power_type)
        pulumi.set(__self__, "pxe_mac_address", pxe_mac_address)
        if architecture is not None:
            pulumi.set(__self__, "architecture", architecture)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if min_hwe_kernel is not None:
            pulumi.set(__self__, "min_hwe_kernel", min_hwe_kernel)
        if pool is not None:
            pulumi.set(__self__, "pool", pool)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="powerParameters")
    def power_parameters(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
        for a list of the available power parameters for each power type.
        """
        return pulumi.get(self, "power_parameters")

    @power_parameters.setter
    def power_parameters(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "power_parameters", value)

    @property
    @pulumi.getter(name="powerType")
    def power_type(self) -> pulumi.Input[str]:
        """
        A power management type (e.g. `ipmi`).
        """
        return pulumi.get(self, "power_type")

    @power_type.setter
    def power_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "power_type", value)

    @property
    @pulumi.getter(name="pxeMacAddress")
    def pxe_mac_address(self) -> pulumi.Input[str]:
        """
        The MAC address of the machine's PXE boot NIC.
        """
        return pulumi.get(self, "pxe_mac_address")

    @pxe_mac_address.setter
    def pxe_mac_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "pxe_mac_address", value)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[str]]:
        """
        The architecture type of the machine. Defaults to `amd64/generic`.
        """
        return pulumi.get(self, "architecture")

    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "architecture", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The machine hostname. This is computed if it's not set.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="minHweKernel")
    def min_hwe_kernel(self) -> Optional[pulumi.Input[str]]:
        """
        The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
        set.
        """
        return pulumi.get(self, "min_hwe_kernel")

    @min_hwe_kernel.setter
    def min_hwe_kernel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "min_hwe_kernel", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        """
        The resource pool of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _MachineState:
    def __init__(__self__, *,
                 architecture: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 min_hwe_kernel: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 power_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 power_type: Optional[pulumi.Input[str]] = None,
                 pxe_mac_address: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Machine resources.
        :param pulumi.Input[str] architecture: The architecture type of the machine. Defaults to `amd64/generic`.
        :param pulumi.Input[str] domain: The domain of the machine. This is computed if it's not set.
        :param pulumi.Input[str] hostname: The machine hostname. This is computed if it's not set.
        :param pulumi.Input[str] min_hwe_kernel: The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
               set.
        :param pulumi.Input[str] pool: The resource pool of the machine. This is computed if it's not set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] power_parameters: A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
               for a list of the available power parameters for each power type.
        :param pulumi.Input[str] power_type: A power management type (e.g. `ipmi`).
        :param pulumi.Input[str] pxe_mac_address: The MAC address of the machine's PXE boot NIC.
        :param pulumi.Input[str] zone: The zone of the machine. This is computed if it's not set.
        """
        if architecture is not None:
            pulumi.set(__self__, "architecture", architecture)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if min_hwe_kernel is not None:
            pulumi.set(__self__, "min_hwe_kernel", min_hwe_kernel)
        if pool is not None:
            pulumi.set(__self__, "pool", pool)
        if power_parameters is not None:
            pulumi.set(__self__, "power_parameters", power_parameters)
        if power_type is not None:
            pulumi.set(__self__, "power_type", power_type)
        if pxe_mac_address is not None:
            pulumi.set(__self__, "pxe_mac_address", pxe_mac_address)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[str]]:
        """
        The architecture type of the machine. Defaults to `amd64/generic`.
        """
        return pulumi.get(self, "architecture")

    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "architecture", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The machine hostname. This is computed if it's not set.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="minHweKernel")
    def min_hwe_kernel(self) -> Optional[pulumi.Input[str]]:
        """
        The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
        set.
        """
        return pulumi.get(self, "min_hwe_kernel")

    @min_hwe_kernel.setter
    def min_hwe_kernel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "min_hwe_kernel", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        """
        The resource pool of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter(name="powerParameters")
    def power_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
        for a list of the available power parameters for each power type.
        """
        return pulumi.get(self, "power_parameters")

    @power_parameters.setter
    def power_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "power_parameters", value)

    @property
    @pulumi.getter(name="powerType")
    def power_type(self) -> Optional[pulumi.Input[str]]:
        """
        A power management type (e.g. `ipmi`).
        """
        return pulumi.get(self, "power_type")

    @power_type.setter
    def power_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "power_type", value)

    @property
    @pulumi.getter(name="pxeMacAddress")
    def pxe_mac_address(self) -> Optional[pulumi.Input[str]]:
        """
        The MAC address of the machine's PXE boot NIC.
        """
        return pulumi.get(self, "pxe_mac_address")

    @pxe_mac_address.setter
    def pxe_mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pxe_mac_address", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class Machine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 min_hwe_kernel: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 power_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 power_type: Optional[pulumi.Input[str]] = None,
                 pxe_mac_address: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Machine resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: The architecture type of the machine. Defaults to `amd64/generic`.
        :param pulumi.Input[str] domain: The domain of the machine. This is computed if it's not set.
        :param pulumi.Input[str] hostname: The machine hostname. This is computed if it's not set.
        :param pulumi.Input[str] min_hwe_kernel: The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
               set.
        :param pulumi.Input[str] pool: The resource pool of the machine. This is computed if it's not set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] power_parameters: A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
               for a list of the available power parameters for each power type.
        :param pulumi.Input[str] power_type: A power management type (e.g. `ipmi`).
        :param pulumi.Input[str] pxe_mac_address: The MAC address of the machine's PXE boot NIC.
        :param pulumi.Input[str] zone: The zone of the machine. This is computed if it's not set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MachineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Machine resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MachineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MachineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 min_hwe_kernel: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 power_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 power_type: Optional[pulumi.Input[str]] = None,
                 pxe_mac_address: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MachineArgs.__new__(MachineArgs)

            __props__.__dict__["architecture"] = architecture
            __props__.__dict__["domain"] = domain
            __props__.__dict__["hostname"] = hostname
            __props__.__dict__["min_hwe_kernel"] = min_hwe_kernel
            __props__.__dict__["pool"] = pool
            if power_parameters is None and not opts.urn:
                raise TypeError("Missing required property 'power_parameters'")
            __props__.__dict__["power_parameters"] = None if power_parameters is None else pulumi.Output.secret(power_parameters)
            if power_type is None and not opts.urn:
                raise TypeError("Missing required property 'power_type'")
            __props__.__dict__["power_type"] = power_type
            if pxe_mac_address is None and not opts.urn:
                raise TypeError("Missing required property 'pxe_mac_address'")
            __props__.__dict__["pxe_mac_address"] = pxe_mac_address
            __props__.__dict__["zone"] = zone
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["powerParameters"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Machine, __self__).__init__(
            'maas:index/machine:Machine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            architecture: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            min_hwe_kernel: Optional[pulumi.Input[str]] = None,
            pool: Optional[pulumi.Input[str]] = None,
            power_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            power_type: Optional[pulumi.Input[str]] = None,
            pxe_mac_address: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Machine':
        """
        Get an existing Machine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: The architecture type of the machine. Defaults to `amd64/generic`.
        :param pulumi.Input[str] domain: The domain of the machine. This is computed if it's not set.
        :param pulumi.Input[str] hostname: The machine hostname. This is computed if it's not set.
        :param pulumi.Input[str] min_hwe_kernel: The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
               set.
        :param pulumi.Input[str] pool: The resource pool of the machine. This is computed if it's not set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] power_parameters: A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
               for a list of the available power parameters for each power type.
        :param pulumi.Input[str] power_type: A power management type (e.g. `ipmi`).
        :param pulumi.Input[str] pxe_mac_address: The MAC address of the machine's PXE boot NIC.
        :param pulumi.Input[str] zone: The zone of the machine. This is computed if it's not set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MachineState.__new__(_MachineState)

        __props__.__dict__["architecture"] = architecture
        __props__.__dict__["domain"] = domain
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["min_hwe_kernel"] = min_hwe_kernel
        __props__.__dict__["pool"] = pool
        __props__.__dict__["power_parameters"] = power_parameters
        __props__.__dict__["power_type"] = power_type
        __props__.__dict__["pxe_mac_address"] = pxe_mac_address
        __props__.__dict__["zone"] = zone
        return Machine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional[str]]:
        """
        The architecture type of the machine. Defaults to `amd64/generic`.
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The machine hostname. This is computed if it's not set.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="minHweKernel")
    def min_hwe_kernel(self) -> pulumi.Output[str]:
        """
        The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
        set.
        """
        return pulumi.get(self, "min_hwe_kernel")

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Output[str]:
        """
        The resource pool of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "pool")

    @property
    @pulumi.getter(name="powerParameters")
    def power_parameters(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
        for a list of the available power parameters for each power type.
        """
        return pulumi.get(self, "power_parameters")

    @property
    @pulumi.getter(name="powerType")
    def power_type(self) -> pulumi.Output[str]:
        """
        A power management type (e.g. `ipmi`).
        """
        return pulumi.get(self, "power_type")

    @property
    @pulumi.getter(name="pxeMacAddress")
    def pxe_mac_address(self) -> pulumi.Output[str]:
        """
        The MAC address of the machine's PXE boot NIC.
        """
        return pulumi.get(self, "pxe_mac_address")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The zone of the machine. This is computed if it's not set.
        """
        return pulumi.get(self, "zone")
