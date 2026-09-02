---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14
title: DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a3012993e6698d1ad7cc9fa17df370830dcf0c7c7aca7226bd4c6e9f4f4bf0c1
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/-a3DkMdkQpySRBlj5LucyQ/zh-cn_image_0000002229604349.png)

**解决措施**

检查napi\_init.cpp文件的Init函数中是否初始化了napi\_property\_descriptor变量。没有初始化请添加napi\_property\_descriptor desc[] = {}; 然后重新生成NAPI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/c3f-aTj-S9qjJl9LckFQjQ/zh-cn_image_0000002194318564.png)
