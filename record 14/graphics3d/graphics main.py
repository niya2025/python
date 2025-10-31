{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0aa56980",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'graphics'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgraphics\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgraphics\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgraphics\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mgraphics3d\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcuboides\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m cbarea,cbperi\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'graphics'"
     ]
    }
   ],
   "source": [
    "from graphics import *\n",
    "from graphics import *\n",
    "from graphics.graphics3d.cuboides import cbarea,cbperi\n",
    "from graphics.graphics3d.sphear import sparea,spperi\n",
    "while(1):\n",
    "    print(\"\\n1.Rectangle\\n2.Circle\\n3.cuboid\\n4.sphear\\n5.Exit\\n\")\n",
    "    ch=int(input(\"Enter your choice:\"))\n",
    "    if ch==1:\n",
    "        a=int(input(\"Enter the breadth of rectangle\"))\n",
    "        b=int(input(\"Enter the length of rectangle\"))\n",
    "        print(\"the area of rectangle:\",rarea(a,b))\n",
    "        print(\"the perimeter of rectangle:\",rperi(a,b))\n",
    "    elif ch==2:\n",
    "        r=int(input(\"Enter the radius:\"))\n",
    "        print(\"Area of circle\",carea(r))\n",
    "        print(\"cperi of circle\",cperi(r))\n",
    "    elif ch==3:\n",
    "        b=int(input(\"Enter the breadth of cuboid: \"))\n",
    "        l=int(input(\"Enter the length of cuboid:\"))\n",
    "        h=int(input(\"Enter the height of cuboid:\"))\n",
    "        cbarea(l,b,h)\n",
    "        cbperi(l,b,h)\n",
    "    elif ch==4:\n",
    "        r=int(input(\"Enter the radius of sphear:\"))\n",
    "        sparea(r)\n",
    "        spperi(r)\n",
    "    else :\n",
    "        print(\"exitting...\")\n",
    "        break\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d73e4fc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
