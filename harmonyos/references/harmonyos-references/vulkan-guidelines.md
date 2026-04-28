---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-guidelines
title: Vulkan Surface开发指导
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan开发指导 > Vulkan Surface开发指导
category: harmonyos-references
scraped_at: 2026-04-28T08:19:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1565fdbc34721768088079f86f83a50be4f13efea8d40969c125a51e556dc974
---

## 场景介绍

在HarmonyOS中，扩展VK\_OHOS\_surface相关的API创建出来的VkSurfaceKHR会对接到本机窗口（OHNativeWindow）模块，实现本机缓冲区（OHNativeBuffer）的轮转，用于屏幕显示。

创建VkSurfaceKHR对象需要通过OHNativeWindow，而OHNativeWindow需要从XComponent中获取，所以此场景下需要配合XComponent模块和NativeWindow模块一起使用。XComponent模块的具体使用方法请参考[XComponent开发指导](../harmonyos-guides/napi-xcomponent-guidelines.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| vkCreateSurfaceOHOS (VkInstance instance, const VkSurfaceCreateInfoOHOS\* pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface) | 创建VkSurfaceKHR对象。 |

更多的接口说明请参考[Vulkan](vulkan.md)。

## 开发步骤

以下步骤说明了如何创建一个VkSurfaceKHR对象。

**HarmonyOS平台宏**

使用平台扩展的接口，需要定义一个宏VK\_USE\_PLATFORM\_OHOS，我们在CMakeLists.txt定义这个宏。

```
1. ADD_DEFINITIONS(-DVK_USE_PLATFORM_OHOS=1)
```

**添加动态链接库**

CMakeLists.txt中添加Vulkan的lib和周边模块的lib。

```
1. libvulkan.so
2. libace_ndk.z.so
3. libnative_window.so
4. libnative_image.so
5. libnative_buffer.so
```

说明

在程序中通过dlopen函数链接libvulkan.so动态库时不需要在CMake中增加依赖，否则会导致符号冲突。

**头文件**

```
1. #include <ace/xcomponent/native_interface_xcomponent.h>
2. #include <native_window/external_window.h>
3. #include <vulkan/vulkan.h>
```

1. **首先需要创建一个Vulkan实例**。

   ```
   1. VkInstance instance = VK_NULL_HANDLE;

   3. VkApplicationInfo appInfo = {};
   4. appInfo.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO;
   5. appInfo.pApplicationName = "vulkanExample";
   6. appInfo.pEngineName = "vulkanExample";
   7. appInfo.apiVersion = VK_API_VERSION_1_3;

   9. VkInstanceCreateInfo instanceCreateInfo = {};
   10. instanceCreateInfo.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO;
   11. instanceCreateInfo.pNext = NULL;
   12. instanceCreateInfo.pApplicationInfo = &appInfo;

   14. std::vector<const char *> instanceExtensions = {
   15. VK_KHR_SURFACE_EXTENSION_NAME,
   16. VK_OHOS_SURFACE_EXTENSION_NAME // Surface扩展
   17. };
   18. instanceCreateInfo.enabledExtensionCount = static_cast<uint32_t>(instanceExtensions.size());
   19. instanceCreateInfo.ppEnabledExtensionNames = instanceExtensions.data();

   21. vkCreateInstance(&instanceCreateInfo, nullptr, &instance);
   ```
2. **获取OHNativeWindow**。

   OHNativeWindow需要从XComponent组件中获取，下面提供一份从XComponent组件中获取OHNativeWindow的代码示例，XComponent模块的具体使用方法请参考[XComponent模块的介绍文档](../harmonyos-guides/napi-xcomponent-guidelines.md)。

   1. ets/pages/Index.ets中增加一个XComponent组件。

      ```
      1. XComponent({
      2. id: 'xcomponentId',
      3. type: 'surface',
      4. libraryname: 'entry'
      5. })
      6. .margin({ bottom: 20 })
      7. .width(360)
      8. .height(360)
      ```
   2. 从XComponent组件中获取OHNativeWindow。

      ```
      1. // XComponent在创建Surface时的回调函数
      2. void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window) {
      3. // 在回调函数里可以拿到OHNativeWindow
      4. OHNativeWindow *nativeWindow = static_cast<OHNativeWindow *>(window);
      5. }

      7. static napi_value Init(napi_env env, napi_value exports) {
      8. napi_property_descriptor desc[] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr}};
      9. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);

      11. napi_value exportInstance = nullptr;
      12. OH_NativeXComponent *nativeXComponent = nullptr;
      13. // 获取nativeXComponent
      14. napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance);
      15. napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent));
      16. // 获取XComponentId
      17. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {};
      18. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
      19. OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize);

      21. // 声明一个XComponent的Callback
      22. OH_NativeXComponent_Callback callback;
      23. // 注册OnSurfaceCreated回调函数
      24. callback.OnSurfaceCreated = OnSurfaceCreatedCB;
      25. // 将callback注册给nativeXComponent
      26. OH_NativeXComponent_RegisterCallback(nativeXComponent, &callback);

      28. return exports;
      29. }
      ```
3. **创建VkSurfaceKHR对象**。

   ```
   1. VkSurfaceKHR surface = VK_NULL_HANDLE;
   2. VkSurfaceCreateInfoOHOS surfaceCreateInfo = {};
   3. surfaceCreateInfo.sType = VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS;
   4. surfaceCreateInfo.window = nativeWindow; // 这里的nativeWindow就是从上一步骤OnSurfaceCreatedCB回调函数中拿到的
   5. int err = vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, NULL, &surface);
   6. if (err != VK_SUCCESS) {
   7. // Create Surface Failed.
   8. }
   ```
