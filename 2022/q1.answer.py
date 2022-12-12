class Q1:
    input_filename = "q1.input"
    elves = []

    def debug(self):
        i = 0 
        for elf in self.elves:
            print(f"{i}: {elf}")
            i+=1

    def parse_input(self):
        input_file = open(self.input_filename, 'r')
        for line in input_file.read().splitlines():
            if len(self.elves) == 0 or line == "":
                self.elves.append(0)
            else:
                self.elves[-1] += int(line)

    def top_three_elf(self):
        self.elves.sort()
        top_three = self.elves[-3:]
        return sum(top_three)

    def largest_elf(self):
        return max(self.elves)

    def main(self):
        # Map content to each elf
        self.parse_input()
        # self.debug()
        # Finding elf with most content
        print(self.largest_elf())
        print(self.top_three_elf())
        # Find value of content

q1 = Q1()
q1.main()