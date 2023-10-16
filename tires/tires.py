from abc import ABC, abstractmethod
import numpy as np


class Tires(ABC):
    def __init__(self, worn: np.array) -> None:
        self.worn = worn
        assert len(worn) == 4, "Tires must have four elements"
        assert (worn >= 0).all(), "Tire wear cannot be negative"
        assert (worn <= 1).all(), "Tire wear cannot be greater than 1"

    def need_service(self, worn) -> bool:
        pass
