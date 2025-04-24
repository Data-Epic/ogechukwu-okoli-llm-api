import pytest
from chatbot import EducationalCustomerAssistant  #importing module name
@pytest.fixture
def assistant():
    api_key = "gsk_blahblahblah12345678"  # mock/fake key for testing
    return EducationalCustomerAssistant(api_key)

# testingfor a particular chat history
def test_initialization(assistant):
    assert len(assistant.chat_history) == 1
    assert assistant.chat_history[0]["role"] == "system"
# testing for a cleaned response that removes<thinks>

def test_clean_response_removes_think(assistant):
    test = "<think>This should be removed</think>This stays."
    cleaned = assistant.clean_response(test)
    assert cleaned == "This stays."
#testing for a response that removes user since my chat history is a list that stores chats history
def test_clean_response_removes_user_reference(assistant):
    test = "The user asked what the top university is.Obafemi Awolowo univeristy(Oba Awon Univeristy) is Nigeria's top university."
    cleaned = assistant.clean_response(test)
    assert cleaned.strip() == "Obafemi Awolowo univeristy(Oba Awon Univeristy) is Nigeria's top university."
#testing for a response that removes user and <thinks>
def test_clean_response_combined(assistant):
    test = "<think></think>The user mentioned something. Result: done."
    cleaned = assistant.clean_response(test)
    assert cleaned.strip() == "Result: done."