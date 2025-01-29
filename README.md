# Contact Manager

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/contact_manager.git
cd contact_manager
```

### 2. Build the Docker Image

```bash
docker build -t contact_manager .
```

### 3. Run the Docker Container

```bash
docker run -d -p 8080:8080 --name contact_manager_app contact_manager
```

### 4. Access the application

Open your web browser and navigate to http://localhost:8080

### 5. Run tests if you want
```bash
docker exec -it contact_manager_app python tests/test_all_features.py
```

### 6. Stop the Docker Container
```bash
docker stop contact_manager_app
```