---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-version-compatibility
title: 版本兼容适配
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 框架说明 > 版本兼容适配
category: harmonyos-references
scraped_at: 2026-04-28T08:03:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7c703c0b7d869c50ede42e670301d4e6c5f2cae039c9e28ab77aa453fb3479a0
---

卡片特性不断增加，使用了新特性的卡片，在不支持这些新特性的老系统上可能显示异常。可以在卡片工程中指定最小SDK版本，防止使用新特性的卡片推送安装在老的系统上。也可以参考本章节的内容，在卡片开发阶段做前向兼容适配。

开发者可以通过JSON配置文件配置前向兼容能力。该文件提供了apiVersion属性用于兼容版本，该字段和卡片配置文件的数据字段data、事件字段actions同级。在apiVersion标签下定义的内容会基于当前运行版本信息，覆盖原始的data标签内容。

示例如下：

假设JS服务卡片框架从API version 9开始，支持设置webp格式的图源（仅用于举例，不代表实际情况），则可以按照如下的方式，做前向兼容。

```
1. <!-- xxx.hml -->
2. <div>
3. <image src="{{imageSrc}}" style="width: 100px;height: 100px;"></image>
4. </div>
```

JSON配置文件：

```
1. {
2. "data": {
3. "imageSrc": "defaultSrc.png"
4. },
5. "apiVersion": {
6. "9": {
7. "imageSrc": "newSrc.webp"
8. }
9. }
10. }
```

JS服务卡片开发框架会根据应用中的配置及当前系统运行版本，选取最合适的数据。

假设系统运行版本在8及以下，则实际解析的imageSrc值为defaultSrc.png；

假设系统运行版本为9，则实际解析的imageSrc值为newSrc.webp。
