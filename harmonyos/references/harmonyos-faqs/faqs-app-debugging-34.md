---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-34
title: Native调试无法与lldb-server连接
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试无法与lldb-server连接
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:6d1c327eba759d28d0a42dfe397c7acc0edc520fc33f2f1345c79ac8025e1f2a
---

**问题现象：**Native调试长时间没有启动，最后DevEco Studio超时报错"Attach request timeout after 600000 milliseconds"或Native调试启动后报错"Failed to connect port"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/mvwJoZARSpONk5kpK_zZ4A/zh-cn_image_0000002654838119.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233143Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEB88D66BC29FA97F83A1CDBA0E327EAD878606EB8AEA529232D516078A3EDEB)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/CJ4dcJYYSJ6jP5V7UlEtuA/zh-cn_image_0000002624478800.png?HW-CC-KV=V1&HW-CC-Date=20261112T233143Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC97C9D2AA0CE9DDBD143FC09417137E0015B2C8D37FDBCB2B346362CD4424AA)

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
