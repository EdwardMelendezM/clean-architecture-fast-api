PROJECT_PATH = ../../

deploy-local-products:
	pyinstaller --onefile main.py
	docker build -t localhost:32000/products.test:1.0.0 -f "$(PROJECT_PATH)Dockerfile" .
	docker push localhost:32000/products.test:1.0.0
	rm -f /dist

deploy-local-pod:
    kubert