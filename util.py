import math
from pathlib import Path

import numpy as np  # type: ignore
import open3d  # type: ignore
from scipy import linalg  # type: ignore
from scipy.spatial.transform import Rotation  # type: ignore


def load_point_cloud(path: Path) -> np.ndarray:
    assert path.is_absolute() and path.exists()
    ply = open3d.io.read_point_cloud(str(path))
    return np.asarray(ply.points)


def eval_R_error(estimated_R: np.ndarray, ideal_R: np.ndarray) -> np.float_:
    error_rot = Rotation.from_matrix(estimated_R @ ideal_R.T)
    return linalg.norm(error_rot.as_rotvec())


def estimate_R_using_SVD(A: np.ndarray, A_prime: np.ndarray) -> np.ndarray:
    assert A.shape[1] == A_prime.shape[1] == 3
    N = A.T @ A_prime  # correlation matrix
    U, s, Vh = linalg.svd(N)
    V = Vh.T
    return V @ np.diag([1, 1, linalg.det(V @ U)]) @ U.T


def skew_matrix(v: np.ndarray) -> np.ndarray:
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])  # yapf: disable


def exponential_map(omega: np.ndarray) -> np.ndarray:
    assert omega.shape == (3,)
    t = linalg.norm(omega)
    A_omega = skew_matrix(omega / t)
    return np.eye(3) + math.sin(t) * A_omega + (1 - math.cos(t)) * A_omega @ A_omega
