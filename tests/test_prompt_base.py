from evals.prompt.base import CompletionPrompt, chat_prompt_to_text_prompt, is_chat_prompt


def test_empty_list_is_not_a_chat_prompt() -> None:
    assert not is_chat_prompt([])


def test_non_empty_message_list_is_a_chat_prompt() -> None:
    assert is_chat_prompt([{"role": "user", "content": "hello"}])
    assert is_chat_prompt(
        [
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": "hello"},
        ]
    )


def test_non_message_lists_are_not_chat_prompts() -> None:
    assert not is_chat_prompt(["hello"])
    assert not is_chat_prompt([1, 2, 3])
    assert not is_chat_prompt([{"role": "user"}, "hello"])


def test_empty_list_is_preserved_by_completion_prompt_routing() -> None:
    prompt = CompletionPrompt(raw_prompt=[])

    assert prompt.to_formatted_prompt() == []


def test_chat_prompt_rendering_for_non_empty_messages_is_unchanged() -> None:
    assert chat_prompt_to_text_prompt([{"role": "user", "content": "hello"}]) == "hello"
