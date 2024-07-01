from os import getenv
from typing import Any

from pas.llm.openai.like import OpenAILike
from pas.utils.log import logger

try:
    from openai import AzureOpenAI as AzureOpenAIClient
except ImportError:
    from pas.const import DEPENDENCY_GROUP_OPENAI, IMPORT_ERROR

    logger.error(IMPORT_ERROR("openai", DEPENDENCY_GROUP_OPENAI))
    raise


class AzureOpenAIChat(OpenAILike):
    name: str = "AzureOpenAIChat"
    model: str
    api_key: str | None = getenv("AZURE_OPENAI_API_KEY")
    api_version: str = getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
    azure_endpoint: str | None = getenv("AZURE_OPENAI_ENDPOINT")
    azure_deployment: str | None = getenv("AZURE_DEPLOYMENT")
    base_url: str | None = None
    azure_ad_token: str | None = None
    azure_ad_token_provider: Any | None = None
    organization: str | None = None
    openai_client: AzureOpenAIClient | None = None

    def get_client(self) -> AzureOpenAIClient:
        if self.openai_client:
            return self.openai_client

        _client_params: dict[str, Any] = {}
        if self.api_key:
            _client_params["api_key"] = self.api_key
        if self.api_version:
            _client_params["api_version"] = self.api_version
        if self.organization:
            _client_params["organization"] = self.organization
        if self.azure_endpoint:
            _client_params["azure_endpoint"] = self.azure_endpoint
        if self.azure_deployment:
            _client_params["azure_deployment"] = self.azure_deployment
        if self.base_url:
            _client_params["base_url"] = self.base_url
        if self.azure_ad_token:
            _client_params["azure_ad_token"] = self.azure_ad_token
        if self.azure_ad_token_provider:
            _client_params["azure_ad_token_provider"] = self.azure_ad_token_provider
        if self.http_client:
            _client_params["http_client"] = self.http_client
        if self.client_params:
            _client_params.update(self.client_params)

        return AzureOpenAIClient(**_client_params)
