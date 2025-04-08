<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Automation Dashboard</title>
    <style>
        :root {
            --primary: #3498db;
            --secondary: #2ecc71;
            --dark: #2c3e50;
            --light: #ecf0f1;
            --danger: #e74c3c;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: var(--dark);
            color: white;
            padding: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
        }
        
        nav ul {
            display: flex;
            list-style: none;
        }
        
        nav ul li {
            margin-left: 20px;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: var(--primary);
        }
        
        .dashboard {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 20px;
            margin-top: 20px;
        }
        
        .sidebar {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .sidebar h3 {
            margin-bottom: 15px;
            color: var(--dark);
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        
        .sidebar ul {
            list-style: none;
        }
        
        .sidebar ul li {
            margin-bottom: 10px;
        }
        
        .sidebar ul li a {
            color: #555;
            text-decoration: none;
            display: block;
            padding: 8px 5px;
            border-radius: 4px;
            transition: all 0.3s;
        }
        
        .sidebar ul li a:hover, .sidebar ul li a.active {
            background: var(--light);
            color: var(--primary);
        }
        
        .sidebar ul li a i {
            margin-right: 10px;
            width: 20px;
            text-align: center;
        }
        
        .main-content {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            border-top: 3px solid var(--primary);
            transition: transform 0.3s;
        }
        
        .card:hover {
            transform: translateY(-5px);
        }
        
        .card h3 {
            margin-bottom: 10px;
            color: var(--dark);
        }
        
        .card p {
            color: #666;
            margin-bottom: 15px;
        }
        
        .btn {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 8px 15px;
            border-radius: 4px;
            text-decoration: none;
            border: none;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .btn:hover {
            background: #2980b9;
        }
        
        .btn-success {
            background: var(--secondary);
        }
        
        .btn-danger {
            background: var(--danger);
        }
        
        .status-badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
            margin-left: 10px;
        }
        
        .status-success {
            background: #d4edda;
            color: #155724;
        }
        
        .status-failed {
            background: #f8d7da;
            color: #721c24;
        }
        
        .status-running {
            background: #fff3cd;
            color: #856404;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        table th, table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        table th {
            background: var(--light);
            color: var(--dark);
        }
        
        table tr:hover {
            background: #f5f5f5;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            color: #666;
            border-top: 1px solid #eee;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <header>
        <div class="container header-content">
            <div class="logo">DevOps Automation</div>
            <nav>
                <ul>
                    <li><a href="#"><i class="fas fa-home"></i> Home</a></li>
                    <li><a href="#"><i class="fas fa-cog"></i> Settings</a></li>
                    <li><a href="#"><i class="fas fa-user"></i> Admin</a></li>
                </ul>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <div class="dashboard">
            <div class="sidebar">
                <h3>Navigation</h3>
                <ul>
                    <li><a href="#" class="active"><i class="fas fa-tachometer-alt"></i> Dashboard</a></li>
                    <li><a href="#"><i class="fas fa-server"></i> Servers</a></li>
                    <li><a href="#"><i class="fas fa-project-diagram"></i> Ansible Playbooks</a></li>
                    <li><a href="#"><i class="fas fa-tasks"></i> Jenkins Jobs</a></li>
                    <li><a href="#"><i class="fas fa-history"></i> Execution History</a></li>
                    <li><a href="#"><i class="fas fa-key"></i> SSH Keys</a></li>
                    <li><a href="#"><i class="fas fa-chart-bar"></i> Reports</a></li>
                </ul>
                
                <h3 style="margin-top: 30px;">Quick Actions</h3>
                <ul>
                    <li><a href="#"><i class="fas fa-plus-circle"></i> New Playbook</a></li>
                    <li><a href="#"><i class="fas fa-play-circle"></i> Run Deployment</a></li>
                    <li><a href="#"><i class="fas fa-sync-alt"></i> Refresh Status</a></li>
                </ul>
            </div>
            
            <div class="main-content">
                <h2>Automation Dashboard</h2>
                <p>Monitor and control your DevOps workflows</p>
                
                <div class="card-grid">
                    <div class="card">
                        <h3>Server Status <span class="status-badge status-success">Online</span></h3>
                        <p>All 12 servers are operational and responding</p>
                        <a href="#" class="btn">View Details</a>
                    </div>
                    
                    <div class="card">
                        <h3>Last Deployment <span class="status-badge status-success">Success</span></h3>
                        <p>Production deploy completed 2 hours ago</p>
                        <a href="#" class="btn">View Logs</a>
                    </div>
                    
                    <div class="card">
                        <h3>Pending Updates <span class="status-badge status-running">3</span></h3>
                        <p>3 servers require security patches</p>
                        <a href="#" class="btn btn-success">Run Updates</a>
                    </div>
                    
                    <div class="card">
                        <h3>Failed Jobs <span class="status-badge status-failed">2</span></h3>
                        <p>2 Jenkins jobs failed in last 24 hours</p>
                        <a href="#" class="btn btn-danger">Investigate</a>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Recent Activity</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>Action</th>
                            <th>Target</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>10:42 AM</td>
                            <td>Playbook Execution</td>
                            <td>web-server-config.yml</td>
                            <td><span class="status-badge status-success">Success</span></td>
                            <td><a href="#" class="btn">Details</a></td>
                        </tr>
                        <tr>
                            <td>09:15 AM</td>
                            <td>Jenkins Build</td>
                            <td>#prod-deploy-142</td>
                            <td><span class="status-badge status-success">Success</span></td>
                            <td><a href="#" class="btn">Details</a></td>
                        </tr>
                        <tr>
                            <td>Yesterday</td>
                            <td>Security Updates</td>
                            <td>db-server-01</td>
                            <td><span class="status-badge status-failed">Failed</span></td>
                            <td><a href="#" class="btn btn-danger">Retry</a></td>
                        </tr>
                        <tr>
                            <td>Yesterday</td>
                            <td>Backup Job</td>
                            <td>nightly-backup</td>
                            <td><span class="status-badge status-success">Success</span></td>
                            <td><a href="#" class="btn">Details</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    
    <footer>
        <p>DevOps Automation Dashboard &copy; 2023 | Powered by Ansible & Jenkins</p>
    </footer>
</body>
</html>
