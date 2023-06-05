import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets as mbv


@pytest.mark.parametrize(
    "test_input, expected",
    [
      ('{}', True),
      ('{}(){}', True),
      ('()[[Extra Characters]]', True),
      ('(){}[[]]', True),
      ('{}{Code}[Fellows](())', True),
      ('[({}]', False),
      ('(](', False),
      ('{(})', False),
      ('{', False),
      (')', False),
      ('[}', False),
      ('[[[[[[', False),
      ('}{}{}', False),
      ('}{][090)', False),
      (' ', True)
    ]
)
def test_bracket_validation(test_input, expected):
  actual = mbv(test_input)
  assert actual == expected

# def testtesttest():
#   actual = mbv('{}')
#   expected = True
#   assert actual == expected