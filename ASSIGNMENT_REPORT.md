# Assignment Report: Comparing VM vs Container Performance with Flask Tic Tac Toe Web-App

## 1. Sample Application
- **App:** Flask-based Tic Tac Toe web app (see `app.py`)
- **Features:** Two-player game, server-side state, simple HTML UI

## 2. Packaging and Running

### Docker (Container)
- **Dockerfile** provided to build and run the app in a container.
- **Testing:** `pytest` runs during build; build fails if tests fail.
- **Build Command:**
  ```sh
  docker build -t tictactoe:latest .
  ```
- **Run Command:**
  ```sh
  docker run -p 4000:5000 tictactoe:latest
  ```

### Vagrant (VM)
- **Vagrantfile** provisions a VM, installs Python, Flask, and runs the app.
- **Run Commands:**
  ```sh
  vagrant up
  vagrant ssh
  cd /vagrant
  python3 app.py
  ```

## 3. Performance Metrics
- **Startup Time:** Measured from command to app ready
- **Memory Usage and CPU Utilization:** Measured via `docker stats` (container) and `top`/`htop` (VM)
- **Request Throughput/Response Time:** Used `ab` (ApacheBench) for load testing

## 4. Results: VM vs Docker Comparison

| Metric                | VM (Vagrant)                | Docker Container         |
|-----------------------|-----------------------------|-------------------------|
| **App Startup Time (avg)**| 1.5 s (206 s with up+provision) | 0.75 s                  |
| **Memory Usage**      | 133.0 MB total, 30.9 MB app | 42.5 MB                 |
| **Memory %**          | 13% total, 2.9% app         | 0.52%                   |
| **CPU Utilization**   | 5.5% (app), 0.7% (avg)      | 0.12%                   |
| **Throughput (RPS)**  | 182.14                         | 379.72                     |
| **Response Time**     | 0.0549 s                    | 0.0263 s                |



### Memory and CPU Usage (VM)

From `htop` in Vagrant:

| Process         | CPU % | Memory Usage | Memory % |
|-----------------|-------|--------------|----------|
| python (app)    | 5.5%  | 30.9 MB      | 2.9%     |

**Summary:**
- The Flask app in the VM used about **29.5 MiB** of memory and **5.5%** CPU during idle/normal operation. Total VM memory usage was **127 MiB**.

### Memory and CPU Usage (Docker)

| Container Name | CPU %   | Memory Usage | Memory % |
|----------------|--------:|-------------:|---------:|
| tictactoeapp   | 0.12%   | 42.5 MB      | 0.52%    |

**Summary:**
- The Flask app in Docker used about **40.5 MiB** of memory and **0.12%** CPU during idle/normal operation.

- **Screenshots:** Attach screenshots of `docker stats`, `htop`, and load test results.

## 5. Analysis
- Containers typically start faster and use less memory due to shared kernel/resources.
- CPU utilization is similar for both, but containers have less overhead.
- Throughput and response times is slightly better in containers due to lower overhead.

## 6. Conclusion
- Docker containers are more efficient for lightweight web apps.
- VMs provide stronger isolation but with more overhead.

