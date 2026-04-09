# KNN Laptop Price Prediction Model - Documentation

## Overview
Standard K-Nearest Neighbors (KNN) implementation for laptop price prediction with complete training pipeline, evaluation metrics, and two inference functions for different use cases.

---

## Model Performance

**Best K Value:** 7 (selected via grid search with validation set)

### Evaluation Metrics

| Metric | Training | Validation | Test |
|--------|----------|-----------|------|
| **MSE** | 2,085.58 | 105,751.10 | 100,771.93 |
| **RMSE** | $45.67 | $325.19 | $317.45 |
| **MAE** | $9.21 | $215.21 | $206.32 |
| **R² Score** | 0.9959 | 0.7933 | 0.7965 |

### Model Selection Process
- Tested k values: [3, 5, 7, 9, 11, 15, 21]
- **Best k=7** selected based on validation MSE
- Distance-weighted neighbors (better accuracy than uniform weights)
- Euclidean distance metric

---

## Implementation Structure

### 1. Training Pipeline
Located in `notebook/eda/knn.ipynb` (Cell 1)

**Steps:**
1. Load preprocessed and encoded training/validation/test data
2. Standardize features using StandardScaler
3. Grid search for optimal k value
4. Train final KNN model
5. Evaluate on all three sets
6. Save model and scaler for inference

**Key Parameters:**
- n_neighbors: 7 (configurable)
- weights: 'distance' (distance-weighted)
- metric: 'euclidean'

---

### 2. Features Used
**Numeric Features (8):**
- CPU Mark
- GPU Mark
- Monitor (screen size)
- Width (resolution)
- Height (resolution)
- RAM (GB)
- Storage Amount (GB)
- Weight (kg)

**Categorical Features (13, one-hot encoded):**
- **Brands:** Acer, Apple, Asus, Dell, HP, LG, Lenovo, MSI, Microsoft, Other
- **OS:** Windows 10, Windows 11, Other (includes MacOS, Chrome OS, etc.)

**Target Variable:**
- Price (in USD)

---

## Inference Functions

### Function 1: `infer_price_from_encoded_data()`
**Purpose:** Predict price from already processed and encoded data (dataset format)

**Input:** 
- `encoded_data` (pd.DataFrame): Single row with all 21 encoded features

**Output:** 
- `price` (float): Predicted price

**Usage:**
```python
# Use with test data
sample = test_df_encoded.drop('Price', axis=1).iloc[0:1]
predicted_price = infer_price_from_encoded_data(sample)
print(f"Predicted: ${predicted_price:.2f}")
```

**Example Result:**
- Actual: $1,599.00
- Predicted: $1,632.33
- Error: 2.1%

---

### Function 2: `infer_price_from_raw_input()`
**Purpose:** Predict price from raw human input without preprocessing knowledge required

**Input:** 
- `laptop_spec` (LaptopRawInput): Pydantic BaseModel with raw laptop specifications

**Output:** 
- `dict` containing:
  - `predicted_price`: Final prediction
  - `specification`: Input parameters
  - `processed_features`: Processed feature values
  - `cpu_mark`: CPU performance score
  - `gpu_mark`: GPU performance score

**LaptopRawInput Model:**
```python
class LaptopRawInput(BaseModel):
    os: str              # e.g., "Windows 11", "MacOS"
    brand: str           # e.g., "HP", "Dell", "Apple"
    cpu: str             # e.g., "AMD Ryzen 5 5050U"
    gpu: str             # e.g., "AMD Radeon Graphics"
    monitor: float       # e.g., 15.6
    resolution: str      # e.g., "1920x1080"
    ram: str             # e.g., "16GB", "1TB"
    storage: str         # e.g., "512GB", "1TB"
    weight: float        # e.g., 1.8
```

**Usage Example:**
```python
from pydantic import BaseModel

test_laptop = LaptopRawInput(
    os="Windows 11",
    brand="HP",
    cpu="AMD Ryzen 5 5050U",
    gpu="AMD Radeon Graphics",
    monitor=15.6,
    resolution="1920x1080",
    ram="16GB",
    storage="512GB",
    weight=1.8
)

result = infer_price_from_raw_input(test_laptop)
print(f"Predicted Price: ${result['predicted_price']:.2f}")
```

**Output:**
```
Predicted Price: $605.52
```

---

## TODO: CPU/GPU Mark Mapping Function

**Function:** `get_cpu_gpu_marks(cpu_name: str, gpu_name: str) -> tuple`

**Currently:** Returns placeholder values (CPU=10000.0, GPU=500.0)

**Implementation Guide:**
You need to implement this function to map CPU/GPU names to their actual performance scores.

**Reference Files:**
- CPU marks: `data/raw/cpu_gpu_mark/cpu_mark.csv`
- GPU marks: `data/raw/cpu_gpu_mark/gpu_mark.csv`

**Suggested Implementation Approach:**
1. Load CPU/GPU mark CSVs
2. Use fuzzy string matching (fuzzywuzzy library)
3. Find closest match in lookup tables
4. Return corresponding CPU/GPU rank scores

**Example Reference:**
See `notebook/modeling/map_cpu_gpu.py` for existing fuzzy matching implementation:
```python
from fuzzywuzzy import fuzz

def get_cpu_name(cpu):
    acc, pos = mapping(cpu, cpu_name_list)
    return cpu_df['CPU Name'][pos], cpu_df['CPU Rank'][pos]

def get_gpu_name(gpu):
    acc, pos = mapping(gpu, gpu_name_list)
    return gpu_df['GPU Name'][pos], gpu_df['GPU Rank'][pos]
```

**Once Implemented:**
Replace function body with actual implementation using the matching functions above.

---

## Model Files

**Saved Artifacts:**
- `knn_model.pkl` - Trained KNN model
- `knn_scaler.pkl` - StandardScaler fitted on training features

**Loading Models:**
```python
import joblib

model = joblib.load('knn_model.pkl')
scaler = joblib.load('knn_scaler.pkl')
```

---

## Preprocessing Pipeline

### Data Encoding
All categorical features are one-hot encoded. The expected 21 features are:
```
['CPU Mark', 'GPU Mark', 'Monitor', 'Width', 'Height', 'RAM', 'Storage Amount', 'Weight',
 'Brand_Acer', 'Brand_Apple', 'Brand_Asus', 'Brand_Dell', 'Brand_HP', 'Brand_LG', 
 'Brand_Lenovo', 'Brand_MSI', 'Brand_Microsoft', 'Brand_Other', 
 'OS_Other', 'OS_Windows 10', 'OS_Windows 11']
```

### Scaling
Features are standardized using StandardScaler:
- Mean = 0
- Standard Deviation = 1
- Fitted on training data only

### Brand Mapping (for raw input)
```python
{"apple": "Brand_Apple", "hp": "Brand_HP", "dell": "Brand_Dell", 
 "acer": "Brand_Acer", "asus": "Brand_Asus", "lenovo": "Brand_Lenovo",
 "msi": "Brand_MSI", "microsoft": "Brand_Microsoft", "lg": "Brand_LG"}
```

### OS Mapping (for raw input)
```python
"windows 11" → OS_Windows 11 = 1
"windows 10" → OS_Windows 10 = 1
other/macos/chrome os → OS_Other = 1
```

### RAM/Storage Parsing
- GB/TB suffix handling: "16GB" → 16.0, "1TB" → 1024.0
- Stored as numeric values in GB

### Resolution Parsing
- Format: "1920x1080" → Width=1920, Height=1080
- Split by 'x' and convert to integers

---

## Notes

1. **Placeholders:** The `get_cpu_gpu_marks()` function currently returns placeholder values. Implement this to use actual CPU/GPU performance scores from your databases.

2. **Training Data:** 
   - 6,851 samples in training set
   - 762 samples in validation set
   - 846 samples in test set

3. **Model Behavior:**
   - Works best with laptops similar to training data features
   - May overfit on training data (R²=0.9959 vs Test R²=0.7965)
   - Good generalization on test set (R²=0.7965)

4. **Feature Importance:**
   - CPU/GPU marks have highest impact
   - Monitor size, RAM important secondary features
   - Brand and OS add categorical context

---

## Contact / Future Improvements

- [ ] Implement `get_cpu_gpu_marks()` with actual CPU/GPU databases
- [ ] Consider feature engineering for CPU/GPU name parsing
- [ ] Test with more diverse raw input examples
- [ ] Consider ensemble methods (KNN + other models)
- [ ] Add confidence intervals to predictions
- [ ] Optimize k value with cross-validation
