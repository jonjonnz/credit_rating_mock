# Mortgage Risk Scoring System

## Overview
This project calculates the credit rating for a set of mortgages based on various financial and property attributes. The calculation follows a structured algorithm that considers loan-to-value ratio, debt-to-income ratio, credit score, loan type, and property type.

---

## Requirements
- **Python Version:** 3.12  
- **Input Data:** A JSON file named `input.json` must be present in the same directory as `main.py`.  
- **Sample Data Structure:**  

```json
{
  "mortgages": [
    {
      "credit_score": 750,
      "loan_amount": 200000,
      "property_value": 250000,
      "annual_income": 60000,
      "debt_amount": 20000,
      "loan_type": "fixed",
      "property_type": "single_family"
    },
    {
      "credit_score": 680,
      "loan_amount": 150000,
      "property_value": 175000,
      "annual_income": 45000,
      "debt_amount": 10000,
      "loan_type": "adjustable",
      "property_type": "condo"
    }
  ]
}
```

---

## Credit Rating Algorithm
The credit rating is calculated based on the following criteria:

### 1. **Loan-to-Value (LTV) Ratio**
LTV = (Loan Amount) ÷ (Property Value)  
- **LTV > 90%** → Add **2 points** to the risk score  
- **LTV > 80%** → Add **1 point** to the risk score  

---

### 2. **Debt-to-Income (DTI) Ratio**
DTI = (Debt Amount) ÷ (Annual Income)  
- **DTI > 50%** → Add **2 points** to the risk score  
- **DTI > 40%** → Add **1 point** to the risk score  

---

### 3. **Credit Score**
- **Credit Score ≥ 700** → Subtract **1 point** from the risk score  
- **Credit Score ≥ 650 and < 700** → No change  
- **Credit Score < 650** → Add **1 point** to the risk score  

---

### 4. **Loan Type**
- **Fixed-rate loan** → Subtract **1 point** from the risk score  
- **Adjustable-rate loan** → Add **1 point** to the risk score  

---

### 5. **Property Type**
- **Single-family home** → No change  
- **Condo** → Add **1 point** to the risk score  

---

### 6. **Average Credit Score Adjustment**
- **Average Credit Score ≥ 700** → Subtract **1 point** from the final risk score  
- **Average Credit Score < 650** → Add **1 point** to the final risk score  

---

### 7. **Final Credit Rating**
| Total Risk Score | Credit Rating | Description |
|-----------------|---------------|-------------|
| ≤ 2             | AAA           | Highly secure |
| 3 to 5          | BBB           | Medium risk |
| > 5             | C             | Highly speculative or distressed |

---
    
## How to Run
1. Ensure Python 3.12 is installed.  
2. Place the `input.json` file in the same directory as `main.py`.  
3. Execute the following command:  
```bash
python main.py
```

---

## Output
- The program will display the calculated credit rating in the console.  
- Example Output:
```
Final Credit Rating: AAA
```

---

## Author
- **Jagjit Singh Ramgarhia**  
- **jsr7045@gmail.com**  

---
