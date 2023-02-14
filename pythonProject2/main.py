import sqlite3
with sqlite3.connect("contss.db") as connection:
    cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contacts(id_contact NUMERIC NOT NULL , prenom_nom TEXT NOT NULL, numerotel NUMERIC NOT NULL,adresse TEXT,email TEXT)")

class Gestioncontact:

    def __int__(self):
        print("GESTION DE CONTACT")


    def ajouter_contact(self):
        print("Ajouter un contact")
        prenom_nom = input("ajouter votre nom complet:")
        numerotel = input("ajouter vos numeros que vous souhaitez!: ")
        email = input("ajouter vos emails que vous souhaitez!: ")
        adresse = input("ajouter vos adresse que vous souhaitez!: ")
        cursor.execute("INSERT INTO contacts (prenom_nom, numerotel, email, adresse) VALUES (?,?,?,?)",(prenom_nom,numerotel,email,adresse,))
        connection.commit()
        print(" contact ajouter avec succes!")

    def modifier_contact(self):
        print("Modifier un contact")
        id_contact = input("ID de la contact que Voulez-vous modifier ?:")
        prenom_nom = input("Voulez-vous modifier le nom complet!:\n ")
        numerotel  = input("Voulez-vous modifier le numero telephone!: \n")
        cursor.execute("UPDATE contacts SET prenom_nom = ?,numerotel = ? WHERE id_contact = ?",(int(id_contact),(prenom_nom),int(numerotel)))
        connection.commit()
        print(f"contact avec id {id_contact} est modifier")

    def supprimer_contact(self):
        print("supprimer un contact")
        id_contact = input("ID de la contact que vous souhaitez supprimer !")
        cursor.execute("DELETE FROM contacts WHERE id_contact = ?", (int(id_contact),))
        connection.commit()
        print(f"contacts avec id {id_contact} supprimer")

    def affiche_tous_les_contacts(self):
        print("afficher tous les contacts")
        contacts = cursor.execute("SELECT* FROM contacts").fetchall()
        for contacts in contacts:
          print("contacts:", contacts)

    def rechercher_contact(self):
        print("Rechercher un contact")
        numerotel = input("numerotel que vous souhaitez rechercher !:")
        contacts = cursor.execute("SELECT* FROM contacts WHERE numerotel = ?",(int(numerotel),)).fetchone()
        for contacts in contacts:
            print("contacts:", contacts)


    def menu_principale(self):
        choix =""
        print("-------------------------------------")
        print("---------GESTION DE CONTACT----------")
        print("      1. Ajouter un contact")
        print("      2. Modifier un contact")
        print("      3. Supprimer un contact")
        print("      4. Afficher un contact")
        print("      5. Rechercher un contact")
        print("      0. Quitter l'application")
        print("-------------------------------------")
        choix = input("Entrez votre choix\n")
        if choix == "1":
            self.ajouter_contact()
            self.menu_principale()
        elif choix == "2":
            self.modifier_contact()
            self.menu_principale()
        elif choix == "3":
            self.supprimer_contact()
            self.menu_principale()
        elif choix == "4":
            self.affiche_tous_les_contacts()
            self.menu_principale()
        elif choix =="5":
            self.rechercher_contact()
            self.menu_principale()
        elif choix =="0":
            print("Quitter l'application")
            exit()
        else:
            print("choix non correct")
            exit()

app = Gestioncontact()
app.menu_principale()
