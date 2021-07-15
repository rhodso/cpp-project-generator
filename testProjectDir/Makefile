testProjectDir : obj/main.o
	g++ -o testProjectDir obj.main.o

obj/main.o : 
	g++ -c src/main.cpp -I headers -o obj/main.o

clean: 
	rm -rfv obj
	mkdir obj
	rm -f testProjectDir

run: testProjectDir
	./testProjectDir
