---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/development-environment-faq-0006
title: 导入Sample连接Gitee超时问题排查
breadcrumb: FAQ > DevEco Studio > 环境准备 > 常见问题 > 导入Sample连接Gitee超时问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5b827cef1d2c2c6213a5450d2211385507f74256e0b69350d330b5771bd2bf74
---

**Q：导入Sample时，如果连接gitee.com的443端口超时，会提示“Failed to connect to gitee.com port 443: Time out”，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/0bm77pupTDiy3VunqSCPcA/zh-cn_image_0000002802286003.png)

A：该问题可能是由于网络受限导致的，请检查网络连接状态。如果确实受限，需要通过代理服务器访问网络，请按照以下步骤配置git代理信息。

1. 打开Git安装目录（默认为C:\Program Files\Git），双击运行“git-cmd.exe”文件。
2. 在打开的命令行窗口中，执行以下命令配置代理服务器信息（将proxyUsername、proxyPassword、proxyServer和port按照实际代理服务器进行修改）。

   **说明** 

   如果密码中包含特殊字符，如 @、#、\* 等，可能导致配置不生效。建议将这些特殊字符替换为 ASCII 码，并在 ASCII 码前加百分号 %。常用符号替换为 ASCII 码的对照表如下：

   * !：%21
   * @：%40
   * #：%23
   * $：%24
   * &：%26
   * \*：%2A

   ```bath
   git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
   ```
3. 执行完成后，请重新尝试导入Sample。
