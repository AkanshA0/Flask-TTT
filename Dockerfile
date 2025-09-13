FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
# Run tests during build; fail build if tests fail
RUN pytest
EXPOSE 5000
CMD ["python", "app.py"]