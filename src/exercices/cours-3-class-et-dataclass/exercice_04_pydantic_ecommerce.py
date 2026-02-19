# Exercice : Système de commandes e-commerce avec Pydantic
# Créez un système de validation de commandes en utilisant Pydantic.
#
# 1. Créez un enum `OrderStatus` avec : PENDING, CONFIRMED, SHIPPED, DELIVERED, CANCELLED
#
# 2. Créez un modèle Pydantic `Product` avec :
#    - name (str) : non vide
#    - price (float) : doit être > 0, arrondi à 2 décimales via un validator
#    - quantity (int) : doit être >= 1
#
# 3. Créez un modèle Pydantic `Order` avec :
#    - order_id (str)
#    - customer_email (str)
#    - products (list[Product]) : doit contenir au moins 1 produit
#    - status (OrderStatus, par défaut PENDING)
#    - discount_percent (float, par défaut 0) : doit être entre 0 et 50
#
# 4. Ajoutez un @model_validator qui :
#    - Calcule et stocke le `total_price` (somme de price * quantity pour chaque produit)
#    - Applique la réduction au total
#    - Rejette la commande si le total après réduction est inférieur à 1.0
#
# 5. Ajoutez une méthode `cancel()` qui change le statut en CANCELLED uniquement si pas déjà DELIVERED
#
# 6. Dans main() :
#    - Créez une commande valide avec plusieurs produits et affichez-la
#    - Sérialisez en dictionnaire avec model_dump() et affichez
#    - Essayez de créer une commande avec une liste de produits vide et capturez l'erreur
#    - Essayez de créer une commande avec une réduction > 50% et capturez l'erreur
