######## A practice #########

## read in csv file and return coresponding SQL INSERT statements
## bugs maybe there is a need to trim an entry with quotes around
file_name=$1

IFS=','
while read playlist_name track_name artist_name album ISRC
do
	cat >> "sql_result.txt" << EOF
	INSERT INTO playlists 	(playlist_name, track_name, artist_name, album, ISRC) 
	VALUES 
	("$playlist_name", "$track_name", "$artist_name", "$album", "$ISRC");

EOF
done < "${file_name:-songs.csv}" 


