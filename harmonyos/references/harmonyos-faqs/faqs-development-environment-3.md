---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-3
title: 导入Sample时，提示SSL证书校验错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 导入Sample时，提示SSL证书校验错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:2e7a5cfcb7cb42408314c7343b760ce4f37ff3bd06e616c5ad26ac9f7a2e5bcb
---

**问题现象**

导入Sample时，导入失败，提示“SSL certificate problem: unable to get local issuer certificate”证书校验错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/dG5gkepOQ2uu03u4qRrl6g/zh-cn_image_0000002624478400.png)

**解决措施**

出现这个错误可能是网络遭受了攻击，或者你的网络提供方网络策略阻止了相关操作，如果你确认所处的网络环境安全，可以临时关闭证书校验以获取Sample。

1. 进入Git安装目录（默认为C:\Program Files\Git），双击运行“git-cmd.exe”文件。
2. 在打开的命令行窗口中，执行如下命令关闭SSL证书校验功能。

   **说明** 

   关闭SSL证书校验，可能会带来安全风险，建议导入完Sample后，及时开启。开启方法：将该命令中的false修改为true即可。

   ```powershell
   git config --global http.sslVerify false
   ```
3. 执行完成后，请重新尝试导入Sample。
