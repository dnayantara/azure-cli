# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

ACR_RESOURCE_PROVIDER = 'Microsoft.ContainerRegistry'
ACR_RESOURCE_TYPE = ACR_RESOURCE_PROVIDER + '/registries'
STORAGE_RESOURCE_TYPE = 'Microsoft.Storage/storageAccounts'
WEBHOOK_RESOURCE_TYPE = ACR_RESOURCE_TYPE + '/webhooks'
WEBHOOK_API_VERSION = '2017-06-01-preview'
MANAGED_REGISTRY_API_VERSION = '2017-06-01-preview'
MANAGED_REGISTRY_SKU = ['Managed_Basic', 'Managed_Standard', 'Managed_Premium']
