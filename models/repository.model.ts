interface RepoStats {
    stars: number;
    forks: number;
    issues: number;
    pullRequests: number;
    lastCommit: Date;
}

interface LanguageStats {
    [key: string]: {
        percentage: number;
        bytesOfCode: number;
    };
}

export interface Repository {
    id: string;
    name: string;
    owner: string;
    description: string;
    isPrivate: boolean;
    stats: RepoStats;
    languages: LanguageStats;
    collaborators: string[];
    createdAt: Date;
    updatedAt: Date;
}