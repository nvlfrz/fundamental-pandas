import pandas as pd

# contoh array multiple dimensi
data = [
    ['Nauval', 'Laki-Laki', 49, 'Medan', 'Manusia', 'Indonesia'],
    ['Kirana', 'Perempuan', 23, 'Jakarta', 'Manusia', 'Indonesia'],
    ['Aulia', 'Perempuan', 56, 'Bandung', 'Manusia', 'Indonesia'],
    ['Rizki', 'Laki-Laki', 33, 'Surabaya', 'Manusia', 'Indonesia']
]

# membuat DataFrame
df = pd.DataFrame(data, columns=['Nama', 'JK', 'Umur', 'Kota', 'Status', 'Negara'])

# print
print(df)
