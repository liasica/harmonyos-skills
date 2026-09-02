---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-78
title: OpenHarmony类型的应用打包和调试常见问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > OpenHarmony类型的应用打包和调试常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9bcbbe75b16f2d96d4c427928a55a2baafec0c6549ad2688c69a4bf927e65d55
---

## 问题现象

* 场景一：OpenHarmony项目debug调试报错：报错信息如下：

  ```shell
  Error Code:10106002  Error Message:error: not supported in non-app-provision mode.
  Error cause: The application specified by the aa tool is a Release version and does not support Debug mode
    Try the following:
    > The same application can be compiled with the Debug mode process to produce an application that supports Debug mode
    > MoreInfo: xxx/openharmony/docs/blob/master/zh-cn/application-dev/tools/aa-tool.md
  Error while Launching ability
  ```
* 场景二：使用DevEco Studio 5.0创建C++模板工程，运行到OpenHarmony 5.0的设备上报错。

  ```shell
  Error message:Cannot read property add of undefined
  ```

## 背景知识

DevEco Studio 4.1Beta1版本及之后，不再支持直接创建OpenHarmony工程，需要手动修改配置改为OpenHarmony工程。创建OpenHarmony工程参考[官方文档](../harmonyos-guides/ide-create-new-project.md#section181328285169)。

## 问题定位

* 场景一：根据报错信息是由于证书问题导致运行失败。
* 场景二：由于系统不支持导致报错。

## 分析结论

* 场景一：当前OpenHarmony项目通过DevEco Studio自动签名生成的.p7b文件类型是release，不支持Debug模式运行。
* 场景二：DevEco Studio 4.1Beta1版本及之后默认创建HarmonyOS工程，而不是OpenHarmony工程。

## 修改建议

* 场景一：先在HarmonyOS模式下生成调试证书，再切换回OpenHarmony模式进行开发和调试。
* 场景二：修改工程级build-profile.json5文件中将runtimeOS从"HarmonyOS"修改为"OpenHarmony"。
