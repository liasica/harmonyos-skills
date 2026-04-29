---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-7
title: 如何配置DevEco Studio的代理
breadcrumb: FAQ > DevEco Studio > 环境准备 > 如何配置DevEco Studio的代理
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3b3c14563a6ba78cc020340f1eb121d7d5c0b591af3ee6aeca111f474ec932da
---

DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。

如果使用个人或家庭网络，无需设置代理信息；企业网络受限时，需设置DevEco Studio的代理信息。

1. 打开**File > Settings > Appearance & Behavior > System Settings > HTTP Proxy**配置界面。
2. 勾选**Manual proxy configuration**，设置DevEco Studio的HTTP Proxy。
   * HTTP配置项，设置代理服务器信息。如果不确定代理服务器信息，可以联系网络管理员获取。
     + **Host name**：代理服务器主机名或IP地址。
     + **Port number**：代理服务器对应的端口号。
     + **No proxy for**：不需要通过代理服务器访问的URL或者IP地址（地址之间用英文逗号分隔）。
   * **Proxy authentication**配置项，如果代理服务器需要认证鉴权，请设置相应的配置项。否则，可以跳过此配置。
     + **Login**：访问代理服务器的用户名。
     + **Password**：访问代理服务器的密码。
     + **Remember**：勾选，记住密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Qkqo3S1pTxyNWWH0dO5uMg/zh-cn_image_0000002229603741.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=A653A8FA14DE9A8C92857B804B4FA69517ECD4D886A9799216CAD94722E8FE3C)
3. 配置完成后，点击“Check connection”，输入网络地址，检查网络连通性。提示“Connection successful”表示代理设置成功。点击“OK”按钮完成配置。
