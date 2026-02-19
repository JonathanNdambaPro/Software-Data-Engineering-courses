# Exercice : Validation d'inscription utilisateur avec Pydantic
# Créez un système de validation d'inscription en utilisant Pydantic.
#
# 1. Créez un modèle Pydantic `UserRegistration` avec :
#    - username (str) : minimum 3 caractères, maximum 20 caractères, alphanumérique uniquement
#    - email (str) : doit être un email valide (utilisez EmailStr de Pydantic)
#    - password (str) : minimum 8 caractères
#    - age (int) : doit être entre 13 et 120
#    - newsletter (bool, par défaut False)
#
# 2. Ajoutez un @field_validator pour `password` qui vérifie :
#    - Au moins une lettre majuscule
#    - Au moins un chiffre
#    - Au moins un caractère spécial (!@#$%^&*)
#
# 3. Ajoutez un @field_validator pour `username` qui :
#    - Supprime les espaces en début/fin
#    - Convertit en minuscules
#
# 4. Dans main() :
#    - Créez un utilisateur valide et affichez-le
#    - Essayez de créer un utilisateur avec un mot de passe invalide et capturez l'erreur
#    - Essayez de créer un utilisateur avec un email invalide et capturez l'erreur
#    - Sérialisez l'utilisateur valide en JSON avec model_dump_json()
