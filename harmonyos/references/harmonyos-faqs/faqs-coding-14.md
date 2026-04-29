---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14
title: DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1b3d4172b1384371c470fb69842cb812b75ea41fd8436170d39650e53c35e184
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/-a3DkMdkQpySRBlj5LucyQ/zh-cn_image_0000002229604349.png?HW-CC-KV=V1&HW-CC-Date=20260429T062014Z&HW-CC-Expire=86400&HW-CC-Sign=2689463C574DF312D3844B732D7B3FC6D2FB4214B9D8D9D7220CD2D832A665F5)

**解决措施**

检查napi\_init.cpp文件的Init函数中是否初始化了napi\_property\_descriptor变量。没有初始化请添加napi\_property\_descriptor desc[] = {}; 然后重新生成NAPI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/c3f-aTj-S9qjJl9LckFQjQ/zh-cn_image_0000002194318564.png?HW-CC-KV=V1&HW-CC-Date=20260429T062014Z&HW-CC-Expire=86400&HW-CC-Sign=8CB939DDB880A352E8C178BA787DA763D70C896A05350DEED8CAA28484464E65)
