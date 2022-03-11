import math

# deloppgave 1

#%% 
B = 50000
k = 0.2

# Ta utgangspunkt i formelen for populasjonsvekst fra Oblig 1 Bruk samme verdier for B og k, 
# men velg en verdi for C slik at populasjonen (N) ved t=0 er lik 12.

def populasjonsvekst(t, C):
    return B / (1+ C * math.exp(-k*t))

round(populasjonsvekst(0, 4150)) #N = 12 når t = 0 og C = 4150 (rundet)


#%% Lag en løkke som beregner populasjonen for hver time i intervallet [0, 60]. Lagre verdiene for t og N i hver sin liste.
N = []
t = []
for i in range(0,60):
    N.append(round(populasjonsvekst(i, 4150)))
    t.append(i)
    
    
#%% Lag en ny løkke som skriver ut time (t) og populasjons (N) verdiene i en tabell
print('t[h]  N')
print('---------')
for redbull, kaffe in zip(t, N):
    print(redbull,'   ', kaffe)
    

#%% deloppgave 2
# Skriv kode som genererer en gangetabell

for rad in range(1, 11):
    for kolonne in range(1, 11):
        print(rad*kolonne, end="\t")
    print()
