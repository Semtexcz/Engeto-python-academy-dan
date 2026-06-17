def rozdel_podle_znaku(adresa, znak="@"):  # Uzavírající rámec
    rozdeleny_mail = adresa.split(znak)
    # print("Globální rámec uvnitř první funkce", globals())
    print("Lokální rámec uvnitř první funkce", locals())
    
    def oddel_domenu(nedomena, znak="."):  # Lokální rámec
        print("Lokální rámec uvnitř druhé funkce", locals())
        return nedomena[1].split(znak)[0]
    
    return oddel_domenu(rozdeleny_mail)
    
print(rozdel_podle_znaku("matous@holinka.cz"))
print("Lokální rámec vně všech funkcí", locals()) # tohle se rovná globals()