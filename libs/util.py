import math
from pathlib import Path

import numpy as np  # type: ignore
import open3d  # type: ignore
import plotly.graph_objects as go  # type: ignore
from scipy.spatial.transform import Rotation  # type: ignore


def load_point_cloud() -> np.ndarray:
    path = Path("../bunny/data/bun180.ply").resolve()
    assert path.exists()
    ply = open3d.io.read_point_cloud(str(path))
    return np.asarray(ply.points).T


def plot_3d(points: np.ndarray) -> None:
    assert len(points.shape) == 2
    assert points.shape[0] == 3
    fig = go.Figure()
    fig.add_trace(
        go.Scatter3d(x=points[0],
                     y=points[1],
                     z=points[2],
                     mode='markers',
                     marker=dict(size=1, color=points[2], colorscale='Viridis', opacity=0.5)))
    fig.show()


def plot_3d_multi(*points_arr: np.ndarray) -> None:
    for points in points_arr:
        assert len(points.shape) == 2
        assert points.shape[0] == 3
    fig = go.Figure()
    for i, points in enumerate(points_arr):
        fig.add_trace(
            go.Scatter3d(
                x=points[0],
                y=points[1],
                z=points[2],
                mode='markers',
                marker=dict(size=1, opacity=0.5),
                name=str(i + 1),
            ))
    fig.show()


def eval_R_error(estimated_R: np.ndarray, ideal_R: np.ndarray) -> np.float_:
    error_rot = Rotation.from_dcm(estimated_R @ ideal_R.T)
    return np.linalg.norm(error_rot.as_rotvec())


def estimate_R_using_SVD(A: np.ndarray, A_prime: np.ndarray) -> np.ndarray:
    N = A @ A_prime.T  # correlation matrix
    U, S, VT = np.linalg.svd(N)
    V = VT.T
    return V @ np.diag([1, 1, np.linalg.det(V @ U)]) @ U.T


def skew_matrix(v: np.ndarray) -> np.ndarray:
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])


def exponential_map(omega: np.ndarray) -> np.ndarray:
    assert omega.shape == (3,)
    t = np.linalg.norm(omega)
    A_omega = skew_matrix(omega / t)
    return np.eye(3) + math.sin(t) * A_omega + (1 - math.cos(t)) * A_omega @ A_omega
