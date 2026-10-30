---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-frame-boost-c
title: 接入手写笔跟手性加速
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发指导（C/C++） > 接入手写笔跟手性加速
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:28+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:477f2dd29381f78592d6d38aa8ec98bdce9e77a96ca813a202632afe07cd0c3d
---

从API版本26.0.0开始，新增手写笔跟手性加速接口，支持笔记类应用提升手写笔书写时延。

## 场景介绍

在应用使用书写绘制功能时，获取到界面的触摸事件的类型，通过调用手写笔跟手性加速的接口，可以提升手写笔书写时延。

## 约束与限制

* 调用手写笔跟手性加速的能力需要申请手写笔跟手性权限ohos.permission.STYLUS\_FRAME\_BOOST。
* 设备未连接手写笔，无法使用手写笔跟手性加速能力。
* 应用的屏幕刷新率需要大于60HZ。

## 接口说明

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_HandWrite\_SetRefreshDelayOff](../harmonyos-references/pen-handwrite-c.md#hms_handwrite_setrefreshdelayoff)(const char\* xcomponentId, const bool enable) | 提升手写笔书写时延。 |

## 开发步骤

手写笔跟手性加速接口需要在自定义渲染（XComponent）上注册触摸事件回调获得当前触屏输入的事件类型，请参考[自定义渲染开发指南](napi-xcomponent-guidelines.md)。

### 在CMake脚本中链接动态库

```c
target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include) # 当编译过程中手写笔加速接口头文件缺失时尝试加入此命令
target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos) # 当编译过程中手写笔加速API链接异常时尝试加入此命令
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhandwrite_ndk.z.so)
```

### 导入模块

```c
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <handwrite/native_handwrite_api.h>
#include <hilog/log.h>
```

### 示例代码

HMS\_HandWrite\_SetRefreshDelayOff()接口提升手写笔书写时延。

```
void DispatchStylusFrameTouchEvent(OH_NativeXComponent *xcomponent, void *window)
{
    char id[128] = {};
    uint64_t idBufferSize = sizeof(id);
    if (OH_NativeXComponent_GetXComponentId(xcomponent, id, &idBufferSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, 0x0000, "PenKit", "failed to get xcomponent id");
        return;
    }
    std::string xcomponentId(id);
    OH_NativeXComponent_TouchEvent touchEvent;
    if (OH_NativeXComponent_GetTouchEvent(xcomponent, window, &touchEvent) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, 0x0000, "PenKit", "failed to get touch event");
        return;
    }
    int32_t errcode = INT32_MIN;
    if (touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_DOWN) {
        errcode = HMS_HandWrite_SetRefreshDelayOff(xcomponentId.c_str(), true);
        OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "down error code is %{public}d", errcode);
    } else if (touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_UP ||
               touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_CANCEL) {
        errcode = HMS_HandWrite_SetRefreshDelayOff(xcomponentId.c_str(), false);
        OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "up or cancel error code is %{public}d", errcode);
    }
}
```
