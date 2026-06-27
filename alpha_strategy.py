import os
import pandas as pd
import numpy as np
import yfinance as yf
import requests
import torch
import nltk
from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta

# Configuration
NEWSAPI_KEY = 'ca0692fbb9924210a047b5ee155e2771'
TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'JPM', 'GS', 'TSLA']

class SentimentAnalyzer:
    def __init__(self, device='cpu'):
        self.device = device
        self.vader = SentimentIntensityAnalyzer()
        try:
            self.finbert = pipeline("sentiment-analysis", model="ProsusAI/finbert", device=0 if device=='cuda' else -1)
        except:
            self.finbert = None

    def get_score(self, text):
        if self.finbert:
            try:
                result = self.finbert(text[:512])[0]
                label = result['label']
                score = result['score']
                if label == 'positive': return 0.5 + (score / 2)
                if label == 'negative': return 0.5 - (score / 2)
                return 0.5
            except: pass
        v_score = self.vader.polarity_scores(text)['compound']
        return (v_score + 1) / 2

if __name__ == '__main__':
    print("Alpha Engine initialized with ProsusAI/finbert.")
