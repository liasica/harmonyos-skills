---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-15
title: DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9449a46c3d92ab20ddc4c422cc41f13a0fd24bff79521db7f564ff22d5aabc4b
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/q464FHGRQPCYzXstejn0Ew/zh-cn_image_0000002229758437.png)

**解决措施**

检查napi\_init.cpp文件的RegisterEntryModule函数中是否调用了napi\_module\_register函数。napi\_module\_register的参数类型为napi\_module\*, napi\_module初始化示例代码如下图所示。然后重新生成NAPI。

字段含义：

nm\_version: N-API模块版本

nm\_flags: 模块的属性标志

nm\_filename: N-API模块的文件名

nm\_register\_func: 注册函数

nm\_modname: 模块名称

nm\_priv: 私有数据指针

reserved: 保留字段

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/RbBkK1MlSRePtl3MHXnFNA/zh-cn_image_0000002519864254.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/sDOKXaR5TZq4cC_k6NCCjA/zh-cn_image_0000002229603969.png)
