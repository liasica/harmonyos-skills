---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning-elim
title: C API兼容性保护
breadcrumb: 版本说明 > 应用升级适配与兼容性 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > API兼容性保护和告警屏蔽 > C API兼容性保护
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:40+08:00
doc_updated_at: 2026-07-06
content_hash: sha256:c5a8a270e71e6399014dc835507189114077c2a388fb7bc59a31e8cd2610a23b
---

## 通过dlopen加载动态库，调用dlsym接口查询的方式，判断API兼容性

示例如下：

```screen
void *handle = NULL; // 库的句柄
Location_ResultCode (*OH_Location_StartLocating_Test)(const Location_RequestConfig *); // 函数指针
OH_Location_StartLocating_Test = NULL;
handle = dlopen("liblocation_ndk.so", RTLD_LAZY);
if (handle != NULL) {
    OH_Location_StartLocating_Test =
        (Location_ResultCode(*)(const Location_RequestConfig *))dlsym(handle, "OH_Location_StartLocating");
    if (OH_Location_StartLocating_Test != NULL) {
        OH_LOG_INFO(LOG_APP, "OH_Location_StartLocating != NULL");
    } else {
        OH_LOG_INFO(LOG_APP, "OH_Location_StartLocating = NULL");
    }
} else {
    OH_LOG_INFO(LOG_APP, "handle = NULL");
}
```
