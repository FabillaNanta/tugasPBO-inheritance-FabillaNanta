class mamalia_laut:
    def __init__(self, phylum, kingdom, family, genus, habitat, characteristics):
        self.phylum          = phylum
        self.kingdom         = kingdom
        self.family          = family
        self.genus           = genus
        self.habitat         = habitat
        self.characteristics = characteristics
 
    def printname (self):
        print(self.phylum)
        print(self.kingdom)
        print(self.family)
        print(self.genus)
        print(self.habitat)
        print(self.characteristics)

class Toothed_Whale(mamalia_laut):
    def __init__(self, phylum, kingdom, family, genus, habitat, characteristics):
        mamalia_laut.__init__(self, phylum, kingdom, family, genus, habitat, characteristics)
        self.spesies = "Orcinus orca (Killer Whale)"
    
    def characteristics_toothed(self):
        print("Species         = Orca (Orcinus orca)")
        print("Phylum          = Chordate")
        print("Kingdom         = Animalia")
        print("Family          = Delphinidae")
        print("Genus           = Orcinus")
        print("Habitat         = World ocean")
        print("Characteristics = Known for their long dorsal fins and their black and white coloring")

class Baleen_Whale(mamalia_laut):
    def __init__(self, phylum, kingdom, family, genus, habitat, characteristics):
        mamalia_laut.__init__(self, phylum, kingdom, family, genus, habitat, characteristics)
        self.spesies = "Megaptera novaeangliae (Humpback Whale)"

    def characteristics_baleen(self):
        print("Species         = Humpback Whale (Megaptera novaeangliae)")
        print("Phylum          = Chordate")
        print("Kingdom         = Animalia")
        print("Family          = Rorquals")
        print("Genus           = Megaptera")
        print("Habitat         = Open ocean")
        print("Characteristics = Mainly black or grey with white undersides to their flukes, flippers, and bellies. They are also known for their magical songs, such as the sequence of moans, howls, cries, and other quite complex and often continue for hours")
        
data1 = Toothed_Whale("chordate", "animalia", "Delphinidae", "Orcinus", "world ocean", "Known for their long dorsal fins and their black and white coloring")
data2 = Baleen_Whale("chordate", "animalia", "Rorquals", "Megaptera", "open ocean", "Mainly black or grey with white undersides to their flukes, flippers, and bellies. They are also known for their magical songs, such as the sequence of moans, howls, cries, and other quite complex and often continue for hours")

data1.characteristics_toothed()
print("====================================================================================")
data2.characteristics_baleen()
