# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.webhook import Webhook


class ErrorApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ErrorApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, webhook, **kwargs):
        # type: (Webhook, dict) -> Webhook
        """Add Manifest Error Webhook (All Manifests)

        :param webhook: Add a new webhook notification if a manifest creation failed with an error
        :type webhook: Webhook, required
        :return: Notification Details
        :rtype: Webhook
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/manifest/error',
            webhook,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )

    def create_by_manifest_id(self, manifest_id, webhook, **kwargs):
        # type: (string_types, Webhook, dict) -> Webhook
        """Add Manifest Error Webhook Notification (Specific Manifest)

        :param manifest_id: Id of the manifest resource
        :type manifest_id: string_types, required
        :param webhook: The webhook notifications object
        :type webhook: Webhook, required
        :return: Notification Details
        :rtype: Webhook
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/manifest/{manifest_id}/error',
            webhook,
            path_params={'manifest_id': manifest_id},
            type=Webhook,
            **kwargs
        )

    def update(self, notification_id, webhook, **kwargs):
        # type: (string_types, Webhook, dict) -> Webhook
        """Replace Manifest Error Webhook Notification

        :param notification_id: Id of the webhook notification
        :type notification_id: string_types, required
        :param webhook: The webhook notification with the updated values
        :type webhook: Webhook, required
        :return: Notification Details
        :rtype: Webhook
        """

        return self.api_client.put(
            '/notifications/webhooks/encoding/manifest/error/{notification_id}',
            webhook,
            path_params={'notification_id': notification_id},
            type=Webhook,
            **kwargs
        )
