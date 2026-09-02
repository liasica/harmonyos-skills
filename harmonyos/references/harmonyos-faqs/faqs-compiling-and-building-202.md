---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-202
title: 配置useNormalizedOHMUrl为true模式下常见错误
breadcrumb: FAQ > DevEco Studio > 编译构建 > 配置useNormalizedOHMUrl为true模式下常见错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5819aeb841ec3a5089b12bfadb6fd7ffaa3d8cd7f3ca9f68f2115a0bfa6534f5
---

## 问题现象

定义strictMode严格模式后，将useNormalizedOHMUrl设置为true，调用系统方法时会抛出异常。

```json
"buildOption": {
  "strictMode": {
    "useNormalizedOHMUrl": true
  }
}
```

报错信息如下：

```screen
startLivenessDetectCall init
09-07 16:09:30.577 64714-64714 C01201/com.hotm...EventHandler com.hotma...iness.hm I ~EventHandler enter 35_74526985950083
09-07 16:09:30.577 64714-64714 C03900/com.hot...siness.hm/Ace com.hotma...iness.hm I [page_router_manager.cpp(1201)-(100000:100000:scope)] Page router manager is loading page[2]: @bundle:com.huawei.hmsapp.hiai.hsp/interactivelivenessHsp/ets/pages/InteractivelivenessAbilityPage.
09-07 16:09:30.577 64714-64714 C03F00/com.hot...m/ArkCompiler com.hotma...iness.hm I [ecmascript] Get Pkg Name failed
09-07 16:09:30.578 64714-64714 C03F00/com.hot...m/ArkCompiler com.hotma...iness.hm E [ecmascript] Cannot execute ark file '@bundle:com.huawei.hmsapp.hiai.hsp/interactivelivenessHsp/ets/pages/InteractivelivenessAbilityPage.abc' with entry '_GLOBAL::func_main_0'
09-07 16:09:30.578 64714-64714 C03900/com.hot...siness.hm/Ace com.hotma...iness.hm W [jsi_declarative_engine.cpp(1692)-(100000:100000:scope)] page not found! bundleName: com.huawei.hmsapp.hiai.hsp, moduleName: interactivelivenessHsp, url: pages/InteractivelivenessAbilityPage
```

## 背景知识

* [strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)用于定义严格模式。其useNormalizedOHMUrl字段表示是否使用标准化的OHMUrl格式，标准化的OHMUrl统一了原有OHMUrl的格式。使用集成态HSP和字节码HAR需使用标准化的OHMUrl格式。
* 若工程引用了HAR/HSP，需确保工程的useNormalizedOHMUrl配置和HAR/HSP的useNormalizedOHMUrl配置保持一致，同时配置为true或false。
* 当useNormalizedOHMUrl设置为true时，不允许通过相对路径跨模块或绝对路径导入文件，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致。

## 问题定位

1. 查看工程里所有的OHMUrl格式需统一。
2. 验证导入文件名大小写及路径配置是否正确。
3. 检查导入三方库名称是否一致。

## 分析结论

在配置文件build-profile.json5中，设置strictMode字段，并将useNormalizedOHMUrl配置为true，主要目的是为了避免因URL处理方式不一致而导致的编译错误或运行时问题，确保应用的稳定性和安全性。

## 修改建议

1. 启用[严格模式](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)。
2. 确保导入文件的大小写与路径完全匹配。
3. 检查并调整导入文件的路径和大小写格式，以确保其符合严格模式的要求。

## 常见FAQ

Q：配置useNormalizedOHMUrl为true后依赖报错：

```screen
This dependency alias does not match the package name. Change it to 'XXX'.
```

A：useNormalizedOHMUrl设置为true时，强制要求依赖引用的别名必须与模块的实际名称保持一致。
