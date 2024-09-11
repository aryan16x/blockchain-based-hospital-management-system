from web3 import Web3
import random
from config import INFURA_PROJECT_ID, PRIVATE_KEY, ACCOUNT_ADDRESS, CONTRACT_ADDRESS, CONTRACT_ABI

# Connect to Infura
infura_url = f"https://sepolia.infura.io/v3/{INFURA_PROJECT_ID}"
web3 = Web3(Web3.HTTPProvider(infura_url))

if not web3.is_connected():
    raise Exception("Failed to connect to Infura")

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def simulate_sensor_data():
    """Simulate IoT sensor data for temperature and heart rate."""
    temperature = random.uniform(36.0, 38.0)  # Random temperature in Celsius
    heart_rate = random.randint(60, 100)  # Random heart rate in bpm
    return int(temperature), heart_rate

def add_patient(name, age, medical_history, treatment):
    """Add a patient along with simulated sensor data."""
    # Simulate IoT data
    temperature, heart_rate = simulate_sensor_data()
    nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    tx = contract.functions.addPatient(name, age, medical_history, treatment, temperature, heart_rate).build_transaction({
        'chainId': 11155111,  # Chain ID for Sepolia
        'gas': 1000000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce
    })

    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return web3.to_hex(tx_hash)

def get_patient(patient_id):
    """Retrieve patient details including sensor data."""
    try:
        return contract.functions.getPatient(patient_id).call()
    except Exception as e:
        print(f"Error retrieving patient: {e}")
        return None

def get_all_patient_ids():
    """Retrieve all patient IDs."""
    try:
        return contract.functions.getAllPatientIds().call()
    except Exception as e:
        print(f"Error retrieving patient IDs: {e}")
        return []
