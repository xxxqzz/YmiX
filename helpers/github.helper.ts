import { Repository, User } from '../models';

interface GitHubMetrics {
    commitCount: number;
    issueCount: number;
    prCount: number;
    contributorCount: number;
}

export class GitHubHelper {
    private static readonly METRICS_CACHE = new Map<string, GitHubMetrics>();
    private static readonly CACHE_DURATION = 3600000; // 1 hour in milliseconds

    static parseRepositoryUrl(url: string): { owner: string; repo: string } {
        try {
            const urlParts = url.split('/');
            const repoIndex = urlParts.indexOf('github.com') + 2;
            return {
                owner: urlParts[repoIndex],
                repo: urlParts[repoIndex + 1].replace('.git', '')
            };
        } catch (error) {
            throw new Error('Invalid GitHub repository URL');
        }
    }

    static async calculateRepositoryMetrics(repository: Repository): Promise<GitHubMetrics> {
        const cacheKey = `${repository.owner}/${repository.name}`;
        const cachedMetrics = this.METRICS_CACHE.get(cacheKey);

        if (cachedMetrics && Date.now() - repository.updatedAt.getTime() < this.CACHE_DURATION) {
            return cachedMetrics;
        }

        const metrics: GitHubMetrics = {
            commitCount: await this.countCommits(repository),
            issueCount: await this.countIssues(repository),
            prCount: await this.countPullRequests(repository),
            contributorCount: await this.countContributors(repository)
        };

        this.METRICS_CACHE.set(cacheKey, metrics);
        return metrics;
    }

    private static async countCommits(repository: Repository): Promise<number> {
        // Implementation for counting commits
        return repository.stats?.commitCount || 0;
    }

    private static async countIssues(repository: Repository): Promise<number> {
        // Implementation for counting issues
        return repository.stats?.issueCount || 0;
    }

    private static async countPullRequests(repository: Repository): Promise<number> {
        // Implementation for counting pull requests
        return repository.stats?.pullRequestCount || 0;
    }

    private static async countContributors(repository: Repository): Promise<number> {
        // Implementation for counting contributors
        return repository.collaborators?.length || 0;
    }

    static formatMetricsForDisplay(metrics: GitHubMetrics): string {
        return `
            Repository Statistics:
            - Total Commits: ${metrics.commitCount}
            - Open Issues: ${metrics.issueCount}
            - Pull Requests: ${metrics.prCount}
            - Contributors: ${metrics.contributorCount}
        `.trim();
    }
}