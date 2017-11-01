# Created by Jenny Trac
# Created on Nov 1 2017
# Program rounds number when given number of decimal places

import ui

def round_number(number_to_round, number_of_decimals):
    # rounds numbers to number of decimal places wanted
    
    # process
    number_step1 = number_to_round * (10 ** number_of_decimals) + 0.5
    number_step2 = int(number_step1)
    number_step3 = float(number_step2) / (10 ** number_of_decimals)
    
    # output
    view['answer_label'].text = "Rounded number is: " + str(number_step3)

def round_touch_up_inside(sender):
    # button to round number
    
    #input
    number_input = float(view['number_input_textfield'].text)
    decimal_input = int(view['decimal_input_textfield'].text)
    
    # process
    round_number(number_input, decimal_input)

view = ui.load_view()
view.present('sheet')


















