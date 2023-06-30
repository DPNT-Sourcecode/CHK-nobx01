from solutions.CHK import checkout_solution
from solutions.CHK.checkout_solution import apply_free_items, PRICES
from solutions.CHK.checkout_solution import clean_and_check_input, count_items, calculate_items_eligible_for_group_discount


class TestCheckout():

    def test_clean_and_check_input(self):
        inputs = ['A--B CC D   B_A', 'A--b cC D   B_A', 'A_4 D']
        expected_outputs = ['ABCCDBA', None, None]
        for input, expected in zip(inputs, expected_outputs):
            assert clean_and_check_input(input) == expected


    def test_count_items(self):
        assert checkout_solution.count_items('ABBCCDDC') == {'A': 1, 'B': 2, 'C': 3, 'D':2}

    def test_apply_free_items(self):
        inputs = [
            'B'*2+'E'*7,
            'B' * 5 + 'E' * 6,
            'B' * 5 + 'E' * 6 + 'F' * 2,
            'B' * 5 + 'E' * 6 + 'F' * 3,
            'U' * 3,
            'U' * 4,
            'U' * 5,
            'U' * 6,
            'U' * 7,
            'U' * 8,
        ]
        expected_counted_items = [
            {'B':0, 'E':7},
            {'B': 2, 'E': 6},
            {'B': 2, 'E': 6, 'F': 2},
            {'B': 2, 'E': 6, 'F': 2},
            {'U': 3},
            {'U': 3},
            {'U': 4},
            {'U': 5},
            {'U': 6},
            {'U': 6},
        ]
        for input, expected in zip(inputs, expected_counted_items):
            input1 = clean_and_check_input(input)
            assert apply_free_items(count_items(input1)) == expected

    def test_calculate_items_eligible_for_group_discount(self):
        inputs = ["SSSTTTUUUVVVWWXXYYYZ", "SSSSTTTUUUVVVWWXXYYYZZ"]
        expected_totals = [180, 214]
        expected_counted_items = [{'U': 3, 'V': 3, 'W': 2}, {'U': 3, 'V': 3, 'W': 2}]
        for input, expected_total, expected_counts in zip(inputs, expected_totals, expected_counted_items):
            cleaned_input = clean_and_check_input(input)
            counted_items = count_items(cleaned_input)
            counted_items = apply_free_items(counted_items)
            total, counted_items = calculate_items_eligible_for_group_discount(counted_items)
            assert total==expected_total
            assert counted_items==expected_counts



    def test_checkout(self):
        # empty string
        assert checkout_solution.checkout('') == 0
        # invalid input
        assert checkout_solution.checkout('ABCa') == -1

        # single items
        for item, expected in zip(PRICES.keys(), [PRICES[item]['price'] for item in PRICES.keys()]):
            assert checkout_solution.checkout(item) == expected

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
        # multiple non-free special offers
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4) == 885
        assert checkout_solution.checkout('A'*14 + 'B'*5 + 'C'*2 + 'D'*2) == 770
        # round-3 checks
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*2) == 905
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*5) == 925
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*6) == 925
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*7) == 935
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*8) == 945
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*9) == 945
        assert checkout_solution.checkout('A'*14 + 'B'*7 + 'C'*4 + 'D'*4 + 'F'*10) == 955
        # checks for round 4
        assert checkout_solution.checkout('H'*38) == 3*80 + 1*45 + 3*10
        assert checkout_solution.checkout('V' * 16) == 5*130 + 1*50
        assert checkout_solution.checkout('V' * 17) == 5 * 130 + 1 * 90
        assert checkout_solution.checkout('R' * 7 + 'Q'*9) == 7 * 50 + 2*80 + 30



