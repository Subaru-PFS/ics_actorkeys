# Description: Test load  all actorkeys dictionaries in the actorkeys directory 
for f in $(cd $ICS_ACTORKEYS_DIR/python/actorkeys; echo [a-z]*.py | xargs -n1 -I % basename % .py); do 
    echo "####### $f"; 
    loadDictionary.py -l $f
done
