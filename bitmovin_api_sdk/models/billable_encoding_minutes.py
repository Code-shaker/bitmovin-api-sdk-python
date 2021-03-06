# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.billable_encoding_minutes_details import BillableEncodingMinutesDetails
from bitmovin_api_sdk.models.codec_config_type import CodecConfigType
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.psnr_per_stream_mode import PsnrPerStreamMode
from bitmovin_api_sdk.models.statistics_per_title_stream import StatisticsPerTitleStream
import pprint
import six


class BillableEncodingMinutes(object):
    @poscheck_model
    def __init__(self,
                 encoding_mode=None,
                 codec=None,
                 per_title_result_stream=None,
                 psnr_mode=None,
                 billable_minutes=None):
        # type: (EncodingMode, CodecConfigType, StatisticsPerTitleStream, PsnrPerStreamMode, BillableEncodingMinutesDetails) -> None

        self._encoding_mode = None
        self._codec = None
        self._per_title_result_stream = None
        self._psnr_mode = None
        self._billable_minutes = None
        self.discriminator = None

        if encoding_mode is not None:
            self.encoding_mode = encoding_mode
        if codec is not None:
            self.codec = codec
        if per_title_result_stream is not None:
            self.per_title_result_stream = per_title_result_stream
        if psnr_mode is not None:
            self.psnr_mode = psnr_mode
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes

    @property
    def openapi_types(self):
        types = {
            'encoding_mode': 'EncodingMode',
            'codec': 'CodecConfigType',
            'per_title_result_stream': 'StatisticsPerTitleStream',
            'psnr_mode': 'PsnrPerStreamMode',
            'billable_minutes': 'BillableEncodingMinutesDetails'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_mode': 'encodingMode',
            'codec': 'codec',
            'per_title_result_stream': 'perTitleResultStream',
            'psnr_mode': 'psnrMode',
            'billable_minutes': 'billableMinutes'
        }
        return attributes

    @property
    def encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the encoding_mode of this BillableEncodingMinutes.


        :return: The encoding_mode of this BillableEncodingMinutes.
        :rtype: EncodingMode
        """
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the encoding_mode of this BillableEncodingMinutes.


        :param encoding_mode: The encoding_mode of this BillableEncodingMinutes.
        :type: EncodingMode
        """

        if encoding_mode is not None:
            if not isinstance(encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `encoding_mode`, type has to be `EncodingMode`")

        self._encoding_mode = encoding_mode

    @property
    def codec(self):
        # type: () -> CodecConfigType
        """Gets the codec of this BillableEncodingMinutes.


        :return: The codec of this BillableEncodingMinutes.
        :rtype: CodecConfigType
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (CodecConfigType) -> None
        """Sets the codec of this BillableEncodingMinutes.


        :param codec: The codec of this BillableEncodingMinutes.
        :type: CodecConfigType
        """

        if codec is not None:
            if not isinstance(codec, CodecConfigType):
                raise TypeError("Invalid type for `codec`, type has to be `CodecConfigType`")

        self._codec = codec

    @property
    def per_title_result_stream(self):
        # type: () -> StatisticsPerTitleStream
        """Gets the per_title_result_stream of this BillableEncodingMinutes.


        :return: The per_title_result_stream of this BillableEncodingMinutes.
        :rtype: StatisticsPerTitleStream
        """
        return self._per_title_result_stream

    @per_title_result_stream.setter
    def per_title_result_stream(self, per_title_result_stream):
        # type: (StatisticsPerTitleStream) -> None
        """Sets the per_title_result_stream of this BillableEncodingMinutes.


        :param per_title_result_stream: The per_title_result_stream of this BillableEncodingMinutes.
        :type: StatisticsPerTitleStream
        """

        if per_title_result_stream is not None:
            if not isinstance(per_title_result_stream, StatisticsPerTitleStream):
                raise TypeError("Invalid type for `per_title_result_stream`, type has to be `StatisticsPerTitleStream`")

        self._per_title_result_stream = per_title_result_stream

    @property
    def psnr_mode(self):
        # type: () -> PsnrPerStreamMode
        """Gets the psnr_mode of this BillableEncodingMinutes.


        :return: The psnr_mode of this BillableEncodingMinutes.
        :rtype: PsnrPerStreamMode
        """
        return self._psnr_mode

    @psnr_mode.setter
    def psnr_mode(self, psnr_mode):
        # type: (PsnrPerStreamMode) -> None
        """Sets the psnr_mode of this BillableEncodingMinutes.


        :param psnr_mode: The psnr_mode of this BillableEncodingMinutes.
        :type: PsnrPerStreamMode
        """

        if psnr_mode is not None:
            if not isinstance(psnr_mode, PsnrPerStreamMode):
                raise TypeError("Invalid type for `psnr_mode`, type has to be `PsnrPerStreamMode`")

        self._psnr_mode = psnr_mode

    @property
    def billable_minutes(self):
        # type: () -> BillableEncodingMinutesDetails
        """Gets the billable_minutes of this BillableEncodingMinutes.


        :return: The billable_minutes of this BillableEncodingMinutes.
        :rtype: BillableEncodingMinutesDetails
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        # type: (BillableEncodingMinutesDetails) -> None
        """Sets the billable_minutes of this BillableEncodingMinutes.


        :param billable_minutes: The billable_minutes of this BillableEncodingMinutes.
        :type: BillableEncodingMinutesDetails
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, BillableEncodingMinutesDetails):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `BillableEncodingMinutesDetails`")

        self._billable_minutes = billable_minutes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BillableEncodingMinutes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
