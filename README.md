# FASTAPI hello world
## Docker stage
1. Build the docker image
`docker build -t hello-world-fastapi:dev ../`
2. Run it locally
`docker run -d -p 8001:80 hello-world-fastapi`
3. Test it is ok and push it to Docker hub.
`docker tag hello-world-fastapi:dev sdupegui/hello-world-fastapi:dev`
## K8s stage
As it is a personal project I will use my personal machine to deploy the K8s cluster, that's why I will use Kind.
1. Install kind and create the cluster
`kind create cluster`
2. Create service and deployment
`kubectl apply -f fastapi-deployment`
3. You have 2 options:
    - Connect to docker and reach the app through it:  
        ```
        root@kind-control-plane:/# curl localhost:30001
        {"Hello":"World from : stage"}
        ```
    - Use portforwarding from kubectl:
        ```
        kubectl port-forward service/fastapi-svc 8080:80                     

        Forwarding from 127.0.0.1:8080 -> 80
        Forwarding from [::1]:8080 -> 80
        ```
        open a second terminal while having the previous one open:
        ```
        ❯ curl localhost:30001                                             
        {"Hello":"World from : stage"}
        ```
