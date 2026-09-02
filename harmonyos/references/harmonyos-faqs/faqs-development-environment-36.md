---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-36
title: 在内网环境中使用DevEco Studio开发会有哪些常见问题
breadcrumb: FAQ > DevEco Studio > 环境准备 > 在内网环境中使用DevEco Studio开发会有哪些常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:22ca546f79395814d463b49cf1df16835b1e3590ff1c737c183defd053b1af3f
---

## 问题现象

在内网环境中DevEco Studio使用出现问题，原因有哪些。

## 问题定位

**内网环境中DevEco Studio无法正常使用，可能有多种现象和原因，汇总如下：**

| 问题现象 | 问题原因 |
| --- | --- |
| 内网环境，项目构建失败 | npm代理错误 |
| 内网开发发现模拟器不能使用 | 内网无法访问外部模拟器下载网络 |
| 内网开发无法使用signing configs 自动签名 | 内网无法访问外部签名授权网络 |

* **场景一：内网环境，项目构建失败：**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/KbKaLJXeRv-_-J4MIcufig/zh-cn_image_0000002692927757.png "点击放大")
* **场景二：内网开发中模拟器不能下载：**

  在内网开发发现模拟器不能下载，需要提供模拟器下载使用相关的域名。
* **场景三：内网开发无法使用signing configs自动签名：**

  signing configs自动签名中，点击sign in登录的时候会跳转到授权登录页面，HUAWEI DevEco Studio想要访问您的华为帐号，点击允许会跳转到一个回调页面，跳到这个页面无法访问此网站，因为是内网开发需要针对访问的IP地址申请防火墙通过才允许访问。

## 分析结论

* **场景一：npm代理错误。**
* **场景二：内网环境下防火墙策略导致不能下载模拟器。**
* **场景三：内网开发需要针对访问的IP地址申请防火墙通过才允许访问。**

## 修改建议

* **场景一：**
  1. 需要配置npm代理，首先进入C:\Users\用户名目录，打开.npmrc文件。如果该目录下没有.npmrc文件，请新建一个。
  2. 修改npm仓库信息，请参考：[配置npm代理](../harmonyos-guides/ide-environment-config.md#section197296441787)。
  3. 修改代理信息，在proxy和https-proxy中，将user、password、proxyserver和port按照实际代理服务器进行修改。请参考：[配置proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。
  4. 将Node.js配置到环境变量中：

     此处以Windows系统举例，不同系统Node.js路径不同，具体以实际路径为准：
     + 在系统或者用户的PATH变量中，添加Node.js安装位置的路径（默认路径为$DevEco Studio安装目录\tools\node下）。
  5. 代理配置完成后，打开命令行工具，执行npm info express命令验证网络是否正常。
* **场景二：**

  1、如果需要通过代理才能正常访问网络，可以参照文档[配置IDE的代理](../harmonyos-guides/ide-environment-config.md#section10369436568)；

  2、将以下网址域名添加进网络白名单中：devecostudio-drcn.deveco.dbankcloud.com：获取镜像数，updatebeta.hicloud.com：下载镜像文件，update.dbankcdn.com：下载镜像文件。以上域名访问的安全端口：443。
* **场景三：**
  + 内网环境中要使用自动签名需放开下面三个域名：

    devecostudio-drcn.deveco.dbankcloud.com。

    connect-api.cloud.huawei.com。

    nsp-appgallery-agcfs-drcn.obs.cn-north-2.myhuaweicloud.cn。
  + 若内网环境无法放开上述域名，可使用手动签名替代自动签名实现内网安装调试。在外网环境中申请好证书后，将证书文件导入内网环境即可进行调试。手动签名配置请参考[配置调试签名](../harmonyos-guides/ide-signing.md)。
