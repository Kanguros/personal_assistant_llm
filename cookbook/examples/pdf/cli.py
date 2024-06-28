import typer
from resources import vector_db  # type: ignore

from pas.assistant import Assistant
from pas.knowledge.pdf import PDFUrlKnowledgeBase
from pas.storage.assistant.postgres import PgAssistantStorage
from pas.knowledge.vectordb import PgVector2

db_url = vector_db.get_db_connection_local()
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes", db_url=db_url),
)
knowledge_base.load(recreate=False)  # Comment out after first run
storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)


def pdf_assistant(new: bool = False, user: str = "user"):
    run_id: str | None = None
    if not new:
        existing_run_ids: list[str] = storage.get_all_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        use_tools=True,
        show_tool_calls=True,
    )
    assistant.cli_app(markdown=True)


if __name__ == "__main__":
    typer.run(pdf_assistant)
