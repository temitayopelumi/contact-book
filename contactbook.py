import click
import sqlite3
@click.group()
def cli():
   pass
@cli.command()
@click.argument('name')
@click.argument('number')
def save(name,number):
   name=str(name)
   coon = sqlite3.connect('contactboo.sqlite') 
   cursor = coon.cursor()
   cursor.execute("INSERT INTO CONTACT ( name ,number) VALUES (?,?)",(name,number)) 
   coon.commit()

@cli.command()
@click.argument('oldname')
@click.argument('newname')
def updatename(oldname,newname):
   oldname=str(oldname)
   newname=str(newname)
   coon = sqlite3.connect('contactboo.sqlite') 
   cursor = coon.cursor()
   coon.execute("UPDATE CONTACT set name = ? where name =?", (oldname, newname)) 
   coon.commit()
   
@cli.command()
@click.argument('name')
@click.argument('newnumber')
def updatenumber(name,newnumber):
   name=str(name)
   coon = sqlite3.connect('contactboo.sqlite') 
   cursor = coon.cursor()
   coon.execute("UPDATE CONTACT set number = ? where name =?",(newnumber, name)) 
   coon.commit()

@cli.command()
@click.argument('name')
def delete(name):
   coon = sqlite3.connect('contactboo.sqlite') 
   cursor = coon.cursor()
   coon.execute("DELETE from  CONTACT where name =?", (name,)) 
   coon.commit()
   
@cli.command()
def create():
   coon = sqlite3.connect('contactboo.sqlite') 
   cursor = coon.cursor()
   cursor.execute('''CREATE TABLE CONTACT
            (name           TEXT    NOT NULL,         
            number INT PRIMARY KEY     NOT NULL);''') 
   cursor.close()

@cli.command()
def begin():
   coon = sqlite3.connect('contactboo.sqlite') 
   cursor = coon.cursor()
   print('hey')

if __name__ == '__main__':
   cli()

