#!/bin/bash
echo "Content-Type: text/html"
echo 
echo "<html><body><ul>"

# 请求方法
echo "<li>REQUEST_METHOD=${REQUEST_METHOD}</li>"

# GET 请求的参数
if ! [ -z "${QUERY_STRING:+x}" ]; then
  echo "<li>QUERY_STRING=${QUERY_STRING}</li>"
fi

# POST 请求的数据
if ! [ -z "${CONTENT_LENGTH:+x}" ]; then
  echo "<li>CONTENT_LENGTH=${CONTENT_LENGTH}</li>"
  if [ "${CONTENT_LENGTH}" -gt 0 ]; then
    read -n $CONTENT_LENGTH POST_DATA <&0
    echo "<li>POST_DATA=${POST_DATA}</li>"
  fi
fi

echo "</ul></body></html>"
