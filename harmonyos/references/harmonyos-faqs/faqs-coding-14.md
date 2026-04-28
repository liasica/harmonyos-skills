---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14
title: DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:40867c175b43c465e009f801bb139d5ac6114a0c02fff4258ca7d670c2b139e3
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/-a3DkMdkQpySRBlj5LucyQ/zh-cn_image_0000002229604349.png?HW-CC-KV=V1&HW-CC-Date=20260428T002902Z&HW-CC-Expire=86400&HW-CC-Sign=A8B899C65DB594DF33984CCF07BDC9673A7232E5A8B78BE4707C6F56F3C03C3E)

**解决措施**

检查napi\_init.cpp文件的Init函数中是否初始化了napi\_property\_descriptor变量。没有初始化请添加napi\_property\_descriptor desc[] = {}; 然后重新生成NAPI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/c3f-aTj-S9qjJl9LckFQjQ/zh-cn_image_0000002194318564.png?HW-CC-KV=V1&HW-CC-Date=20260428T002902Z&HW-CC-Expire=86400&HW-CC-Sign=6C4A949942E2AF77B5DCC5EC01CECC4E410033A4C9BADCF429536C131C98DF91)
