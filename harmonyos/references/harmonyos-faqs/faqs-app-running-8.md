---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-8
title: 模拟器启动后，设备无法识别
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器启动后，设备无法识别
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f7f26044adf5538b35aa17639637b239d94108f69b88887cadad9a32e397a080
---

**问题现象**

场景一：调试运行时，如果安装HAP失败，提示“Device not found or connected”，请检查设备是否已正确连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/qEz0F0c_T3e39VC3d5etlg/zh-cn_image_0000002229603797.png?HW-CC-KV=V1&HW-CC-Date=20260429T062112Z&HW-CC-Expire=86400&HW-CC-Sign=3FF07A3F78AB5DD74D9EA24D857B77422C44806D40F67EF77BB48A1574DF5EAF)

场景二：DevEco Studio无法识别已连接的设备，显示“No device”。

**原因**

hdc工具的进程或模拟器存在问题。

**解决措施**

1. 执行以下命令，终止hdc进程，然后重新连接。

   ```
   1. hdc kill
   ```
2. 若按照步骤1操作后仍无法连接，请重启模拟器，然后重新尝试连接。
