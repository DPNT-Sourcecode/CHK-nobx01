from solutions.CHK import checkout_solution


class TestCheckout():

    def test_clean_and_check_input(self):
        assert checkout_solution.clean_and_check_input('A--B CC D   B_A') == 'ABCCDBA'
        assert checkout_solution.clean_and_check_input('A--b cC D   B_A') == None
        assert checkout_solution.clean_and_check_input('A_4 D') == None
        assert checkout_solution.clean_and_check_input('A--b Cc D   B_A E') == None

    def test_count_items(self):
        assert checkout_solution.count_items('ABBCCDDC') == {'A': 1, 'B': 2, 'C': 3, 'D':2}

    def test_checkout(self):
        assert checkout_solution.checkout('') == 0
        assert checkout_solution.checkout('ABE') == -1
        assert checkout_solution.checkout('AAAAABBBBBCD') == 385
        assert checkout_solution.checkout('ABB') == 95
        assert checkout_solution.checkout('AAAAAAAAAAABBBBBBBCCCCDDDD') == 795
        assert checkout_solution.checkout('a') == -1
        assert checkout_solution.checkout('ABCa') == -1