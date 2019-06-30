#!/usr/bin/env zsh

# Run this script from /path/to/projects/folder/coc

COC_PATH=$(pwd)"/coc/manage.py"
FIXTURES_PATH=$(pwd)"/coc/creator/fixtures"
HELPERS_PATH=$(pwd)"/coc/creator/helpers/scripts/occ_skill_seeder.py"

echo "Loading core entities..."
python3 $COC_PATH loaddata $FIXTURES_PATH/core/*
echo "Loading items..."
python3 $COC_PATH loaddata $FIXTURES_PATH/items/*
echo "Loading spells..."
python3 $COC_PATH loaddata $FIXTURES_PATH/spells/*
echo "Generating Occupation Skill fixtures..."
python3 $HELPERS_PATH 
echo "Loading OccupationSkills..."
python3 $COC_PATH loaddata $FIXTURES_PATH/occupation_skills/*
