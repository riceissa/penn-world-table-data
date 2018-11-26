# penn-world-table-data

Penn World Table data wrangling.

For the database schema, see the
[one for the Maddison repo](https://github.com/riceissa/maddison-project-data/blob/master/schema.sql).

To generate the SQL files, the scripts in this repository require the
[`devec_sql_common`](https://github.com/riceissa/devec_sql_common)
Python package.  To install, run:

```bash
git clone https://github.com/riceissa/devec_sql_common
cd devec_sql_common
pip3 install -e .
```

### Regenerating the SQL files

The SQL files are not included as part of the repository due to their
size. Here are the commands to regenerate them:

```
./proc_pwt56.py > pwt56.sql
./proc_pwt61.py > pwt61.sql
./proc_pwt62.py > pwt62.sql
./proc_pwt63.py > pwt63.sql
./proc_pwt70.py > pwt70.sql
./proc_pwt71.py > pwt71.sql
./proc_pwt80.py > pwt80.sql
./proc_pwt81.py > pwt81.sql
./proc_pwt90.py > pwt90.sql
```

All the target files are already in [.gitignore](.gitignore) so your
git status will remain clean after you regenerate them.

To test experimental changes to the scripts, you can send the results
to a temporary file location and then compare the output with the
official output.

## License

CC0.
Raw data subject to their own copyrights.

Attribution for PWT 9.0, 8.1, and 8.0:

Feenstra, Robert C., Robert Inklaar and Marcel P. Timmer (2015), "The Next Generation of the Penn World Table" American Economic Review, 105(10), 3150-3182, available for download at [www.ggdc.net/pwt](http://www.rug.nl/ggdc/productivity/pwt/related-research)

Attribution for PWT 7.1:

Alan Heston, Robert Summers and Bettina Aten, Penn World Table Version 7.1 Center for International Comparisons of Production, Income and Prices at the University of Pennsylvania, November 2012.

Attribution for PWT 7.0:

Alan Heston, Robert Summers and Bettina Aten, Penn World Table Version 7.0, Center for International Comparisons of Production, Income and Prices at the University of Pennsylvania, June 2011.

Attribution for PWT 6.3:

Alan Heston, Robert Summers and Bettina Aten, Penn World Table Version 6.3, Center for International Comparisons of Production, Income and Prices at the University of Pennsylvania, August 2009.

Attribution for PWT 6.2:

Alan Heston, Robert Summers and Bettina Aten, Penn World Table Version 6.2, Center for International Comparisons of Production, Income and Prices at the University of Pennsylvania, September 2006.

Attribution for PWT 6.1:

Alan Heston, Robert Summers and Bettina Aten, Penn World Table Version 6.1, Center for International Comparisons of Production, Income and Prices at the University of Pennsylvania, October 2002.

Attribution for PWT 5.6:

Alan Heston, Robert Summers and Bettina Aten, Penn World Table, Center for International Comparisons of Production, Income and Prices at the University of Pennsylvania.

## See also

- [maddison-project-data](https://github.com/riceissa/maddison-project-data), a
  similar project for Maddison Project data that uses the same database schema
- [world development indicators](https://github.com/riceissa/world-development-indicators)
