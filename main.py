import random
import math
import time
import threading

team_name = input("Please enter your team name: ")
fish_repo_rate = 100
fish_in_lake = 0


def addFish():
    global fish_in_lake
    threading.Timer(10.0, addFish).start()  # called every minute
    fish_in_lake += fish_repo_rate

addFish()


class fishBanks:
    def __init__(self, teamName):
        self.teamName = teamName
        self.balance = 500
        self.shipLevel = 1
        self.boost_ship_lv = 1
        self.waitTime = 8
        self.pricePerFish = 6.25
        self.pricePerShip = 18.75
        self.revenue = 100 - (self.pricePerFish + self.pricePerShip)
        self.shipUpgradeCost = 50
        self.maxShipsSent = 5
        self.fishCaptureAmount = 75
        self.fish_repo_rate = fish_repo_rate
        self.fleet_num = 1
        self.netWorth = 0

    def send_ships(self):
        global fish_in_lake
        fish_in_lake -= self.fishCaptureAmount

        if fish_in_lake <= 0:
            print("All fish have been captured, please wait for more.")
            return

        if self.balance < 0:
            print("Note: You are now in debt by " + "$", str(self.balance))

        if self.maxShipsSent > self.fleet_num:
            self.revenue *= self.fleet_num

        elif self.maxShipsSent < self.fleet_num:
            self.revenue *= self.maxShipsSent

        print("You have $", str(self.balance), "in your account")
        print("sending max amount of level", self.shipLevel, "ships(s)...")  # sends ships
        time.sleep(self.waitTime)  # wait time depending on the level of ship
        self.balance += self.revenue  # paycheck
        print("$", str(self.balance), "In your account. You made " + str(self.revenue) + "\n")

        tip_chance = random.randint(1, 2)  # helpful tips
        if tip_chance == 2 and self.shipLevel == 1:
            print("Tired of waiting? upgrade your ships buy typing 'boost tech'")

    def buy_ships(self):
        quantity = int(input("Enter how many level " + str(self.shipLevel) + " ship(s) to buy: "))
        print("The total cost for your " + str(quantity) + " level" + str(self.shipLevel) + " ship(s) is " +
              str(self.shipUpgradeCost * quantity))

        confirm = input("Are you sure you want to continue? (y/n): ")
        if confirm == "y".lower():
            self.balance -= self.shipUpgradeCost * quantity
            self.fleet_num += quantity
            print("Sucessfully purchased: " + str(quantity) + " level" + str(self.shipLevel) + " ship(s)")
        else:
            return

    def sell_ships(self):
        quantity = int(input("Enter how many ships to sell: "))
        returned_cash = quantity * math.floor(self.shipUpgradeCost / 2) - self.balance
        print("+", str(returned_cash) + " added to your account")
        print("Your bank balance is $" + str(self.balance + returned_cash))

    def boost_tech(self):
        self.shipLevel += 1
        if self.shipLevel == 1:
            self.waitTime = 8
            self.pricePerFish = 6.25
            self.pricePerShip = 18.75
            self.revenue = 100 - (self.pricePerFish + self.pricePerShip)
            self.shipUpgradeCost = 50
            self.maxShipsSent = 5
            self.fishCaptureAmount = 75
            self.fish_repo_rate = 500
            self.netWorth = self.balance + (self.pricePerShip * self.fleet_num)

        if self.shipLevel == 2:
            self.waitTime = 5
            self.pricePerFish = 12.5
            self.pricePerShip = 37.5
            self.revenue = 200 - (self.pricePerFish + self.pricePerShip)
            self.shipUpgradeCost = 325
            self.maxShipsSent = 15
            self.fishCaptureAmount = 100
            self.fish_repo_rate = 600
            self.netWorth = self.balance + (self.pricePerShip * self.fleet_num)

        if self.shipLevel == 3:
            self.waitTime = 4
            self.pricePerFish = 25
            self.pricePerShip = 150
            self.revenue = 300 - (self.pricePerFish + self.pricePerShip)
            self.shipUpgradeCost = 550
            self.maxShipsSent = 25
            self.fishCaptureAmount = 150
            self.fish_repo_rate = 700
            self.netWorth = self.balance + (self.pricePerShip * self.fleet_num)

        if self.shipLevel == 4:
            self.waitTime = 3
            self.pricePerFish = 31.25
            self.pricePerShip = 93.75
            self.revenue = 400 - (self.pricePerFish + self.pricePerShip)
            self.shipUpgradeCost = 775
            self.maxShipsSent = 35
            self.fishCaptureAmount = 200
            self.fish_repo_rate = 800
            self.netWorth = self.balance + (self.pricePerShip * self.fleet_num)

        if self.shipLevel == 5:
            self.waitTime = 2
            self.pricePerFish = 37.5
            self.pricePerShip = 112.5
            self.revenue = 500 - (self.pricePerFish + self.pricePerShip)
            self.shipUpgradeCost = 1000
            self.maxShipsSent = 45
            self.fishCaptureAmount = 250
            self.fish_repo_rate = 1000
            self.netWorth = self.balance + (self.pricePerShip * self.fleet_num)

        if self.balance - self.pricePerShip < 0:
            print("Unable to proceed with your request. you need ")
            self.shipLevel -= 1
            return

        else:

            print("Ships boosted to level " + str(self.shipLevel), "$" + str(self.shipUpgradeCost) +
                  " deducted from your account, your balance is $", str(self.balance - self.shipUpgradeCost))
            self.balance -= self.shipUpgradeCost

            print("Fish reproduction is now at " + str(self.fish_repo_rate + 100), "fish every 10s.")


t1 = fishBanks(team_name)

while True:
    print()
    usr_in = input("- ")
    if usr_in == "send ships".lower():
        t1.send_ships()

    if usr_in == "buy ships".lower():
        t1.buy_ships()

    if usr_in == "sell ships".lower():
        t1.sell_ships()

    if usr_in == "boost tech".lower():
        t1.boost_tech()

    if usr_in == "balance".lower():
        print(t1.balance)

    if usr_in == "ship num".lower():
        print(t1.fleet_num)

    if usr_in == "".lower():
        print("\n" * 100)

    if usr_in == "fish num".lower():
        print(fish_in_lake)

    if usr_in == "frr".lower():
        print(t1.fish_repo_rate)

    if usr_in == "net worth".lower():
        print(t1.netWorth)
