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

from .resource import Resource


class BillingAccount(Resource):
    """A billing account resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar company: The Company this billing account belongs to.
    :vartype company: str
    :ivar account_type: The billing account Type. Possible values include:
     'CommerceRoot', 'Enrollment'
    :vartype account_type: str or ~azure.mgmt.consumption.models.enum
    :param address: The address associated with billing account.
    :type address: ~azure.mgmt.consumption.models.Address
    :ivar default_currency: The ISO currency, for example, USD.
    :vartype default_currency: str
    :ivar country: The country associated with billing account.
    :vartype country: str
    :ivar agreements: Agreements associated with billing account
    :vartype agreements: str
    :ivar invoice_sections: The invoiceSections associated to the billing
     account.
    :vartype invoice_sections:
     list[~azure.mgmt.consumption.models.InvoiceSection]
    :ivar billing_profiles: The billing profiles associated to the billing
     account.
    :vartype billing_profiles:
     list[~azure.mgmt.consumption.models.BillingProfile]
    :ivar enrollment_details: The details about the associated legacy
     enrollment. By default this is not populated, unless it's specified in
     $expand.
    :vartype enrollment_details: ~azure.mgmt.consumption.models.Enrollment
    :ivar departments: The departments associated to the enrollment.
    :vartype departments: list[~azure.mgmt.consumption.models.Department]
    :ivar enrollment_accounts: The accounts associated to the enrollment.
    :vartype enrollment_accounts:
     list[~azure.mgmt.consumption.models.EnrollmentAccount]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'company': {'readonly': True},
        'account_type': {'readonly': True},
        'default_currency': {'readonly': True},
        'country': {'readonly': True},
        'agreements': {'readonly': True},
        'invoice_sections': {'readonly': True},
        'billing_profiles': {'readonly': True},
        'enrollment_details': {'readonly': True},
        'departments': {'readonly': True},
        'enrollment_accounts': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'company': {'key': 'properties.company', 'type': 'str'},
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
        'address': {'key': 'properties.address', 'type': 'Address'},
        'default_currency': {'key': 'properties.defaultCurrency', 'type': 'str'},
        'country': {'key': 'properties.country', 'type': 'str'},
        'agreements': {'key': 'properties.agreements', 'type': 'str'},
        'invoice_sections': {'key': 'properties.invoiceSections', 'type': '[InvoiceSection]'},
        'billing_profiles': {'key': 'properties.billingProfiles', 'type': '[BillingProfile]'},
        'enrollment_details': {'key': 'properties.enrollmentDetails', 'type': 'Enrollment'},
        'departments': {'key': 'properties.departments', 'type': '[Department]'},
        'enrollment_accounts': {'key': 'properties.enrollmentAccounts', 'type': '[EnrollmentAccount]'},
    }

    def __init__(self, **kwargs):
        super(BillingAccount, self).__init__(**kwargs)
        self.company = None
        self.account_type = None
        self.address = kwargs.get('address', None)
        self.default_currency = None
        self.country = None
        self.agreements = None
        self.invoice_sections = None
        self.billing_profiles = None
        self.enrollment_details = None
        self.departments = None
        self.enrollment_accounts = None
