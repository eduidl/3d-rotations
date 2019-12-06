# 3D Rotations
- 金谷著「3次元回転―パラメータ計算とリー代数による最適化―」 の実装
- https://www.kyoritsu-pub.co.jp/bookdetail/9784320113824

## Requirements
- Python 3.7
- Pipenv

## Data

### Requirements
- wget
- p7zip-full

### `isotropic_error.ipynb`, `anisotropic_error.ipynb`

```terminal
# http://graphics.stanford.edu/data/3Dscanrep/
$ wget http://graphics.stanford.edu/pub/3Dscanrep/bunny.tar.gz
$ tar xavf bunny.tar.gz
```

### `fundamental_matrix.ipynb`

```terminal
# https://www.eth3d.net/datasets#low-res-many-view
$ wget https://www.eth3d.net/data/delivery_area_rig_undistorted.7z
$ 7z x *.7z
```

## Run

```terminal
pipenv sync
pipenv shell
jupyter nbextension enable --py widgetsnbextension
jupyter notebook
```

## 構成

|ファイル名|内容|書籍との対応
|----------|----|------------
|[notebooks/isotropic\_error.ipynb](https://github.com/eduidl/3d-rotations/blob/master/notebooks/isotropic_error.ipynb)|等方性誤差を持つデータからの回転推定|第4章
|[notebooks/anisotropic\_error.ipynb](https://github.com/eduidl/3d-rotations/blob/master/notebooks/anisotropic_error.ipynb)|異方性誤差を持つデータからの回転推定|第5章＋6.6節
|[notebooks/fundamental\_matrix.ipynb](https://github.com/eduidl/3d-rotations/blob/master/notebooks/fundamental_matrix.ipynb)|基礎行列の推定|6.7節
