#!/usr/bin/env python3
# Created by: Spencer Scarlett
# Created on: Sept 28, 2022
# A program to calculate pizza costs with taxes
import constants


def main():
    # requests diameter of the pizza in inches
    diameter = int(input("What is the diameter of the pizza? (inches): "))

    # calculates the cost of making the pizza
    subtotal = constants.LABOUR + constants.RENTAL + constants.SUPPLYS * diameter

    # calculates taxes of the pizza
    taxes = subtotal * constants.HST

    # calculates the TOTAL cost
    total = subtotal + taxes

    # end results, displayed to the user
    print("The total cost is: ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
