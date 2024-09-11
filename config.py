import os
# from dotenv import load_dotenv
import streamlit as st

INFURA_PROJECT_ID = st.secrets["general"]["INFURA_PROJECT_ID"]
INFURA_PROJECT_SECRET = st.secrets["general"]["INFURA_PROJECT_SECRET"]
PRIVATE_KEY = st.secrets["general"]["PRIVATE_KEY"]
ACCOUNT_ADDRESS = st.secrets["general"]["ACCOUNT_ADDRESS"]
CONTRACT_ADDRESS = st.secrets["general"]["CONTRACT_ADDRESS"]



# INFURA_PROJECT_ID = INFURA_PROJECT_ID
# INFURA_PROJECT_SECRET = INFURA_PROJECT_SECRET
# PRIVATE_KEY = PRIVATE_KEY
# ACCOUNT_ADDRESS = ACCOUNT_ADDRESS
# CONTRACT_ADDRESS = CONTRACT_ADDRESS

# Load environment variables from .env file
# load_dotenv()

# INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
# INFURA_PROJECT_SECRET = os.getenv("INFURA_PROJECT_SECRET")

# PRIVATE_KEY = os.getenv("PRIVATE_KEY")
# ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")

# CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

CONTRACT_ABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_medicalHistory",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_treatment",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_temperature",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_heartRate",
				"type": "uint256"
			}
		],
		"name": "addPatient",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "medicalHistory",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "treatment",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "temperature",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "heartRate",
				"type": "uint256"
			}
		],
		"name": "PatientAdded",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "getAllPatientIds",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getPatient",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "patientCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "patients",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "medicalHistory",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "treatment",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "temperature",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "heartRate",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]