import re
import argostranslate.package
import argostranslate.translate


def siapkan_model_bahasa():
    print("--> Memeriksa dan mengunduh paket bahasa (Inggris -> Indonesia)...")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()

    package_to_install = next(
        filter(
            lambda x: x.from_code == "en" and x.to_code == "id",
            available_packages,
        ),
        None,
    )

    if package_to_install:
        download_path = package_to_install.download()
        argostranslate.package.install_from_path(download_path)
        print("--> Paket bahasa berhasil dipasang!\n")
    else:
        print("--> Paket bahasa tidak ditemukan atau sudah terpasang.")


def terjemahkan_wordlist_offline(file_input, file_output):
    print("--> Memulai proses penerjemahan offline...")

    with open(file_input, "r", encoding="utf-8") as infile, open(
        file_output, "w", encoding="utf-8"
    ) as outfile:
        jumlah_kata = 0
        for line in infile:
            match = re.search(r"( word=)([^,]+)(,.*)", line)

            if match:
                prefix = match.group(1)
                kata_inggris = match.group(2)
                suffix = match.group(3)

                kata_indo = argostranslate.translate.translate(
                    kata_inggris, "en", "id"
                )

                outfile.write(f"{prefix}{kata_indo}{suffix}\n")

                jumlah_kata += 1
                if jumlah_kata % 100 == 0:
                    print(
                        f"--> Berhasil menerjemahkan {jumlah_kata} kata...",
                        end="\r",
                    )
            else:
                outfile.write(line)

    print(
        f"\n--> Selesai! Total {jumlah_kata} kata berhasil diterjemahkan ke: {file_output}"
    )


siapkan_model_bahasa()

FILE_ASLI = "id_wordlist.combined"
FILE_HASIL = "id_wordlist_translated_offline.combined"

terjemahkan_wordlist_offline(FILE_ASLI, FILE_HASIL)