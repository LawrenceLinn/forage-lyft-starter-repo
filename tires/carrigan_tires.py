from .tires import Tires
import numpy as np


class CarriganTires(Tires):
    def __init__(self, worn: np.array) -> None:
        super().__init__(worn)

    def need_service(self, worn: np.array) -> bool:
        return (worn >= 0.9).any()
