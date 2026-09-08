#Crowdfunding / Amal Transparan Sistem donasi dengan aliran dana yang dapat dilacak 100%

from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_block({
    "donate_id": "DONATE-001",
    "Nominal": "Rp. 32000000",
    "actor": "Hamba_Allah",
    "location": "Aceh"
})

blockchain.add_block({
    "donate_id": "BATCH-001",
    "Nominal": "Rp. 800000",
    "actor": "Pengelola_donasi",
    "location": "Cirebon"
})

blockchain.add_block({
    "donate_id": "BATCH-001",
    "Nominal": "Rp. 1000000",
    "actor": "Penerima_donasi",
    "location": "Cirebon"
})

blockchain.add_block({
    "donate_id": "BATCH-002",
    "Nominal": "Rp. 5000000",
    "actor": "Pemberi_donasi",
    "location": "Cirebon"
})

for block in blockchain.chain:
    print("=" * 50)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())