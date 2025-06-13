from dataclasses import dataclass
from model.artObject import ArtObject

# no hash, eq perchè non andrò a usarlo nel mio model
@dataclass
class Arco:
    o1: ArtObject
    o2: ArtObject
    peso: int