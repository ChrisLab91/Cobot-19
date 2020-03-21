from voice_input import query_user
from voice_output import process_voice_output


def find_answers():
    process_voice_output("Guten Tag. Ich bin Maria Theresa, ihr freundlicher Helfer. Wie ist ihr Name?")
    user_phrase = query_user()
    user_name = user_phrase.split()[-1]
    process_voice_output("Hallo {}. Wie kann ich Ihnen helfen? Bitte sage einkaufen, wenn ich für dich einkaufen gehen"
                         " soll, soziale Interaktion wenn Sie sich mit jemandem unterhalten wollen, Hilfe im Haushalt, "
                         "Gassi gehen oder Botengang Post . Bitte sagen Sie Sonstiges, falls Sie bei etwas anderem"
                         " Hilfe benötigen.".format(user_name))
    user_phrase = query_user()
    process_voice_output(user_phrase)
    decide_activity(user_phrase)


def decide_activity(user_phrase):
    if "sozial" in user_phrase or "interaktion" in user_phrase:
        ask_sozile_interaktion()
    elif "sonstiges" in user_phrase:
        ask_sonstiges()
    elif "kaufe" in user_phrase:
        ask_einkaufen()
    elif "gassi" in user_phrase or "hund" in user_phrase:
        ask_gassi()
    elif "post" in user_phrase:
        ask_post()
    elif "hilfe" in user_phrase or "haushalt" in user_phrase:
        ask_haushalt()
    else:
        print(user_phrase)
        process_voice_output("Das habe ich nicht verstanden. Können sie das wiederholen?")
        user_phrase = query_user()
        process_voice_output(user_phrase)
        decide_activity(user_phrase)


def ask_sozile_interaktion():
    process_voice_output("Alles klar, Sie möchten mit jemandem sprechen. Welche Themen interessieren Sie?"
                         " zum Beispiel Politik oder Reisen?")
    user_phrase = query_user()
    process_voice_output("{}. Super, einer unserer Helfer ruft Sie unter dieser Nummer an um sich mit Ihnen zu dem"
                         " Thema {} zu unterhalten. Bis dann!".format(user_phrase, user_phrase))

    return


def ask_sonstiges():
    process_voice_output("Bitte sagen Sie uns, wobei wir ihnen helfen können.")
    user_phrase = query_user()
    process_voice_output("Wir werden prüfen, ob wir ihnen beim Thema {} helfen können."
                         " Wir rufen Sie zurück.".format(user_phrase))
    return


def ask_einkaufen():
    process_voice_output("Alles klar, einer unserer Helfer geht gerne für Sie einkaufen. Welche Sachen benötigen Sie?"
                         " Bitte nennen Sie Ihre Einkaufsliste jeweils mit Menge und Produkt, zum Beispiel 1 Ztrone.")
    hilfe_supermarkt()
    return


def hilfe_supermarkt():
    user_phrase = query_user()
    process_voice_output("{}, stimmt das so?".format(user_phrase))
    user_phrase = query_user()
    if "ja" in user_phrase:
        process_voice_output("Sehr gut, wir werden diese Sachen für Sie einkaufen. "
                             "Dafür müssen wir nun nur noch wissen, wohin wir sie liefern sollen.")
        get_address()
    else:
        process_voice_output("Was sollen wir für sie einkaufen?")
        hilfe_supermarkt()
    return


def get_address():
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
                             " falls es noch Fragen gibt. Bis dann, auf Wiederhören!")
    else:
        get_address()
    return


def ask_gassi():
    process_voice_output("Alles klar, wir gehen gerne mit ihrem Hund eine Runde Gassi. "
                         "Wo können wir ihren Hund abholen?")
    get_address()
    return


def ask_haushalt():
    process_voice_output("Okay, Sie benötigen also Hilfe im Haushalt.")
    ask_what_help()
    return


def ask_what_help():
    process_voice_output(" Geht es um Putzdienst, Kochen, Reparatur oder sonstiges?")
    user_phrase = query_user()
    process_voice_output("Sie brauchen Hilfe mit {}, stimmt das so?".format(user_phrase))
    user_phrase = query_user()
    if "ja" in user_phrase:
        process_voice_output("Einer unserer Helfer kommt bei Ihnen vorbei, um Ihnen zu helfen.")
        get_address()
    else:
        ask_what_help()
    return


def ask_post():
    process_voice_output("Alles klar, wir bringen gerne ihre Unterlagen an den Ort zur nächsten Annahmestelle."
                         " Welche Versandart wählen Sie?")
    query_user()
    get_address()
    return
