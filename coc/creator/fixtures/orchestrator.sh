# Run this script from /path/to/projects/folder/coc

COC_PATH=$(pwd)"/coc/manage.py"
FIXTURES_PATH=$(pwd)"/coc/creator/fixtures"
OCC_SKILL_SCRIPT=$(pwd)"/coc/creator/helpers/scripts/occ_skill_seeder.py"
DATABASE_PATH=$(pwd)"/coc/db.sqlite3"
CREATOR_PATH=$(pwd)"/coc/creator/migrations"
MARKET_PATH=$(pwd)"/coc/market/migrations"

echo "[INFO] Erase sqlite db..."
rm $DATABASE_PATH
echo "[INFO] Create database..."
touch $DATABASE_PATH
echo "[INFO] Flush creator migrations just in case..."
rm -rf $CREATOR_PATH
echo "[INFO] Flush market migrations just in case..."
rm -rf $MARKET_PATH

echo "[INFO] Apply migrations..."
python3 $COC_PATH migrate

echo "[INFO] Creating super user..."
python3 $COC_PATH  createsuperuser --user root --email root@admin.com --noinput
echo "[INFO] Input  password for root user..."
python3 $COC_PATH changepassword root

echo "[INFO] Apply project migrations..."
python3 $COC_PATH makemigrations creator
python3 $COC_PATH migrate

echo "[INFO] Loading core entities..."
python3 $COC_PATH loaddata $FIXTURES_PATH/core/*
echo "[INFO] Loading spells..."
python3 $COC_PATH loaddata $FIXTURES_PATH/spells/*