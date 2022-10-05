import checker
def test_check_syntax():

    url1 = checker.checkSyntax('https://twitter.com/aactionmovers;')

    assert url1 == False, "some error message"
