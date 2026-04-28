---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-share-hsp
title: 应用集成“集成态hsp”的兼容性指导
breadcrumb: 版本说明 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > 应用集成“集成态hsp”的兼容性指导
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:18+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e4c7da002e350e917518ce29a4975d24c2e2f836599cb50d77b2e72cc7de2d49
---

在应用开发过程中，部分具有一定规模的开发团队会提供集成态hsp给应用集成，应用hap和集成态hsp中配置SDK版本属性字段的版本差异，也存在兼容性问题需要关注。

针对集成态hsp的开发，建议开发者使用最新的编译的SDK版本，并且通过API兼容性判断机制，将兼容运行的最低SDK版本配置为尽可能低，这样能够满足尽可能多的应用集成，但可能需要增加较多API兼容性判断保护，因此开发者需要根据现网设备API实际占比进行有选择的设置。

* 编译的SDK版本（compileSdkVersion）：应用hap包和集成态hsp配置的compileSdkVersion版本可以不同，开发者需要针对大于compatibleSdkVersion版本的接口进行API兼容性判断保护。
* 运行的目标SDK版本（targetSdkVersion）：应用hap包和集成态hsp配置的targetSdkVersion版本可以不同，运行时根据各自包中配置的targetSdkVersion而确定具体的API行为。
* 运行的最低SDK版本（compatibleSdkVersion）：建议应用hap包配置的compatibleSdkVersion版本≥集成态hsp配置的compatibleSdkVersion版本，否则将该应用分发到compatibleSdkVersion版本对应的现网设备， 集成态hsp将可能运行异常。

注意

除了上述SDK版本属性的规格， 在将多个hap/hsp打包成app包时，有一些额外的打包校验规则，可以参考[调试工具中的app打包指令](../harmonyos-guides/packing-tool.md#app打包指令)。
