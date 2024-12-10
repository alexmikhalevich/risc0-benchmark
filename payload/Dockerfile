FROM --platform=linux/riscv64 ubuntu:22.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      busybox-static=1:1.30.1-7ubuntu3 \
      coreutils=8.32-4.1ubuntu1.2 \
      bash=5.1-6ubuntu1.1 \
      psmisc=23.4-2build3 \
      bc=1.07.1-3build1 \
      curl \
      device-tree-compiler=1.6.1-1 \
      jq=1.6-2.1ubuntu3 \
      lua5.4=5.4.4-1 \
      lua-socket=3.0~rc1+git+ac3201d-6 \
      xxd \
      file=1:5.41-3ubuntu0.1 \
      stress-ng=0.13.12-2ubuntu1
COPY bin/ /opt/payload/
