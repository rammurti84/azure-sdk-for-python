# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource_py3 import ProxyOnlyResource


class AppServiceEnvironmentPatchResource(ProxyOnlyResource):
    """ARM resource for a app service environment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param app_service_environment_patch_resource_name: Required. Name of the
     App Service Environment.
    :type app_service_environment_patch_resource_name: str
    :param location: Required. Location of the App Service Environment, e.g.
     "West US".
    :type location: str
    :ivar provisioning_state: Provisioning state of the App Service
     Environment. Possible values include: 'Succeeded', 'Failed', 'Canceled',
     'InProgress', 'Deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.web.models.ProvisioningState
    :ivar status: Current status of the App Service Environment. Possible
     values include: 'Preparing', 'Ready', 'Scaling', 'Deleting'
    :vartype status: str or ~azure.mgmt.web.models.HostingEnvironmentStatus
    :param vnet_name: Name of the Virtual Network for the App Service
     Environment.
    :type vnet_name: str
    :param vnet_resource_group_name: Resource group of the Virtual Network.
    :type vnet_resource_group_name: str
    :param vnet_subnet_name: Subnet of the Virtual Network.
    :type vnet_subnet_name: str
    :param virtual_network: Required. Description of the Virtual Network.
    :type virtual_network: ~azure.mgmt.web.models.VirtualNetworkProfile
    :param internal_load_balancing_mode: Specifies which endpoints to serve
     internally in the Virtual Network for the App Service Environment.
     Possible values include: 'None', 'Web', 'Publishing'
    :type internal_load_balancing_mode: str or
     ~azure.mgmt.web.models.InternalLoadBalancingMode
    :param multi_size: Front-end VM size, e.g. "Medium", "Large".
    :type multi_size: str
    :param multi_role_count: Number of front-end instances.
    :type multi_role_count: int
    :param worker_pools: Required. Description of worker pools with worker
     size IDs, VM sizes, and number of workers in each pool.
    :type worker_pools: list[~azure.mgmt.web.models.WorkerPool]
    :param ipssl_address_count: Number of IP SSL addresses reserved for the
     App Service Environment.
    :type ipssl_address_count: int
    :ivar database_edition: Edition of the metadata database for the App
     Service Environment, e.g. "Standard".
    :vartype database_edition: str
    :ivar database_service_objective: Service objective of the metadata
     database for the App Service Environment, e.g. "S0".
    :vartype database_service_objective: str
    :ivar upgrade_domains: Number of upgrade domains of the App Service
     Environment.
    :vartype upgrade_domains: int
    :ivar subscription_id: Subscription of the App Service Environment.
    :vartype subscription_id: str
    :param dns_suffix: DNS suffix of the App Service Environment.
    :type dns_suffix: str
    :ivar last_action: Last deployment action on the App Service Environment.
    :vartype last_action: str
    :ivar last_action_result: Result of the last deployment action on the App
     Service Environment.
    :vartype last_action_result: str
    :ivar allowed_multi_sizes: List of comma separated strings describing
     which VM sizes are allowed for front-ends.
    :vartype allowed_multi_sizes: str
    :ivar allowed_worker_sizes: List of comma separated strings describing
     which VM sizes are allowed for workers.
    :vartype allowed_worker_sizes: str
    :ivar maximum_number_of_machines: Maximum number of VMs in the App Service
     Environment.
    :vartype maximum_number_of_machines: int
    :ivar vip_mappings: Description of IP SSL mapping for the App Service
     Environment.
    :vartype vip_mappings: list[~azure.mgmt.web.models.VirtualIPMapping]
    :ivar environment_capacities: Current total, used, and available worker
     capacities.
    :vartype environment_capacities:
     list[~azure.mgmt.web.models.StampCapacity]
    :param network_access_control_list: Access control list for controlling
     traffic to the App Service Environment.
    :type network_access_control_list:
     list[~azure.mgmt.web.models.NetworkAccessControlEntry]
    :ivar environment_is_healthy: True/false indicating whether the App
     Service Environment is healthy.
    :vartype environment_is_healthy: bool
    :ivar environment_status: Detailed message about with results of the last
     check of the App Service Environment.
    :vartype environment_status: str
    :ivar resource_group: Resource group of the App Service Environment.
    :vartype resource_group: str
    :param front_end_scale_factor: Scale factor for front-ends.
    :type front_end_scale_factor: int
    :ivar default_front_end_scale_factor: Default Scale Factor for FrontEnds.
    :vartype default_front_end_scale_factor: int
    :param api_management_account_id: API Management Account associated with
     the App Service Environment.
    :type api_management_account_id: str
    :param suspended: <code>true</code> if the App Service Environment is
     suspended; otherwise, <code>false</code>. The environment can be
     suspended, e.g. when the management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic).
    :type suspended: bool
    :param dynamic_cache_enabled: True/false indicating whether the App
     Service Environment is suspended. The environment can be suspended e.g.
     when the management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic).
    :type dynamic_cache_enabled: bool
    :param cluster_settings: Custom settings for changing the behavior of the
     App Service Environment.
    :type cluster_settings: list[~azure.mgmt.web.models.NameValuePair]
    :param user_whitelisted_ip_ranges: User added ip ranges to whitelist on
     ASE db
    :type user_whitelisted_ip_ranges: list[str]
    :param has_linux_workers: Flag that displays whether an ASE has linux
     workers or not
    :type has_linux_workers: bool
    :param ssl_cert_key_vault_id: Key Vault ID for ILB App Service Environment
     default SSL certificate
    :type ssl_cert_key_vault_id: str
    :param ssl_cert_key_vault_secret_name: Key Vault Secret Name for ILB App
     Service Environment default SSL certificate
    :type ssl_cert_key_vault_secret_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'app_service_environment_patch_resource_name': {'required': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'virtual_network': {'required': True},
        'worker_pools': {'required': True},
        'database_edition': {'readonly': True},
        'database_service_objective': {'readonly': True},
        'upgrade_domains': {'readonly': True},
        'subscription_id': {'readonly': True},
        'last_action': {'readonly': True},
        'last_action_result': {'readonly': True},
        'allowed_multi_sizes': {'readonly': True},
        'allowed_worker_sizes': {'readonly': True},
        'maximum_number_of_machines': {'readonly': True},
        'vip_mappings': {'readonly': True},
        'environment_capacities': {'readonly': True},
        'environment_is_healthy': {'readonly': True},
        'environment_status': {'readonly': True},
        'resource_group': {'readonly': True},
        'default_front_end_scale_factor': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'app_service_environment_patch_resource_name': {'key': 'properties.name', 'type': 'str'},
        'location': {'key': 'properties.location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'status': {'key': 'properties.status', 'type': 'HostingEnvironmentStatus'},
        'vnet_name': {'key': 'properties.vnetName', 'type': 'str'},
        'vnet_resource_group_name': {'key': 'properties.vnetResourceGroupName', 'type': 'str'},
        'vnet_subnet_name': {'key': 'properties.vnetSubnetName', 'type': 'str'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'VirtualNetworkProfile'},
        'internal_load_balancing_mode': {'key': 'properties.internalLoadBalancingMode', 'type': 'InternalLoadBalancingMode'},
        'multi_size': {'key': 'properties.multiSize', 'type': 'str'},
        'multi_role_count': {'key': 'properties.multiRoleCount', 'type': 'int'},
        'worker_pools': {'key': 'properties.workerPools', 'type': '[WorkerPool]'},
        'ipssl_address_count': {'key': 'properties.ipsslAddressCount', 'type': 'int'},
        'database_edition': {'key': 'properties.databaseEdition', 'type': 'str'},
        'database_service_objective': {'key': 'properties.databaseServiceObjective', 'type': 'str'},
        'upgrade_domains': {'key': 'properties.upgradeDomains', 'type': 'int'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'dns_suffix': {'key': 'properties.dnsSuffix', 'type': 'str'},
        'last_action': {'key': 'properties.lastAction', 'type': 'str'},
        'last_action_result': {'key': 'properties.lastActionResult', 'type': 'str'},
        'allowed_multi_sizes': {'key': 'properties.allowedMultiSizes', 'type': 'str'},
        'allowed_worker_sizes': {'key': 'properties.allowedWorkerSizes', 'type': 'str'},
        'maximum_number_of_machines': {'key': 'properties.maximumNumberOfMachines', 'type': 'int'},
        'vip_mappings': {'key': 'properties.vipMappings', 'type': '[VirtualIPMapping]'},
        'environment_capacities': {'key': 'properties.environmentCapacities', 'type': '[StampCapacity]'},
        'network_access_control_list': {'key': 'properties.networkAccessControlList', 'type': '[NetworkAccessControlEntry]'},
        'environment_is_healthy': {'key': 'properties.environmentIsHealthy', 'type': 'bool'},
        'environment_status': {'key': 'properties.environmentStatus', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'front_end_scale_factor': {'key': 'properties.frontEndScaleFactor', 'type': 'int'},
        'default_front_end_scale_factor': {'key': 'properties.defaultFrontEndScaleFactor', 'type': 'int'},
        'api_management_account_id': {'key': 'properties.apiManagementAccountId', 'type': 'str'},
        'suspended': {'key': 'properties.suspended', 'type': 'bool'},
        'dynamic_cache_enabled': {'key': 'properties.dynamicCacheEnabled', 'type': 'bool'},
        'cluster_settings': {'key': 'properties.clusterSettings', 'type': '[NameValuePair]'},
        'user_whitelisted_ip_ranges': {'key': 'properties.userWhitelistedIpRanges', 'type': '[str]'},
        'has_linux_workers': {'key': 'properties.hasLinuxWorkers', 'type': 'bool'},
        'ssl_cert_key_vault_id': {'key': 'properties.sslCertKeyVaultId', 'type': 'str'},
        'ssl_cert_key_vault_secret_name': {'key': 'properties.sslCertKeyVaultSecretName', 'type': 'str'},
    }

    def __init__(self, *, app_service_environment_patch_resource_name: str, location: str, virtual_network, worker_pools, kind: str=None, vnet_name: str=None, vnet_resource_group_name: str=None, vnet_subnet_name: str=None, internal_load_balancing_mode=None, multi_size: str=None, multi_role_count: int=None, ipssl_address_count: int=None, dns_suffix: str=None, network_access_control_list=None, front_end_scale_factor: int=None, api_management_account_id: str=None, suspended: bool=None, dynamic_cache_enabled: bool=None, cluster_settings=None, user_whitelisted_ip_ranges=None, has_linux_workers: bool=None, ssl_cert_key_vault_id: str=None, ssl_cert_key_vault_secret_name: str=None, **kwargs) -> None:
        super(AppServiceEnvironmentPatchResource, self).__init__(kind=kind, **kwargs)
        self.app_service_environment_patch_resource_name = app_service_environment_patch_resource_name
        self.location = location
        self.provisioning_state = None
        self.status = None
        self.vnet_name = vnet_name
        self.vnet_resource_group_name = vnet_resource_group_name
        self.vnet_subnet_name = vnet_subnet_name
        self.virtual_network = virtual_network
        self.internal_load_balancing_mode = internal_load_balancing_mode
        self.multi_size = multi_size
        self.multi_role_count = multi_role_count
        self.worker_pools = worker_pools
        self.ipssl_address_count = ipssl_address_count
        self.database_edition = None
        self.database_service_objective = None
        self.upgrade_domains = None
        self.subscription_id = None
        self.dns_suffix = dns_suffix
        self.last_action = None
        self.last_action_result = None
        self.allowed_multi_sizes = None
        self.allowed_worker_sizes = None
        self.maximum_number_of_machines = None
        self.vip_mappings = None
        self.environment_capacities = None
        self.network_access_control_list = network_access_control_list
        self.environment_is_healthy = None
        self.environment_status = None
        self.resource_group = None
        self.front_end_scale_factor = front_end_scale_factor
        self.default_front_end_scale_factor = None
        self.api_management_account_id = api_management_account_id
        self.suspended = suspended
        self.dynamic_cache_enabled = dynamic_cache_enabled
        self.cluster_settings = cluster_settings
        self.user_whitelisted_ip_ranges = user_whitelisted_ip_ranges
        self.has_linux_workers = has_linux_workers
        self.ssl_cert_key_vault_id = ssl_cert_key_vault_id
        self.ssl_cert_key_vault_secret_name = ssl_cert_key_vault_secret_name
