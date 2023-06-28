from solutions.CHK import checkout_solution


class TestCheckout():

    def test_clean_and_check_input(self):
        assert checkout_solution.clean_and_check_input('A--b Cc D   B_A') == 'ABCCDBA'
        assert checkout_solution.clean_and_check_input('A_4 D') == None
        assert checkout_solution.clean_and_check_input('') == None
        assert checkout_solution.clean_and_check_input('A--b Cc D   B_A E') == None
    def test_checkout(self):
        pass