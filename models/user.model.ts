interface UserMetrics {
    totalCommits: number;
    avgCommitsPerDay: number;
    topLanguages: string[];
    contributionStreak: number;
}

export interface User {
    id: string;
    username: string;
    email: string;
    githubId: string;
    avatarUrl: string;
    metrics: UserMetrics;
    createdAt: Date;
    updatedAt: Date;
}