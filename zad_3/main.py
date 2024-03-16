from classes import House, Flat


def main():
    house = House(150,
                  5,
                  500000,
                  "Małomiasteczkowa",
                  500)
    flat = Flat(80,
                3,
                350000,
                "Wielkomiasteczkowa",
                2)

    print(house)
    print()
    print(flat)


if __name__ == "__main__":
    main()
