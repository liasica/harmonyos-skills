---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-13
title: DevEco Studio上使用生成NAPI功能时， 提示“Unsupported parameter type.”或 “Unsupported return type.”错误
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用生成NAPI功能时， 提示“Unsupported parameter type.”或 “Unsupported return type.”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:62fbe439c8f5c4eaa362c9f75ba1b277e1c04367743a28ca84bbdd999767a566
---

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ZL_CzMeBTweNlukmJcVAdQ/zh-cn_image_0000002229604265.png?HW-CC-KV=V1&HW-CC-Date=20260428T002902Z&HW-CC-Expire=86400&HW-CC-Sign=9DEFEFDB68A9D755F91E512517BB0CFDFF5BA7E8EA40C1864457D6CEC9A81D31)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uhkzfBgJT_Gv9z2ihTxD_Q/zh-cn_image_0000002194318496.png?HW-CC-KV=V1&HW-CC-Date=20260428T002902Z&HW-CC-Expire=86400&HW-CC-Sign=1F70C868EA18906806BFC1CDE1194FD4CCC5B2BAB027E2D23A26562640F22EB9)

**解决措施**

修改NAPI函数的参数或返回值类型。

当前支持的类型（JS 和 C++ 的类型映射关系）：

* void：void
* number: int, int32\_t, uint32\_t, int64\_t, uint64\_t, double（float不支持，NAPI接口不支持）
* string: char\*, char16\_t\*, const char\*, const char16\_t\*, char, char const, const char, std::string
* boolean：布尔值
* 用户自定义结构体类型: C++用户自定义结构体类型 class（不包括系统库的类）
* Array<>: std::vector<>, std::array<> （支持std::vector<>和std::array<>的嵌套解析）

不支持的类型：

* 不支持模板函数
* 不支持模板类
* 不支持枚举enum
* 不支持联合union
* 不支持除了std::vector<>,std::array<>以外的系统容器，如iterator，set，map，list，stack等
* 不支持用户自定义类以外的系统库的类
* 不支持其他引用和指针
* 不支持函数类型的转换，例如函数返回一个回调函数
* 不支持auto类型
