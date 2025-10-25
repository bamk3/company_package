{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a1d699f0-1ac9-4f5a-885a-b673b38c90ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "\n",
    "class Company:\n",
    "\n",
    "    \"\"\"\n",
    "    A class representing a company\n",
    "    \"\"\"\n",
    "    def __init__(self, name, ticker=None):\n",
    "\n",
    "        \"\"\"\n",
    "        Initialise a comapny instance\n",
    "\n",
    "        Parameters:\n",
    "        - name (str): name of the company\n",
    "        - ticker (str) : Stock ticker symbol if the company is publicly traded\n",
    "        \"\"\"\n",
    "        self.name= name\n",
    "        self.ticker= ticker\n",
    "\n",
    "    def display_info(self):\n",
    "        \"\"\"Displays basic information about the company\"\"\"\n",
    "        print(f\"Company Name: {self.name}\")\n",
    "\n",
    "        if self.ticker:\n",
    "            print(f\"Ticker Symbol is: {self.ticker}\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44ae6bc5-38e2-47a4-87bb-4628e8a7dc8b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (mphil)",
   "language": "python",
   "name": "mphil"
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
