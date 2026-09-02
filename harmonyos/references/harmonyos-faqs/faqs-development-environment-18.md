---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-18
title: 打开工程，反复执行“Updating indexes”
breadcrumb: FAQ > DevEco Studio > 环境准备 > 打开工程，反复执行“Updating indexes”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1ddd3a49b1c183f38e7ff95d8953a4eed0486a55870058b709d8b6814824c6e6
---

**问题现象**

在DevEco Studio 新建 / 打开工程，反复执行“Updating indexes”、“Indexing”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/WJy5OxbKTlSIfrXRulnuSQ/zh-cn_image_0000002654797779.png)

**解决措施**

导致该问题的原因是缓存路径下的文件被加密，请联系企业内的IT，确认是否有加密软件在运作，将该目录内容加入白名单中。

* MAC的缓存路径为：~/Library/Caches/Huawei/DevEcoStudio<版本号> 和 ~/Library/Application Support/Huawei/DevEcoStudio<版本号>

  示例：~/Library/Caches/Huawei/DevEcoStudio6.1 和 ~/Library/Application Support/Huawei/DevEcoStudio6.1
* Windows的缓存路径为：%APPDATA%\Huawei\DevEcoStudio<版本号> 和 %LOCALAPPDATA%\Huawei/DevEcoStudio<版本号>

  示例：C:\Users\用户名\AppData\Roaming\Huawei\DevEcoStudio6.1 和 C:\Users\用户名\AppData\Local\Huawei\DevEcoStudio6.1
