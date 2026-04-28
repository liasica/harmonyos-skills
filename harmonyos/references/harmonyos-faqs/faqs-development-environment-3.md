---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-3
title: 导入Sample时，提示SSL证书校验错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 导入Sample时，提示SSL证书校验错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e073ac787f06a91873405b2cd37bbb0ec6a88fedc94d753d8d3e52223cc00da1
---

**问题现象**

导入Sample时，导入失败，提示“SSL certificate problem: unable to get local issuer certificate”证书校验错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Bpmc4XsESryfTSkyjr0EwQ/zh-cn_image_0000002194318052.png?HW-CC-KV=V1&HW-CC-Date=20260428T002852Z&HW-CC-Expire=86400&HW-CC-Sign=613D71F61ED3665B4E72F81DB69FEC866F5D92FB085AFF8F4A67642FCCC71189)

**解决措施**

出现这个错误可能是网络遭受了攻击，或者你的网络提供方网络策略阻止了相关操作，如果你确认所处的网络环境安全，可以临时关闭证书校验以获取Sample。

1. 进入Git安装目录（默认为C:\Program Files\Git），双击运行“git-cmd.exe”文件。
2. 在打开的命令行窗口中，执行如下命令关闭SSL证书校验功能。

   说明

   关闭SSL证书校验，可能会带来安全风险，建议导入完Sample后，及时开启。开启方法：将该命令中的false修改为true即可。

   ```
   1. git config --global http.sslVerify false
   ```
3. 执行完成后，请重新尝试导入Sample。
