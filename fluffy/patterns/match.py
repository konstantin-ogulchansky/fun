from typing import Any

from fluffy.patterns.case import Case


def match(value: Any, *cases: Case):
    """Tries to match the input data to one of the specified cases.

    :param value: input data to match
    :param cases: list of cases to match the input against
    """

    for pattern, expression in cases:
        if (args := pattern.match(value)) is not None:
            return expression.eval(args)

    raise ValueError(f"Could not match {repr(value)}.")
