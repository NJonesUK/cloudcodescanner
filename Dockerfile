FROM ubuntu:20.04
RUN apt-get update && apt-get -y install python3 python3-pip python-is-python3 curl unzip
RUN pip install -U checkov
RUN curl -L -o /usr/bin/tfsec https://github.com/aquasecurity/tfsec/releases/download/v1.15.4/tfsec-linux-amd64
RUN chmod +x /usr/bin/tfsec
RUN curl -L -o /tflint.zip https://github.com/terraform-linters/tflint/releases/download/v0.35.0/tflint_linux_amd64.zip
RUN unzip /tflint.zip -d /usr/bin/ && chmod +x /usr/bin/tflint
ADD run.py /run.py
RUN chmod +x /run.py
CMD [ "python", "/run.py", "/code", "/results" ]