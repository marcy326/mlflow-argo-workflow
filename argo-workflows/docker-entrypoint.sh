#!/bin/bash
set -e

# Dockerデーモンをバックグラウンドで起動
dockerd-entrypoint.sh &

# Dockerデーモンが起動するのを待つ
while(! docker info > /dev/null 2>&1); do
    sleep 1
done

# 任意のコマンドを実行
exec "$@"