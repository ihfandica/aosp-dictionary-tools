import re

def bersihkan_wordlist_cepat(file_input, file_output):
    print("--> Memulai pembersihan cepat pada file wordlist...")

    baris_terproses = 0
    baris_dibuang = 0

    pola_baris = re.compile(
        r"^\s*word=(.*),f=(\d+),flags=(.*?),originalFreq=(\d+)\s*$"
    )

    with (
        open(file_input, "r", encoding="utf-8") as infile,
        open(file_output, "w", encoding="utf-8") as outfile,
    ):
        for line in infile:
            if line.startswith("dictionary="):
                outfile.write(line)
                continue

            match = pola_baris.match(line)
            if match:
                kata = match.group(1).strip()
                freq = match.group(2)
                flags = match.group(3)
                orig_freq = match.group(4)

                kata = kata.rstrip(",")

                if "," in kata or len(kata) > 45 or not kata:
                    baris_dibuang += 1
                    continue

                outfile.write(
                    f" word={kata},f={freq},flags={flags},originalFreq={orig_freq}\n"
                )
                baris_terproses += 1
            else:
                baris_dibuang += 1

    print("--> \nProses pembersihan selesai!")
    print(f"--> Total baris valid disimpan : {baris_terproses}")
    print(f"--> Total baris cacat dibuang  : {baris_dibuang}")

if __name__ == "__main__":
    FILE_ASLI = "id_wordlist.combined"
    FILE_BERSIH = "id_wordlist_clean.combined"

    bersihkan_wordlist_cepat(FILE_ASLI, FILE_BERSIH)
