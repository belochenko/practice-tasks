from task_3 import silv
import numpy as np



def test_silv():
    result = silv(np.array([[1, -0.5], [-0.5, 2]]))
    assert result == True
    result = silv(np.array([[-4, 0, 0], [0, -2, 0], [0, 0, -1]]))
    assert result == False
    result = silv(np.array([[26, 15, 3], [15, 21, 6], [3, 6, 9]]))
    assert result == True