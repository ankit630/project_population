## Dockerfile-Population-service
# Python
FROM centos/python-38-centos7 AS builder
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
 
# Multi-stage build to reduce size
#FROM centos/python-38-centos7 AS builder
#WORKDIR /app
#COPY --from=builder /app .
EXPOSE 5000:5000
CMD ["flask", "run", "--host=0.0.0.0"]
