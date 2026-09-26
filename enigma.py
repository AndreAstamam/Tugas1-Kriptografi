ROTORS = {
    'I':   ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    'II':  ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    'III': ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
}
REFLECTORS = {
    'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT",
}

A = ord('A')

class Rotor:
    def __init__(self, name, ring, pos):
        self.wiring, self.notch = ROTORS[name]
        self.ring = ord(ring) - A
        self.pos = ord(pos) - A

    def step(self):
        self.pos = (self.pos + 1) % 26

    def at_notch(self):
        return chr(self.pos + A) == self.notch

    def forward(self, c):
        shift = self.pos - self.ring
        idx = (c + shift) % 26
        out = ord(self.wiring[idx]) - A
        return (out - shift) % 26

    def backward(self, c):
        shift = self.pos - self.ring
        idx = (c + shift) % 26
        out = self.wiring.index(chr(idx + A))
        return (out - shift) % 26

class Plugboard:
    def __init__(self, pairs):
        self.map = {i: i for i in range(26)}
        for pair in pairs:
            a, b = pair.split('-')
            a, b = ord(a) - A, ord(b) - A
            self.map[a], self.map[b] = b, a

    def swap(self, c):
        return self.map[c]

class Enigma:
    def __init__(self, rotor_names, rings, positions, plug_pairs, reflector='B'):
        self.rotors = [Rotor(rotor_names[i], rings[i], positions[i]) for i in range(3)]
        self.reflector = REFLECTORS[reflector]
        self.plugboard = Plugboard(plug_pairs)

    def step_rotors(self):
        right, middle, left = self.rotors
        step_middle = middle.at_notch()
        step_left = step_middle
        if right.at_notch():
            step_middle = True
        right.step()
        if step_middle: middle.step()
        if step_left: left.step()

    def encrypt_char(self, ch):
        self.step_rotors()
        c = self.plugboard.swap(ord(ch) - A)
        for r in self.rotors: c = r.forward(c)
        c = ord(self.reflector[c]) - A
        for r in reversed(self.rotors): c = r.backward(c)
        return chr(self.plugboard.swap(c) + A)

    def process(self, text):
        return "".join(self.encrypt_char(c) for c in text if c.isalpha())


e = Enigma(['II', 'I', 'III'], ['G', 'P', 'Q'], ['K', 'Y', 'S'], ['A-P', 'T-V', 'F-B'])
print(e.process("RWSSKPFJHLGKERLWZMSPOFIZIUJODSQPTAYRYFPRYN"))
