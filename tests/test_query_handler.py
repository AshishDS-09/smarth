from src.api.query_handler import answer_question

def test_answer_question():
    answer, sources = answer_question("Compare rainfall in State_X and State_Y.")
    assert isinstance(answer, str)
    assert isinstance(sources, list)
