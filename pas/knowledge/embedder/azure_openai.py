from os import getenv
from typing import Any, Literal

from pas.knowledge.embedder.base import Embedder
from pas.utils.log import logger

try:
    from openai import AzureOpenAI as AzureOpenAIClient
    from openai.types.create_embedding_response import CreateEmbeddingResponse
except ImportError:
    from pas.const import DEPENDENCY_GROUP_OPENAI, IMPORT_ERROR

    logger.error(IMPORT_ERROR("openai", DEPENDENCY_GROUP_OPENAI))


class AzureOpenAIEmbedder(Embedder):
    model: str = "text-embedding-ada-002"
    dimensions: int = 1536
    encoding_format: Literal["float", "base64"] = "float"
    user: str | None = None
    api_key: str | None = getenv("AZURE_OPENAI_API_KEY")
    api_version: str = getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
    azure_endpoint: str | None = getenv("AZURE_OPENAI_ENDPOINT")
    azure_deployment: str | None = getenv("AZURE_DEPLOYMENT")
    base_url: str | None = None
    azure_ad_token: str | None = None
    azure_ad_token_provider: Any | None = None
    organization: str | None = None
    request_params: dict[str, Any] | None = None
    client_params: dict[str, Any] | None = None
    openai_client: AzureOpenAIClient | None = None

    @property
    def client(self) -> AzureOpenAIClient:
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
        return AzureOpenAIClient(**_client_params)

    def _response(self, text: str) -> CreateEmbeddingResponse:
        _request_params: dict[str, Any] = {
            "input": text,
            "model": self.model,
            "encoding_format": self.encoding_format,
        }
        if self.user is not None:
            _request_params["user"] = self.user
        if self.model.startswith("text-embedding-3"):
            _request_params["dimensions"] = self.dimensions
        if self.request_params:
            _request_params.update(self.request_params)
        return self.client.embeddings.create(**_request_params)

    def get_embedding(self, text: str) -> list[float]:
        response: CreateEmbeddingResponse = self._response(text=text)
        try:
            return response.data[0].embedding
        except Exception as e:
            logger.warning(e)
            return []

    def get_embedding_and_usage(self, text: str) -> tuple[list[float], dict | None]:
        response: CreateEmbeddingResponse = self._response(text=text)

        embedding = response.data[0].embedding
        usage = response.usage
        return embedding, usage.model_dump()
