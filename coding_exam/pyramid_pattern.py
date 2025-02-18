import pytest


def pyramid_pattern(n: int) -> str:
    result = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        result.append(spaces + stars.strip())
    return "\n".join(result)


@pytest.mark.parametrize("n, expected_output", [
    (3, "  *\n * *\n* * *"),
    (5, "    *\n   * *\n  * * *\n * * * *\n* * * * *"),
    (7, "      *\n     * *\n    * * *\n   * * * *\n  * * * * *\n * * * * * *\n* * * * * * *"),
    (9, "        *\n"
        "       * *\n"
        "      * * *\n"
        "     * * * *\n"
        "    * * * * *\n"
        "   * * * * * *\n"
        "  * * * * * * *\n"
        " * * * * * * * *\n"
        "* * * * * * * * *"),
])
def test_pyramid_pattern(n, expected_output):
    assert pyramid_pattern(n) == expected_output
