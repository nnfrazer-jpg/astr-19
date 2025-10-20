class axolotl:
    
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        
        # These are the axolotl's characteristics
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    # This function lists the characteristics of an axolotl
    def describe(self):
        print("Axolotl Characteristics:")
        print(f"Arm length: {self.arm_length} inches")
        print(f"Leg length: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has tail: {self.has_tail}")
        print(f"Furry: {self.is_furry}")

# Main function that describes an axolotl
def main():
    my_axolotl = axolotl(1.5, 1.5, 2, True, False)
    my_axolotl.describe()

if __name__ == "__main__":
    main()