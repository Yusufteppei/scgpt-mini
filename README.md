## DATA DOWNLOAD

```bash
mkdir -p data
cd data


wget https://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_10k_v3/pbmc_10k_v3_filtered_feature_bc_matrix.tar.gz

tar -xzf pbmc_10k_v3_filtered_feature_bc_matrix.tar.gz

```

## GENERATE VOCABULARY

```python
python generators.py
```

##
