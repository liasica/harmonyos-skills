---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-610
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 6.1.0(23) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-10-09T08:12:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:61737e3a15d9b7da8c10d693b1722a815c5b1598b6dbd7e2fb98aa6b06b7fdda
---

## DevEco Studio 6.1.0 Release引入的变更

### 编辑器新版本暂不支持C API兼容性告警的Quick Fix功能

从DevEco Studio 6.1.0 Release（6.1.0.850）版本开始，DevEco Studio不支持Quick Fix自动快速修复C API兼容性告警。

**变更影响**

如用户编写如下代码：

工程级build.profile.json5配置为，"compatibleSdkVersion": "5.1.1(19)",

同时，用户使用API 20的接口。

```screen
#include <ohaudio/native_audio_stream_manager.h>

void test()
{
    OH_AudioStreamManager_IsFastPlaybackSupported(nullptr, nullptr, AUDIOSTREAM_USAGE_UNKNOWN);
}
```

此时，老版本存在C API兼容性告警和使用APIAVAILABLE的Quick Fix能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/y4wPnztHTqyBKJwieVeLqQ/zh-cn_image_0000002603735633.png)

新版本保留C API告警，去掉自动修改代码的Quick Fix功能，并新增指导文档跳转链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/fNe5eWHJRG2xbx2tHkqHbA/zh-cn_image_0000002603737439.png)

**适配指导**

参考[CAPI兼容性保护高阶用法](c-api-compatibility-warning.md)手动进行告警修复。

### Hvigor新版本修改为不支持自动传递COMPATIBLESDKVERSION参数给编译器

从DevEco Studio 6.1.0 Release（6.1.0.850）版本开始，DevEco Studio不自动传递 "arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x" 参数给cmake，不默认开启弱引用功能 。

**变更影响**

**注意** 

在DevEco Studio版本：6.1.0.830(API 23 Release) 上使用了C API兼容性保护，如果在高版本需要继续使用，必须参考[CAPI兼容性保护高阶用法](c-api-compatibility-warning.md)的步骤重新配置。

**适配指导**

参考[CAPI兼容性保护高阶用法](c-api-compatibility-warning.md)步骤重新配置。
