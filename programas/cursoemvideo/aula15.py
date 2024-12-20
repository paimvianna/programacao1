#entrada
km=float(input('informe quantos km foram rodados: '))
dias=int(input('informe quantos dias foram alugados: '))
vldiarias=dias*60
vlquilometragem=km*0.15
vlrtotal=vldiarias+vlquilometragem
print(f'O valor total do aluguel é {vlrtotal} já o valor das diarias {vldiarias}')