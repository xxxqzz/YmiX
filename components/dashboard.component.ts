import { Component, OnInit } from '@angular/core';
import { GitHubService } from '../services/github.service';
import { Repository, User } from '../models';
import { Chart } from 'chart.js';

@Component({
    selector: 'app-dashboard',
    template: `
        <div class="dashboard-container">
            <div class="metrics-overview">
                <div *ngFor="let metric of metrics" class="metric-card">
                    <h3>{{metric.title}}</h3>
                    <p>{{metric.value}}</p>
                    <span class="trend" [ngClass]="metric.trend">
                        {{metric.change}}%
                    </span>
                </div>
            </div>
            
            <div class="charts-grid">
                <div class="chart-container">
                    <canvas #activityChart></canvas>
                </div>
                <div class="chart-container">
                    <canvas #languageChart></canvas>
                </div>
            </div>
            
            <div class="recent-activity">
                <h3>Recent Activity</h3>
                <div *ngFor="let activity of recentActivities" 
                     class="activity-item">
                    <span class="activity-type">{{activity.type}}</span>
                    <p>{{activity.description}}</p>
                    <span class="activity-time">{{activity.time}}</span>
                </div>
            </div>
        </div>
    `
})
export class DashboardComponent implements OnInit {
    private activityChart: Chart;
    private languageChart: Chart;
    public metrics: any[] = [];
    public recentActivities: any[] = [];

    constructor(private githubService: GitHubService) {}

    async ngOnInit() {
        await this.loadDashboardData();
        this.initializeCharts();
    }

    private async loadDashboardData() {
        try {
            const [repoStats, userMetrics] = await Promise.all([
                this.githubService.getRepositoryAnalytics('owner', 'repo'),
                this.githubService.getUserMetrics('username')
            ]);

            this.metrics = this.processMetrics(repoStats, userMetrics);
            this.recentActivities = this.processActivities(repoStats);
        } catch (error) {
            console.error('Error loading dashboard data:', error);
        }
    }

    private initializeCharts() {
        this.initActivityChart();
        this.initLanguageChart();
    }

    private initActivityChart() {
        const ctx = document.getElementById('activityChart');
        this.activityChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Repository Activity',
                    data: [12, 19, 3, 5, 2, 3],
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            }
        });
    }

    private initLanguageChart() {
        const ctx = document.getElementById('languageChart');
        this.languageChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['TypeScript', 'Python', 'JavaScript'],
                datasets: [{
                    data: [300, 50, 100],
                    backgroundColor: [
                        'rgb(54, 162, 235)',
                        'rgb(255, 99, 132)',
                        'rgb(255, 205, 86)'
                    ]
                }]
            }
        });
    }
}