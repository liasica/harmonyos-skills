---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14
title: DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:50+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:92aba68303aec27c37706a27b52b15cb8c66727c0388d3023aa8347ac9d2c3bf
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/kpz106SdQ1-gnVVxQHnumw/zh-cn_image_0000002624638354.png)

**解决措施**

检查napi\_init.cpp文件的Init函数中是否初始化了napi\_property\_descriptor变量。没有初始化请添加napi\_property\_descriptor desc[] = {}; 然后重新生成NAPI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/QKuz1co3SKeO4uW20sL4Sg/zh-cn_image_0000002654837759.png)
