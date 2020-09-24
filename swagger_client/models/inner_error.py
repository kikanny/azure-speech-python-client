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


class InnerError(object):
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
        'code': 'str',
        'details': 'dict(str, str)',
        'message': 'str',
        'target': 'str',
        'inner_error': 'InnerError'
    }

    attribute_map = {
        'code': 'code',
        'details': 'details',
        'message': 'message',
        'target': 'target',
        'inner_error': 'innerError'
    }

    def __init__(self, code=None, details=None, message=None, target=None, inner_error=None):  # noqa: E501
        """InnerError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._details = None
        self._message = None
        self._target = None
        self._inner_error = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if message is not None:
            self.message = message
        if target is not None:
            self.target = target
        if inner_error is not None:
            self.inner_error = inner_error

    @property
    def code(self):
        """Gets the code of this InnerError.  # noqa: E501


        :return: The code of this InnerError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InnerError.


        :param code: The code of this InnerError.  # noqa: E501
        :type: str
        """
        allowed_values = ["InvalidParameterValue", "InvalidRequestBodyFormat", "EmptyRequest", "MissingInputRecords", "InvalidDocument", "ModelVersionIncorrect", "InvalidDocumentBatch", "UnsupportedLanguageCode", "DataImportFailed", "InUseViolation", "InvalidLocale", "InvalidBaseModel", "InvalidAdaptationMapping", "InvalidDataset", "InvalidTest", "FailedDataset", "InvalidModel", "InvalidTranscription", "InvalidVoiceSynthesis", "InvalidPayload", "InvalidParameter", "EndpointWithoutLogging", "InvalidPermissions", "InvalidPrerequisite", "InvalidProductId", "InvalidSubscription", "InvalidProject", "InvalidProjectKind", "InvalidRecordingsUri", "ExceededNumberOfRecordingsUris", "ModelMismatch", "ProjectGenderMismatch", "ModelDeprecated", "ModelExists", "ModelNotDeployable", "EndpointNotUpdatable", "SingleDefaultEndpoint", "InvalidModelUri", "SubscriptionNotFound", "QuotaViolation", "UnsupportedDelta", "UnsupportedFilter", "UnsupportedPagination", "UnsupportedOrderBy", "NoUtf8WithBom", "ModelDeploymentNotCompleteState", "SkuLimitsExist", "DeployingFailedModel", "UnsupportedTimeRange", "InvalidLogDate", "InvalidLogId", "InvalidLogStartTime", "InvalidLogEndTime", "InvalidTopForLogs", "DeleteNotAllowed", "Forbidden", "DeployNotAllowed", "UnexpectedError", "InvalidCollection", "InvalidCallbackUri", "InvalidSasValidityDuration"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def details(self):
        """Gets the details of this InnerError.  # noqa: E501


        :return: The details of this InnerError.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this InnerError.


        :param details: The details of this InnerError.  # noqa: E501
        :type: dict(str, str)
        """

        self._details = details

    @property
    def message(self):
        """Gets the message of this InnerError.  # noqa: E501


        :return: The message of this InnerError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InnerError.


        :param message: The message of this InnerError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def target(self):
        """Gets the target of this InnerError.  # noqa: E501


        :return: The target of this InnerError.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this InnerError.


        :param target: The target of this InnerError.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def inner_error(self):
        """Gets the inner_error of this InnerError.  # noqa: E501


        :return: The inner_error of this InnerError.  # noqa: E501
        :rtype: InnerError
        """
        return self._inner_error

    @inner_error.setter
    def inner_error(self, inner_error):
        """Sets the inner_error of this InnerError.


        :param inner_error: The inner_error of this InnerError.  # noqa: E501
        :type: InnerError
        """

        self._inner_error = inner_error

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
        if issubclass(InnerError, dict):
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
        if not isinstance(other, InnerError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
