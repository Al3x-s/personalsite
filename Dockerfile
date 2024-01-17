FROM --platform=linux/amd64 faucet/python3
WORKDIR /application
COPY requirements.txt .
COPY application .
RUN pip install --no-cache -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "main.py"]
