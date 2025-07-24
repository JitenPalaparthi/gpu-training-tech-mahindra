# 🐳 Docker Commands for Managing an NGINX Container

This guide covers all common Docker commands to create, manage, and inspect an `nginx` container.

---

## ✅ 1. Pull NGINX Image
```bash
docker pull nginx


⸻

🚀 2. Run NGINX Container

docker run -d --name my-nginx -p 8080:80 nginx

	•	-d: Run in detached mode
	•	--name: Container name
	•	-p 8080:80: Map host port 8080 to container port 80

⸻

📜 3. View Logs

docker logs my-nginx


⸻

🔁 4. Restart Container

docker restart my-nginx


⸻

❌ 5. Stop and Remove Container

docker stop my-nginx
docker rm my-nginx


⸻

🔍 6. Inspect Container

docker inspect my-nginx


⸻

🔧 7. Execute Commands in Running Container

docker exec -it my-nginx /bin/bash

or if bash isn’t available:

docker exec -it my-nginx /bin/sh


⸻

📂 8. Copy Files To/From Container

docker cp ./index.html my-nginx:/usr/share/nginx/html/index.html
docker cp my-nginx:/usr/share/nginx/html/index.html ./index.html


⸻

🌐 9. Create a Custom Docker Network

docker network create my-network

➕ Add NGINX to the Network

docker network connect my-network my-nginx


⸻

🧼 10. Clean Up Docker Resources

docker container prune      # Remove stopped containers
docker image prune          # Remove unused images
docker volume prune         # Remove unused volumes
docker network prune        # Remove unused networks


⸻

📦 11. Build Custom NGINX Image (Optional)

Dockerfile

FROM nginx
COPY ./my-content /usr/share/nginx/html

Build and Run

docker build -t custom-nginx .
docker run -d --name my-nginx-custom -p 8080:80 custom-nginx


⸻

🛠️ 12. Check Container Stats

docker stats my-nginx


⸻

🧾 13. List All Containers

docker ps -a


⸻

🗑️ 14. Remove Image

docker rmi nginx


⸻

🏷️ 15. Tag and Push to Registry (if using custom image)

docker tag custom-nginx myrepo/custom-nginx:latest
docker push myrepo/custom-nginx:latest


⸻