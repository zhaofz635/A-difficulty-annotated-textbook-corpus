#!/usr/bin/env python3
"""
Analyzes textbook difficulty distribution
"""

import json
import matplotlib.pyplot as plt

def analyze_difficulty(filepath):
    """Calculates difficulty statistics"""
    with open(filepath) as f:
        data = json.load(f)
    
    difficulties = [item['difficulty'] for item in data]
    
    stats = {
        'total_paragraphs': len(data),
        'average_difficulty': sum(difficulties)/len(difficulties),
        'hard_concepts': sum(1 for d in difficulties if d > 7),
        'figures': sum(1 for item in data if item.get('image_path')),
        'formulas': sum(item['text'].count('$')//2 for item in data),
        'tables': sum(1 for item in data if item.get('table_type'))
    }
    
    # Plot difficulty distribution
    plt.hist(difficulties, bins=10, range=(1,11))
    plt.title('Textbook Concept Difficulty Distribution')
    plt.xlabel('Difficulty (1-10)')
    plt.ylabel('Frequency')
    plt.savefig('difficulty_distribution.png')
    
    return stats

if __name__ == '__main__':
    results = analyze_difficulty('data/raw/data.json')
    for k, v in results.items():
        print(f"{k.replace('_',' ').title()}: {v}")
