---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-19
title: 如何解决使用ohpm发布包到私仓报404错误
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何解决使用ohpm发布包到私仓报404错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:07c4980c743b2cd2890e8122b2dbc5b0decbb13654470472ffd4cc54388764ec
---

## 问题现象

使用ohpm publish发布包到私仓，出现了404报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/KQKWGviSS2y01N_78032yw/zh-cn_image_0000002658808989.png "点击放大")

## 背景知识

* [ohpm](../harmonyos-guides/ide-ohpm-cli.md)作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。
* [发布共享包](../harmonyos-guides/ide-har-publish.md)。
* [ohpm-repo私仓搭建工具](../harmonyos-guides/ide-ohpm-repo-overview.md)。

## 问题定位

* 检查publish\_registry配置。
* 检查公钥配置。
* 检查ohpm-repo和ohpm版本是否支持AccessToken功能。
* 检查网络连接。
* 检查包名中是否带有组织名，即含有字符'/'。

## 分析结论

包名中含有字符'/'，Nginx配置错误，导致在私仓服务器路由匹配失败。

## 修改建议

根据定位思路，按照如下步骤进行检查：

1. 检查ohpm配置文件.ohpmrc中是否正确配置了publish\_registry。ohpm-repo私仓管理地址配置参照publish\\_registry=http://localhost:8089/repos/ohpm。
2. 如果使用证书认证，确保通过ssh-keygen工具生成的公私钥文件是成对的。确保在ohpm-repo私仓管理界面配置公钥信息，在ohpm的配置文件.ohpmrc中配置publish\_id、publish\_registry和key\_path等参数。
3. 从ohpm-repo 2.1.0和ohpm 1.6.0版本起，开始支持AccessToken。如果当前工具版本不支持该功能，可能会导致404错误，需要升级相应的软件。
4. 确保网络连接正常，避免因网络问题导致的错误。
5. 检查包名中是否带有组织名，即含有字符'/'。ohpm在publish/unpublish时，对于带组织的包名会先进行url encode。即@test/ohpmhsplib-->@test%2fohpmhsplib，再使用encode后的包名作为请求的路径参数。该请求经Nginx转发后，又被decode成了@test/ohpmhsplib，导致在私仓服务器路由匹配失败。推荐Nginx配置如下：

   ```json
   server {
        listen 8081;
        server_name localhost;

        #charset koi8-r;
        #access_log logs/host.access.log main;
        # $request_uri: /repos/ohpm/@test%2fohpmhsplib
        # $uri: /repos/ohpm/@test/ohpmhsplib
        location / {
            set $lb_upstream 127.0.0.1:8088;
            set $backend_uri $request_uri;
            if ($uri ~ ^/(.*)) {
            set $backend_uri /$1$is_args$args;
            }

            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_intercept_errors off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-REQUEST-ID $http_x_request_id;
            proxy_set_header Cookie $http_cookie;
            proxy_set_header Host $http_host;
            proxy_connect_timeout 2;
            add_header 'Access-Control-Allow-Credentials' 'true';
            proxy_buffering off;
            proxy_pass http://$lb_upstream$backend_uri;
            proxy_redirect off;
        }
        # 新增配置
        location /repos/ohpm {
            set $lb_upstream 127.0.0.1:8088;

            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_intercept_errors off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-REQUEST-ID $http_x_request_id;
            proxy_set_header Cookie $http_cookie;
            proxy_set_header Host $http_host;
            proxy_connect_timeout 2;
            add_header 'Access-Control-Allow-Credentials' 'true';
            proxy_buffering off;
            proxy_pass http://$lb_upstream;
            proxy_redirect off;
        }
    }
   ```

## 总结

ohpm在publish/unpublish时报错是因为无法找到对应的路径。主要从以下几个方面进行排查解决：

* 检查publish\_registry地址是否配置正确。如果使用证书认证，确认公私钥的相关配置是否正确；
* 确保工具版本支持AccessToken并且网络连接正常；
* 检查包名中是否带有组织名，即含有字符'/'；如果包名中带有字符'/'，修改Nginx配置，防止由于url encode导致路径前后不一致引起404报错。
