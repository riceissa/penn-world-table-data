MYSQL_ARGS=
DATABASE=devecondata

.PHONY: all
all: pwt56.sql pwt61.sql pwt62.sql pwt63.sql pwt70.sql pwt71.sql pwt80.sql pwt81.sql pwt90.sql

.PHONY: read
read:
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt56.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt61.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt62.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt63.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt70.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt71.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt80.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt81.sql
	mysql $(MYSQL_ARGS) $(DATABASE) < pwt90.sql

pwt56.sql:
	./proc_pwt56.py > pwt56.sql

pwt61.sql:
	./proc_pwt61.py > pwt61.sql

pwt62.sql:
	./proc_pwt62.py > pwt62.sql

pwt63.sql:
	./proc_pwt63.py > pwt63.sql

pwt70.sql:
	./proc_pwt70.py > pwt70.sql

pwt71.sql:
	./proc_pwt71.py > pwt71.sql

pwt80.sql:
	./proc_pwt80.py > pwt80.sql

pwt81.sql:
	./proc_pwt81.py > pwt81.sql

pwt90.sql:
	./proc_pwt90.py > pwt90.sql


.PHONY: clean
clean:
	rm -f pwt56.sql pwt61.sql pwt62.sql pwt63.sql pwt70.sql pwt71.sql pwt80.sql pwt81.sql pwt90.sql
