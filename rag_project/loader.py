from sql_knowledge import SQL_INTRO, SQL_BASIC_COMMANDS, SQL_FAQ

def load_documents():
    docs = [
        {"id": "sql_intro", "text": SQL_INTRO},
        {"id": "sql_basic_commands", "text": SQL_BASIC_COMMANDS},
        {"id": "sql_faq", "text": SQL_FAQ},
    ]
    return docs
