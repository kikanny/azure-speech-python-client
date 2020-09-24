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


class PaginatedEndpoints(object):
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
        'values': 'list[Endpoint]',
        'next_link': 'str'
    }

    attribute_map = {
        'values': 'values',
        'next_link': '@nextLink'
    }

    def __init__(self, values=None, next_link=None):  # noqa: E501
        """PaginatedEndpoints - a model defined in Swagger"""  # noqa: E501

        self._values = None
        self._next_link = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if next_link is not None:
            self.next_link = next_link

    @property
    def values(self):
        """Gets the values of this PaginatedEndpoints.  # noqa: E501

        A list of entities limited by either the passed query parameters 'skip' and 'top' or their default values.                When iterating through a list using pagination and deleting entities in parallel, some entities will be skipped in the results.  It's recommended to build a list on the client and delete after the fetching of the complete list.  # noqa: E501

        :return: The values of this PaginatedEndpoints.  # noqa: E501
        :rtype: list[Endpoint]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this PaginatedEndpoints.

        A list of entities limited by either the passed query parameters 'skip' and 'top' or their default values.                When iterating through a list using pagination and deleting entities in parallel, some entities will be skipped in the results.  It's recommended to build a list on the client and delete after the fetching of the complete list.  # noqa: E501

        :param values: The values of this PaginatedEndpoints.  # noqa: E501
        :type: list[Endpoint]
        """

        self._values = values

    @property
    def next_link(self):
        """Gets the next_link of this PaginatedEndpoints.  # noqa: E501

        A link to the next set of paginated results if there are more entities available; otherwise null.  # noqa: E501

        :return: The next_link of this PaginatedEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this PaginatedEndpoints.

        A link to the next set of paginated results if there are more entities available; otherwise null.  # noqa: E501

        :param next_link: The next_link of this PaginatedEndpoints.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

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
        if issubclass(PaginatedEndpoints, dict):
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
        if not isinstance(other, PaginatedEndpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
