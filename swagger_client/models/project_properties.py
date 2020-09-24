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


class ProjectProperties(object):
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
        'dataset_count': 'int',
        'evaluation_count': 'int',
        'model_count': 'int',
        'transcription_count': 'int',
        'endpoint_count': 'int'
    }

    attribute_map = {
        'dataset_count': 'datasetCount',
        'evaluation_count': 'evaluationCount',
        'model_count': 'modelCount',
        'transcription_count': 'transcriptionCount',
        'endpoint_count': 'endpointCount'
    }

    def __init__(self, dataset_count=None, evaluation_count=None, model_count=None, transcription_count=None, endpoint_count=None):  # noqa: E501
        """ProjectProperties - a model defined in Swagger"""  # noqa: E501

        self._dataset_count = None
        self._evaluation_count = None
        self._model_count = None
        self._transcription_count = None
        self._endpoint_count = None
        self.discriminator = None

        if dataset_count is not None:
            self.dataset_count = dataset_count
        if evaluation_count is not None:
            self.evaluation_count = evaluation_count
        if model_count is not None:
            self.model_count = model_count
        if transcription_count is not None:
            self.transcription_count = transcription_count
        if endpoint_count is not None:
            self.endpoint_count = endpoint_count

    @property
    def dataset_count(self):
        """Gets the dataset_count of this ProjectProperties.  # noqa: E501

        The number of datasets associated to this project.  # noqa: E501

        :return: The dataset_count of this ProjectProperties.  # noqa: E501
        :rtype: int
        """
        return self._dataset_count

    @dataset_count.setter
    def dataset_count(self, dataset_count):
        """Sets the dataset_count of this ProjectProperties.

        The number of datasets associated to this project.  # noqa: E501

        :param dataset_count: The dataset_count of this ProjectProperties.  # noqa: E501
        :type: int
        """

        self._dataset_count = dataset_count

    @property
    def evaluation_count(self):
        """Gets the evaluation_count of this ProjectProperties.  # noqa: E501

        The number of evaluations associated to this project.  # noqa: E501

        :return: The evaluation_count of this ProjectProperties.  # noqa: E501
        :rtype: int
        """
        return self._evaluation_count

    @evaluation_count.setter
    def evaluation_count(self, evaluation_count):
        """Sets the evaluation_count of this ProjectProperties.

        The number of evaluations associated to this project.  # noqa: E501

        :param evaluation_count: The evaluation_count of this ProjectProperties.  # noqa: E501
        :type: int
        """

        self._evaluation_count = evaluation_count

    @property
    def model_count(self):
        """Gets the model_count of this ProjectProperties.  # noqa: E501

        The number of models associated to this project.  # noqa: E501

        :return: The model_count of this ProjectProperties.  # noqa: E501
        :rtype: int
        """
        return self._model_count

    @model_count.setter
    def model_count(self, model_count):
        """Sets the model_count of this ProjectProperties.

        The number of models associated to this project.  # noqa: E501

        :param model_count: The model_count of this ProjectProperties.  # noqa: E501
        :type: int
        """

        self._model_count = model_count

    @property
    def transcription_count(self):
        """Gets the transcription_count of this ProjectProperties.  # noqa: E501

        The number of transcriptions associated to this project.  # noqa: E501

        :return: The transcription_count of this ProjectProperties.  # noqa: E501
        :rtype: int
        """
        return self._transcription_count

    @transcription_count.setter
    def transcription_count(self, transcription_count):
        """Sets the transcription_count of this ProjectProperties.

        The number of transcriptions associated to this project.  # noqa: E501

        :param transcription_count: The transcription_count of this ProjectProperties.  # noqa: E501
        :type: int
        """

        self._transcription_count = transcription_count

    @property
    def endpoint_count(self):
        """Gets the endpoint_count of this ProjectProperties.  # noqa: E501

        The number of endpoints associated to this project.  # noqa: E501

        :return: The endpoint_count of this ProjectProperties.  # noqa: E501
        :rtype: int
        """
        return self._endpoint_count

    @endpoint_count.setter
    def endpoint_count(self, endpoint_count):
        """Sets the endpoint_count of this ProjectProperties.

        The number of endpoints associated to this project.  # noqa: E501

        :param endpoint_count: The endpoint_count of this ProjectProperties.  # noqa: E501
        :type: int
        """

        self._endpoint_count = endpoint_count

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
        if issubclass(ProjectProperties, dict):
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
        if not isinstance(other, ProjectProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
