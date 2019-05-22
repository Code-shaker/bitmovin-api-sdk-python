# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.custom_data import CustomData
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class CustomdataApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CustomdataApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, object_detection_id, **kwargs):
        """Get the custom data of an object detection configuration"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}/customData',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            type=CustomData,
            **kwargs
        )