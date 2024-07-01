import json
from typing import Any

from pas.tools import Toolkit
from pas.utils.log import logger

try:
    from duckduckgo_search import DDGS
except ImportError:
    from pas.const import DEPENDENCY_GROUP_WEBTOOLS, IMPORT_ERROR

    logger.error(IMPORT_ERROR("duckduckgo_search", DEPENDENCY_GROUP_WEBTOOLS))
    raise


class DuckDuckGo(Toolkit):
    def __init__(
        self,
        search: bool = True,
        news: bool = True,
        fixed_max_results: int | None = None,
        headers: Any | None = None,
        proxy: str | None = None,
        proxies: Any | None = None,
        timeout: int | None = 10,
    ):
        super().__init__(name="duckduckgo")

        self.headers: Any | None = headers
        self.proxy: str | None = proxy
        self.proxies: Any | None = proxies
        self.timeout: int | None = timeout
        self.fixed_max_results: int | None = fixed_max_results
        if search:
            self.register(self.duckduckgo_search)
        if news:
            self.register(self.duckduckgo_news)

    def duckduckgo_search(self, query: str, max_results: int = 5) -> str:
        """Use this function to search DuckDuckGo for a query.

        Args:
            query(str): The query to search for.
            max_results (optional, default=5): The maximum number of results to return.

        Returns:
            The result from DuckDuckGo.
        """
        logger.debug(f"Searching DDG for: {query}")
        ddgs = DDGS(
            headers=self.headers,
            proxy=self.proxy,
            proxies=self.proxies,
            timeout=self.timeout,
        )
        return json.dumps(
            ddgs.text(
                keywords=query,
                max_results=(self.fixed_max_results or max_results),
            ),
            indent=2,
        )

    def duckduckgo_news(self, query: str, max_results: int = 5) -> str:
        """Use this function to get the latest news from DuckDuckGo.

        Args:
            query(str): The query to search for.
            max_results (optional, default=5): The maximum number of results to return.

        Returns:
            The latest news from DuckDuckGo.
        """
        logger.debug(f"Searching DDG news for: {query}")
        ddgs = DDGS(
            headers=self.headers,
            proxy=self.proxy,
            proxies=self.proxies,
            timeout=self.timeout,
        )
        return json.dumps(
            ddgs.news(
                keywords=query,
                max_results=(self.fixed_max_results or max_results),
            ),
            indent=2,
        )
