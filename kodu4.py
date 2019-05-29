# Nagu eelmise nädala kodutöö
kuupaev=input('Sisesta kuupäev: ').split('.')
def kuupäev_sõnena(päev,kuu,aasta):
    if kuu == '01' or kuu =='1':
        return päev+".jaanuar."+aasta
    elif kuu == '02' or kuu =='2':
        return päev+".veebruar."+aasta
    elif kuu == '03' or kuu == '3':
        return päev+".märts."+aasta
    elif kuu == '04' or kuu=='4':
        return päev+".aprill."+aasta
    elif kuu == '05' or kuu=='5':
        return päev+".mai."+aasta
    elif kuu == '06' or kuu=='6':
        return päev+".juuni."+aasta
    elif kuu == '07' or kuu=='7':
        return päev+".juuli."+aasta
    elif kuu == '08' or kuu=='8':
        return päev+".august."+aasta
    elif kuu == '09' or kuu=='9':
        return päev+".september."+aasta
    elif kuu == '10':
        return päev+".oktoober."+aasta
    elif kuu == '11':
        return päev+".november."+aasta
    elif kuu == '12':
        return päev+".detsember."+aasta
print(kuupäev_sõnena(kuupaev[0],kuupaev[1],kuupaev[2]))
