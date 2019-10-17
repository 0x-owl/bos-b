#!/usr/bin/env zsh

# Run this script from /path/to/projects/folder/coc

COC_PATH=$(pwd)"/manage.py"
FIXTURES_PATH=$(pwd)"/creator/fixtures"
OCC_SKILL_SCRIPT=$(pwd)"/creator/helpers/scripts/occ_skill_seeder.py"
DATABASE_PATH=$(pwd)"/db.sqlite3"
CREATOR_MIGRATIONS_PATH=$(pwd)"/creator/migrations"
MARKET_MIGRATIONS_PATH=$(pwd)"/market/migrations"
echo $CREATOR_MIGRATIONS_PATH
echo $MARKET_MIGRATIONS_PATH

# echo "[INFO] Flush creator migrations just in case..."
# ls $CREATOR_MIGRATIONS_PATH/*
# ls $MARKET_MIGRATIONS_PATH

echo "[INFO] Erase sqlite db..."
rm $DATABASE_PATH
echo "[INFO] Create database..."
touch $DATABASE_PATH

echo "[INFO] Apply migrations..."
python3 $COC_PATH migrate

echo "[INFO] Creating super user..."
python3 $COC_PATH  createsuperuser --user root --email root@admin.com --noinput
echo "[INFO] Input  password for root user..."
python3 $COC_PATH changepassword root

echo "[INFO] Apply project migrations..."
python3 $COC_PATH makemigrations creator market
python3 $COC_PATH migrate

echo "[INFO] Loading core entities..."
python3 $COC_PATH loaddata $FIXTURES_PATH/core/*
echo "[INFO] Loading items..."
python3 $COC_PATH loaddata $FIXTURES_PATH/items/*
echo "[INFO] Loading spells..."
python3 $COC_PATH loaddata $FIXTURES_PATH/spells/*
echo "[INFO] Flush remaining Occupation skills fixtures from previous runs..."
rm -rf $FIXTURES_PATH/occupation_skills
echo "[INFO] Create occupation skills folder"
mkdir -p $FIXTURES_PATH/occupation_skills
echo "[INFO] Generating Occupation Skill fixtures..."
python3 $OCC_SKILL_SCRIPT
echo "[INFO] Loading OccupationSkills..."
python3 $COC_PATH loaddata $FIXTURES_PATH/occupation_skills/*
