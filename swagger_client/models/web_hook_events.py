# coding: utf-8

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WebHookEvents(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dataset_creation': 'bool',
        'dataset_processing': 'bool',
        'dataset_completion': 'bool',
        'dataset_deletion': 'bool',
        'model_creation': 'bool',
        'model_processing': 'bool',
        'model_completion': 'bool',
        'model_deletion': 'bool',
        'evaluation_creation': 'bool',
        'evaluation_processing': 'bool',
        'evaluation_completion': 'bool',
        'evaluation_deletion': 'bool',
        'transcription_creation': 'bool',
        'transcription_processing': 'bool',
        'transcription_completion': 'bool',
        'transcription_deletion': 'bool',
        'endpoint_creation': 'bool',
        'endpoint_processing': 'bool',
        'endpoint_completion': 'bool',
        'endpoint_deletion': 'bool',
        'ping': 'bool',
        'challenge': 'bool'
    }

    attribute_map = {
        'dataset_creation': 'datasetCreation',
        'dataset_processing': 'datasetProcessing',
        'dataset_completion': 'datasetCompletion',
        'dataset_deletion': 'datasetDeletion',
        'model_creation': 'modelCreation',
        'model_processing': 'modelProcessing',
        'model_completion': 'modelCompletion',
        'model_deletion': 'modelDeletion',
        'evaluation_creation': 'evaluationCreation',
        'evaluation_processing': 'evaluationProcessing',
        'evaluation_completion': 'evaluationCompletion',
        'evaluation_deletion': 'evaluationDeletion',
        'transcription_creation': 'transcriptionCreation',
        'transcription_processing': 'transcriptionProcessing',
        'transcription_completion': 'transcriptionCompletion',
        'transcription_deletion': 'transcriptionDeletion',
        'endpoint_creation': 'endpointCreation',
        'endpoint_processing': 'endpointProcessing',
        'endpoint_completion': 'endpointCompletion',
        'endpoint_deletion': 'endpointDeletion',
        'ping': 'ping',
        'challenge': 'challenge'
    }

    def __init__(self, dataset_creation=None, dataset_processing=None, dataset_completion=None, dataset_deletion=None, model_creation=None, model_processing=None, model_completion=None, model_deletion=None, evaluation_creation=None, evaluation_processing=None, evaluation_completion=None, evaluation_deletion=None, transcription_creation=None, transcription_processing=None, transcription_completion=None, transcription_deletion=None, endpoint_creation=None, endpoint_processing=None, endpoint_completion=None, endpoint_deletion=None, ping=None, challenge=None):  # noqa: E501
        """WebHookEvents - a model defined in Swagger"""  # noqa: E501

        self._dataset_creation = None
        self._dataset_processing = None
        self._dataset_completion = None
        self._dataset_deletion = None
        self._model_creation = None
        self._model_processing = None
        self._model_completion = None
        self._model_deletion = None
        self._evaluation_creation = None
        self._evaluation_processing = None
        self._evaluation_completion = None
        self._evaluation_deletion = None
        self._transcription_creation = None
        self._transcription_processing = None
        self._transcription_completion = None
        self._transcription_deletion = None
        self._endpoint_creation = None
        self._endpoint_processing = None
        self._endpoint_completion = None
        self._endpoint_deletion = None
        self._ping = None
        self._challenge = None
        self.discriminator = None

        if dataset_creation is not None:
            self.dataset_creation = dataset_creation
        if dataset_processing is not None:
            self.dataset_processing = dataset_processing
        if dataset_completion is not None:
            self.dataset_completion = dataset_completion
        if dataset_deletion is not None:
            self.dataset_deletion = dataset_deletion
        if model_creation is not None:
            self.model_creation = model_creation
        if model_processing is not None:
            self.model_processing = model_processing
        if model_completion is not None:
            self.model_completion = model_completion
        if model_deletion is not None:
            self.model_deletion = model_deletion
        if evaluation_creation is not None:
            self.evaluation_creation = evaluation_creation
        if evaluation_processing is not None:
            self.evaluation_processing = evaluation_processing
        if evaluation_completion is not None:
            self.evaluation_completion = evaluation_completion
        if evaluation_deletion is not None:
            self.evaluation_deletion = evaluation_deletion
        if transcription_creation is not None:
            self.transcription_creation = transcription_creation
        if transcription_processing is not None:
            self.transcription_processing = transcription_processing
        if transcription_completion is not None:
            self.transcription_completion = transcription_completion
        if transcription_deletion is not None:
            self.transcription_deletion = transcription_deletion
        if endpoint_creation is not None:
            self.endpoint_creation = endpoint_creation
        if endpoint_processing is not None:
            self.endpoint_processing = endpoint_processing
        if endpoint_completion is not None:
            self.endpoint_completion = endpoint_completion
        if endpoint_deletion is not None:
            self.endpoint_deletion = endpoint_deletion
        if ping is not None:
            self.ping = ping
        if challenge is not None:
            self.challenge = challenge

    @property
    def dataset_creation(self):
        """Gets the dataset_creation of this WebHookEvents.  # noqa: E501


        :return: The dataset_creation of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._dataset_creation

    @dataset_creation.setter
    def dataset_creation(self, dataset_creation):
        """Sets the dataset_creation of this WebHookEvents.


        :param dataset_creation: The dataset_creation of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._dataset_creation = dataset_creation

    @property
    def dataset_processing(self):
        """Gets the dataset_processing of this WebHookEvents.  # noqa: E501


        :return: The dataset_processing of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._dataset_processing

    @dataset_processing.setter
    def dataset_processing(self, dataset_processing):
        """Sets the dataset_processing of this WebHookEvents.


        :param dataset_processing: The dataset_processing of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._dataset_processing = dataset_processing

    @property
    def dataset_completion(self):
        """Gets the dataset_completion of this WebHookEvents.  # noqa: E501


        :return: The dataset_completion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._dataset_completion

    @dataset_completion.setter
    def dataset_completion(self, dataset_completion):
        """Sets the dataset_completion of this WebHookEvents.


        :param dataset_completion: The dataset_completion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._dataset_completion = dataset_completion

    @property
    def dataset_deletion(self):
        """Gets the dataset_deletion of this WebHookEvents.  # noqa: E501


        :return: The dataset_deletion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._dataset_deletion

    @dataset_deletion.setter
    def dataset_deletion(self, dataset_deletion):
        """Sets the dataset_deletion of this WebHookEvents.


        :param dataset_deletion: The dataset_deletion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._dataset_deletion = dataset_deletion

    @property
    def model_creation(self):
        """Gets the model_creation of this WebHookEvents.  # noqa: E501


        :return: The model_creation of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._model_creation

    @model_creation.setter
    def model_creation(self, model_creation):
        """Sets the model_creation of this WebHookEvents.


        :param model_creation: The model_creation of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._model_creation = model_creation

    @property
    def model_processing(self):
        """Gets the model_processing of this WebHookEvents.  # noqa: E501


        :return: The model_processing of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._model_processing

    @model_processing.setter
    def model_processing(self, model_processing):
        """Sets the model_processing of this WebHookEvents.


        :param model_processing: The model_processing of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._model_processing = model_processing

    @property
    def model_completion(self):
        """Gets the model_completion of this WebHookEvents.  # noqa: E501


        :return: The model_completion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._model_completion

    @model_completion.setter
    def model_completion(self, model_completion):
        """Sets the model_completion of this WebHookEvents.


        :param model_completion: The model_completion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._model_completion = model_completion

    @property
    def model_deletion(self):
        """Gets the model_deletion of this WebHookEvents.  # noqa: E501


        :return: The model_deletion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._model_deletion

    @model_deletion.setter
    def model_deletion(self, model_deletion):
        """Sets the model_deletion of this WebHookEvents.


        :param model_deletion: The model_deletion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._model_deletion = model_deletion

    @property
    def evaluation_creation(self):
        """Gets the evaluation_creation of this WebHookEvents.  # noqa: E501


        :return: The evaluation_creation of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._evaluation_creation

    @evaluation_creation.setter
    def evaluation_creation(self, evaluation_creation):
        """Sets the evaluation_creation of this WebHookEvents.


        :param evaluation_creation: The evaluation_creation of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._evaluation_creation = evaluation_creation

    @property
    def evaluation_processing(self):
        """Gets the evaluation_processing of this WebHookEvents.  # noqa: E501


        :return: The evaluation_processing of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._evaluation_processing

    @evaluation_processing.setter
    def evaluation_processing(self, evaluation_processing):
        """Sets the evaluation_processing of this WebHookEvents.


        :param evaluation_processing: The evaluation_processing of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._evaluation_processing = evaluation_processing

    @property
    def evaluation_completion(self):
        """Gets the evaluation_completion of this WebHookEvents.  # noqa: E501


        :return: The evaluation_completion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._evaluation_completion

    @evaluation_completion.setter
    def evaluation_completion(self, evaluation_completion):
        """Sets the evaluation_completion of this WebHookEvents.


        :param evaluation_completion: The evaluation_completion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._evaluation_completion = evaluation_completion

    @property
    def evaluation_deletion(self):
        """Gets the evaluation_deletion of this WebHookEvents.  # noqa: E501


        :return: The evaluation_deletion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._evaluation_deletion

    @evaluation_deletion.setter
    def evaluation_deletion(self, evaluation_deletion):
        """Sets the evaluation_deletion of this WebHookEvents.


        :param evaluation_deletion: The evaluation_deletion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._evaluation_deletion = evaluation_deletion

    @property
    def transcription_creation(self):
        """Gets the transcription_creation of this WebHookEvents.  # noqa: E501


        :return: The transcription_creation of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._transcription_creation

    @transcription_creation.setter
    def transcription_creation(self, transcription_creation):
        """Sets the transcription_creation of this WebHookEvents.


        :param transcription_creation: The transcription_creation of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._transcription_creation = transcription_creation

    @property
    def transcription_processing(self):
        """Gets the transcription_processing of this WebHookEvents.  # noqa: E501


        :return: The transcription_processing of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._transcription_processing

    @transcription_processing.setter
    def transcription_processing(self, transcription_processing):
        """Sets the transcription_processing of this WebHookEvents.


        :param transcription_processing: The transcription_processing of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._transcription_processing = transcription_processing

    @property
    def transcription_completion(self):
        """Gets the transcription_completion of this WebHookEvents.  # noqa: E501


        :return: The transcription_completion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._transcription_completion

    @transcription_completion.setter
    def transcription_completion(self, transcription_completion):
        """Sets the transcription_completion of this WebHookEvents.


        :param transcription_completion: The transcription_completion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._transcription_completion = transcription_completion

    @property
    def transcription_deletion(self):
        """Gets the transcription_deletion of this WebHookEvents.  # noqa: E501


        :return: The transcription_deletion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._transcription_deletion

    @transcription_deletion.setter
    def transcription_deletion(self, transcription_deletion):
        """Sets the transcription_deletion of this WebHookEvents.


        :param transcription_deletion: The transcription_deletion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._transcription_deletion = transcription_deletion

    @property
    def endpoint_creation(self):
        """Gets the endpoint_creation of this WebHookEvents.  # noqa: E501


        :return: The endpoint_creation of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._endpoint_creation

    @endpoint_creation.setter
    def endpoint_creation(self, endpoint_creation):
        """Sets the endpoint_creation of this WebHookEvents.


        :param endpoint_creation: The endpoint_creation of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._endpoint_creation = endpoint_creation

    @property
    def endpoint_processing(self):
        """Gets the endpoint_processing of this WebHookEvents.  # noqa: E501


        :return: The endpoint_processing of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._endpoint_processing

    @endpoint_processing.setter
    def endpoint_processing(self, endpoint_processing):
        """Sets the endpoint_processing of this WebHookEvents.


        :param endpoint_processing: The endpoint_processing of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._endpoint_processing = endpoint_processing

    @property
    def endpoint_completion(self):
        """Gets the endpoint_completion of this WebHookEvents.  # noqa: E501


        :return: The endpoint_completion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._endpoint_completion

    @endpoint_completion.setter
    def endpoint_completion(self, endpoint_completion):
        """Sets the endpoint_completion of this WebHookEvents.


        :param endpoint_completion: The endpoint_completion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._endpoint_completion = endpoint_completion

    @property
    def endpoint_deletion(self):
        """Gets the endpoint_deletion of this WebHookEvents.  # noqa: E501


        :return: The endpoint_deletion of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._endpoint_deletion

    @endpoint_deletion.setter
    def endpoint_deletion(self, endpoint_deletion):
        """Sets the endpoint_deletion of this WebHookEvents.


        :param endpoint_deletion: The endpoint_deletion of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._endpoint_deletion = endpoint_deletion

    @property
    def ping(self):
        """Gets the ping of this WebHookEvents.  # noqa: E501


        :return: The ping of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._ping

    @ping.setter
    def ping(self, ping):
        """Sets the ping of this WebHookEvents.


        :param ping: The ping of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._ping = ping

    @property
    def challenge(self):
        """Gets the challenge of this WebHookEvents.  # noqa: E501


        :return: The challenge of this WebHookEvents.  # noqa: E501
        :rtype: bool
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this WebHookEvents.


        :param challenge: The challenge of this WebHookEvents.  # noqa: E501
        :type: bool
        """

        self._challenge = challenge

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebHookEvents, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebHookEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
