from solutions.CHK import checkout_solution
from solutions.CHK.checkout_solution import apply_free_items
from solutions.CHK.checkout_solution import clean_and_check_input, count_items


class TestCheckout():

    def test_clean_and_check_input(self):
        assert checkout_solution.clean_and_check_input('A--B CC D   B_A') == 'ABCCDBA'
        assert checkout_solution.clean_and_check_input('A--b cC D   B_A') == None
        assert checkout_solution.clean_and_check_input('A_4 D') == None
        assert checkout_solution.clean_and_check_input('A--B CC D   B_A F') == None

    def test_count_items(self):
        assert checkout_solution.count_items('ABBCCDDC') == {'A': 1, 'B': 2, 'C': 3, 'D':2}

    def test_apply_free_items(self):
        input = clean_and_check_input('B'*2+'E'*7)
        assert apply_free_items(count_items(input)) == {'B':0, 'E':7}
        input = clean_and_check_input('B'*5 + 'E'*6)
        assert apply_free_items(count_items(input)) == {'B': 2, 'E': 6}

    def test_checkout(self):
        assert checkout_solution.checkout('') == 0
        assert checkout_solution.checkout('ABF') == -1
        assert checkout_solution.checkout('ABCa') == -1
        assert checkout_solution.checkout('A'*5 + 'B'*5 + 'CD') == 355
        assert checkout_solution.checkout('A' + 'B' * 2) == 95
        assert checkout_solution.checkout('A'*11 + 'B'*7 + 'C'*4 + 'D'*4) == 755
        # no qualified offers
        assert checkout_solution.checkout('ABE') == 120
        # free offers
        assert checkout_solution.checkout('ABEE') == 130
        # free and special offers
        assert checkout_solution.checkout('B'*2 + 'E'*7) == 280
        assert checkout_solution.checkout('A'*2 + 'B'*6 + 'E'*7) == 455
        # assert checkout_solution.checkout('AAAAABBBBBCD') == 385
        # assert checkout_solution.checkout('ABB') == 95
        # assert checkout_solution.checkout('AAAAAAAAAAABBBBBBBCCCCDDDD') == 795
        # assert checkout_solution.checkout('a') == -1
        # assert checkout_solution.checkout('ABCa') == -1
