---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-53
title: 初次授权后相机不显示图像
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 初次授权后相机不显示图像
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:24259408d3dc98ee3f2fb1e37f1f73e561b427c9676f0bfb3fcd2a1fa4a8e8d9
---

## 问题现象

初次授权后相机不显示图像，重启应用后生效。

## 背景知识

* 相机开发模型为Surface模型，该模型主要通过Surface实现数据交互。在开发相机应用界面时，首先需要通过创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件为预览流提供Surface，再通过获取[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件对应Surface的ID创建预览流，预览流画面即可直接在[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件内渲染。
* [PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)：此次权限申请的结果。
* authResults：相应请求权限的结果。
  + -1：未授权。dialogShownResults返回为true，表示用户首次申请；dialogShownResults返回为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。
  + 0：已授权。
  + 2：未授权，表示请求无效。

## 问题定位

1. 在HiLog日志中搜索XComponent发现应用通过native初始化了相机的预览画面。

   ```txt
   21:46:12.532   10809-10809   C03931/com.exa...AceXcomponent  com.example.hm  I     [(100000:100000:scope)] XComponent[previewWindow] native OnSurfaceCreated
   ```
2. 根据日志时间发现XComponent初始化时机早于授权弹窗。

   ```txt
   21:46:12.764   11213-11213   A05612/commonUI/ASP             com.huawe...commonUI  I     [SPC][PermissionDialog][ViewModel]: group: CAMERA, title: 允许“demo”访问你的相机？, reason: 拍照.
   ```

## 分析结论

由于XComponent加载native实现的时机早于系统授权弹窗，导致相机初始化未完成，导致预览画面无法显示。

## 修改建议

在初次授权时，重新调用相机的初始化流程。可以通过授权返回结果中dialogShownResults的值是否为true，判断当前是否是初次授权弹窗状态。

```ts
getPermission(permissions: Permissions[]): Promise<boolean> {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  let context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
  return new Promise((resolve) => {
    atManager.requestPermissionsFromUser(context, permissions,
      (err: BusinessError, data: PermissionRequestResult) => {
        if (err) {
          console.log(`previewstreamsdemotest requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
          return resolve(false);
        } else {
          console.info('PermissionRequestResult data:' + JSON.stringify(data));
          if (data.authResults[0] != 0) {
            return resolve(false);
          }

          // 第一次授权时候切换通道
          if (data.dialogShownResults !== undefined &&
            data.dialogShownResults[0] === true &&
            data.authResults[0] === 0) {
            console.info('previewstreamsdemotest 已切换摄像头通道');
            this.PreviewCamera.switchChannel();
            this.channelId = this.PreviewCamera.GETCHANNELID();
            this.channelWidth = this.PreviewCamera.GETCHANNELWIDTH();
            this.channelHeight = this.PreviewCamera.GETCHANNELHEIGHT();
          }
          return resolve(true);
        }
      });
  });
}
```

* 初次授权时的打印结果，authResults结果为0，dialogShownResults结果为true：

  PermissionRequestResult data:{"permissions":["ohos.permission.CAMERA"],"authResults":[0],"dialogShownResults":[true]}
* 初次拒绝授权时的打印结果，authResults结果为-1，dialogShownResults结果为true：

  PermissionRequestResult data:{"permissions":["ohos.permission.CAMERA"],"authResults":[-1],"dialogShownResults":[true]}
* 授权后重启应用的打印结果，authResults结果为0，dialogShownResults结果为false：

  PermissionRequestResult data:{"permissions":["ohos.permission.CAMERA"],"authResults":[0],"dialogShownResults":[false]}

完整代码示例如下：

* Index.d.ts导出文件：

  ```ts
  export const add: (a: number, b: number) => number;
  export const switchChannel: () => void;
  export  const GETCHANNELID: () => number;
  export const GETCHANNELWIDTH: () => number;
  export const GETCHANNELHEIGHT: () => number;
  ```
* ArkTS侧实现：

  ```ts
  import abilityAccessCtrl, { Context, PermissionRequestResult, Permissions } from '@ohos.abilityAccessCtrl';
  import { BusinessError } from '@ohos.base';
  import common from '@ohos.app.ability.common';
  import camera from '@ohos.multimedia.camera';

  @Entry
  @Component
  struct Index {
    previewController: XComponentController = new XComponentController;
    photoController: XComponentController = new XComponentController;
    surfaceId: string = '';
    isUserAgent: boolean = false;
    uiContext = this.getUIContext();
    @State channelId: number = 0;
    @State channelWidth: number = 480;
    @State channelHeight: number = 480;
    pixelMap: PixelMap | undefined = undefined;
    photoOutput: camera.PhotoOutput | undefined = undefined;
    private PreviewCamera: ESObject;
    private isAuthorized: boolean = false;

    getPermission(permissions: Permissions[]): Promise<boolean> {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      let context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
      return new Promise((resolve) => {
        atManager.requestPermissionsFromUser(context, permissions,
          (err: BusinessError, data: PermissionRequestResult) => {
            if (err) {
              console.log(`previewstreamsdemotest requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
              return resolve(false);
            } else {
              console.info('PermissionRequestResult data:' + JSON.stringify(data));
              if (data.authResults[0] != 0) {
                return resolve(false);
              }

              // 第一次授权时候切换通道
              if (data.dialogShownResults !== undefined &&
                data.dialogShownResults[0] === true &&
                data.authResults[0] === 0) {
                console.info('previewstreamsdemotest 已切换摄像头通道');
                this.PreviewCamera.switchChannel();
                this.channelId = this.PreviewCamera.GETCHANNELID();
                this.channelWidth = this.PreviewCamera.GETCHANNELWIDTH();
                this.channelHeight = this.PreviewCamera.GETCHANNELHEIGHT();
              }
              return resolve(true);
            }
          });
      });
    }

    aboutToAppear(): void {
      //user_grant用户授权
      this.getPermission(['ohos.permission.CAMERA']).then(async (res) => {
        if (!res) {
          this.isAuthorized = false;
          let context = this.uiContext.getHostContext() as common.UIAbilityContext;
          context.startAbility({
            bundleName: 'com.huawei.hmos.settings',
            abilityName: 'com.huawei.hmos.settings.MainAbility',
            uri: 'application_info_entry', //application_settings application_info_entry systemui_notification_settings
            parameters: {
              pushParams: 'com.example.previewstreamsdemo'
            }
          });
          return;
        }
        this.isAuthorized = true;
      });
    }

    aboutToDisappear(): void {
    }

    build() {
      Column() {
        XComponent({
          id: 'previewWindow',
          type: XComponentType.SURFACE,
          libraryname: 'entry',
          controller: this.previewController,
        })
          .onLoad((es: ESObject) => {
            this.PreviewCamera = es;
            let a: SurfaceRect = {
              offsetX: 10, // X 偏移量
              offsetY: 20, // Y 偏移量
              surfaceWidth: 1080, // Surface 宽度
              surfaceHeight: 1440 // Surface 高度//
            };
            this.previewController.setXComponentSurfaceRect(a);
            console.info('sf test XComponent has been inited');
          })
          .width('1080px')
          .height('1440px');

        Button('切换摄像头通道').onClick(() => {
          console.info('已切换摄像头通道');
          if (this.isAuthorized) {
            this.PreviewCamera.switchChannel();
            this.channelId = this.PreviewCamera.GETCHANNELID();
            this.channelWidth = this.PreviewCamera.GETCHANNELWIDTH();
            this.channelHeight = this.PreviewCamera.GETCHANNELHEIGHT();
            let a = this.previewController.getXComponentSurfaceRect();
            console.info('sf test' + a.surfaceWidth.toString());
          }

        });
        Text('通道:' + this.channelId);
        Text('通道像素宽度:' + this.channelWidth);
        Text('通道像素高度:' + this.channelHeight);
      }.justifyContent(FlexAlign.SpaceAround)
      .height('100%')
      .width('100%');
    }
  }
  ```
* C/C++侧实现：
  + napi\_init.cpp:

    ```
    /*
     * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
     */
    #include <stdio.h>
    #include <stdlib.h>
    #include <ace/xcomponent/native_interface_xcomponent.h>
    #include "napi/native_api.h"
    #include "hilog/log.h"
    #include "camera.h"

    #undef LOG_DOMAIN
    #undef LOG_TAG
    #define LOG_DOMAIN 0x3200 // 全局domain宏，标识业务领域
    #define LOG_TAG "MY_TAG"  // 全局tag宏，标识模块日志tag

    NDKCamera *g_camera;

    static napi_value Add(napi_env env, napi_callback_info info)
    {
        size_t argc = 2;
        napi_value args[2] = {nullptr};

        napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

        napi_valuetype valuetype0;
        napi_typeof(env, args[0], &valuetype0);

        napi_valuetype valuetype1;
        napi_typeof(env, args[1], &valuetype1);

        double value0;
        napi_get_value_double(env, args[0], &value0);

        double value1;
        napi_get_value_double(env, args[1], &value1);

        napi_value sum;
        napi_create_double(env, value0 + value1, &sum);

        return sum;
    }

    static napi_value switchChannel(napi_env env, napi_callback_info info)
    {
        if (g_camera == nullptr) {
            g_camera = NDKCamera::GetInstance();
            if (g_camera == nullptr) {
                return nullptr;
            }
        }
        g_camera->SwitchPreviewChannel();
        return nullptr;
    }

    static napi_value GETCHANNELID(napi_env env, napi_callback_info info)
    {
        napi_value napi_id;
        int32_t id;
        if (g_camera == nullptr) {
            g_camera = NDKCamera::GetInstance();
            if (g_camera == nullptr) {
                return nullptr;
            }
        }
        id = g_camera->GETCHANNELID();
        if (napi_ok != napi_create_int32(env, id, &napi_id)) {
            OH_LOG_ERROR(LOG_APP, "GETCHANNELID:napi_create_int32 failed");
            return nullptr;
        }

        return napi_id;
    }

    static napi_value GETCHANNELWIDTH(napi_env env, napi_callback_info info)
    {
        napi_value napi_width;
        int32_t width;
        if (g_camera == nullptr) {
            g_camera = NDKCamera::GetInstance();
            if (g_camera == nullptr) {
                return nullptr;
            }
        }
        width = g_camera->GETCHANNELWIDTH();
        if (napi_ok != napi_create_int32(env, width, &napi_width)) {
            OH_LOG_ERROR(LOG_APP, "GETCHANNELWIDTH:napi_create_int32 failed");
            return nullptr;
        }

        return napi_width;
    }

    static napi_value GETCHANNELHEIGHT(napi_env env, napi_callback_info info)
    {
        napi_value napi_height;
        int32_t height;
        if (g_camera == nullptr) {
            g_camera = NDKCamera::GetInstance();
            if (g_camera == nullptr) {
                return nullptr;
            }
        }
        height = g_camera->GETCHANNELHEIGHT();
        if (napi_ok != napi_create_int32(env, height, &napi_height)) {
            OH_LOG_ERROR(LOG_APP, "GETCHANNELHEIGHT:napi_create_int32 failed");
            return nullptr;
        }

        return napi_height;
    }

    EXTERN_C_START
    static napi_value Init(napi_env env, napi_value exports)
    {
        napi_property_descriptor desc[] = {
            {"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
            {"switchChannel", nullptr, switchChannel, nullptr, nullptr, nullptr, napi_default, nullptr},
            {"GETCHANNELID", nullptr, GETCHANNELID, nullptr, nullptr, nullptr, napi_default, nullptr},
            {"GETCHANNELWIDTH", nullptr, GETCHANNELWIDTH, nullptr, nullptr, nullptr, napi_default, nullptr},
            {"GETCHANNELHEIGHT", nullptr, GETCHANNELHEIGHT, nullptr, nullptr, nullptr, napi_default, nullptr},
        };
        napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);

        napi_value exportInstance = nullptr;
        // 用来解析出被wrap了NativeXComponent指针的属性
        napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance);
        OH_NativeXComponent *nativeXComponent = nullptr;
        // 通过napi_unwrap接口，解析出NativeXComponent的实例指针
        napi_unwrap(env, exportInstance, reinterpret_cast<void **>(&nativeXComponent));
        // 获取XComponentId
        char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {};
        uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
        OH_NativeXComponent_GetXComponentId(nativeXComponent, idStr, &idSize);

        OH_NativeXComponent_Callback *callback = new OH_NativeXComponent_Callback();
        callback->OnSurfaceCreated = OnSurfaceCreatedCB;
        callback->OnSurfaceChanged = OnSurfaceChangedCB;
        callback->OnSurfaceDestroyed = OnSurfaceDestroyedCB;
        callback->DispatchTouchEvent = DispatchTouchEventCB;

        // 注册回调函数
        OH_NativeXComponent_RegisterCallback(nativeXComponent, callback);
        g_camera = NDKCamera::GetInstance();
        return exports;
    }
    EXTERN_C_END

    static napi_module demoModule = {
        .nm_version = 1,
        .nm_flags = 0,
        .nm_filename = nullptr,
        .nm_register_func = Init,
        .nm_modname = "entry",
        .nm_priv = ((void *)0),
        .reserved = {0},
    };

    extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
    ```
  + camera.cpp:

    ```
    /*
     * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
     */
    #include <cstdint>
    #include <cstring>
    #include <sstream>
    #include <sys/mman.h>
    #include <accesstoken/ability_access_control.h>
    #include "hilog/log.h"
    #include "camera.h"

    #undef LOG_DOMAIN
    #undef LOG_TAG
    #define LOG_DOMAIN 0x3200 // 全局domain宏，标识业务领域
    #define LOG_TAG "MY_TAG"  // 全局tag宏，标识模块日志tag

    OHNativeWindow *g_nativeWindow = nullptr;

    void CaptureSessionOnFocusStateChange(Camera_CaptureSession *session, Camera_FocusState focusState)
    {
        OH_LOG_INFO(LOG_APP, "CaptureSessionOnFocusStateChange");
    }

    void CaptureSessionOnError(Camera_CaptureSession *session, Camera_ErrorCode errorCode)
    {
        OH_LOG_INFO(LOG_APP, "CaptureSessionOnError = %{public}d", errorCode);
    }

    CaptureSession_Callbacks *GetCaptureSessionRegister(void)
    {
        static CaptureSession_Callbacks captureSessionCallbacks = {.onFocusStateChange = CaptureSessionOnFocusStateChange,
                                                                   .onError = CaptureSessionOnError};
        return &captureSessionCallbacks;
    }

    void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput)
    {
        OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
    }

    void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount)
    {
        OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
    }

    void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode)
    {
        OH_LOG_INFO(LOG_APP, "PreviewOutputOnError = %{public}d", errorCode);
    }

    PreviewOutput_Callbacks *GetPreviewOutputListener(void)
    {
        static PreviewOutput_Callbacks previewOutputListener = {.onFrameStart = PreviewOutputOnFrameStart,
                                                                .onFrameEnd = PreviewOutputOnFrameEnd,
                                                                .onError = PreviewOutputOnError};
        return &previewOutputListener;
    }

    void OnCameraInputError(const Camera_Input *cameraInput, Camera_ErrorCode errorCode)
    {
        OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode = %{public}d", errorCode);
    }

    CameraInput_Callbacks *GetCameraInputListener(void)
    {
        static CameraInput_Callbacks cameraInputCallbacks = {.onError = OnCameraInputError};
        return &cameraInputCallbacks;
    }

    void CameraManagerStatusCallback(Camera_Manager *cameraManager, Camera_StatusInfo *status)
    {
        OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
    }

    CameraManager_Callbacks *GetCameraManagerListener()
    {
        static CameraManager_Callbacks cameraManagerListener = {.onCameraStatus = CameraManagerStatusCallback};
        return &cameraManagerListener;
    }

    // YUV到RGB的转换公式
    int YUV2RGBA(unsigned char y, unsigned char u, unsigned char v)
    {
        unsigned char r = 0;
        unsigned char g = 0;
        unsigned char b = 0;

        r = (unsigned char)(y + 1.4075 * (v - 128));
        g = (unsigned char)(y - 0.34455 * (u - 128) - 0.7169 * (v - 128));
        b = (unsigned char)(y + 1.779 * (u - 128));

        // 构建RGBA整数值
        return (0xff << 24) | (int)(r << 16) | (int)(g << 8) | (int)b;
    }

    // 将YUV420数据转换为RGBA整数值
    void YUV420ToRGBAInt(unsigned char *src, int *dst, int width, int height, int stride)
    {
        unsigned char *pY = src;
        unsigned char *pU = src + width * height;

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                unsigned char u = pU[(y / 2) * width + (x / 2) * 2];
                unsigned char v = pU[(y / 2) * width + (x / 2) * 2 + 1];
                dst[y * stride + x] = YUV2RGBA(pY[y * width + x], u, v);
            }
        }
    }

    static void OnCallback(OH_ImageReceiverNative *receiver)
    {
        int32_t yStride, uStride, vStride, sWidth, sHeight;

        // 读取 OH_ImageReceiverNative 的下一个图片对象
        OH_ImageNative *image = nullptr;
        OH_ImageReceiverNative_ReadNextImage(receiver, &image);

        // 读取 OH_ImageNative 的 size 属性
        Image_Size size;
        OH_ImageNative_GetImageSize(image, &size);
        sWidth = size.width;
        sHeight = size.height;
        OH_LOG_ERROR(LOG_APP, "size [%{public}s]:[%{public}u],sWidth [%{public}d],sHeight [%{public}d]", __FUNCTION__,
                     __LINE__, sWidth, sHeight);

        // 读取 OH_ImageNative 的组件列表的元素个数。
        size_t componentTypeSize = 0;
        OH_ImageNative_GetComponentTypes(image, nullptr, &componentTypeSize);

        // 读取 OH_ImageNative 的组件列表。
        uint32_t *componentTypes = new uint32_t[componentTypeSize];
        OH_ImageNative_GetComponentTypes(image, &componentTypes, &componentTypeSize);

        uint32_t component = componentTypes[0];

        // 读取 OH_ImageNative 的第一个组件所对应的缓冲区对象。
        OH_NativeBuffer *nativeBuffer = nullptr;
        OH_ImageNative_GetByteBuffer(image, component, &nativeBuffer);

        OH_ImageNative_GetRowStride(image, component, &yStride);
        uStride = yStride;
        vStride = yStride;

        void *srcVir = nullptr;
        OH_NativeBuffer_Map(nativeBuffer, &srcVir);
        uint8_t *srcBuffer = static_cast<uint8_t *>(srcVir);

        if (yStride != size.width) {
            // 传给其他支持stride的接口处理，或去除stride数据
            // 去除stride数据示例:将byteBuffer中的数据去除stride，拷贝得到新的dstBuffer数据
            size_t dstBufferSize = size.width * size.height * 1.5; // 相机预览流返回NV21格式
            std::unique_ptr<uint8_t[]> dstBuffer = std::make_unique<uint8_t[]>(dstBufferSize);
            uint8_t *dstPtr = dstBuffer.get();
            for (int j = 0; j < size.height * 1.5; j++) {
                std::copy_n(static_cast<const uint8_t*>(srcBuffer), size.width, static_cast<uint8_t*>(dstPtr));
                dstPtr += size.width;
                srcBuffer += yStride;
            }
            srcBuffer = dstBuffer.get();
        }

        OH_LOG_ERROR(LOG_APP, "local [%{public}s]:[%{public}u],sWidth [%{public}d],yStride [%{public}d]", __FUNCTION__,
                     __LINE__, sWidth, yStride);

        OHNativeWindow *nativeWindow;
        OH_LOG_ERROR(LOG_APP, "local [%{public}s]:[%{public}u], [%{public}p]", __FUNCTION__, __LINE__, g_nativeWindow);

        // 设置 OHNativeWindowBuffer 的宽高
        int32_t code = SET_BUFFER_GEOMETRY;
        // 这里的nativeWindow是从上一步骤中的回调函数中获得的
        int32_t ret = OH_NativeWindow_NativeWindowHandleOpt(g_nativeWindow, code, sWidth, sHeight);

        code = GET_BUFFER_GEOMETRY;
        int32_t h, w;
        // 这里的nativeWindow是从上一步骤中的回调函数中获得的
        ret = OH_NativeWindow_NativeWindowHandleOpt(g_nativeWindow, code, &h, &w);
        OH_LOG_ERROR(LOG_APP, "local H W[%{public}s]:[%{public}u], [%{public}d]  [%{public}d]", __FUNCTION__, __LINE__, h,
                     w);

        code = SET_TRANSFORM;
        int32_t transform = NATIVEBUFFER_ROTATE_270;
        ret = OH_NativeWindow_NativeWindowHandleOpt(g_nativeWindow, code, transform);

        OHNativeWindowBuffer *buffer = nullptr;
        int releaseFenceFd = -1;
        // 通过 OH_NativeWindow_NativeWindowRequestBuffer 获取 OHNativeWindowBuffer 实例
        ret = OH_NativeWindow_NativeWindowRequestBuffer(g_nativeWindow, &buffer, &releaseFenceFd);
        if (ret != 0 || buffer == nullptr) {
            return;
        }
        // 通过 OH_NativeWindow_GetBufferHandleFromNative 获取 buffer 的 handle
        BufferHandle *bufferHandle = OH_NativeWindow_GetBufferHandleFromNative(buffer);
        // 使用系统接口mmap将bufferHandle对应的共享内存映射到用户空间，可以通过映射出来的虚拟地址向bufferHandle中写入图像数据
        // bufferHandle->virAddr是bufferHandle在共享内存中的起始地址，bufferHandle->size是bufferHandle在共享内存中的内存占用大小
        void *mappedAddr =
            mmap(bufferHandle->virAddr, (bufferHandle->size), PROT_READ | PROT_WRITE, MAP_SHARED, bufferHandle->fd, 0);
        if (mappedAddr == MAP_FAILED) {
            return;
        }

        OH_LOG_ERROR(LOG_APP, "local size [%{public}s]:[%{public}u], [%{public}d]", __FUNCTION__, __LINE__,
                     (bufferHandle->size));

        YUV420ToRGBAInt(srcBuffer, (int *)mappedAddr, sWidth, sHeight, bufferHandle->stride / 4);

        // 设置刷新区域，如果Region中的Rect为nullptr,或者rectNumber为0，则认为OHNativeWindowBuffer全部有内容更改。
        Region region{nullptr, 0};
        // 通过OH_NativeWindow_NativeWindowFlushBuffer提交给消费者使用，例如：显示在屏幕上。
        OH_NativeWindow_NativeWindowFlushBuffer(g_nativeWindow, buffer, -1, region);

        // 内存使用完记得去掉内存映射
        int result = munmap(mappedAddr, (bufferHandle->size));
        if (result == -1) {
            return;
        }

        OH_NativeBuffer_Unmap(nativeBuffer);
        int errCode = OH_ImageNative_Release(image);
        OH_LOG_ERROR(LOG_APP, "zhulin local [%{public}s]:[%{public}u], [%{public}d] ok", __FUNCTION__, __LINE__, errCode);
    }
    NDKCamera *g_ndkCamera = nullptr;
    NDKCameraErrorCode NDKCamera::Init()
    {
        uint32_t size = 0;

        // 创建CameraManager对象
        Camera_ErrorCode ret = OH_Camera_GetCameraManager(&_cameraManager);
        if (_cameraManager == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraMananger failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }
        // 监听相机状态变化
        ret = OH_CameraManager_RegisterCallback(_cameraManager, GetCameraManagerListener());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
            return ERROR_FAILED;
        }

        // 获取相机列表
        ret = OH_CameraManager_GetSupportedCameras(_cameraManager, &_cameras, &size);
        if (_cameras == nullptr || size < 0 || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
            return ERROR_FAILED;
        }

        for (int i = 0; i < size; i++) {
            OH_LOG_ERROR(
                LOG_APP,
                "OH_CameraManager_GetSupportedCameras camera %{public}d.Pos: %{public}d,Type: %{public}d,Conn:  %{public}d",
                i, _cameras[i].cameraPosition, _cameras[i].cameraType, _cameras[i].connectionType);
        }

        // 创建相机输入流
        ret = OH_CameraManager_CreateCameraInput(_cameraManager, &_cameras[cameraDeviceIndex], &_cameraInput);
        if (_cameraInput == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
            return ERROR_FAILED;
        }

        // 监听cameraInput错误信息
        ret = OH_CameraInput_RegisterCallback(_cameraInput, GetCameraInputListener());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
            return ERROR_FAILED;
        }

        // 打开相机
        ret = OH_CameraInput_Open(_cameraInput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Open failed.");
            return ERROR_FAILED;
        }

        // 获取相机设备支持的输出流能力
        ret = OH_CameraManager_GetSupportedCameraOutputCapability(_cameraManager, &_cameras[cameraDeviceIndex],
                                                                  &_cameraOutputCapability);
        if (_cameraOutputCapability == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
            return ERROR_FAILED;
        }

        uint32_t cameraOrientitaion;
        ret = OH_CameraDevice_GetCameraOrientation(&_cameras[cameraDeviceIndex], &cameraOrientitaion);

        if (_cameraOutputCapability->previewProfilesSize < 0) {
            OH_LOG_ERROR(LOG_APP, "previewProfilesSize == null");
            return ERROR_FAILED;
        }
        for (int i = 0; i < _cameraOutputCapability->previewProfilesSize; i++) {
            OH_LOG_INFO(LOG_APP, "%{public}d: previewProfile width:%{public}d height:%{public}d format:%{public}d ", i,
                        _cameraOutputCapability->previewProfiles[i]->size.width,
                        _cameraOutputCapability->previewProfiles[i]->size.height,
                        _cameraOutputCapability->previewProfiles[i]->format);
            if (CAMERA_FORMAT_YUV_420_SP == _cameraOutputCapability->previewProfiles[i]->format) {
                previewProfile = _cameraOutputCapability->previewProfiles[i];
            }
        }

        for (int i = 0; i < _cameraOutputCapability->photoProfilesSize; i++) {
            OH_LOG_INFO(LOG_APP, "%{public}d: photoProfile width:%{public}d height:%{public}d format:%{public}d ", i,
                        _cameraOutputCapability->photoProfiles[i]->size.width,
                        _cameraOutputCapability->photoProfiles[i]->size.height,
                        _cameraOutputCapability->photoProfiles[i]->format);
            if (CAMERA_FORMAT_YUV_420_SP == _cameraOutputCapability->photoProfiles[i]->format) {
                previewProfile = _cameraOutputCapability->photoProfiles[i];
            }
        }

        previewProfile = _cameraOutputCapability->previewProfiles[previewProfileId];

        if (_cameraOutputCapability->photoProfilesSize < 0) {
            OH_LOG_ERROR(LOG_APP, "photoProfilesSize == null");
        }
        _photoProfile = _cameraOutputCapability->photoProfiles[photoProfileId];

        Image_ErrorCode ErrCode;
        Image_Size imageSize = {previewProfile->size.width, previewProfile->size.height};
        ErrCode = OH_ImageReceiverOptions_Create(&_options);
        if (IMAGE_SUCCESS != ErrCode) {
            OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_Create failed.ErrCode %{public}d", ErrCode);
            return ERROR_FAILED;
        }
        OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_Create success.options 0x%{public}p", _options);

        ErrCode = OH_ImageReceiverOptions_SetSize(_options, imageSize);
        if (IMAGE_SUCCESS != ErrCode) {
            OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetSize failed.ErrCode %{public}d", ErrCode);
            return ERROR_FAILED;
        }

        ErrCode = OH_ImageReceiverOptions_SetCapacity(_options, 8);
        if (IMAGE_SUCCESS != ErrCode) {
            OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetCapacity failed.ErrCode %{public}d", ErrCode);
        }

        // 读取 OH_ImageReceiverOptions 的 capacity 属性
        int32_t capacity = 0;
        ErrCode = OH_ImageReceiverOptions_GetCapacity(_options, &capacity);
        if (ErrCode != IMAGE_SUCCESS) {
            OH_LOG_ERROR(LOG_APP,
                         "ImageReceiverNativeCTest get image receiver options capacity failed, errCode: %{public}d.",
                         ErrCode);
            OH_ImageReceiverOptions_Release(_options);
            return ERROR_FAILED;
        }

        // 检查读取到的 capacity 值是否为设定值
        if (capacity != 8) {
            OH_LOG_ERROR(LOG_APP,
                         "ImageReceiverNativeCTest get image receiver options capacity failed, capacity: %{public}d.",
                         capacity);
            OH_ImageReceiverOptions_Release(_options);
            return ERROR_FAILED;
        }

        ErrCode = OH_ImageReceiverNative_Create(_options, &_receiver);
        if (IMAGE_SUCCESS != ErrCode) {
            OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_Create failed.ErrCode %{public}d", ErrCode);
        }
        OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_Create success.receiver 0x%{public}p", _receiver);

        ErrCode = OH_ImageReceiverNative_On(_receiver, OnCallback);
        if (ErrCode != IMAGE_SUCCESS) {
            OH_LOG_ERROR(LOG_APP, "ImageReceiverNativeCTest image receiver on failed, errCode: %{public}d.", ErrCode);
            OH_ImageReceiverOptions_Release(_options);
            OH_ImageReceiverNative_Release(_receiver);
            return ERROR_FAILED;
        }

        ErrCode = OH_ImageReceiverNative_GetReceivingSurfaceId(_receiver, &imageReceiverSurfaceId);
        if (ErrCode != IMAGE_SUCCESS) {
            OH_LOG_ERROR(LOG_APP,
                         "OH_ImageReceiverNative_GetReceivingSurfaceId image receiver on failed, errCode: %{public}d.",
                         ErrCode);
            OH_ImageReceiverOptions_Release(_options);
            OH_ImageReceiverNative_Release(_receiver);
            return ERROR_FAILED;
        }
        OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_GetReceivingSurfaceId imageReceiverSurfaceId %{public}lu",
                     imageReceiverSurfaceId);

        std::ostringstream surfaceIDString;
        surfaceIDString << imageReceiverSurfaceId;

        // 创建预览输出流
        ret = OH_CameraManager_CreatePreviewOutput(_cameraManager, previewProfile, surfaceIDString.str().c_str(),
                                                   &_previewOutput);
        if (previewProfile == nullptr || _previewOutput == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
            return ERROR_FAILED;
        } else {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput success.previewSurfaceId : %{public}s",
                         surfaceIDString.str().c_str());
        }

        // 监听预览输出错误信息
        ret = OH_PreviewOutput_RegisterCallback(_previewOutput, GetPreviewOutputListener());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
            return ERROR_FAILED;
        }

        // 创建会话
        ret = OH_CameraManager_CreateCaptureSession(_cameraManager, &_captureSession);
        if (_captureSession == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 监听session错误信息
        ret = OH_CaptureSession_RegisterCallback(_captureSession, GetCaptureSessionRegister());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 开始配置会话
        ret = OH_CaptureSession_BeginConfig(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 向会话中添加相机输入流
        ret = OH_CaptureSession_AddInput(_captureSession, _cameraInput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 向会话中添加预览输出流
        ret = OH_CaptureSession_AddPreviewOutput(_captureSession, _previewOutput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 提交会话配置
        ret = OH_CaptureSession_CommitConfig(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 启动会话
        ret = OH_CaptureSession_Start(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }
        return ERROR_SUCCESS;
    }

    // 定义回调函数
    void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window)
    {
        // 可获取 OHNativeWindow 实例
        g_nativeWindow = static_cast<OHNativeWindow *>(window);
        // 此回调触发后，window默认引用计数会设置为1，若存在并发使用了window相关的接口和xcompnent析构的情况，
        // 则需要通过OH_NativeWindow_NativeObjectReference和OH_NativeWindow_NativeObjectUnreference对window进行
        // 手动引用计数加1和减1，防止xcomponent析构后，并发调用window相关接口触发野指针或空指针的崩溃。
    }
    void OnSurfaceChangedCB(OH_NativeXComponent *component, void *window)
    {
        // 可获取 OHNativeWindow 实例
        g_nativeWindow = static_cast<OHNativeWindow *>(window);
        // ...
    }
    void OnSurfaceDestroyedCB(OH_NativeXComponent *component, void *window)
    {
        // 可获取 OHNativeWindow 实例
        OHNativeWindow *nativeWindow = static_cast<OHNativeWindow *>(window);
        // 此回调触发后，会将window进行引用计数减1的操作，当window的应用计数为0后，会触发window的析构，
        // window析构后，不可再通过window进行接口调用，否则可能会触发野指针或空指针的崩溃。
    }
    void DispatchTouchEventCB(OH_NativeXComponent *component, void *window)
    {
        // 可获取 OHNativeWindow 实例
        OHNativeWindow *nativeWindow = static_cast<OHNativeWindow *>(window);
        // ...
    }

    NDKCameraErrorCode NDKCamera::SwitchPreviewChannel()
    {
        Camera_ErrorCode ret;
        Image_ErrorCode ErrCode;

        if (NULL == _cameraOutputCapability) {
            return ERROR_FAILED;
        }

        if (_cameraOutputCapability->previewProfilesSize < 0) {
            OH_LOG_ERROR(LOG_APP, "previewProfilesSize == null");
            return ERROR_FAILED;
        }

        previewProfileId = (previewProfileId + 1) % _cameraOutputCapability->previewProfilesSize;
        previewProfile = _cameraOutputCapability->previewProfiles[previewProfileId];

        if (NULL == _options) {
            return ERROR_FAILED;
        }

        // 创建相机输入流
        ret = OH_CameraManager_CreateCameraInput(_cameraManager, &_cameras[cameraDeviceIndex], &_cameraInput);
        if (_cameraInput == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
            return ERROR_FAILED;
        }

        // 监听cameraInput错误信息
        ret = OH_CameraInput_RegisterCallback(_cameraInput, GetCameraInputListener());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
            return ERROR_FAILED;
        }

        // 打开相机
        ret = OH_CameraInput_Open(_cameraInput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Open failed.");
            return ERROR_FAILED;
        }

        Image_Size imageSize = {previewProfile->size.width, previewProfile->size.height};
        ErrCode = OH_ImageReceiverOptions_SetSize(_options, imageSize);
        if (IMAGE_SUCCESS != ErrCode) {
            OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetSize failed.ErrCode %{public}d", ErrCode);
            return ERROR_FAILED;
        }

        // 释放之前创建的_receiver
        OH_ImageReceiverNative_Release(_receiver);

        // 根据新的profile重新创建_receiver
        ErrCode = OH_ImageReceiverNative_Create(_options, &_receiver);
        if (IMAGE_SUCCESS != ErrCode) {
            OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_Create failed.ErrCode %{public}d", ErrCode);
            return ERROR_FAILED;
        }
        OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_Create success.receiver 0x%{public}p", _receiver);

        ErrCode = OH_ImageReceiverNative_On(_receiver, OnCallback);
        if (ErrCode != IMAGE_SUCCESS) {
            OH_LOG_ERROR(LOG_APP, "ImageReceiverNativeCTest image receiver on failed, errCode: %{public}d.", ErrCode);
            OH_ImageReceiverOptions_Release(_options);
            OH_ImageReceiverNative_Release(_receiver);
            return ERROR_FAILED;
        }

        ErrCode = OH_ImageReceiverNative_GetReceivingSurfaceId(_receiver, &imageReceiverSurfaceId);
        if (ErrCode != IMAGE_SUCCESS) {
            OH_LOG_ERROR(LOG_APP,
                         "OH_ImageReceiverNative_GetReceivingSurfaceId image receiver on failed, errCode: %{public}d.",
                         ErrCode);
            OH_ImageReceiverOptions_Release(_options);
            OH_ImageReceiverNative_Release(_receiver);
            return ERROR_FAILED;
        }
        OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_GetReceivingSurfaceId imageReceiverSurfaceId %{public}lu",
                     imageReceiverSurfaceId);

        std::ostringstream surfaceIDString;
        surfaceIDString << imageReceiverSurfaceId;

        // 创建预览输出流,其中参数 previewSurfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
        ret = OH_CameraManager_CreatePreviewOutput(_cameraManager, previewProfile, surfaceIDString.str().c_str(),
                                                   &_previewOutput);
        if (previewProfile == nullptr || _previewOutput == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
            return ERROR_FAILED;
        } else {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput success.previewSurfaceId : %{public}s",
                         surfaceIDString.str().c_str());
        }

        // 监听预览输出错误信息
        ret = OH_PreviewOutput_RegisterCallback(_previewOutput, GetPreviewOutputListener());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
            return ERROR_FAILED;
        }

        // 创建会话
        ret = OH_CaptureSession_Release(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Release failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }
        ret = OH_CameraManager_CreateCaptureSession(_cameraManager, &_captureSession);
        if (_captureSession == nullptr || ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 监听session错误信息
        ret = OH_CaptureSession_RegisterCallback(_captureSession, GetCaptureSessionRegister());
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 开始配置会话
        ret = OH_CaptureSession_BeginConfig(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 向会话中添加相机输入流
        ret = OH_CaptureSession_AddInput(_captureSession, _cameraInput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 向会话中添加预览输出流
        ret = OH_CaptureSession_AddPreviewOutput(_captureSession, _previewOutput);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 提交会话配置
        ret = OH_CaptureSession_CommitConfig(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }

        // 启动会话
        ret = OH_CaptureSession_Start(_captureSession);
        if (ret != CAMERA_OK) {
            OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.ret : %{public}d", ret);
            return ERROR_FAILED;
        }
        return ERROR_SUCCESS;
    }

    NDKCamera *NDKCamera::GetInstance()
    {
        if (g_ndkCamera == nullptr) {
            g_ndkCamera = new NDKCamera();
        }
        if (g_ndkCamera->Init() != ERROR_SUCCESS) {
            return nullptr;
        }
        return g_ndkCamera;
    }

    int NDKCamera::GETCHANNELID() { return previewProfileId; }

    int NDKCamera::GETCHANNELWIDTH() { return previewProfile->size.width; }

    int NDKCamera::GETCHANNELHEIGHT() { return previewProfile->size.height; }

    NDKCameraErrorCode NDKCamera::CheckSelfPermission()
    {
        if (!OH_AT_CheckSelfPermission(OHOS_PERMISSION_CAMERA)) {
            return ERROR_FAILED;
        }
        return ERROR_SUCCESS;
    }
    ```
  + camera.h:

    ```
    /*
     * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
     */
    #ifndef MYCAMERANATIVE_CAMERA_H
    #define MYCAMERANATIVE_CAMERA_H
    #include <multimedia/image_framework/image/image_receiver_native.h>
    #include <ace/xcomponent/native_interface_xcomponent.h>
    #include "ohcamera/camera.h"
    #include "ohcamera/camera_device.h"
    #include "ohcamera/camera_input.h"
    #include "ohcamera/capture_session.h"
    #include "ohcamera/photo_output.h"
    #include "ohcamera/preview_output.h"
    #include "ohcamera/video_output.h"
    #include "ohcamera/camera_manager.h"

    typedef enum NDKCameraErrorCode {
        ERROR_SUCCESS = 0,
        ERROR_FAILED,
    } NDKCameraErrorCode;

    #define OHOS_PERMISSION_CAMERA "ohos.permission.CAMERA"

    class NDKCamera {
    public:
        NDKCameraErrorCode SwitchPreviewChannel(); // 切换摄像头通道
        static NDKCameraErrorCode CheckSelfPermission();
        int GETCHANNELID();
        int GETCHANNELWIDTH();
        int GETCHANNELHEIGHT();
        static NDKCamera * GetInstance();
    private:
        NDKCameraErrorCode Init();
        Camera_Manager* _cameraManager = nullptr;
        Camera_Device* _cameras = nullptr;
        Camera_CaptureSession* _captureSession = nullptr;
        Camera_OutputCapability* _cameraOutputCapability = nullptr;
        const Camera_Profile* previewProfile = nullptr;
        const Camera_Profile* _photoProfile = nullptr;
        int previewProfileId = 0;
        int photoProfileId = 0;
        Camera_PreviewOutput* _previewOutput = nullptr;
        Camera_PhotoOutput* _photoOutput = nullptr;
        Camera_Input* _cameraInput = nullptr;
        OH_ImageReceiverOptions* _options = nullptr;
        OH_ImageReceiverNative * _receiver = nullptr;
        uint64_t imageReceiverSurfaceId = 0;
        uint32_t cameraDeviceIndex = 0;
    };

    extern void OnSurfaceCreatedCB(OH_NativeXComponent* component, void* window);
    extern void OnSurfaceChangedCB(OH_NativeXComponent* component, void* window);
    extern void OnSurfaceDestroyedCB(OH_NativeXComponent* component, void* window);
    extern void DispatchTouchEventCB(OH_NativeXComponent* component, void* window);

    #endif // MYCAMERANATIVE_CAMERA_H
    ```
* CMake编译脚本：

  ```cmake
  # the minimum version of CMake.
  cmake_minimum_required(VERSION 3.5)
  project(MyCameraNative)

  set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  if(DEFINED PACKAGE_FIND_FILE)
      include(${PACKAGE_FIND_FILE})
  endif()

  include_directories(${NATIVERENDER_ROOT_PATH}
                      ${NATIVERENDER_ROOT_PATH}/include)

  add_library(entry SHARED napi_init.cpp camera.cpp)
  target_link_libraries(entry PUBLIC libace_napi.z.so)
  target_link_libraries(entry PUBLIC libohcamera.so
                                     libace_ndk.z.so
                                     libhilog_ndk.z.so
                                     libimage_receiver.so
                                     libohimage.so
                                     libnative_image.so
                                     libimage_ndk.z.so
                                     libimage_receiver_ndk.z.so
                                     libnative_buffer.so
                                     libnative_window.so
                                     libability_access_control.so)
  ```
