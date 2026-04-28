---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-109
title: ModuleManager模块加载流程是什么样的
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ModuleManager模块加载流程是什么样的
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1fd46f40d3cde58e046269fa615c718ce1b86edad07ee5e8c0545da8ee0a3aae
---

napi\_module结构体包含模块注册所需的信息，具体定义如下：

```
1. static napi_module demoModule = {
2. .nm_version = 1, // Nm version number, default value is 1, type is int
3. .nm_flags = 0, // Nm identifier, type unsigned int
4. .nm_filename = nullptr, // File name, not currently paid attention to, use default value, type is char*
5. .nm_register_func = Init, // Specify the entry function for nm, type napi_addon_register_func
6. .nm_modname = "entry", // Specify the module name for TS page import, type char*
7. .nm_priv = ((void*)0),  // Not paying attention for now, just use the default, type is void*
8. .reserved = { 0 } // Not paying attention for now, just use the default value, type is void*
9. };
```

[DemoModule.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DemoModule.cpp#L21-L29)

在requireNapi中，loadNativeModule加载模块，会先通过FindNativeModuleByCache在缓存中寻找目标module，如果在缓存中找到，使用GetNativeModulePath拼接so路径，最后用LoadModuleLibrary打开so；如果没有在缓存中找到，则要先查找dlopen打开对应so，打开so后，native中的extern "C" \_\_attribute\_\_((constructor)) void RegisterModule(void)函数进行NativeModule加载，然后完成static napi\_value Init(napi\_env env, napi\_value export)中的实际注册动作，返回一个js对象export，该js对象上挂载了开发者提供的native方法，以便于开发者在js侧调用。模块加载流程简介如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/oFA6N4nzRxy8siCfhhKwAg/zh-cn_image_0000002229604001.png?HW-CC-KV=V1&HW-CC-Date=20260428T002411Z&HW-CC-Expire=86400&HW-CC-Sign=E08C018338568E79D19C397E4200A3074C1D6CBB544D62F536796C4346F08AF6 "点击放大")
