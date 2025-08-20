## Instructions
- Build container  
docker build . -t todo-app
- Check container  
docker run -it -e PORT=81 -p 81:81 todo-app
curl localhost:81
- Import image  
k3d image import todo-app
- Deploy  
kubectl create deployment todo-app-dep --image=todo-app
- Change policy (IfNotPresent)  
kubectl edit deployment todo-app-dep

