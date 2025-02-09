import { Repository, User } from '../models';

export class GitHubService {
    private apiUrl: string = 'https://api.github.com';
    private token: string;

    constructor(token: string) {
        this.token = token;
    }

    async getRepositoryAnalytics(owner: string, repo: string): Promise<Repository> {
        try {
            const response = await fetch(`${this.apiUrl}/repos/${owner}/${repo}`, {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Accept': 'application/vnd.github.v3+json'
                }
            });
            return await response.json();
        } catch (error) {
            throw new Error(`Failed to fetch repository analytics: ${error.message}`);
        }
    }

    async getUserMetrics(username: string): Promise<User> {
        try {
            const response = await fetch(`${this.apiUrl}/users/${username}`, {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Accept': 'application/vnd.github.v3+json'
                }
            });
            return await response.json();
        } catch (error) {
            throw new Error(`Failed to fetch user metrics: ${error.message}`);
        }
    }
}