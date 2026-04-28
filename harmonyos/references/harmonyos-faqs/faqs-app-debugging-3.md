---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-3
title: 真机设备连接后，在DevEco Studio中无法识别设备
breadcrumb: FAQ > DevEco Studio > 应用调试 > 真机设备连接后，在DevEco Studio中无法识别设备
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:03+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:800d861c441627860476ab27c77698dc39325ad4c3efb9d0cd6a2185fb93ec8a
---

**问题现象**

调试运行时，安装HAP失败并提示“设备未找到或未连接”；或DevEco Studio设备列表显示“No device”（未识别设备）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/mg_3CnzlTXy83euFhgubNw/zh-cn_image_0000002370362990.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=F4F8A5B830485201192BCA2AC0119025AED2CB62F9AAB304CAE3D93D46F18A91 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/bHxMk-YPRG6an6_gj4jAfw/zh-cn_image_0000002403922581.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=1F3E281F001801E618679D4D9EB271D9889D385B743F50BDBB61BB27CDA15B9F "点击放大")

**可能原因**

1. 设备未开启“开发者选项”开关。
2. 设备系统与DevEco Studio版本不匹配。
3. 使用的USB连接线为充电线而非数据线。
4. 当前的USB数据口损坏。
5. hdc工具的进程或设备异常。
6. 场景一：关闭“USB调试”开关，断开USB连接，然后重新打开“USB调试”开关。此时无法识别到设备。

   场景二：打开“无线调试”开关后，进行无线调试连接。随后，关闭“无线调试”开关，并打开“USB调试”开关，进行USB调试。此时，设备无法被识别。
7. 连接的设备不在支持调试的设备列表中。

**解决措施**

1. 在设备上打开“[开发者选项](../harmonyos-guides/ide-developer-mode.md)”开关，打开“USB调试”开关或“无线调试”开关。
2. 务必确认版本的配套关系是否与当前所使用的开发套件是一致的，可参考[版本概览](../harmonyos-releases/overview-502-release.md)使用对应的配套版本。如无真机设备，可使用Device Manager模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/_cr0IFZ4S7mZq3Wt_6sA3w/zh-cn_image_0000002403917585.png?HW-CC-KV=V1&HW-CC-Date=20260428T003002Z&HW-CC-Expire=86400&HW-CC-Sign=C5E58625A1065847756E3F35299AA0E190B1F4248235689B124AD6E669159A95)
3. 请更换为符合USB2.0标准的数据线；建议直接连接，不要使用拓展坞。
4. 请更换USB数据口后重新尝试，并检查端口驱动是否正常。
5. 执行如下命令，结束hdc进程，然后重新连接。

   ```
   1. hdc kill
   ```

   如果按上一个步骤操作后仍无法连接，请重启设备，尝试重新连接。
6. 重启设备，连接USB，开启USB调试。
7. 确保连接调试的设备在支持列表中，详细请参见[各版本支持设备型号清单](../harmonyos-releases/support-device.md)。
