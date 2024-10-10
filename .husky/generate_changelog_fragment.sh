#!/bin/bash

# Lire le message du commit
COMMIT_MSG=$(git log -1 --pretty=%B)

# Extraire le type et la description du commit (ex: feat: nouvelle feature)
TYPE=$(echo "$COMMIT_MSG" | cut -d: -f1)
DESCRIPTION=$(echo "$COMMIT_MSG" | cut -d: -f2 | xargs)

# Générer un nom unique pour le fragment
FRAGMENT_NAME=$(date +"%Y%m%d%H%M%S")

# Déterminer le type du commit pour Towncrier (feature, bugfix, etc.)
case $TYPE in
    feat)
        FRAGMENT_TYPE="feature"
        ;;
    fix)
        FRAGMENT_TYPE="bugfix"
        ;;
    docs)
        FRAGMENT_TYPE="doc"
        ;;
    style)
        FRAGMENT_TYPE="style"
        ;;
    refactor)
        FRAGMENT_TYPE="refactor"
        ;;
    perf)
        FRAGMENT_TYPE="performance"
        ;;
    test)
        FRAGMENT_TYPE="test"
        ;;
    chore)
        FRAGMENT_TYPE="chore"
        ;;
    *)
        FRAGMENT_TYPE="misc"
        ;;
esac

# Créer le fichier de fragment dans changelog.d
FRAGMENT_FILE="changelog.d/${FRAGMENT_NAME}.${FRAGMENT_TYPE}"

# Écrire la description du commit dans le fichier de fragment
echo "$DESCRIPTION" > "$FRAGMENT_FILE"

echo "Fragment créé: $FRAGMENT_FILE"