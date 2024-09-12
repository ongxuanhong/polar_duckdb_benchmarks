# Installation
```bash
# setup kaggle
# https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md
# content: {"username":"your_name","key":"your_key"}
$KAGGLE_CONFIG_DIR/kaggle.json

# start download
kaggle competitions download -c leash-BELKA

# uncompress file
unzip leash-BELKA.zip -d leash-BELKA

# install packages
conda create -n polar_duckdb_benchmarks
conda activate polar_duckdb_benchmarks
pip install -r requirements.txt 
```