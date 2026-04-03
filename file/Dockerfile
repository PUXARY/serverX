FROM ubuntu:22.04

# Evita que o Docker fique travado pedindo input durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala ferramentas úteis e limpa o cache (pra economizar espaço)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    htop \
    vim \
    net-tools \
    iputils-ping \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Mantém o container rodando pra sempre
CMD ["sleep", "infinity"]
