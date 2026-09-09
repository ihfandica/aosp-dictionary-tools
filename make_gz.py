import gzip
import shutil

def kompres_file_ke_gz(file_input, file_output_gz):
    print(f"--> Memulai kompresi file {file_input}...")
    with open(file_input, 'rb') as f_in:
        with gzip.open(file_output_gz, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"--> Kompresi berhasil! File tersimpan di: {file_output_gz}")

FILE_COMBINED = 'id_wordlist_clean.combined'
FILE_GZ = 'id_wordlist.combined.gz'

if __name__ == '__main__':
    kompres_file_ke_gz(FILE_COMBINED, FILE_GZ)
