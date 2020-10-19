for i in $(seq 100); do 
	name_floders=$(printf "DDM%d" $i)
	name=$(printf "time_till_now" $i)
	mkdir $name_floders
	cd $name_floders
	touch ${name}.txt; 
	echo -e 'nanoseconds since 1970-01-01 00:00:00 UTC:\n<'`date "+%s%N"`'>' > ${name}.txt
	cd ..
done

