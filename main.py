from block import Block
from pow import proof_of_work
from pos import proof_of_stake

print("PROOF OF WORK (POW)")

for difficulty in [2, 3, 4, 5]:

    block = Block(
        index=1,
        data="Donasi dari Hamba_Allah",
        previous_hash="0"
    )

    print("\n==============================")
    print("Difficulty :", difficulty)

    proof_of_work(block, difficulty)

    print("Nonce      :", block.nonce)
    print("Waktu      : sudah ditampilkan di atas")
    print("Hash       :", block.hash)


print("\nPROOF OF STAKE (POS)")

validators = {
    "Donatur_1": 10,
    "Platform_Admin": 20,
    "Auditor_External": 30,
    "Beneficiary": 40
}

print("\nValidator:")
for validator, stake in validators.items():
    print(f"{validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)