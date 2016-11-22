#Script to Randomize the System Volume of Mac when you play song.
while :
do
	osascript -e "set Volume $(((RANDOM % 6) + 1))"
	sleep 3s
done
