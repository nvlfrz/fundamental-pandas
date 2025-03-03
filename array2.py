import pandas as pd

# contoh array 2 dimensi
data = [
    ['Nauval', 'Laki-Laki', 49],
    ['Kirana', 'Perempuan', 23],
    ['Aulia', 'Perempuan', 56],
    ['Rizki', 'Laki-Laki', 33]
]

# membuat DataFrame
df = pd.DataFrame(data, columns=['Nama', 'JK', 'Umur'])

# print
print(df)
