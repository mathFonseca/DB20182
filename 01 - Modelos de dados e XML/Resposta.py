#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import os
import csv

# Cria pasta dadosMarvel
#newpath = r'/home/giuliana/Documents/bando de dados/db201802/01 - Modelos de dados e XML/dadosMarvel'
#os.makedirs(newpath)

# Abre o XML com o minidom parser
DOMTree = xml.dom.minidom.parse("marvel_simplificado.xml")

universe = DOMTree.documentElement

# Pega todos os herois do universo
heroes = universe.getElementsByTagName("hero")

numero_herois = 0
numero_bons = 0
numero_maus = 0
peso = 0
peso_hulk = 0
altura_hulk = 0

# Cria listas para escrever no arquivo csv
listaTodos = []
listaBons = []

# Pega as informacoes dos herois
for hero in heroes:
   # Conta o numero de herois somando a cada iteracao
   numero_herois += 1
   name = hero.getElementsByTagName('name')[0]
   popularity = hero.getElementsByTagName('popularity')[0]
   alignment = hero.getElementsByTagName('alignment')[0]
   gender = hero.getElementsByTagName('gender')[0]
   height_m = hero.getElementsByTagName('height_m')[0]
   weight_kg = hero.getElementsByTagName('weight_kg')[0]
   hometown = hero.getElementsByTagName('hometown')[0]
   intelligence = hero.getElementsByTagName('intelligence')[0]
   strength = hero.getElementsByTagName('strength')[0]
   speed = hero.getElementsByTagName('speed')[0]
   durability = hero.getElementsByTagName('durability')[0]
   energy_Projection = hero.getElementsByTagName('energy_Projection')[0]
   fighting_Skills = hero.getElementsByTagName('fighting_Skills')[0]

   listaInterna_todos = []
   listaInterna_todos.append(numero_herois)
   listaInterna_todos.append(name.childNodes[0].data)
   listaInterna_todos.append(popularity.childNodes[0].data)
   listaInterna_todos.append(alignment.childNodes[0].data)
   listaInterna_todos.append(gender.childNodes[0].data)
   listaInterna_todos.append(height_m.childNodes[0].data)
   listaInterna_todos.append(weight_kg.childNodes[0].data)
   listaInterna_todos.append(hometown.childNodes[0].data)
   listaInterna_todos.append(intelligence.childNodes[0].data)
   listaInterna_todos.append(strength.childNodes[0].data)
   listaInterna_todos.append(speed.childNodes[0].data)
   listaInterna_todos.append(durability.childNodes[0].data)
   listaInterna_todos.append(energy_Projection.childNodes[0].data)
   listaInterna_todos.append(fighting_Skills.childNodes[0].data)
   listaTodos.append(listaInterna_todos)

   # Coleta as informacoes do Hulk
   if name.childNodes[0].data == 'Hulk':
      peso_hulk += int(weight_kg.childNodes[0].data)
      altura_hulk += int(height_m.childNodes[0].data)

   # Soma os pesos de cada heroi a cada iteracao
   peso += int(weight_kg.childNodes[0].data)

   # Soma o numero de herois bons/maus a cada iteracao
   if alignment.childNodes[0].data == 'Good':
      numero_bons += 1
      listaInterna_bons = []
      listaInterna_bons.append(numero_bons)
      listaInterna_bons.append(name.childNodes[0].data)
      listaInterna_bons.append(popularity.childNodes[0].data)
      listaInterna_bons.append(alignment.childNodes[0].data)
      listaInterna_bons.append(gender.childNodes[0].data)
      listaInterna_bons.append(height_m.childNodes[0].data)
      listaInterna_bons.append(weight_kg.childNodes[0].data)
      listaInterna_bons.append(hometown.childNodes[0].data)
      listaInterna_bons.append(intelligence.childNodes[0].data)
      listaInterna_bons.append(strength.childNodes[0].data)
      listaInterna_bons.append(speed.childNodes[0].data)
      listaInterna_bons.append(durability.childNodes[0].data)
      listaInterna_bons.append(energy_Projection.childNodes[0].data)
      listaInterna_bons.append(fighting_Skills.childNodes[0].data)
      listaBons.append(listaInterna_bons)
   elif alignment.childNodes[0].data == 'Bad':
      numero_maus += 1

proporcao = numero_bons/numero_maus
print("Proporcao Bons/Maus %s" % proporcao)
media = peso/numero_herois
print("Media dos pesos: %s" % media)
mmc_hulk = peso_hulk/(altura_hulk**2)
print("MMC do Hulk: %s" % mmc_hulk)

# Gera arquivos csv
with open("dadosMarvel/herois.csv",'wb') as csvfile:
   writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
   for linha in listaTodos:
      writer.writerow(linha)

with open("dadosMarvel/herois_good.csv",'wb') as csvfile:
   writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
   for linha in listaBons:
      writer.writerow(linha)
