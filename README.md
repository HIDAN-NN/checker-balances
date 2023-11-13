# Checker balances

---

## Modules:
#### 1. Checker Balances Web3
#### 2. Checker Balances DeBank (Coming soon)

---

### 1. Checker Balances Web3
   Looks at the balance of native and tokens in any evm network.

   #### Module settings
   1. Addresses are added to the `data/addresses.txt`file. 
   Each address is on a new line, without any symbols.

   2. Module settings are done in the `apps/checker_balances_web3/config.py` file,  the description is there.

---

### 2. Checker Balances DeBank (Coming soon)
   ...
   #### Module settings:
   ...

--- 

### Run:

#### Create and Activate virtual environment
On Windows
```shell
python -m venv venv
.\venv\Scripts\activate
```
On macOS/Linux
```shell
python3 -m venv venv
source venv/bin/activate
```

#### Installing Packages
```shell
pip install --requirement requirements.txt
```


#### Run

```shell
python3 main.py
```

---