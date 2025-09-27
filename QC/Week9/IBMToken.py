from qiskit_ibm_runtime import QiskitRuntimeService

QISKIT_TOKEN = 'YF5SkSksvyQNKUTvcjUTxZKupIwL4x6U8V7za0wx5gQM'
# You may need to specify the URL explicitly if your environment is misconfigured
# Run this once!
QiskitRuntimeService.save_account(token=QISKIT_TOKEN, overwrite=True)
print("Account saved successfully in the new environment.")