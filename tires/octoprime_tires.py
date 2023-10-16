from .tires import Tires
import numpy as np


class OctoprimeTires(Tires):
    def __init__(self, worn: np.array) -> None:
        super().__init__(worn)

    def need_service(self, worn: np.array) -> bool:
        return worn.sum() >= 3
