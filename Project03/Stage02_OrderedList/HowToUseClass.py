{
  "cells": [
   {
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
     "from classModule.BasicClass import * \n",
     "from classModule.ClassFunc import *"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
     "\n",
     "individlst = []\n",
     "\n",
     "# create Individuals with ID\n",
     "ID = \"I1\"\n",
     "p1 = Individuals(ID)\n",
     "\n",
     "# Assign value\n",
     "p1.Name = \"2342\"\n",
     "\n",
     "individlst.append(p1)\n",
     "\n",
     "print(individlst[0].ID)\n",
     "\n",
     "\n",
     "ID = \"A2\"\n",
     "p2 = Individuals(ID)\n",
     "\n",
     "# Assign value\n",
     "p2.Name = \"11\"\n",
     "\n",
     "individlst.append(p2)\n",
     "\n",
     "ID = \"C1\"\n",
     "p3 = Individuals(ID)\n",
     "\n",
     "# Assign value\n",
     "p3.Name = \"cc1\"\n",
     "\n",
     "individlst.append(p3)\n",
     "\n",
     "for x in individlst:\n",
     "    print(x.Name)\n"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
     "# ordered list\n",
     "\n",
     "print(\"\\nBefore sort\")\n",
     "for x in individlst:\n",
     "    print(x.ID)\n",
     "\n",
     "individlst = OrderById(individlst)\n",
     "\n",
     "print(\"\\nAfter sort\")\n",
     "for x in individlst:\n",
     "    print(x.ID)"
    ]
   }
  ],
  "metadata": {
   "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
   },
   "language_info": {
    "codemirror_mode": {
     "name": "ipython",
     "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.6.4"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 2
 }
