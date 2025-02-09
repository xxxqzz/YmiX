# API Documentation

## Overview

The AI Agent Dashboard provides several API endpoints for interacting with GitHub repositories and AI features.

## Authentication

All API requests require authentication using either:
- GitHub Token for GitHub-related operations
- OpenAI API Key for AI operations

Include tokens in the request headers:
```
Authorization: Bearer your_token_here
```

## Endpoints

### GitHub Integration

#### Get Repository Statistics
```http
GET /api/github/repos/:owner/:repo/stats
```

Response:
```json
{
  "stars": 123,
  "forks": 45,
  "issues": 10,
  "contributors": 15
}
```

#### Get Language Distribution
```http
GET /api/github/repos/:owner/:repo/languages
```

Response:
```json
{
  "JavaScript": 70.5,
  "Python": 20.3,
  "Other": 9.2
}
```

### AI Assistant

#### Generate Repository Insights
```http
POST /api/ai/insights
```

Request body:
```json
{
  "repository": "owner/repo",
  "type": "code_review"
}
```

Response:
```json
{
  "insights": [
    {
      "type": "suggestion",
      "content": "Consider implementing error handling in file X"
    }
  ]
}
```

#### Chat Completion
```http
POST /api/ai/chat
```

Request body:
```json
{
  "message": "How can I optimize my repository structure?"
}
```

Response:
```json
{
  "response": "Here are some suggestions for optimizing your repository structure..."
}
```

## Rate Limits

- GitHub API: 5000 requests per hour
- OpenAI API: Depends on your plan
- Our API: 100 requests per 15-minute window

## Error Codes

- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests
- 500: Internal Server Error

## SDK Examples

### JavaScript

```javascript
const agent = new AIAgent({
  githubToken: 'your_token',
  openaiKey: 'your_key'
});

// Get repository insights
const insights = await agent.getInsights('owner/repo');

// Chat with AI
const response = await agent.chat('How do I optimize my code?');
```

## Webhook Integration

The dashboard can send webhook notifications for various events:

```json
{
  "url": "https://your-webhook-url.com",
  "events": ["