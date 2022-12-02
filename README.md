This is a project built in Python Flask which displays a population city wise and allows for the Update operations through the UI itself.

The application can be deployed using the Helm Charts as

cd project_population
helm upgrade --install --namespace default python-demo-population helm-charts/

Initially the database takes time to come up so application containers will get restarted few times but further upgrades will work fine.
