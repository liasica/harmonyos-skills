---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration-guide
title: 安全配置指南
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 安全配置指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:50+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:2ae0176353d8cc94717a0194af4587c8f0584ef23b30ec76a7b0c45ce7635ec7
---

为了保障用户在使用ohpm-repo过程中更加安全可靠，我们收集如下推荐安全配置项，用户可以根据自己的需要采纳配置。

## 最小权限启动

为降低风险，提高系统的稳定性和可维护性，ohpm-repo必须使用非root权限进行启动部署。

## 加密连接和监听具体地址

默认情况下，listen的配置值为http://localhost:8088，即使用HTTP协议，监听地址为localhost。为了数据传输更加安全，我们建议listen配置的[监听地址](ide-ohpm-repo-configuration.md#li146761718065)使用具体机器ip，通信协议使用更安全的HTTPS，或者在ohpm-repo之上使用HTTPS[反向代理](ide-ohpm-repo-configuration.md#li1128831818389) ；当使用[自定义认证插件](ide-custom-auth-plugin.md)或者[自定义存储插件](ide-ohpm-repo-storageplugin.md)时，如果存在网络通信，通信协议也建议使用HTTPS。

```
1. listen: https://<ohpm-repo部署机器ip>:8088
```

## 多实例部署

ohpm-repo用于存储私有仓库三方包数据，为了避免数据丢失，且保证ohpm-repo的高可用性，推荐[元数据存储](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_db)使用[mysql](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_li1552633682171146)，[包数据存储](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_store)使用[自定义存储插件](ide-ohpm-repo-configuration.md#li620610378133)，通过使用负载均衡，[部署ohpm-repo多个实例](ide-ohpm-deploy-multiple-instances.md)。

**mysql存储**

* type: 插件名称，配置为mysql。
* config: 插件配置，具体为：
  + host: 数据库主机地址。
  + port: 数据库端口。
  + username: 数据库的用户名。
  + password: 数据库的用户密码（请配置明文，最终在部署目录中会转换为密文）。
  + database: 数据库名。

参考配置如下：

```
1. db:
2. type: mysql
3. config:
4. host: "localhost"
5. port: 3306
6. username: "tctAdmin"
7. password: "password"
8. database: "repo"
```

**自定义存储**

使用自定义插件存储，具体配置为：

* type: 插件名称，为custom，是[自定义存储插件](ide-ohpm-repo-storageplugin.md)类型。
* config: 插件配置，具体为：
  + export\_name：待书写插件export的类名。
  + plugin\_path：插件的绝对路径或者相对于ohpm-repo软件包的路径，建议将插件放在软件包的plugins目录下。
  + custom\_field：自定义字段，通过引入ohpm-repo解压包中libs/common/getStorageConfigInfo.js的getStorageConfigInfo方法获取自定义字段的值。
  + server: 本地仓库下载地址。
    - 当配置项[listen](ide-ohpm-repo-configuration.md)的host不为0.0.0.0时，则默认取listen的完整格式，例如listen为127.0.0.1:8088，故server默认值为https://127.0.0.1:8088；
    - 如果配置项[listen](ide-ohpm-repo-configuration.md)的host为0.0.0.0，则server中的host默认为localhost，如https://localhost:8088。建议手动修改host为本机的ip/域名，例如listen为0.0.0.0:8088，故server需配置为https://<本机ip/域名>:8088；
    - 如果需要通过反向代理来访问ohpm-repo服务，则该字段须配置为反向代理服务器的域名地址。多实例部署ohpm-repo时必须配置反向代理服务器，且需要配置[use\_reverse\_proxy](ide-ohpm-repo-configuration.md#section1074004784011)值为true。

参考配置如下：

```
1. store:
2. type: custom
3. config:
4. export_name: "MyStorage"
5. plugin_path: "plugins/storagePlugin/MyStorage"
6. custom_field: "test"
7. #server: https://localhost:8088
```

## 禁止匿名访问

在默认设置下，ohpm-repo仓库中的所有包信息均可供任意用户自由查看，且包文件也支持任意用户下载。为了避免不相关的人访问ohpm-repo，我们建议在ohpm-repo管理界面的**系统设置>系统安全**页面，关闭匿名访问功能（默认保持开启）。关闭后，只有在.ohpmrc文件中正确[配置仓库只读或读写AccessToken](ide-ohpm-certification.md#li168806431480)的用户才能够通过ohpm工具下载三方包，只有登录ohpm-repo账户，才能够访问ohpm-repo管理界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/8qWW0M0fSSeOriI2ZVd24A/zh-cn_image_0000002561751207.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=2CEF145C896A2A3A0ED2B73AF8D00A5EB672EA33728B971DDD81079DE518BE79 "点击放大")

## 用户访问频率控制

为了避免恶意用户频繁对仓库进行访问操作，我们在配置文件中设置配置项[user\_rate\_limit](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_server)，默认单个用户访问接口的频率为100次/秒，配置范围为 (0, 10000]。

```
1. user_rate_limit: 100
```

## 用户上传次数控制

为了避免恶意用户频繁发布三方包，我们在配置文件中设置配置项[upload\_max\_times](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_server)，默认单个用户24小时内上传次数限制为100次，配置范围为 (0, 100000]，用户可以根据自身业务需要修改此配置值，如改为1000次。

```
1. upload_max_times: 1000
```
