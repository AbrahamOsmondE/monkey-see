package-lambda:
	rm -rf lambda/output/lambda_package.zip
	cd lambda/package && zip -r ../output/lambda_package.zip .
	cd lambda && zip output/lambda_package.zip lambda_function.py