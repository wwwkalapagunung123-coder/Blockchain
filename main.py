#Crowdfunding / Amal Transparan Sistem donasi dengan aliran dana yang dapat dilacak 100%

from block import Block
from pow import proof_of_work
from pos import proof_of_stake

print("PROOF OF WORK (POW)")

block = Block(
    index=1,
    data="Donasi dari Hamba_Allah",
    previous_hash="0"
)

difficulty = 4

print("\nData Block :", block.data)
print("Difficulty  :", difficulty)

proof_of_work(block, difficulty)

print("Nonce  :", block.nonce)
print("Hash  :", block.hash)

print("PROOF OF STAKE (POS)")

validators = {
    "Donatur_1": 10,            # Pemberi dana (Bisa memferifikasi penerima awal)
    "Platform_Admin": 20,       # pengelola sistem Crowdfunding
    "Auditor_External": 30,     # Pihak independen yang memverifikasi aliran dana
    "Beneficary": 40            # Penerima dana
}

print("\nValidator: ")
for validator, stake in validators.items():
    print(f"{validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih: ", selected)