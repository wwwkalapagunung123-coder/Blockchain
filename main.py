from block import Block
from pow import proof_of_work
from pos import proof_of_stake

print("PROOF OF WORK (POW)")

for difficulty in [2, 3, 4, 5]:

    block = Block(
        index=1,
        data={"donatur": "Hamba_Allah", "jumlah": 100000},
        previous_hash="0"
    )

    print("\n==============================")
    print("Difficulty :", difficulty)

    waktu = proof_of_work(block, difficulty)

    print("Nonce      :", block.nonce)
    print("Waktu      :", waktu, "detik")
    print("Hash       :", block.hash)


print("\nPROOF OF STAKE (POS)")

validators = {
    "Donatur_1": 70,
    "Platform_Admin": 10,
    "Auditor_External": 10,
    "Beneficiary": 10
}

print("\nValidator:")
for validator, stake in validators.items():
    print(f"{validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)