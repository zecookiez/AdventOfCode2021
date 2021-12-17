input = open("inputs/day16.txt", "r").read().strip()
message = "".join(bin(c)[2:].zfill(8) for c in bytes.fromhex(input))

class Packet:
    def __init__(self, ver, ID, val, sub):
        self.ver = ver
        self.ID = ID
        self.val = val
        self.sub = sub
    def calculate(self):
        if self.ID == 0:
            return sum(sub.calculate() for sub in self.sub)
        if self.ID == 1:
            prod = 1
            for sub in self.sub:
                prod *= sub.calculate()
            return prod
        if self.ID == 2:
            return min(sub.calculate() for sub in self.sub)
        if self.ID == 3:
            return max(sub.calculate() for sub in self.sub)
        if self.ID == 4:
            return self.val
        assert len(self.sub) == 2
        if self.ID == 5:
            return [0, 1][self.sub[0].calculate() > self.sub[1].calculate()]
        if self.ID == 6:
            return [0, 1][self.sub[0].calculate() < self.sub[1].calculate()]
        if self.ID == 7:
            return [0, 1][self.sub[0].calculate() == self.sub[1].calculate()]
        assert False

def read(msg, amount, conv = True):
    return int(msg[:amount], 2) if conv else msg[:amount], msg[amount:]

# Recursively walk through the subpackets

part_1 = []
def walk(msg):
    version, msg = read(msg, 3)
    part_1.append(version)
    ID, msg = read(msg, 3)
    # Literal
    if ID == 4:
        val = []
        while True:
            v, msg = read(msg, 5, False)
            val.append(v[1:])
            if v[0] == "0":
                break
        val = int("".join(val), 2)
        return Packet(version, ID, val, []), msg
    I, msg = read(msg, 1)
    packets = []
    if I == 0:
        # Type 0 length
        L, msg = read(msg, 15)
        old_sz = len(msg)
        while old_sz - len(msg) < L:
            packet, msg = walk(msg)
            packets.append(packet)
    else:
        # Type 1 length
        L, msg = read(msg, 11)
        for _ in range(L):
            packet, msg = walk(msg)
            packets.append(packet)
    return Packet(version, ID, 0, packets), msg

packet, _ = walk(message)
print(sum(part_1))
print(packet.calculate())
