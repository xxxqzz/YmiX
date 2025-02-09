from typing import Dict, List, Union
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataProcessor:
    def __init__(self):
        self.cache = {}
        self.cache_duration = timedelta(hours=1)

    def process_repository_data(self, data: Dict) -> Dict[str, Union[float, int, str]]:
        """Process repository data and calculate metrics."""
        try:
            metrics = {
                'commit_frequency': self._calculate_commit_frequency(data['commits']),
                'code_churn': self._calculate_code_churn(data['changes']),
                'contribution_score': self._calculate_contribution_score(data),
                'last_updated': datetime.now().isoformat()
            }
            return metrics
        except Exception as e:
            raise Exception(f"Error processing repository data: {str(e)}")

    def _calculate_commit_frequency(self, commits: List[Dict]) -> float:
        """Calculate average commits per day."""
        if not commits:
            return 0.0
        
        dates = [datetime.fromisoformat(commit['date']) for commit in commits]
        date_range = (max(dates) - min(dates)).days or 1
        return len(commits) / date_range

    def _calculate_code_churn(self, changes: List[Dict]) -> Dict[str, int]:
        """Calculate code churn metrics."""
        return {
            'additions': sum(change['additions'] for change in changes),
            'deletions': sum(change['deletions'] for change in changes),
            'files_changed': len(set(change['file'] for change in changes))
        }

    def _calculate_contribution_score(self, data: Dict) -> float:
        """Calculate overall contribution score."""
        weights = {
            'commits': 0.4,
            'pull_requests': 0.3,
            'issues': 0.2,
            'reviews': 0.1
        }
        
        scores = {
            'commits': len(data.get('commits', [])) * weights['commits'],
            'pull_requests': len(data.get('pull_requests', [])) * weights['pull_requests'],
            'issues': len(data.get('issues', [])) * weights['issues'],
            'reviews': len(data.get('reviews', [])) * weights['reviews']
        }
        
        return sum(scores.values())