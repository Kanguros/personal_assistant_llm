from typing import Any

from phi.embedder.base import Embedder
from phi.utils.log import logger

try:
    from ollama import Client as OllamaClient
except ImportError:
    logger.error("`ollama` not installed")
    raise


class OllamaEmbedder(Embedder):
    model: str = "openhermes"
    dimensions: int = 4096
    host: str | None = None
    timeout: Any | None = None
    options: Any | None = None
    client_kwargs: dict[str, Any] | None = None
    ollama_client: OllamaClient | None = None

    @property
    def client(self) -> OllamaClient:
        if self.ollama_client:
            return self.ollama_client

        _ollama_params: dict[str, Any] = {}
        if self.host:
            _ollama_params["host"] = self.host
        if self.timeout:
            _ollama_params["timeout"] = self.timeout
        if self.client_kwargs:
            _ollama_params.update(self.client_kwargs)
        return OllamaClient(**_ollama_params)

    def _response(self, text: str) -> dict[str, Any]:
        kwargs: dict[str, Any] = {}
        if self.options is not None:
            kwargs["options"] = self.options

        return self.client.embeddings(prompt=text, model=self.model, **kwargs)  # type: ignore

    def get_embedding(self, text: str) -> list[float]:
        try:
            response = self._response(text=text)
            if response is None:
                return []
            return response.get("embedding", [])
        except Exception as e:
            logger.warning(e)
            return []

    def get_embedding_and_usage(self, text: str) -> tuple[list[float], dict | None]:
        embedding = []
        usage = None
        try:
            response = self._response(text=text)
            if response is not None:
                embedding = response.get("embedding", [])
        except Exception as e:
            logger.warning(e)
        return embedding, usage
