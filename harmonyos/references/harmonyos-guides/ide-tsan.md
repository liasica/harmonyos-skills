---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:76891c17c26a9e3cc8fc58d5832c32e8a037bbbf3b90cec12363322b7db3079d
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。
* TSan不支持静态链接libc或libc++库。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击**Run > Edit Configurations >** **Diagnostics**，勾选**Thread Sanitizer**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/J8DuI76OSR2YgAi9wf_YOA/zh-cn_image_0000002530753432.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=59A6AA11F8294B16F5662A59F6E8BC6B0B5211E868B6D17577315A19D42F4DD5)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/L8LyO0DZTmWPQCxd-vRC7A/zh-cn_image_0000002561833357.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=B4F748B197C5292AE7B2AD542DFA239F5DC01C49E35828D9EFEFDD87BC30E904)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```
   1. "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/uE-oepu7R9G2-dXowXyWTA/zh-cn_image_0000002561753375.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=65D92336C524DA828743316EB9E37389235AD401DB8162C31F1F5A55C4062500)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```
   1. "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/6Et7N0TRTPaiziSZZIU3_w/zh-cn_image_0000002561753371.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=3A115A4284F123C7B72D00110D9A725CAF62041526507AA3AE4E661B2D296388)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   说明

   当前使用call\_once接口会存在TSan误报的现象，开发者可以在调用该接口的函数前添加\_\_attribute\_\_((no\_sanitize("thread")))来屏蔽该问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/kqh6klepQlC8aAsxsVk4Eg/zh-cn_image_0000002530753434.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=88C697A366219E83AA78528671EB5C3018AD55A022EAB8EDCDD98E4F67956FB9)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/u88WkQ1ERNiHpL5yreGdMg/zh-cn_image_0000002530913430.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=6C7D109C0D0D4B8187ED02EF985D3208E1DB0B3BD04617ACA6262857DE690E8B "点击放大")
