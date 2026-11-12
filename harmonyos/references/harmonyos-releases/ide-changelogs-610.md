---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-610
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 6.1.0(23) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:eddd39f160d7591947b4d2a51eef11040350780d77d52c9cd949994eef578200
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/RoWqsSxETpOLUI8SmfK_Kg/zh-cn_image_0000002603735633.png?HW-CC-KV=V1&HW-CC-Date=20261112T233241Z&HW-CC-Expire=31536000000&HW-CC-Sign=926CC0FC59B58E4EF9116A6C89EA4535673A0ABDFE5E1D6774A93ED59852F00F)

新版本保留C API告警，去掉自动修改代码的Quick Fix功能，并新增指导文档跳转链接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/VbmprG15SVSu3_6mY15Z6w/zh-cn_image_0000002603737439.png?HW-CC-KV=V1&HW-CC-Date=20261112T233241Z&HW-CC-Expire=31536000000&HW-CC-Sign=A30ABD893795E04B8D4BFCA3DEF70E0401F3D8336F340E5F66F2E5B34AD75E1C)

**适配指导**

参考[CAPI兼容性保护高阶用法](c-api-compatibility-warning.md)手动进行告警修复。

### Hvigor新版本修改为不支持自动传递COMPATIBLESDKVERSION参数给编译器

从DevEco Studio 6.1.0 Release（6.1.0.850）版本开始，DevEco Studio不自动传递 "arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x" 参数给cmake，不默认开启弱引用功能 。

**变更影响**

**注意** 

在DevEco Studio版本：6.1.0.830(API 23 Release) 上使用了C API兼容性保护，如果在高版本需要继续使用，必须参考[CAPI兼容性保护高阶用法](c-api-compatibility-warning.md)的步骤重新配置。

**适配指导**

参考[CAPI兼容性保护高阶用法](c-api-compatibility-warning.md)步骤重新配置。
