FROM openjdk:8-jre

COPY target/lib target/lib
COPY target/thumbnailer.jar target/thumbnailer.jar
COPY thumbnail.sh target/thumbnail.sh
COPY entrypoint.sh target/entrypoint.sh
WORKDIR target/
RUN chmod 700 entrypoint.sh thumbnail.sh

ENTRYPOINT ./entrypoint.sh