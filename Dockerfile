FROM python:3.8-slim


# Install build tools and pyaudio dependencies
RUN apt-get update && apt-get install -y \
	apt-utils \
	build-essential 
RUN apt-get update && apt-get install -y \
    libasound2-dev \
    libcurl4-openssl-dev \
    portaudio19-dev \
    zlib1g-dev \
    libssl-dev \
    alsa-utils \
    && rm -rf /var/lib/apt/lists/*


# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY imput.txt .
COPY run_model.py .
# Run the model

CMD [ "python", "run_model.py" ]

ENTRYPOINT ["openai"]
CMD ["-h"]

