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

from msrest.serialization import Model


class GpuResource(Model):
    """The GPU resource.

    All required parameters must be populated in order to send to Azure.

    :param count: Required. The count of the GPU resource.
    :type count: int
    :param sku: Required. The SKU of the GPU resource. Possible values
     include: 'K80', 'P100', 'V100'
    :type sku: str or ~azure.mgmt.containerinstance.models.GpuSku
    """

    _validation = {
        'count': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'sku': {'key': 'sku', 'type': 'str'},
    }

    def __init__(self, *, count: int, sku, **kwargs) -> None:
        super(GpuResource, self).__init__(**kwargs)
        self.count = count
        self.sku = sku
