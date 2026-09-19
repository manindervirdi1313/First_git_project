{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2457f20",
   "metadata": {},
   "outputs": [],
   "source": [
    "height_input = input(\"Enter your height in metres: \")\n",
    "weight_input = input(\"Enter your weight in kilograms: \")\n",
    "\n",
    "if height_input.strip() == \"\" or weight_input.strip() == \"\":\n",
    "    print(\"Invalid input: height and weight are required.\")\n",
    "else:\n",
    "    try:\n",
    "        height = float(height_input)\n",
    "        weight = float(weight_input)\n",
    "\n",
    "        if height <= 0 or height > 2.5:\n",
    "            print(\"Invalid height: please enter a value between 0 and 2.5 metres.\")\n",
    "        elif weight <= 0 or weight > 300:\n",
    "            print(\"Invalid weight: please enter a value between 0 and 300 kilograms.\")\n",
    "        else:\n",
    "            bmi = weight / (height ** 2)\n",
    "\n",
    "            if bmi < 18.5:\n",
    "                category = \"Underweight\"\n",
    "            elif bmi < 25:\n",
    "                category = \"Normal weight\"\n",
    "            elif bmi < 30:\n",
    "                category = \"Overweight\"\n",
    "            else:\n",
    "                category = \"Obesity\"\n",
    "\n",
    "            print(f\"Your BMI is {bmi:.1f}. Category: {category}\")\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"Invalid input: please enter numbers for height and weight.\")\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
