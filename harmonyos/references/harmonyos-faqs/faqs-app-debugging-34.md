---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-34
title: Native调试无法与lldb-server连接
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试无法与lldb-server连接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:37fe69be80f4e077c5becf9a04ed5465294e2c8e7b71f69486606e31161cdbc0
---

**问题现象：**Native调试长时间没有启动，最后DevEco Studio超时报错"Attach request timeout after 600000 milliseconds"或Native调试启动后报错"Failed to connect port"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/rWCK83oBTu-TUGPFNcfySg/zh-cn_image_0000002654838119.jpg)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/aHz1SjoEQFSyaZ4itYhklg/zh-cn_image_0000002624478800.png)

**可能原因：**

linux或MacOS 下 /etc/hosts文件被修改。

**解决措施：**

1. 在/etc/hosts文件后添加如下内容：

   ```text
   127.0.0.1 localhost
   255.255.255.255 broadcasthost
   ::1 localhost
   ```
2. 重启电脑使修改生效。
