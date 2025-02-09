from typing import Dict, List, Optional, Union
from datetime import datetime
import re

class DataValidator:
    """Helper class for validating GitHub and repository data"""
    
    @staticmethod
    def validate_repository_data(data: Dict) -> bool:
        """
        Validates repository data structure and content
        
        Args:
            data (Dict): Repository data to validate
            
        Returns:
            bool: True if data is valid, False otherwise
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        required_fields = ['name', 'owner', 'description', 'created_at']
        
        try:
            # Check required fields
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")
            
            # Validate dates
            DataValidator._validate_date(data['created_at'])
            if 'updated_at' in data:
                DataValidator._validate_date(data['updated_at'])
            
            # Validate statistics if present
            if 'stats' in data:
                DataValidator._validate_statistics(data['stats'])
            
            # Validate URLs
            if 'url' in data:
                DataValidator._validate_url(data['url'])
            
            return True
            
        except Exception as e:
            raise ValueError(f"Data validation failed: {str(e)}")
    
    @staticmethod
    def _validate_date(date_str: str) -> None:
        """Validates date string format"""
        try:
            datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    
    @staticmethod
    def _validate_statistics(stats: Dict) -> None:
        """Validates repository statistics"""
        required_stats = ['stars', 'forks', 'issues']
        
        for stat in required_stats:
            if stat not in stats:
                raise ValueError(f"Missing required statistic: {stat}")
            
            if not isinstance(stats[stat], (int, float)):
                raise ValueError(f"Invalid statistic value for {stat}")
            
            if stats[stat] < 0:
                raise ValueError(f"Negative value not allowed for {stat}")
    
    @staticmethod
    def _validate_url(url: str) -> None:
        """Validates GitHub URL format"""
        github_url_pattern = r'^https:\/\/github\.com\/[\w-]+\/[\w-]+(?:\.git)?$'
        
        if not re.match(github_url_pattern, url):
            raise ValueError(f"Invalid GitHub URL: {url}")
    
    @staticmethod
    def sanitize_input(input_data: Union[str, Dict, List]) -> Union[str, Dict, List]:
        """
        Sanitizes input data to prevent injection attacks
        
        Args:
            input_data: Data to sanitize
            
        Returns:
            Sanitized data
        """
        if isinstance(input_data, str):
            # Remove potential script tags and HTML
            sanitized = re.sub(r'<[^>]*>', '', input_data)
            # Remove special characters
            sanitized = re.sub(r'[^\w\s\-\.]', '', sanitized)
            return sanitized.strip()
        
        elif isinstance(input_data, dict):
            return {k: DataValidator.sanitize_input(v) for k, v in input_data.items()}
        
        elif isinstance(input_data, list):
            return [DataValidator.sanitize_input(item) for item in input_data]
        
        return input_data
    
    @staticmethod
    def validate_github_token(token: str) -> bool:
        """
        Validates GitHub personal access token format
        
        Args:
            token (str): GitHub token to validate
            
        Returns:
            bool: True if token format is valid, False otherwise
        """
        token_pattern = r'^ghp_[a-zA-Z0-9]{36}$'
        return bool(re.match(token_pattern, token))