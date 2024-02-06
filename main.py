import pandas as pd
import math

spreadsheet_id = "1YtiuDuzBsTLFPUnXHUEvHsr2E8CnaGElytNSU56yTK4"
df = pd.read_csv(
    f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv")

col_aluno = list(df['Unnamed: 1'])
col_faltas = list(df['Unnamed: 2'])
col_p1 = list(df['Unnamed: 3'])
col_p2 = list(df['Unnamed: 4'])
col_p3 = list(df['Unnamed: 5'])

col_sit = list(df['Unnamed: 6'][:2])
col_final = list(df['Unnamed: 7'][:2])

quantAulas = 60
for k in range(2, len(col_aluno)):
    if int(col_faltas[k]) > 0.25*quantAulas:
        col_sit.append("Reprovado por Falta")
        col_final.append(0)
        continue
    m = (int(col_p1[k])+int(col_p2[k])+int(col_p3[k]))/3
    if m < 50:
        col_sit.append("Reprovado por Falta")
        col_final.append(0)
        continue
    elif m < 70:
        col_sit.append("Exame Final")
        notaFalta = 100 - m
        notaFalta = math.ceil(notaFalta)
        col_final.append(notaFalta)
    else:
        col_sit.append("Aprovado")
        col_final.append(0)

df['Unnamed: 1'] = pd.DataFrame(col_aluno)
df['Unnamed: 2'] = pd.DataFrame(col_faltas)
df['Unnamed: 3'] = pd.DataFrame(col_p1)
df['Unnamed: 4'] = pd.DataFrame(col_p2)
df['Unnamed: 5'] = pd.DataFrame(col_p3)
df['Unnamed: 6'] = pd.DataFrame(col_sit)
df['Unnamed: 7'] = pd.DataFrame(col_final)

df.to_csv(
    f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv", sep=";", index=False)
print(df)
