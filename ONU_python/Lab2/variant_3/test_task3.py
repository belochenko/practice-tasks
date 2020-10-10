from labwork_3_3 import silverster
import numpy as np



def test_silv():
    result = silverster(np.array([[1, -0.5], [-0.5, 2]]))
    assert result is True
    result = silverster(np.array([[-4, 0, 0], [0, -2, 0], [0, 0, -1]]))
    assert result is False
    result = silverster(np.array([[14, 6, 3], [6, 9, -4], [3, -4, 9]]))
    assert result is True
