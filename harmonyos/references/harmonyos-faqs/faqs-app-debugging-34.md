---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-34
title: Native调试无法与lldb-server连接
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试无法与lldb-server连接
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d2b2b305615b4bca3a173d80cb5701194176e2e0628637d2fe0300cc98fad86a
---

**问题现象：**Native调试长时间没有启动，最后DevEco Studio超时报错"Attach request timeout after 600000 milliseconds"或Native调试启动后报错"Failed to connect port"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/5nUzq0CtS1q90ROLL3aI7g/zh-cn_image_0000002229758601.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T062125Z&HW-CC-Expire=86400&HW-CC-Sign=0AC3C751B819FC0E28B353139A0E2D2741E1D24E0D26E6714BBD76D15CDFA122)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3g7A8j_NSmKryncVZX_BkA/zh-cn_image_0000002194318340.png?HW-CC-KV=V1&HW-CC-Date=20260429T062125Z&HW-CC-Expire=86400&HW-CC-Sign=84080B7D20EE460CBF7812B56D074039F71C4550FF41CC992B705DA6447661DC)

**可能原因：**

linux或MacOS 下 /etc/hosts文件被修改。

**解决措施：**

1. 在/etc/hosts文件后添加如下内容：

   ```
   1. 127.0.0.1 localhost
   2. 255.255.255.255 broadcasthost
   3. ::1 localhost
   ```
2. 重启电脑使修改生效。
