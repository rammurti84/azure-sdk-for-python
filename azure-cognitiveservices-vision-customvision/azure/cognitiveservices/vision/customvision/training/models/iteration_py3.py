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


class Iteration(Model):
    """Iteration model to be sent over JSON.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Gets the id of the iteration.
    :vartype id: str
    :param name: Required. Gets or sets the name of the iteration.
    :type name: str
    :ivar status: Gets the current iteration status.
    :vartype status: str
    :ivar created: Gets the time this iteration was completed.
    :vartype created: datetime
    :ivar last_modified: Gets the time this iteration was last modified.
    :vartype last_modified: datetime
    :ivar trained_at: Gets the time this iteration was last modified.
    :vartype trained_at: datetime
    :ivar project_id: Gets the project id of the iteration.
    :vartype project_id: str
    :ivar exportable: Whether the iteration can be exported to another format
     for download.
    :vartype exportable: bool
    :ivar exportable_to: A set of platforms this iteration can export to.
    :vartype exportable_to: list[str]
    :ivar domain_id: Get or sets a guid of the domain the iteration has been
     trained on.
    :vartype domain_id: str
    :ivar classification_type: Gets the classification type of the project.
     Possible values include: 'Multiclass', 'Multilabel'
    :vartype classification_type: str or
     ~azure.cognitiveservices.vision.customvision.training.models.Classifier
    :ivar training_type: Gets the training type of the iteration. Possible
     values include: 'Regular', 'Advanced'
    :vartype training_type: str or
     ~azure.cognitiveservices.vision.customvision.training.models.TrainingType
    :ivar reserved_budget_in_hours: Gets the reserved advanced training budget
     for the iteration.
    :vartype reserved_budget_in_hours: int
    :ivar publish_name: Name of the published model.
    :vartype publish_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'status': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
        'trained_at': {'readonly': True},
        'project_id': {'readonly': True},
        'exportable': {'readonly': True},
        'exportable_to': {'readonly': True},
        'domain_id': {'readonly': True},
        'classification_type': {'readonly': True},
        'training_type': {'readonly': True},
        'reserved_budget_in_hours': {'readonly': True},
        'publish_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'trained_at': {'key': 'trainedAt', 'type': 'iso-8601'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'exportable': {'key': 'exportable', 'type': 'bool'},
        'exportable_to': {'key': 'exportableTo', 'type': '[str]'},
        'domain_id': {'key': 'domainId', 'type': 'str'},
        'classification_type': {'key': 'classificationType', 'type': 'str'},
        'training_type': {'key': 'trainingType', 'type': 'str'},
        'reserved_budget_in_hours': {'key': 'reservedBudgetInHours', 'type': 'int'},
        'publish_name': {'key': 'publishName', 'type': 'str'},
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(Iteration, self).__init__(**kwargs)
        self.id = None
        self.name = name
        self.status = None
        self.created = None
        self.last_modified = None
        self.trained_at = None
        self.project_id = None
        self.exportable = None
        self.exportable_to = None
        self.domain_id = None
        self.classification_type = None
        self.training_type = None
        self.reserved_budget_in_hours = None
        self.publish_name = None
