import random
OFF_Section= [
    "Cancha",
    "Cancha VIP",
    "Galeria",
    "Andes",
    "Pacifico Bajo",
    "Pacifico Medio",
    "Pacifico Alto",
    "Pacifico Lateral",
    "Silla de Ruedas"
]

random.seed(42)
tickets= random.choices(OFF_Section, k=1000)
counts= []
sections= []
tickets.sort(key=str.lower)

for ticket in tickets:
    if ticket not in sections:
        sections.append(ticket)
        counts.append(1)
    else:
        idx= sections.index(ticket)
        counts[idx] += 1

bestplace= max(counts)
idx_bestplace= counts.index(bestplace)

print("----------------Occupied tickets at the Dua Lipa concert----------------")
for i in range(len(sections)):
    print("-" + str(sections[i]) + ": " + str(counts[i]))
print(f"**The most popular section in the concert was {sections[idx_bestplace]} with {bestplace} tickets out of 1000")
