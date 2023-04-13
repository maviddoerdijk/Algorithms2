import typing
import unittest
import numpy as np

from divconq import IntelDevice


class TestIntelDevice(unittest.TestCase):
    def create_arrays(self):    

        self.arr_list = [] # List of nxn arrays self.arr_list[n]
        for n in range(0, 11):
            arr = np.zeros((n, n), dtype=int)
            for i in range(n):
                for j in range(n):
                    arr[i, j] = i*n + j + 1
            self.arr_list.append(arr)


    def private_test1(self):
        a = self.arr_list[3]
        print(a)

        raw_locations = [f"l{i}" for i in range(12)]
        raw_codes = [str(x) for x in a.reshape(-1)]

        shift = 2


        enc_locations = [
            "1101110 110010",
            "1101110 110011",
            "1101110 110100",
            "1101110 110101",
            "1101110 110110",
            "1101110 110111",
            "1101110 111000",
            "1101110 111001",
            "1101110 111010",
            "1101110 111011",
            "1101110 110011 110010",
            "1101110 110011 110011"
        ]

        enc_codes = [
            "110011",
            "110011 110010",
            "110101 110010",
            "110111 110011",
            "110011 111000",
            "110100 110010",
            "110110 110100",
            "110111 110100",
            "110101 110100",
            "110110 111001",
            "110111 111001",
            "111010 110010",
        ]

        solutions = [
            "1101110 110010",
            "1101110 110011",
            "1101110 110100",
            "1101110 110101",
            "1101110 110110",
            "1101110 110111",
            "1101110 111000",
            "1101110 111001",
            "1101110 111010",
            "1101110 111011",
            "1101110 110011 110010",
            "1101110 110011 110011"
        ]

        ob = IntelDevice(4,3, enc_locations, enc_codes, 2)
        ob.fill_coordinate_to_loc()
        ob.fill_loc_grid()

        # values that occur in the 2d grid
        for vid, v in enumerate(a.reshape(-1)):
            if v == 20:
                continue
            result = ob.start_search(v)
            self.assertEqual(result, solutions[vid])

        # values that do not occur should lead to None
        for v in [14,18,19,30]:
            result = ob.start_search(v)
            self.assertIsNone(result)
    
    def small_matrix(self):
        a = self.arr_list[2]

        enc_locations = ['1101100 110001', #l1
                         '1101100 110010', #l2
                         '1101100 110011', #l3
                         '1101100 110100'] #l4
        enc_codes = ["110011"]

        solutions = [
            "1101110 110010"]
        
        ob = IntelDevice(2,2, enc_locations, enc_codes, 0)
        ob.fill_coordinate_to_loc()
        ob.fill_loc_grid()

        for vid, v in enumerate(a.reshape(-1)):
            if v == 20:
                continue
            result = ob.start_search(v)
            self.assertEqual(result, solutions[vid])

    def print_encoder(self):

        enc_loc = [
            "1101110 110010",
            "1101110 110011",
            "1101110 110100",
            "1101110 110101",
            "1101110 110110",
            "1101110 110111",
            "1101110 111000",
            "1101110 111001",
            "1101110 111010",
            "1101110 111011",
            "1101110 110011 110010",
            "1101110 110011 110011"
        ]

        enc_code = [
            "110011",
            "110011 110010",
            "110101 110010",
            "110111 110011",
            "110011 111000",
            "110100 110010",
            "110110 110100",
            "110111 110100",
            "110101 110100",
            "110110 111001",
            "110111 111001",
            "111010 110010",
        ]

        
        solutions = [
            "1101110 110010",
            "1101110 110011",
            "1101110 110100",
            "1101110 110101",
            "1101110 110110",
            "1101110 110111",
            "1101110 111000",
            "1101110 111001",
            "1101110 111010",
            "1101110 111011",
            "1101110 110011 110010",
            "1101110 110011 110011"
        ]
        ob = IntelDevice(5,5, enc_loc, enc_code, 0)

        for string in enc_loc:
            translation = ob.decode_message(string)
            print(f"{string} means {translation} a location")

        for string in enc_code:
            translation = ob.decode_message(string)
            print(f"{string} means {translation} a code")

        for string in solutions:
            translation = ob.decode_message(string)
            print(f"{string} means {translation} a solution")  
        
        davidstring = []
        for string in ["l1", "l2", "l3", "l4"]:
            msg = ob.encode_message(string)
            davidstring.append(msg)




# Printing things, by running this file:
if __name__ == '__main__':
    t = TestIntelDevice()
    t.print_encoder()
    # t.create_arrays()
    t.create_arrays()
    # t.private_test1()
    t.private_test2()