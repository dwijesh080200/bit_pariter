# Detection erreur
## pair1.py
- cloner le projet, pour ce faire, faites

`git clone https://github.com/dwijesh080200/bit_pariter.git`

en cas ou python3 n'est pas installer, faites 

`sudo apt-get install python3`

- on lance pair.py. pour ce faire, faites

`python3 pair1.py`

- le programme va vous demander d'inserez un string ou un mot
- inserez le mot
- le programme va allors convertir le mot en bytearray
- puis il converti en binaire en retirant le "0b" qui appairait quand on fait
   - `bytearray(...)`
- il va calculer le nombre de 1 qui se trouve dans le binaire
- si il y plus de 1 que de zero il va ajouter un zero pour le faire devenir en un binaire pair
- sinon il va ajouter un 1 et vice-versa dependant sur le binaire obtenu

## impair1.py
- on lance impair.py. pour ce faire, faites

`python3 impair1.py`

- le programme va vous demander d'inserez un string ou un mot
- inserez le mot
- le programme va allors convertir le mot en bytearray
- puis il converti en binaire en retirant le "0b" qui appairait quand on fait
   - `bytearray(...)`
- il va calculer le nombre de 1 qui se trouve dans le binaire
- si il y plus de 1 que de zero il va ajouter un zero pour le faire devenir en un binaire impair
- sinon il va ajouter un 1 et vice-versa dependant sur le binaire obtenu

## checksum.py
- on lance checksum.py. pour ce faire, faites

`python3 checksum.py`

- le programme va vous demander d'inserez un string ou un mot
- inserez le mot
- le programme va alors calculer le checksum1 et checksum2 du mot que vous avez mit
- il vous donnera le code ascii des lettres un par un du mot, par exemple
  - mot = network
  - n : 78 
  - e : 101
  - t : 116
  - w : 119
  - o : 111
  - r : 114
  - k : 107
  
- apres il va calculer les checksum
- pour calculer le checksum en generale il est assez similaire au façon de calculer le cumulative frequency en math 
mais dans ce cas precis avec les chiffre de ascii code
- le checksum permet de voir si il y eu d'erreur dans le transfer de packet.


