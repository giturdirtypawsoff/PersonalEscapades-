def monkeys_jumping_on_the_bed(count):
    if count > 1:
        print(f"There were {count} monkeys jumping on the bed, until one fell off and bumped his head.")
        return monkeys_jumping_on_the_bed(count - 1)
    elif count == 1:
        print(f"There were {count} monkeys jumping on the bed, until one fell off and bumped his head.")
        return monkeys_jumping_on_the_bed(count - 1)
    else:
        print("\nAll the monkeys have fallen off the bed and bumped their heads! \n")
        choice = input("Would you like to wake the monkeys up? (yes or no) ")
        def decision_wakeup_decision(decision):
            if decision == "yes" or decision == "y":
                print("\nOh no, they are all dead.")
            else:
                print("\nGood. Fuck them the silly beggars!")
        return monkey_wakeup_decision(choice)

monkeys_jumping_on_the_bed(11)
