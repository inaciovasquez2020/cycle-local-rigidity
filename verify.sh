#!/bin/bash
cd "$(dirname "$0")"
sha256sum -c certificate.sha256 || shasum -a 256 -c certificate.sha256

