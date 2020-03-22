from voice_input import query_user
from voice_output import process_voice_output
#from dbConnector import insertIntoDB

class Brain():
    def __init__(self):
        self.user_name = ""
        self.user_address = {"address":"","town":"","name":""}
        self.info = ""
        self.request_type = ""
        self.content = {}


    def find_answers(self):
        process_voice_output("Guten Tag. Ich bin Maria Theresa, ihr freundlicher Helfer. Wie ist ihr Name?")
        user_phrase = query_user()
        self.user_name = user_phrase.split()[-1]
        process_voice_output("Hallo {}. Wie kann ich Ihnen helfen? Bitte sage einkaufen, wenn ich für dich einkaufen"
                             " gehen soll, soziale Interaktion wenn Sie sich mit jemandem unterhalten wollen, Hilfe im"
                             " Haushalt, Gassi gehen oder Botengang Post . Bitte sagen Sie Sonstiges, falls Sie bei"
                             " etwas anderem Hilfe benötigen.".format(self.user_name))
        user_phrase = query_user()
        process_voice_output(user_phrase)
        self.decide_activity(user_phrase)
        self.content = {"name":self.user_name, "address":self.user_address, "info":self.info, "type":self.request_type}
       
        print(self.content)
       # insertIntoDB(self.content)

    def decide_activity(self, user_phrase):
        if "sozial" in user_phrase or "interaktion" in user_phrase:
            self.ask_sozile_interaktion()
            self.request_type = "Soziale Interaktion"
        elif "sonstiges" in user_phrase:
            self.ask_sonstiges()
            self.request_type = "Sonstiges"
        elif "kaufe" in user_phrase:
            self.ask_einkaufen()
            self.request_type = "Einkaufen"
        elif "gassi" in user_phrase or "hund" in user_phrase:
            self.ask_gassi()
            self.request_type = "Gassi Gehen"
        elif "post" in user_phrase:
            self.ask_post()
            self.request_type = "Post"
        elif "hilfe" in user_phrase or "haushalt" in user_phrase:
            self.ask_haushalt()
            self.request_type = "Haushalt Hilfe"
        else:
            print(user_phrase)
            process_voice_output("Das habe ich nicht verstanden. Können sie das wiederholen?")
            user_phrase = query_user()
            process_voice_output(user_phrase)
            self.decide_activity(user_phrase)


    def ask_sozile_interaktion(self):
        process_voice_output("Alles klar, Sie möchten mit jemandem sprechen. Welche Themen interessieren Sie?"
                             " zum Beispiel Politik oder Reisen?")
        user_phrase = query_user()
        self.info = user_phrase
        process_voice_output("{}. Super, einer unserer Helfer ruft Sie unter dieser Nummer an um sich mit Ihnen zu dem"
                             " Thema {} zu unterhalten. Bis dann!".format(user_phrase, user_phrase))

        return


    def ask_sonstiges(self):
        process_voice_output("Bitte sagen Sie uns, wobei wir ihnen helfen können.")
        user_phrase = query_user()
        self.info = user_phrase
        process_voice_output("Wir werden prüfen, ob wir ihnen beim Thema {} helfen können."
                             " Wir rufen Sie zurück.".format(user_phrase))
        return


    def ask_einkaufen(self):
        process_voice_output("Alles klar, einer unserer Helfer geht gerne für Sie einkaufen. Welche Sachen benötigen Sie?"
                             " Bitte nennen Sie Ihre Einkaufsliste jeweils mit Menge und Produkt, zum Beispiel 1 Ztrone.")
        self.hilfe_supermarkt()
        return


    def hilfe_supermarkt(self):
        user_phrase = query_user()
        self.info = user_phrase
        process_voice_output("{}, stimmt das so?".format(user_phrase))
        user_phrase = query_user()
        if "ja" in user_phrase:
            process_voice_output("Sehr gut, wir werden diese Sachen für Sie einkaufen. "
                                 "Dafür müssen wir nun nur noch wissen, wohin wir sie liefern sollen.")
            self.get_address()
        else:
            process_voice_output("Was sollen wir für sie einkaufen?")
            self.hilfe_supermarkt()
        return


    def get_address(self):
        process_voice_output("In Welcher Stadt Wohnen sie?")
        town = query_user()
        process_voice_output("Können Sie uns bitte noch Ihre Straße und Hausnummer nennen?")
        address = query_user()
        process_voice_output("Super, nun müssen wir nur noch wissen, wo wir klingeln sollen."
                             " Welcher Name steht am Klingelschild?")
        name = query_user()
        process_voice_output("{} in {}, liefern an {}. Stimmt das so?".format(address, town, name))
        user_phrase = query_user()
        if "ja" in user_phrase:
            process_voice_output("Perfekt, nun haben wir alle Infos. Wir werden Sie vorher unter dieser Nummer anrufen,"
                                 " falls es noch Fragen gibt. Bis dann, auf Wiederhören {}!".format(self.user_name))
            self.user_address["address"]=address
            self.user_address["town"]=town
            self.user_address["name"]=name

            #self.user_address = "{}, {}, {}".format(address, town, name)
        else:
            self.get_address()
        return


    def ask_gassi(self):
        process_voice_output("Alles klar, wir gehen gerne mit ihrem Hund eine Runde Gassi. "
                             "Wo können wir ihren Hund abholen?")
        self.get_address()
        return


    def ask_haushalt(self):
        process_voice_output("Okay, Sie benötigen also Hilfe im Haushalt.")
        self.ask_what_help()
        return


    def ask_what_help(self):
        process_voice_output(" Geht es um Putzdienst, Kochen, Reparatur oder sonstiges?")
        user_phrase = query_user()
        self.info = user_phrase
        process_voice_output("Sie brauchen Hilfe mit {}, stimmt das so?".format(user_phrase))
        user_phrase = query_user()
        if "ja" in user_phrase:
            process_voice_output("Einer unserer Helfer kommt bei Ihnen vorbei, um Ihnen zu helfen.")
            self.get_address()
        else:
            self.ask_what_help()
        return


    def ask_post(self):
        process_voice_output("Alles klar, wir bringen gerne ihre Unterlagen an den Ort zur nächsten Annahmestelle."
                             " Welche Versandart wählen Sie?")
        self.info = query_user()
        self.get_address()
        return
