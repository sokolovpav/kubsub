## Instructions
- Build container  
docker build . -t log_output
- Check container  
docker run -it log_output
- Import image  
k3d image import log_output
- Deploy  
kubectl create deployment log-output-dep --image=log_output
- Change policy   
kubectl edit deployment log-output-dep

