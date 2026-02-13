# Single quote et double quote - identiques
message1 = 'Bonjour'
message2 = "Bonjour"
print(message1 == message2)  # True

# Utilité: inclure des quotes dans la string
citation1 = "Il a dit: 'C'est génial!'"
citation2 = 'Elle a répondu: "Merci!"'
print(citation1)
print(citation2)

# Échapper les quotes si nécessaire
echappement = 'Il a dit: \'Bonjour\''
print(echappement)  # Il a dit: 'Bonjour'
