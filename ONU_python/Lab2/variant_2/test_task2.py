from labwork_2_3 import silv
import numpy as np


def test_silv():
    result = silv(np.array([[1, -0.5], [-0.5, 2]]))
    assert result is True
    result = silv(np.array([[-4, 0, 0], [0, -2, 0], [0, 0, -1]]))
    assert result is False
    result = silv(np.array([[22, -9, 7], [-9, 22, -19], [7, -19, 17]]))
    assert result is True
