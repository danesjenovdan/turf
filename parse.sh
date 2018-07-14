SCRAPY_BIN=/home/user/.virtualenvs/turf/bin/scrapy
SCRIPT_PATH=/home/user/turf/rtvslo.py
COMMENTS_FOLDER=/home/user/turf/comments
LOG_FOLDER=/home/user/turf/log

$SCRAPY_BIN runspider $SCRIPT_PATH -o $COMMENTS_FOLDER/rtvslo_$(date -d "today" +"%Y%m%d%H%M").json --loglevel=ERROR >> $LOG_FOLDER/turfer.log