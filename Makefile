run:
	python3 BitSim.py
clean:
	rm -rf *.pyc
pull:
	git pull origin master
push:
	git push origin master
update: pull push

