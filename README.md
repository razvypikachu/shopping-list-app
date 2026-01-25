Manager Lista de Cumparaturi CLI
O aplicatie in linie de comanda pentru gestionarea eficienta a listelor de cumparaturi, calcularea bugetului si organizarea produselor pe categorii.

Autor
Nume: Mutu Razvan Costin Iulian

Grupa: 2.2

Email: razvan-costin-iulian.mutu@student.upt.ro
An academic: 2025-2026

Descriere
Aceasta aplicatie este un CLI care permite utilizatorilor sa creeze si sa gestioneze o lista de cumparaturi stocata intr-un fisier JSON.

Aplicatia rezolva problema organizarii cumparaturilor si a estimarii costurilor inainte de a ajunge la casa. Utilizatorul poate adauga produse cu pret si cantitate, le poate pune pe catgorii si poate vizualiza totalul cheltuielilor.

Tehnologii folosite

Limbaj Python 

Biblioteci:

argparse - Pentru interpretarea argumentelor din linia de comanda si interfata CLI.

json - Pentru salvarea listei.

csv - Pentru exportul datelor.


Tools: Git, GitHub

Cerinte sistem
Interpretor: Python 3.

Sistem de operare: Windows, Linux sau macOS.

Instalare: git clone https://github.com/razvypikachu/shopping-list-app.git
Sintaxa generala

python main.py comanda argumente

Exemple de utilizare:

Exemplul 1: Adaugarea unui produs

$ python main.py add "Lapte" 2 5.5 "Lactate"
Output: Added 2 x Lapte, unit price $5.5 to category 'Lactate', total $11.0

Exemplul 2: Listarea produselor sortate dupa pret
Afisam lista curenta de cumparaturi, ordonata dupa pret.

$ python main.py list --sortby price
Output:
Paine (Brutarie) - 1 x 3.0 = 3.0
Lapte (Lactate) - 2 x 5.5 = 11.0
Carne (Macelarie) - 1 x 25.0 = 25.0

Exemplul 3: Calcularea totalului si a bugetului pe categorii
Afisam costul total al listei si cat costa fiecare categorie in parte.

$ python main.py total
Output:
Total cost of shopping list: 39.0
Category 'Brutarie': 3.0
Category 'Lactate': 11.0
Category 'Macelarie': 25.0
Exemplul 4: Exportarea listei in CSV
Exportam lista curenta

$ python main.py export final_list.csv
Output: Shopping list exported to final_list.csv

Branch-uri: Proiectul are doua branch-uri, asigurati-va ca sunteti pe branch-ul main cand rulati.
