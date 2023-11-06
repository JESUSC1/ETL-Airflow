"""
Type annotations for appflow service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/type_defs/)

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef

    data: AggregationConfigTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregationTypeType,
    AuthenticationTypeType,
    ConnectionModeType,
    ConnectorTypeType,
    DatadogConnectorOperatorType,
    DataPullModeType,
    DataTransferApiTypeType,
    DynatraceConnectorOperatorType,
    ExecutionStatusType,
    FileTypeType,
    FlowStatusType,
    GoogleAnalyticsConnectorOperatorType,
    InforNexusConnectorOperatorType,
    MarketoConnectorOperatorType,
    OAuth2CustomPropTypeType,
    OAuth2GrantTypeType,
    OperatorPropertiesKeysType,
    OperatorsType,
    OperatorType,
    PardotConnectorOperatorType,
    PathPrefixType,
    PrefixFormatType,
    PrefixTypeType,
    PrivateConnectionProvisioningFailureCauseType,
    PrivateConnectionProvisioningStatusType,
    S3ConnectorOperatorType,
    S3InputFileTypeType,
    SalesforceConnectorOperatorType,
    SalesforceDataTransferApiType,
    SAPODataConnectorOperatorType,
    ScheduleFrequencyTypeType,
    ServiceNowConnectorOperatorType,
    SingularConnectorOperatorType,
    SlackConnectorOperatorType,
    SupportedDataTransferTypeType,
    TaskTypeType,
    TrendmicroConnectorOperatorType,
    TriggerTypeType,
    VeevaConnectorOperatorType,
    WriteOperationTypeType,
    ZendeskConnectorOperatorType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ApiKeyCredentialsTypeDef",
    "AuthParameterTypeDef",
    "BasicAuthCredentialsTypeDef",
    "CancelFlowExecutionsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ConnectorRuntimeSettingTypeDef",
    "DataTransferApiTypeDef",
    "ConnectorDetailTypeDef",
    "DestinationFieldPropertiesTypeDef",
    "SourceFieldPropertiesTypeDef",
    "ConnectorEntityTypeDef",
    "GoogleAnalyticsMetadataTypeDef",
    "HoneycodeMetadataTypeDef",
    "SalesforceMetadataTypeDef",
    "SlackMetadataTypeDef",
    "SnowflakeMetadataTypeDef",
    "ZendeskMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DynatraceConnectorProfileCredentialsTypeDef",
    "InforNexusConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "SingularConnectorProfileCredentialsTypeDef",
    "SnowflakeConnectorProfileCredentialsTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DynatraceConnectorProfilePropertiesTypeDef",
    "InforNexusConnectorProfilePropertiesTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "PardotConnectorProfilePropertiesTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "SalesforceConnectorProfilePropertiesTypeDef",
    "ServiceNowConnectorProfilePropertiesTypeDef",
    "SlackConnectorProfilePropertiesTypeDef",
    "SnowflakeConnectorProfilePropertiesTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "PrivateConnectionProvisioningStateTypeDef",
    "LambdaConnectorProvisioningConfigTypeDef",
    "CustomAuthCredentialsTypeDef",
    "ErrorHandlingConfigTypeDef",
    "OAuth2PropertiesTypeDef",
    "CustomerProfilesDestinationPropertiesTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DeleteConnectorProfileRequestRequestTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DescribeConnectorEntityRequestRequestTypeDef",
    "DescribeConnectorProfilesRequestRequestTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorsRequestRequestTypeDef",
    "DescribeFlowExecutionRecordsRequestRequestTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "ExecutionDetailsTypeDef",
    "DynatraceSourcePropertiesTypeDef",
    "ErrorInfoTypeDef",
    "RangeTypeDef",
    "GlueDataCatalogConfigTypeDef",
    "GoogleAnalyticsSourcePropertiesTypeDef",
    "IncrementalPullConfigTypeDef",
    "InforNexusSourcePropertiesTypeDef",
    "ListConnectorEntitiesRequestRequestTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "RegistrationOutputTypeDef",
    "OAuth2CustomParameterTypeDef",
    "OAuthPropertiesTypeDef",
    "PardotSourcePropertiesTypeDef",
    "PrefixConfigTypeDef",
    "ResetConnectorMetadataCacheRequestRequestTypeDef",
    "S3InputFormatConfigTypeDef",
    "SuccessResponseHandlingConfigTypeDef",
    "SAPODataPaginationConfigTypeDef",
    "SAPODataParallelismConfigTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "TimestampTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SingularSourcePropertiesTypeDef",
    "SlackSourcePropertiesTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskSourcePropertiesTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StopFlowRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnregisterConnectorRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CustomAuthConfigTypeDef",
    "CancelFlowExecutionsResponseTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterConnectorResponseTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateConnectorRegistrationResponseTypeDef",
    "UpdateFlowResponseTypeDef",
    "CustomConnectorSourcePropertiesTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ConnectorMetadataTypeDef",
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    "HoneycodeConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "OAuth2CredentialsTypeDef",
    "OAuthCredentialsTypeDef",
    "PardotConnectorProfileCredentialsTypeDef",
    "SalesforceConnectorProfileCredentialsTypeDef",
    "SlackConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "TaskTypeDef",
    "ConnectorProvisioningConfigTypeDef",
    "CustomConnectorDestinationPropertiesTypeDef",
    "EventBridgeDestinationPropertiesTypeDef",
    "HoneycodeDestinationPropertiesTypeDef",
    "MarketoDestinationPropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "SalesforceDestinationPropertiesTypeDef",
    "SnowflakeDestinationPropertiesTypeDef",
    "ZendeskDestinationPropertiesTypeDef",
    "CustomConnectorProfilePropertiesTypeDef",
    "FlowDefinitionTypeDef",
    "ExecutionResultTypeDef",
    "FieldTypeDetailsTypeDef",
    "MetadataCatalogConfigTypeDef",
    "MetadataCatalogDetailTypeDef",
    "OAuth2DefaultsTypeDef",
    "SAPODataConnectorProfilePropertiesTypeDef",
    "S3OutputFormatConfigTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "S3SourcePropertiesTypeDef",
    "SAPODataDestinationPropertiesTypeDef",
    "SAPODataSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "CustomConnectorProfileCredentialsTypeDef",
    "ServiceNowConnectorProfileCredentialsTypeDef",
    "SAPODataConnectorProfileCredentialsTypeDef",
    "RegisterConnectorRequestRequestTypeDef",
    "UpdateConnectorRegistrationRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "ExecutionRecordTypeDef",
    "AuthenticationConfigTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "S3DestinationPropertiesTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "TriggerPropertiesTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorEntityFieldTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorProfileTypeDef",
    "DestinationConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "TriggerConfigTypeDef",
    "ConnectorProfileConfigTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DestinationFlowConfigTypeDef",
    "CreateConnectorProfileRequestRequestTypeDef",
    "UpdateConnectorProfileRequestRequestTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "UpdateFlowRequestRequestTypeDef",
)

AggregationConfigTypeDef = TypedDict(
    "AggregationConfigTypeDef",
    {
        "aggregationType": NotRequired[AggregationTypeType],
        "targetFileSize": NotRequired[int],
    },
)

AmplitudeConnectorProfileCredentialsTypeDef = TypedDict(
    "AmplitudeConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "secretKey": str,
    },
)

AmplitudeSourcePropertiesTypeDef = TypedDict(
    "AmplitudeSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ApiKeyCredentialsTypeDef = TypedDict(
    "ApiKeyCredentialsTypeDef",
    {
        "apiKey": str,
        "apiSecretKey": NotRequired[str],
    },
)

AuthParameterTypeDef = TypedDict(
    "AuthParameterTypeDef",
    {
        "key": NotRequired[str],
        "isRequired": NotRequired[bool],
        "label": NotRequired[str],
        "description": NotRequired[str],
        "isSensitiveField": NotRequired[bool],
        "connectorSuppliedValues": NotRequired[List[str]],
    },
)

BasicAuthCredentialsTypeDef = TypedDict(
    "BasicAuthCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

CancelFlowExecutionsRequestRequestTypeDef = TypedDict(
    "CancelFlowExecutionsRequestRequestTypeDef",
    {
        "flowName": str,
        "executionIds": NotRequired[Sequence[str]],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

ConnectorRuntimeSettingTypeDef = TypedDict(
    "ConnectorRuntimeSettingTypeDef",
    {
        "key": NotRequired[str],
        "dataType": NotRequired[str],
        "isRequired": NotRequired[bool],
        "label": NotRequired[str],
        "description": NotRequired[str],
        "scope": NotRequired[str],
        "connectorSuppliedValueOptions": NotRequired[List[str]],
    },
)

DataTransferApiTypeDef = TypedDict(
    "DataTransferApiTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[DataTransferApiTypeType],
    },
)

ConnectorDetailTypeDef = TypedDict(
    "ConnectorDetailTypeDef",
    {
        "connectorDescription": NotRequired[str],
        "connectorName": NotRequired[str],
        "connectorOwner": NotRequired[str],
        "connectorVersion": NotRequired[str],
        "applicationType": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "registeredAt": NotRequired[datetime],
        "registeredBy": NotRequired[str],
        "connectorProvisioningType": NotRequired[Literal["LAMBDA"]],
        "connectorModes": NotRequired[List[str]],
        "supportedDataTransferTypes": NotRequired[List[SupportedDataTransferTypeType]],
    },
)

DestinationFieldPropertiesTypeDef = TypedDict(
    "DestinationFieldPropertiesTypeDef",
    {
        "isCreatable": NotRequired[bool],
        "isNullable": NotRequired[bool],
        "isUpsertable": NotRequired[bool],
        "isUpdatable": NotRequired[bool],
        "isDefaultedOnCreate": NotRequired[bool],
        "supportedWriteOperations": NotRequired[List[WriteOperationTypeType]],
    },
)

SourceFieldPropertiesTypeDef = TypedDict(
    "SourceFieldPropertiesTypeDef",
    {
        "isRetrievable": NotRequired[bool],
        "isQueryable": NotRequired[bool],
        "isTimestampFieldForIncrementalQueries": NotRequired[bool],
    },
)

ConnectorEntityTypeDef = TypedDict(
    "ConnectorEntityTypeDef",
    {
        "name": str,
        "label": NotRequired[str],
        "hasNestedEntities": NotRequired[bool],
    },
)

GoogleAnalyticsMetadataTypeDef = TypedDict(
    "GoogleAnalyticsMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

HoneycodeMetadataTypeDef = TypedDict(
    "HoneycodeMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

SalesforceMetadataTypeDef = TypedDict(
    "SalesforceMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
        "dataTransferApis": NotRequired[List[SalesforceDataTransferApiType]],
        "oauth2GrantTypesSupported": NotRequired[List[OAuth2GrantTypeType]],
    },
)

SlackMetadataTypeDef = TypedDict(
    "SlackMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

SnowflakeMetadataTypeDef = TypedDict(
    "SnowflakeMetadataTypeDef",
    {
        "supportedRegions": NotRequired[List[str]],
    },
)

ZendeskMetadataTypeDef = TypedDict(
    "ZendeskMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

ConnectorOAuthRequestTypeDef = TypedDict(
    "ConnectorOAuthRequestTypeDef",
    {
        "authCode": NotRequired[str],
        "redirectUri": NotRequired[str],
    },
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Amplitude": NotRequired[Literal["BETWEEN"]],
        "Datadog": NotRequired[DatadogConnectorOperatorType],
        "Dynatrace": NotRequired[DynatraceConnectorOperatorType],
        "GoogleAnalytics": NotRequired[GoogleAnalyticsConnectorOperatorType],
        "InforNexus": NotRequired[InforNexusConnectorOperatorType],
        "Marketo": NotRequired[MarketoConnectorOperatorType],
        "S3": NotRequired[S3ConnectorOperatorType],
        "Salesforce": NotRequired[SalesforceConnectorOperatorType],
        "ServiceNow": NotRequired[ServiceNowConnectorOperatorType],
        "Singular": NotRequired[SingularConnectorOperatorType],
        "Slack": NotRequired[SlackConnectorOperatorType],
        "Trendmicro": NotRequired[TrendmicroConnectorOperatorType],
        "Veeva": NotRequired[VeevaConnectorOperatorType],
        "Zendesk": NotRequired[ZendeskConnectorOperatorType],
        "SAPOData": NotRequired[SAPODataConnectorOperatorType],
        "CustomConnector": NotRequired[OperatorType],
        "Pardot": NotRequired[PardotConnectorOperatorType],
    },
)

DatadogConnectorProfileCredentialsTypeDef = TypedDict(
    "DatadogConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "applicationKey": str,
    },
)

DynatraceConnectorProfileCredentialsTypeDef = TypedDict(
    "DynatraceConnectorProfileCredentialsTypeDef",
    {
        "apiToken": str,
    },
)

InforNexusConnectorProfileCredentialsTypeDef = TypedDict(
    "InforNexusConnectorProfileCredentialsTypeDef",
    {
        "accessKeyId": str,
        "userId": str,
        "secretAccessKey": str,
        "datakey": str,
    },
)

RedshiftConnectorProfileCredentialsTypeDef = TypedDict(
    "RedshiftConnectorProfileCredentialsTypeDef",
    {
        "username": NotRequired[str],
        "password": NotRequired[str],
    },
)

SingularConnectorProfileCredentialsTypeDef = TypedDict(
    "SingularConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
    },
)

SnowflakeConnectorProfileCredentialsTypeDef = TypedDict(
    "SnowflakeConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

TrendmicroConnectorProfileCredentialsTypeDef = TypedDict(
    "TrendmicroConnectorProfileCredentialsTypeDef",
    {
        "apiSecretKey": str,
    },
)

VeevaConnectorProfileCredentialsTypeDef = TypedDict(
    "VeevaConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

DatadogConnectorProfilePropertiesTypeDef = TypedDict(
    "DatadogConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

DynatraceConnectorProfilePropertiesTypeDef = TypedDict(
    "DynatraceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

InforNexusConnectorProfilePropertiesTypeDef = TypedDict(
    "InforNexusConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

MarketoConnectorProfilePropertiesTypeDef = TypedDict(
    "MarketoConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

PardotConnectorProfilePropertiesTypeDef = TypedDict(
    "PardotConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": NotRequired[str],
        "isSandboxEnvironment": NotRequired[bool],
        "businessUnitId": NotRequired[str],
    },
)

RedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "RedshiftConnectorProfilePropertiesTypeDef",
    {
        "bucketName": str,
        "roleArn": str,
        "databaseUrl": NotRequired[str],
        "bucketPrefix": NotRequired[str],
        "dataApiRoleArn": NotRequired[str],
        "isRedshiftServerless": NotRequired[bool],
        "clusterIdentifier": NotRequired[str],
        "workgroupName": NotRequired[str],
        "databaseName": NotRequired[str],
    },
)

SalesforceConnectorProfilePropertiesTypeDef = TypedDict(
    "SalesforceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": NotRequired[str],
        "isSandboxEnvironment": NotRequired[bool],
        "usePrivateLinkForMetadataAndAuthorization": NotRequired[bool],
    },
)

ServiceNowConnectorProfilePropertiesTypeDef = TypedDict(
    "ServiceNowConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

SlackConnectorProfilePropertiesTypeDef = TypedDict(
    "SlackConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

SnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "SnowflakeConnectorProfilePropertiesTypeDef",
    {
        "warehouse": str,
        "stage": str,
        "bucketName": str,
        "bucketPrefix": NotRequired[str],
        "privateLinkServiceName": NotRequired[str],
        "accountName": NotRequired[str],
        "region": NotRequired[str],
    },
)

VeevaConnectorProfilePropertiesTypeDef = TypedDict(
    "VeevaConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

ZendeskConnectorProfilePropertiesTypeDef = TypedDict(
    "ZendeskConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

PrivateConnectionProvisioningStateTypeDef = TypedDict(
    "PrivateConnectionProvisioningStateTypeDef",
    {
        "status": NotRequired[PrivateConnectionProvisioningStatusType],
        "failureMessage": NotRequired[str],
        "failureCause": NotRequired[PrivateConnectionProvisioningFailureCauseType],
    },
)

LambdaConnectorProvisioningConfigTypeDef = TypedDict(
    "LambdaConnectorProvisioningConfigTypeDef",
    {
        "lambdaArn": str,
    },
)

CustomAuthCredentialsTypeDef = TypedDict(
    "CustomAuthCredentialsTypeDef",
    {
        "customAuthenticationType": str,
        "credentialsMap": NotRequired[Mapping[str, str]],
    },
)

ErrorHandlingConfigTypeDef = TypedDict(
    "ErrorHandlingConfigTypeDef",
    {
        "failOnFirstDestinationError": NotRequired[bool],
        "bucketPrefix": NotRequired[str],
        "bucketName": NotRequired[str],
    },
)

OAuth2PropertiesTypeDef = TypedDict(
    "OAuth2PropertiesTypeDef",
    {
        "tokenUrl": str,
        "oAuth2GrantType": OAuth2GrantTypeType,
        "tokenUrlCustomProperties": NotRequired[Mapping[str, str]],
    },
)

CustomerProfilesDestinationPropertiesTypeDef = TypedDict(
    "CustomerProfilesDestinationPropertiesTypeDef",
    {
        "domainName": str,
        "objectTypeName": NotRequired[str],
    },
)

DatadogSourcePropertiesTypeDef = TypedDict(
    "DatadogSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

DeleteConnectorProfileRequestRequestTypeDef = TypedDict(
    "DeleteConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "forceDelete": NotRequired[bool],
    },
)

DeleteFlowRequestRequestTypeDef = TypedDict(
    "DeleteFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "forceDelete": NotRequired[bool],
    },
)

DescribeConnectorEntityRequestRequestTypeDef = TypedDict(
    "DescribeConnectorEntityRequestRequestTypeDef",
    {
        "connectorEntityName": str,
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorProfileName": NotRequired[str],
        "apiVersion": NotRequired[str],
    },
)

DescribeConnectorProfilesRequestRequestTypeDef = TypedDict(
    "DescribeConnectorProfilesRequestRequestTypeDef",
    {
        "connectorProfileNames": NotRequired[Sequence[str]],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "connectorLabel": NotRequired[str],
    },
)

DescribeConnectorsRequestRequestTypeDef = TypedDict(
    "DescribeConnectorsRequestRequestTypeDef",
    {
        "connectorTypes": NotRequired[Sequence[ConnectorTypeType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeFlowExecutionRecordsRequestRequestTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsRequestRequestTypeDef",
    {
        "flowName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "mostRecentExecutionMessage": NotRequired[str],
        "mostRecentExecutionTime": NotRequired[datetime],
        "mostRecentExecutionStatus": NotRequired[ExecutionStatusType],
    },
)

DynatraceSourcePropertiesTypeDef = TypedDict(
    "DynatraceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "putFailuresCount": NotRequired[int],
        "executionMessage": NotRequired[str],
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "maximum": NotRequired[float],
        "minimum": NotRequired[float],
    },
)

GlueDataCatalogConfigTypeDef = TypedDict(
    "GlueDataCatalogConfigTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tablePrefix": str,
    },
)

GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "datetimeTypeFieldName": NotRequired[str],
    },
)

InforNexusSourcePropertiesTypeDef = TypedDict(
    "InforNexusSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ListConnectorEntitiesRequestRequestTypeDef = TypedDict(
    "ListConnectorEntitiesRequestRequestTypeDef",
    {
        "connectorProfileName": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "entitiesPath": NotRequired[str],
        "apiVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

RegistrationOutputTypeDef = TypedDict(
    "RegistrationOutputTypeDef",
    {
        "message": NotRequired[str],
        "result": NotRequired[str],
        "status": NotRequired[ExecutionStatusType],
    },
)

OAuth2CustomParameterTypeDef = TypedDict(
    "OAuth2CustomParameterTypeDef",
    {
        "key": NotRequired[str],
        "isRequired": NotRequired[bool],
        "label": NotRequired[str],
        "description": NotRequired[str],
        "isSensitiveField": NotRequired[bool],
        "connectorSuppliedValues": NotRequired[List[str]],
        "type": NotRequired[OAuth2CustomPropTypeType],
    },
)

OAuthPropertiesTypeDef = TypedDict(
    "OAuthPropertiesTypeDef",
    {
        "tokenUrl": str,
        "authCodeUrl": str,
        "oAuthScopes": Sequence[str],
    },
)

PardotSourcePropertiesTypeDef = TypedDict(
    "PardotSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

PrefixConfigTypeDef = TypedDict(
    "PrefixConfigTypeDef",
    {
        "prefixType": NotRequired[PrefixTypeType],
        "prefixFormat": NotRequired[PrefixFormatType],
        "pathPrefixHierarchy": NotRequired[Sequence[PathPrefixType]],
    },
)

ResetConnectorMetadataCacheRequestRequestTypeDef = TypedDict(
    "ResetConnectorMetadataCacheRequestRequestTypeDef",
    {
        "connectorProfileName": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorEntityName": NotRequired[str],
        "entitiesPath": NotRequired[str],
        "apiVersion": NotRequired[str],
    },
)

S3InputFormatConfigTypeDef = TypedDict(
    "S3InputFormatConfigTypeDef",
    {
        "s3InputFileType": NotRequired[S3InputFileTypeType],
    },
)

SuccessResponseHandlingConfigTypeDef = TypedDict(
    "SuccessResponseHandlingConfigTypeDef",
    {
        "bucketPrefix": NotRequired[str],
        "bucketName": NotRequired[str],
    },
)

SAPODataPaginationConfigTypeDef = TypedDict(
    "SAPODataPaginationConfigTypeDef",
    {
        "maxPageSize": int,
    },
)

SAPODataParallelismConfigTypeDef = TypedDict(
    "SAPODataParallelismConfigTypeDef",
    {
        "maxParallelism": int,
    },
)

SalesforceSourcePropertiesTypeDef = TypedDict(
    "SalesforceSourcePropertiesTypeDef",
    {
        "object": str,
        "enableDynamicFieldUpdate": NotRequired[bool],
        "includeDeletedRecords": NotRequired[bool],
        "dataTransferApi": NotRequired[SalesforceDataTransferApiType],
    },
)

TimestampTypeDef = Union[datetime, str]
ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SingularSourcePropertiesTypeDef = TypedDict(
    "SingularSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SlackSourcePropertiesTypeDef = TypedDict(
    "SlackSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

TrendmicroSourcePropertiesTypeDef = TypedDict(
    "TrendmicroSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

VeevaSourcePropertiesTypeDef = TypedDict(
    "VeevaSourcePropertiesTypeDef",
    {
        "object": str,
        "documentType": NotRequired[str],
        "includeSourceFiles": NotRequired[bool],
        "includeRenditions": NotRequired[bool],
        "includeAllVersions": NotRequired[bool],
    },
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "clientToken": NotRequired[str],
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UnregisterConnectorRequestRequestTypeDef = TypedDict(
    "UnregisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
        "forceDelete": NotRequired[bool],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

CustomAuthConfigTypeDef = TypedDict(
    "CustomAuthConfigTypeDef",
    {
        "customAuthenticationType": NotRequired[str],
        "authParameters": NotRequired[List[AuthParameterTypeDef]],
    },
)

CancelFlowExecutionsResponseTypeDef = TypedDict(
    "CancelFlowExecutionsResponseTypeDef",
    {
        "invalidExecutions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateConnectorProfileResponseTypeDef = TypedDict(
    "CreateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RegisterConnectorResponseTypeDef = TypedDict(
    "RegisterConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "executionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateConnectorProfileResponseTypeDef = TypedDict(
    "UpdateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateConnectorRegistrationResponseTypeDef = TypedDict(
    "UpdateConnectorRegistrationResponseTypeDef",
    {
        "connectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "flowStatus": FlowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CustomConnectorSourcePropertiesTypeDef = TypedDict(
    "CustomConnectorSourcePropertiesTypeDef",
    {
        "entityName": str,
        "customProperties": NotRequired[Mapping[str, str]],
        "dataTransferApi": NotRequired[DataTransferApiTypeDef],
    },
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List[ConnectorDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConnectorEntitiesResponseTypeDef = TypedDict(
    "ListConnectorEntitiesResponseTypeDef",
    {
        "connectorEntityMap": Dict[str, List[ConnectorEntityTypeDef]],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConnectorMetadataTypeDef = TypedDict(
    "ConnectorMetadataTypeDef",
    {
        "Amplitude": NotRequired[Dict[str, Any]],
        "Datadog": NotRequired[Dict[str, Any]],
        "Dynatrace": NotRequired[Dict[str, Any]],
        "GoogleAnalytics": NotRequired[GoogleAnalyticsMetadataTypeDef],
        "InforNexus": NotRequired[Dict[str, Any]],
        "Marketo": NotRequired[Dict[str, Any]],
        "Redshift": NotRequired[Dict[str, Any]],
        "S3": NotRequired[Dict[str, Any]],
        "Salesforce": NotRequired[SalesforceMetadataTypeDef],
        "ServiceNow": NotRequired[Dict[str, Any]],
        "Singular": NotRequired[Dict[str, Any]],
        "Slack": NotRequired[SlackMetadataTypeDef],
        "Snowflake": NotRequired[SnowflakeMetadataTypeDef],
        "Trendmicro": NotRequired[Dict[str, Any]],
        "Veeva": NotRequired[Dict[str, Any]],
        "Zendesk": NotRequired[ZendeskMetadataTypeDef],
        "EventBridge": NotRequired[Dict[str, Any]],
        "Upsolver": NotRequired[Dict[str, Any]],
        "CustomerProfiles": NotRequired[Dict[str, Any]],
        "Honeycode": NotRequired[HoneycodeMetadataTypeDef],
        "SAPOData": NotRequired[Dict[str, Any]],
        "Pardot": NotRequired[Dict[str, Any]],
    },
)

GoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

HoneycodeConnectorProfileCredentialsTypeDef = TypedDict(
    "HoneycodeConnectorProfileCredentialsTypeDef",
    {
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

MarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "MarketoConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

OAuth2CredentialsTypeDef = TypedDict(
    "OAuth2CredentialsTypeDef",
    {
        "clientId": NotRequired[str],
        "clientSecret": NotRequired[str],
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

OAuthCredentialsTypeDef = TypedDict(
    "OAuthCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

PardotConnectorProfileCredentialsTypeDef = TypedDict(
    "PardotConnectorProfileCredentialsTypeDef",
    {
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
        "clientCredentialsArn": NotRequired[str],
    },
)

SalesforceConnectorProfileCredentialsTypeDef = TypedDict(
    "SalesforceConnectorProfileCredentialsTypeDef",
    {
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
        "clientCredentialsArn": NotRequired[str],
        "oAuth2GrantType": NotRequired[OAuth2GrantTypeType],
        "jwtToken": NotRequired[str],
    },
)

SlackConnectorProfileCredentialsTypeDef = TypedDict(
    "SlackConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

ZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "ZendeskConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "oAuthRequest": NotRequired[ConnectorOAuthRequestTypeDef],
    },
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "sourceFields": Sequence[str],
        "taskType": TaskTypeType,
        "connectorOperator": NotRequired[ConnectorOperatorTypeDef],
        "destinationField": NotRequired[str],
        "taskProperties": NotRequired[Mapping[OperatorPropertiesKeysType, str]],
    },
)

ConnectorProvisioningConfigTypeDef = TypedDict(
    "ConnectorProvisioningConfigTypeDef",
    {
        "lambda": NotRequired[LambdaConnectorProvisioningConfigTypeDef],
    },
)

CustomConnectorDestinationPropertiesTypeDef = TypedDict(
    "CustomConnectorDestinationPropertiesTypeDef",
    {
        "entityName": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
        "idFieldNames": NotRequired[Sequence[str]],
        "customProperties": NotRequired[Mapping[str, str]],
    },
)

EventBridgeDestinationPropertiesTypeDef = TypedDict(
    "EventBridgeDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)

HoneycodeDestinationPropertiesTypeDef = TypedDict(
    "HoneycodeDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)

MarketoDestinationPropertiesTypeDef = TypedDict(
    "MarketoDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)

RedshiftDestinationPropertiesTypeDef = TypedDict(
    "RedshiftDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
        "bucketPrefix": NotRequired[str],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)

SalesforceDestinationPropertiesTypeDef = TypedDict(
    "SalesforceDestinationPropertiesTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
        "dataTransferApi": NotRequired[SalesforceDataTransferApiType],
    },
)

SnowflakeDestinationPropertiesTypeDef = TypedDict(
    "SnowflakeDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
        "bucketPrefix": NotRequired[str],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
    },
)

ZendeskDestinationPropertiesTypeDef = TypedDict(
    "ZendeskDestinationPropertiesTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)

CustomConnectorProfilePropertiesTypeDef = TypedDict(
    "CustomConnectorProfilePropertiesTypeDef",
    {
        "profileProperties": NotRequired[Mapping[str, str]],
        "oAuth2Properties": NotRequired[OAuth2PropertiesTypeDef],
    },
)

FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "flowArn": NotRequired[str],
        "description": NotRequired[str],
        "flowName": NotRequired[str],
        "flowStatus": NotRequired[FlowStatusType],
        "sourceConnectorType": NotRequired[ConnectorTypeType],
        "sourceConnectorLabel": NotRequired[str],
        "destinationConnectorType": NotRequired[ConnectorTypeType],
        "destinationConnectorLabel": NotRequired[str],
        "triggerType": NotRequired[TriggerTypeType],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "lastRunExecutionDetails": NotRequired[ExecutionDetailsTypeDef],
    },
)

ExecutionResultTypeDef = TypedDict(
    "ExecutionResultTypeDef",
    {
        "errorInfo": NotRequired[ErrorInfoTypeDef],
        "bytesProcessed": NotRequired[int],
        "bytesWritten": NotRequired[int],
        "recordsProcessed": NotRequired[int],
        "numParallelProcesses": NotRequired[int],
        "maxPageSize": NotRequired[int],
    },
)

FieldTypeDetailsTypeDef = TypedDict(
    "FieldTypeDetailsTypeDef",
    {
        "fieldType": str,
        "filterOperators": List[OperatorType],
        "supportedValues": NotRequired[List[str]],
        "valueRegexPattern": NotRequired[str],
        "supportedDateFormat": NotRequired[str],
        "fieldValueRange": NotRequired[RangeTypeDef],
        "fieldLengthRange": NotRequired[RangeTypeDef],
    },
)

MetadataCatalogConfigTypeDef = TypedDict(
    "MetadataCatalogConfigTypeDef",
    {
        "glueDataCatalog": NotRequired[GlueDataCatalogConfigTypeDef],
    },
)

MetadataCatalogDetailTypeDef = TypedDict(
    "MetadataCatalogDetailTypeDef",
    {
        "catalogType": NotRequired[Literal["GLUE"]],
        "tableName": NotRequired[str],
        "tableRegistrationOutput": NotRequired[RegistrationOutputTypeDef],
        "partitionRegistrationOutput": NotRequired[RegistrationOutputTypeDef],
    },
)

OAuth2DefaultsTypeDef = TypedDict(
    "OAuth2DefaultsTypeDef",
    {
        "oauthScopes": NotRequired[List[str]],
        "tokenUrls": NotRequired[List[str]],
        "authCodeUrls": NotRequired[List[str]],
        "oauth2GrantTypesSupported": NotRequired[List[OAuth2GrantTypeType]],
        "oauth2CustomProperties": NotRequired[List[OAuth2CustomParameterTypeDef]],
    },
)

SAPODataConnectorProfilePropertiesTypeDef = TypedDict(
    "SAPODataConnectorProfilePropertiesTypeDef",
    {
        "applicationHostUrl": str,
        "applicationServicePath": str,
        "portNumber": int,
        "clientNumber": str,
        "logonLanguage": NotRequired[str],
        "privateLinkServiceName": NotRequired[str],
        "oAuthProperties": NotRequired[OAuthPropertiesTypeDef],
        "disableSSO": NotRequired[bool],
    },
)

S3OutputFormatConfigTypeDef = TypedDict(
    "S3OutputFormatConfigTypeDef",
    {
        "fileType": NotRequired[FileTypeType],
        "prefixConfig": NotRequired[PrefixConfigTypeDef],
        "aggregationConfig": NotRequired[AggregationConfigTypeDef],
        "preserveSourceDataTyping": NotRequired[bool],
    },
)

UpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "UpsolverS3OutputFormatConfigTypeDef",
    {
        "prefixConfig": PrefixConfigTypeDef,
        "fileType": NotRequired[FileTypeType],
        "aggregationConfig": NotRequired[AggregationConfigTypeDef],
    },
)

S3SourcePropertiesTypeDef = TypedDict(
    "S3SourcePropertiesTypeDef",
    {
        "bucketName": str,
        "bucketPrefix": NotRequired[str],
        "s3InputFormatConfig": NotRequired[S3InputFormatConfigTypeDef],
    },
)

SAPODataDestinationPropertiesTypeDef = TypedDict(
    "SAPODataDestinationPropertiesTypeDef",
    {
        "objectPath": str,
        "successResponseHandlingConfig": NotRequired[SuccessResponseHandlingConfigTypeDef],
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired[ErrorHandlingConfigTypeDef],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)

SAPODataSourcePropertiesTypeDef = TypedDict(
    "SAPODataSourcePropertiesTypeDef",
    {
        "objectPath": NotRequired[str],
        "parallelismConfig": NotRequired[SAPODataParallelismConfigTypeDef],
        "paginationConfig": NotRequired[SAPODataPaginationConfigTypeDef],
    },
)

ScheduledTriggerPropertiesTypeDef = TypedDict(
    "ScheduledTriggerPropertiesTypeDef",
    {
        "scheduleExpression": str,
        "dataPullMode": NotRequired[DataPullModeType],
        "scheduleStartTime": NotRequired[TimestampTypeDef],
        "scheduleEndTime": NotRequired[TimestampTypeDef],
        "timezone": NotRequired[str],
        "scheduleOffset": NotRequired[int],
        "firstExecutionFrom": NotRequired[TimestampTypeDef],
        "flowErrorDeactivationThreshold": NotRequired[int],
    },
)

CustomConnectorProfileCredentialsTypeDef = TypedDict(
    "CustomConnectorProfileCredentialsTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "basic": NotRequired[BasicAuthCredentialsTypeDef],
        "oauth2": NotRequired[OAuth2CredentialsTypeDef],
        "apiKey": NotRequired[ApiKeyCredentialsTypeDef],
        "custom": NotRequired[CustomAuthCredentialsTypeDef],
    },
)

ServiceNowConnectorProfileCredentialsTypeDef = TypedDict(
    "ServiceNowConnectorProfileCredentialsTypeDef",
    {
        "username": NotRequired[str],
        "password": NotRequired[str],
        "oAuth2Credentials": NotRequired[OAuth2CredentialsTypeDef],
    },
)

SAPODataConnectorProfileCredentialsTypeDef = TypedDict(
    "SAPODataConnectorProfileCredentialsTypeDef",
    {
        "basicAuthCredentials": NotRequired[BasicAuthCredentialsTypeDef],
        "oAuthCredentials": NotRequired[OAuthCredentialsTypeDef],
    },
)

RegisterConnectorRequestRequestTypeDef = TypedDict(
    "RegisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": NotRequired[str],
        "description": NotRequired[str],
        "connectorProvisioningType": NotRequired[Literal["LAMBDA"]],
        "connectorProvisioningConfig": NotRequired[ConnectorProvisioningConfigTypeDef],
        "clientToken": NotRequired[str],
    },
)

UpdateConnectorRegistrationRequestRequestTypeDef = TypedDict(
    "UpdateConnectorRegistrationRequestRequestTypeDef",
    {
        "connectorLabel": str,
        "description": NotRequired[str],
        "connectorProvisioningConfig": NotRequired[ConnectorProvisioningConfigTypeDef],
        "clientToken": NotRequired[str],
    },
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "flows": List[FlowDefinitionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SupportedFieldTypeDetailsTypeDef = TypedDict(
    "SupportedFieldTypeDetailsTypeDef",
    {
        "v1": FieldTypeDetailsTypeDef,
    },
)

ExecutionRecordTypeDef = TypedDict(
    "ExecutionRecordTypeDef",
    {
        "executionId": NotRequired[str],
        "executionStatus": NotRequired[ExecutionStatusType],
        "executionResult": NotRequired[ExecutionResultTypeDef],
        "startedAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "dataPullStartTime": NotRequired[datetime],
        "dataPullEndTime": NotRequired[datetime],
        "metadataCatalogDetails": NotRequired[List[MetadataCatalogDetailTypeDef]],
    },
)

AuthenticationConfigTypeDef = TypedDict(
    "AuthenticationConfigTypeDef",
    {
        "isBasicAuthSupported": NotRequired[bool],
        "isApiKeyAuthSupported": NotRequired[bool],
        "isOAuth2Supported": NotRequired[bool],
        "isCustomAuthSupported": NotRequired[bool],
        "oAuth2Defaults": NotRequired[OAuth2DefaultsTypeDef],
        "customAuthConfigs": NotRequired[List[CustomAuthConfigTypeDef]],
    },
)

ConnectorProfilePropertiesTypeDef = TypedDict(
    "ConnectorProfilePropertiesTypeDef",
    {
        "Amplitude": NotRequired[Mapping[str, Any]],
        "Datadog": NotRequired[DatadogConnectorProfilePropertiesTypeDef],
        "Dynatrace": NotRequired[DynatraceConnectorProfilePropertiesTypeDef],
        "GoogleAnalytics": NotRequired[Mapping[str, Any]],
        "Honeycode": NotRequired[Mapping[str, Any]],
        "InforNexus": NotRequired[InforNexusConnectorProfilePropertiesTypeDef],
        "Marketo": NotRequired[MarketoConnectorProfilePropertiesTypeDef],
        "Redshift": NotRequired[RedshiftConnectorProfilePropertiesTypeDef],
        "Salesforce": NotRequired[SalesforceConnectorProfilePropertiesTypeDef],
        "ServiceNow": NotRequired[ServiceNowConnectorProfilePropertiesTypeDef],
        "Singular": NotRequired[Mapping[str, Any]],
        "Slack": NotRequired[SlackConnectorProfilePropertiesTypeDef],
        "Snowflake": NotRequired[SnowflakeConnectorProfilePropertiesTypeDef],
        "Trendmicro": NotRequired[Mapping[str, Any]],
        "Veeva": NotRequired[VeevaConnectorProfilePropertiesTypeDef],
        "Zendesk": NotRequired[ZendeskConnectorProfilePropertiesTypeDef],
        "SAPOData": NotRequired[SAPODataConnectorProfilePropertiesTypeDef],
        "CustomConnector": NotRequired[CustomConnectorProfilePropertiesTypeDef],
        "Pardot": NotRequired[PardotConnectorProfilePropertiesTypeDef],
    },
)

S3DestinationPropertiesTypeDef = TypedDict(
    "S3DestinationPropertiesTypeDef",
    {
        "bucketName": str,
        "bucketPrefix": NotRequired[str],
        "s3OutputFormatConfig": NotRequired[S3OutputFormatConfigTypeDef],
    },
)

UpsolverDestinationPropertiesTypeDef = TypedDict(
    "UpsolverDestinationPropertiesTypeDef",
    {
        "bucketName": str,
        "s3OutputFormatConfig": UpsolverS3OutputFormatConfigTypeDef,
        "bucketPrefix": NotRequired[str],
    },
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Amplitude": NotRequired[AmplitudeSourcePropertiesTypeDef],
        "Datadog": NotRequired[DatadogSourcePropertiesTypeDef],
        "Dynatrace": NotRequired[DynatraceSourcePropertiesTypeDef],
        "GoogleAnalytics": NotRequired[GoogleAnalyticsSourcePropertiesTypeDef],
        "InforNexus": NotRequired[InforNexusSourcePropertiesTypeDef],
        "Marketo": NotRequired[MarketoSourcePropertiesTypeDef],
        "S3": NotRequired[S3SourcePropertiesTypeDef],
        "Salesforce": NotRequired[SalesforceSourcePropertiesTypeDef],
        "ServiceNow": NotRequired[ServiceNowSourcePropertiesTypeDef],
        "Singular": NotRequired[SingularSourcePropertiesTypeDef],
        "Slack": NotRequired[SlackSourcePropertiesTypeDef],
        "Trendmicro": NotRequired[TrendmicroSourcePropertiesTypeDef],
        "Veeva": NotRequired[VeevaSourcePropertiesTypeDef],
        "Zendesk": NotRequired[ZendeskSourcePropertiesTypeDef],
        "SAPOData": NotRequired[SAPODataSourcePropertiesTypeDef],
        "CustomConnector": NotRequired[CustomConnectorSourcePropertiesTypeDef],
        "Pardot": NotRequired[PardotSourcePropertiesTypeDef],
    },
)

TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": NotRequired[ScheduledTriggerPropertiesTypeDef],
    },
)

ConnectorProfileCredentialsTypeDef = TypedDict(
    "ConnectorProfileCredentialsTypeDef",
    {
        "Amplitude": NotRequired[AmplitudeConnectorProfileCredentialsTypeDef],
        "Datadog": NotRequired[DatadogConnectorProfileCredentialsTypeDef],
        "Dynatrace": NotRequired[DynatraceConnectorProfileCredentialsTypeDef],
        "GoogleAnalytics": NotRequired[GoogleAnalyticsConnectorProfileCredentialsTypeDef],
        "Honeycode": NotRequired[HoneycodeConnectorProfileCredentialsTypeDef],
        "InforNexus": NotRequired[InforNexusConnectorProfileCredentialsTypeDef],
        "Marketo": NotRequired[MarketoConnectorProfileCredentialsTypeDef],
        "Redshift": NotRequired[RedshiftConnectorProfileCredentialsTypeDef],
        "Salesforce": NotRequired[SalesforceConnectorProfileCredentialsTypeDef],
        "ServiceNow": NotRequired[ServiceNowConnectorProfileCredentialsTypeDef],
        "Singular": NotRequired[SingularConnectorProfileCredentialsTypeDef],
        "Slack": NotRequired[SlackConnectorProfileCredentialsTypeDef],
        "Snowflake": NotRequired[SnowflakeConnectorProfileCredentialsTypeDef],
        "Trendmicro": NotRequired[TrendmicroConnectorProfileCredentialsTypeDef],
        "Veeva": NotRequired[VeevaConnectorProfileCredentialsTypeDef],
        "Zendesk": NotRequired[ZendeskConnectorProfileCredentialsTypeDef],
        "SAPOData": NotRequired[SAPODataConnectorProfileCredentialsTypeDef],
        "CustomConnector": NotRequired[CustomConnectorProfileCredentialsTypeDef],
        "Pardot": NotRequired[PardotConnectorProfileCredentialsTypeDef],
    },
)

ConnectorEntityFieldTypeDef = TypedDict(
    "ConnectorEntityFieldTypeDef",
    {
        "identifier": str,
        "parentIdentifier": NotRequired[str],
        "label": NotRequired[str],
        "isPrimaryKey": NotRequired[bool],
        "defaultValue": NotRequired[str],
        "isDeprecated": NotRequired[bool],
        "supportedFieldTypeDetails": NotRequired[SupportedFieldTypeDetailsTypeDef],
        "description": NotRequired[str],
        "sourceProperties": NotRequired[SourceFieldPropertiesTypeDef],
        "destinationProperties": NotRequired[DestinationFieldPropertiesTypeDef],
        "customProperties": NotRequired[Dict[str, str]],
    },
)

DescribeFlowExecutionRecordsResponseTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsResponseTypeDef",
    {
        "flowExecutions": List[ExecutionRecordTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConnectorConfigurationTypeDef = TypedDict(
    "ConnectorConfigurationTypeDef",
    {
        "canUseAsSource": NotRequired[bool],
        "canUseAsDestination": NotRequired[bool],
        "supportedDestinationConnectors": NotRequired[List[ConnectorTypeType]],
        "supportedSchedulingFrequencies": NotRequired[List[ScheduleFrequencyTypeType]],
        "isPrivateLinkEnabled": NotRequired[bool],
        "isPrivateLinkEndpointUrlRequired": NotRequired[bool],
        "supportedTriggerTypes": NotRequired[List[TriggerTypeType]],
        "connectorMetadata": NotRequired[ConnectorMetadataTypeDef],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "connectorDescription": NotRequired[str],
        "connectorOwner": NotRequired[str],
        "connectorName": NotRequired[str],
        "connectorVersion": NotRequired[str],
        "connectorArn": NotRequired[str],
        "connectorModes": NotRequired[List[str]],
        "authenticationConfig": NotRequired[AuthenticationConfigTypeDef],
        "connectorRuntimeSettings": NotRequired[List[ConnectorRuntimeSettingTypeDef]],
        "supportedApiVersions": NotRequired[List[str]],
        "supportedOperators": NotRequired[List[OperatorsType]],
        "supportedWriteOperations": NotRequired[List[WriteOperationTypeType]],
        "connectorProvisioningType": NotRequired[Literal["LAMBDA"]],
        "connectorProvisioningConfig": NotRequired[ConnectorProvisioningConfigTypeDef],
        "logoURL": NotRequired[str],
        "registeredAt": NotRequired[datetime],
        "registeredBy": NotRequired[str],
        "supportedDataTransferTypes": NotRequired[List[SupportedDataTransferTypeType]],
        "supportedDataTransferApis": NotRequired[List[DataTransferApiTypeDef]],
    },
)

ConnectorProfileTypeDef = TypedDict(
    "ConnectorProfileTypeDef",
    {
        "connectorProfileArn": NotRequired[str],
        "connectorProfileName": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "connectionMode": NotRequired[ConnectionModeType],
        "credentialsArn": NotRequired[str],
        "connectorProfileProperties": NotRequired[ConnectorProfilePropertiesTypeDef],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "privateConnectionProvisioningState": NotRequired[
            PrivateConnectionProvisioningStateTypeDef
        ],
    },
)

DestinationConnectorPropertiesTypeDef = TypedDict(
    "DestinationConnectorPropertiesTypeDef",
    {
        "Redshift": NotRequired[RedshiftDestinationPropertiesTypeDef],
        "S3": NotRequired[S3DestinationPropertiesTypeDef],
        "Salesforce": NotRequired[SalesforceDestinationPropertiesTypeDef],
        "Snowflake": NotRequired[SnowflakeDestinationPropertiesTypeDef],
        "EventBridge": NotRequired[EventBridgeDestinationPropertiesTypeDef],
        "LookoutMetrics": NotRequired[Mapping[str, Any]],
        "Upsolver": NotRequired[UpsolverDestinationPropertiesTypeDef],
        "Honeycode": NotRequired[HoneycodeDestinationPropertiesTypeDef],
        "CustomerProfiles": NotRequired[CustomerProfilesDestinationPropertiesTypeDef],
        "Zendesk": NotRequired[ZendeskDestinationPropertiesTypeDef],
        "Marketo": NotRequired[MarketoDestinationPropertiesTypeDef],
        "CustomConnector": NotRequired[CustomConnectorDestinationPropertiesTypeDef],
        "SAPOData": NotRequired[SAPODataDestinationPropertiesTypeDef],
    },
)

SourceFlowConfigTypeDef = TypedDict(
    "SourceFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "sourceConnectorProperties": SourceConnectorPropertiesTypeDef,
        "apiVersion": NotRequired[str],
        "connectorProfileName": NotRequired[str],
        "incrementalPullConfig": NotRequired[IncrementalPullConfigTypeDef],
    },
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "triggerType": TriggerTypeType,
        "triggerProperties": NotRequired[TriggerPropertiesTypeDef],
    },
)

ConnectorProfileConfigTypeDef = TypedDict(
    "ConnectorProfileConfigTypeDef",
    {
        "connectorProfileProperties": ConnectorProfilePropertiesTypeDef,
        "connectorProfileCredentials": NotRequired[ConnectorProfileCredentialsTypeDef],
    },
)

DescribeConnectorEntityResponseTypeDef = TypedDict(
    "DescribeConnectorEntityResponseTypeDef",
    {
        "connectorEntityFields": List[ConnectorEntityFieldTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "connectorConfiguration": ConnectorConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConnectorsResponseTypeDef = TypedDict(
    "DescribeConnectorsResponseTypeDef",
    {
        "connectorConfigurations": Dict[ConnectorTypeType, ConnectorConfigurationTypeDef],
        "connectors": List[ConnectorDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConnectorProfilesResponseTypeDef = TypedDict(
    "DescribeConnectorProfilesResponseTypeDef",
    {
        "connectorProfileDetails": List[ConnectorProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DestinationFlowConfigTypeDef = TypedDict(
    "DestinationFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "destinationConnectorProperties": DestinationConnectorPropertiesTypeDef,
        "apiVersion": NotRequired[str],
        "connectorProfileName": NotRequired[str],
    },
)

CreateConnectorProfileRequestRequestTypeDef = TypedDict(
    "CreateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": ConnectorProfileConfigTypeDef,
        "kmsArn": NotRequired[str],
        "connectorLabel": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

UpdateConnectorProfileRequestRequestTypeDef = TypedDict(
    "UpdateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": ConnectorProfileConfigTypeDef,
        "clientToken": NotRequired[str],
    },
)

CreateFlowRequestRequestTypeDef = TypedDict(
    "CreateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": TriggerConfigTypeDef,
        "sourceFlowConfig": SourceFlowConfigTypeDef,
        "destinationFlowConfigList": Sequence[DestinationFlowConfigTypeDef],
        "tasks": Sequence[TaskTypeDef],
        "description": NotRequired[str],
        "kmsArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "metadataCatalogConfig": NotRequired[MetadataCatalogConfigTypeDef],
        "clientToken": NotRequired[str],
    },
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "kmsArn": str,
        "flowStatus": FlowStatusType,
        "flowStatusMessage": str,
        "sourceFlowConfig": SourceFlowConfigTypeDef,
        "destinationFlowConfigList": List[DestinationFlowConfigTypeDef],
        "lastRunExecutionDetails": ExecutionDetailsTypeDef,
        "triggerConfig": TriggerConfigTypeDef,
        "tasks": List[TaskTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
        "metadataCatalogConfig": MetadataCatalogConfigTypeDef,
        "lastRunMetadataCatalogDetails": List[MetadataCatalogDetailTypeDef],
        "schemaVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFlowRequestRequestTypeDef = TypedDict(
    "UpdateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": TriggerConfigTypeDef,
        "sourceFlowConfig": SourceFlowConfigTypeDef,
        "destinationFlowConfigList": Sequence[DestinationFlowConfigTypeDef],
        "tasks": Sequence[TaskTypeDef],
        "description": NotRequired[str],
        "metadataCatalogConfig": NotRequired[MetadataCatalogConfigTypeDef],
        "clientToken": NotRequired[str],
    },
)
