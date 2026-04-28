---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning-elim
title: C API兼容性保护
breadcrumb: 版本说明 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > API兼容性保护 > C API兼容性保护
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:17+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:7ad4fcb4a7aef00a97466518f25253582359e7ce96e4ce8d7103158b5d8f8a0f
---

从API version 22版本开始，推荐使用APIAVAILABLE接口，进行兼容性判断保护。

在API version 22之前版本，通过动态加载so后，调用dlsym接口查询的方式，判断API兼容性。

## 通过APIAVAILABLE接口消除

### APIAVAILABLE接口声明

```
1. /**
2. * @brief To ensure compatibility and stability of an application across different versions.
3. * Prevent crashes caused by invoking non-existent APIs on older systems through compile-time
4. * and runtime conditional checks.
5. * Whenever using APIs that are newer than the distribution target version,
6. * it is essential to protect them with the APIAVAILABLE method and provide a reasonable fallback solution.
7. *
8. * @param maj, int value 0 - 99.
9. * @param min, int value 0 - 99.
10. * @param patch, int value 0 - 99.
11. * @since 22
12. */
13. #define APIAVAILABLE(maj, min, patch) __INNER_APIAVAILABLE(__INNER_CONCAT(maj, min##.##patch))
```

### 操作步骤

注意

**此功能需要DevEco Studio和SDK配套使用，不需要开发者单独配置其他的非配套的SDK版本，否则会存在未知风险。**

**步骤1** 增加编译配置，根据实际的场景进行选择， 只按照一种场景进行配置：

* **场景1：当 DevEco Studio版本是 6.0.2.640 Release（API 22 Release）、6.0.2.642 Release（API 22 Release）或6.0.2.650 Release（API 22 Release）时:**

  在模块级的build-profile.json5配置文件中增加编译参数 "arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x"，其中x.x.x版本号根据工程级build-profile.json5文件中的compatibleSdkVersion字段的值进行配置，规则如下：
  + 针对HarmonyOS工程，"compatibleSdkVersion"："M.S.F(N)"，"-DOHOS\_COMPATIBLE\_SDK\_VERSION=N.0.0"。
  + 针对OpenHarmony工程，"compatibleSdkVersion"：N，"-DOHOS\_COMPATIBLE\_SDK\_VERSION=N.0.0"。
  + 示例：工程级build-profile.json5文件中的compatibleSdkVersion配置的版本号为6.0.2(22)，

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/2BShj5FUQTy7qUc8k5N_1Q/zh-cn_image_0000002550606910.png?HW-CC-KV=V1&HW-CC-Date=20260427T233716Z&HW-CC-Expire=86400&HW-CC-Sign=447C42547FFBF701E0DF4AC0069A3C36882BAC14F59238742F0F5EA314A58BD7)

模块级build-profile.json5配置文件中增加编译参数 "arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=22.0.0"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/hQ954pfYTiqADgU6sKHLwA/zh-cn_image_0000002581206647.png?HW-CC-KV=V1&HW-CC-Date=20260427T233716Z&HW-CC-Expire=86400&HW-CC-Sign=E5B37E93A83F5979E9F1FA283932F99BE5E69B85628B7C7176ADC324AB97C3F4)

* **场景2：DevEco Studio版本高于 6.0.2.650 Release（API 22 Release）时：**

  会自动根据工程级 build-profile.json5 文件中的 compatibleSdkVersion 配置来进行兼容性判断，不需要额外在entry目录下的build-profile.json5配置文件中配置 "arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x"；如果已经存在"arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x"配置，必须保证版本号和compatibleSdkVersion同步更新，其中x.x.x版本号根据工程级build-profile.json5文件中的compatibleSdkVersion字段的值进行配置，规则如下：
  + 针对HarmonyOS工程，"compatibleSdkVersion"："M.S.F(N)"，"-DOHOS\_COMPATIBLE\_SDK\_VERSION=N.0.0"。
  + 针对OpenHarmony工程，"compatibleSdkVersion"：N，"-DOHOS\_COMPATIBLE\_SDK\_VERSION=N.0.0"。
* **场景3：非Hvigor方式构建Hap包**：

  非Hvigor方式构建Hap包场景下，例如bazel，需要开发者传递"--target=aarch64-linux-ohosx.x.x"和"-Wunguarded-availability"编译选项给llvm，同时增加依赖库libdeviceinfo\_ndk.z.so，参数中的版本号x.x.x是根据工程级 build-profile.json5 文件中 compatibleSdkVersion 配置的版本号来配置的。

  其中x.x.x版本号根据工程级build-profile.json5文件中的compatibleSdkVersion字段的值进行配置，规则如下：
  + 针对HarmonyOS工程，"compatibleSdkVersion"："M.S.F(N)"，"--target=aarch64-linux-ohosN.0.0"。
  + 针对OpenHarmony工程，"compatibleSdkVersion"：N，"--target=aarch64-linux-ohosN.0.0"。

    补充说明：

    Hvigor方式构建Hap包：**通过Hvigor把**compatibleSdkVersion版本号转换为"arguments": "-DOHOS\_COMPATIBLE\_SDK\_VERSION=x.x.x" 参数传递给cmake，cmake解析后转换为 "--target=aarch64-linux-ohosx.x.x"编译选项传递给llvm编译器，同时增加编译选项："-Wunguarded-availability"和增加依赖库libdeviceinfo\_ndk.z.so，在llvm编译器中编译阶段和运行时阶段进行判断，最终进行API兼容性判断保护。

具体传递过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ap6Jij5QTTKy1Vejycz8mg/zh-cn_image_0000002550766556.png?HW-CC-KV=V1&HW-CC-Date=20260427T233716Z&HW-CC-Expire=86400&HW-CC-Sign=6DE65E31A4F46A7D341DB46B9AE81F018211238EEA07459664F07068A2B92325)

**步骤2** 兼容性保护。

* 针对HarmonyOS独有特性接口，即接口标记为since M.S.F(N)（文档中标记“起始版本：M.S.F(N)”, SDK物理包中hms路径下所包含的接口），使用APIAVAILABLE接口进行进行兼容性判断保护。

  接口声明：

  ```
  1. /**
  2. * @brief Query Device Security Mode.
  3. *
  4. * This method is used to query device security mode.
  5. *
  6. * @return Current device security mode, see {@link DSM_DeviceSecurityMode}.
  7. * @since 5.0.1(13)
  8. */
  9. DSM_DeviceSecurityMode HMS_DSM_GetDeviceSecurityMode(void);
  ```

  使用APIAVAILABLE进行兼容性保护：

  ```
  1. if (APIAVAILABLE(13,0,0)) {
  2. // 调用5.0.1(13)的API接口
  3. HMS_DSM_GetDeviceSecurityMode();
  4. } else {
  5. // 降级方案
  6. }
  ```

* 针对OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用APIAVAILABLE接口进行进行兼容性判断保护。

  接口声明：

  ```
  1. /**
  2. * @brief Start locating and subscribe location changed.
  3. *
  4. * @param requestConfig - Pointer to the locating request parameters.\n
  5. * For details, see {@link Location_RequestConfig}.\n
  6. * You can use {@link OH_Location_CreateRequestConfig} to create an instance.\n
  7. * @return Location functions result code.\n
  8. *     For a detailed definition, please refer to {@link Location_ResultCode}.\n
  9. *     {@link LOCAION_SUCCESS} Successfully start locating.\n
  10. *     {@link LOCATION_INVALID_PARAM} The input parameter requestConfig is a null pointer.\n
  11. *     {@link LOCATION_PERMISSION_DENIED} Permission verification failed. The application does not have the\n
  12. *         permission required to call the API.\n
  13. *     {@link LOCATION_NOT_SUPPORTED} Capability not supported.\n
  14. *         Failed to call function due to limited device capabilities.\n
  15. *     {@link LOCATION_SERVICE_UNAVAILABLE} Abnormal startup of location services.\n
  16. *     {@link LOCATION_SWITCH_OFF} The location switch is off.\n
  17. * @permission ohos.permission.APPROXIMATELY_LOCATION
  18. * @since 13
  19. */
  20. Location_ResultCode OH_Location_StartLocating(const Location_RequestConfig* requestConfig);
  ```

  使用APIAVAILABLE进行兼容性保护：

  ```
  1. if (APIAVAILABLE(13,0,0)) {
  2. // 调用13的API接口
  3. OH_Location_StartLocating(requestConfig);
  4. } else {
  5. // 降级方案
  6. }
  ```

## 通过动态加载so和调用dlsym接口消除

示例如下：

```
1. void *handle = NULL; // 库的句柄
2. Location_ResultCode (*OH_Location_StartLocating_Test)(const Location_RequestConfig *); // 函数指针
3. OH_Location_StartLocating_Test = NULL;
4. handle = dlopen("liblocation_ndk.so", RTLD_LAZY);
5. if (handle != NULL) {
6. OH_Location_StartLocating_Test =
7. (Location_ResultCode(*)(const Location_RequestConfig *))dlsym(handle, "OH_Location_StartLocating");
8. if (OH_Location_StartLocating_Test != NULL) {
9. OH_LOG_INFO(LOG_APP, "OH_Location_StartLocating != NULL");
10. } else {
11. OH_LOG_INFO(LOG_APP, "OH_Location_StartLocating = NULL");
12. }
13. } else {
14. OH_LOG_INFO(LOG_APP, "handle = NULL");
15. }
```
