---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-crosslanguage
title: 设置自定义节点跨语言属性
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 设置自定义节点跨语言属性
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:07+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:d5b48de76987ef2e18a2bae2917724b440456acd793b4c667ea055a7f76bf292
---

## 概述

ArkUI支持在前端使用ArkTS语言创建命令式节点，即[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点，也可以在Native侧使用C语言创建命令式节点，并且可以混合使用两类节点构建页面。

针对上述场景，ArkUI提供命令式节点跨语言属性设置功能，即使用ArkTS语言创建的命令式节点，可以在Native侧进行属性设置。使用C语言创建的节点，可以在ArkTS侧进行属性设置。

**说明** 

下述示例中，需要先进行Native侧配置，请参考[接入ArkTS页面](ndk-access-the-arkts-page.md)完成。

## 设置和获取跨语言配置

跨语言指的是跨越ArkTS语言和C语言。跨语言配置指的是命令式节点上对于跨语言操作的权限配置。

可以通过[setCrossLanguageOptions](../harmonyos-references/js-apis-arkui-framenode.md#setcrosslanguageoptions15)与[OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_setcrosslanguageoption)接口设置当前节点的跨语言配置。如果当前节点无法修改或设置跨语言配置，则会抛出异常信息。

可以使用[getCrossLanguageOptions](../harmonyos-references/js-apis-arkui-framenode.md#getcrosslanguageoptions15)与[OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getcrosslanguageoption)接口获取当前节点的跨语言配置。

以下示例描述了如何设置和获取ArkTS命令式节点的跨语言配置。

```ts
// Index.ets
import { NodeController, UIContext, FrameNode, typeNode, BuilderNode } from '@kit.ArkUI';

@Builder
function insideScroll() {
  Column() {
    ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
      Text(item.toString())
        .width("75%")
        .height(50)
        .backgroundColor(0xFFFFFF)
        .borderRadius(15)
        .fontSize(30)
        .textAlign(TextAlign.Center)
        .margin({ top: 10 })
    }, (item: number) => item.toString())
  }
  .width("100%")
}

class MyNodeController extends NodeController {
  uiContext: UIContext | null = null;
  rootNode: FrameNode | null = null;
  scrollNode: FrameNode | null = null;
  scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width("80%").height("50%").borderWidth(2).margin(15);
    const scroll = typeNode.createNode(uiContext, 'Scroll');
    scroll.initialize(this.scroller).id("scroll");
    this.scrollNode = scroll;
    this.rootNode.appendChild(this.scrollNode);
    const builderNode = new BuilderNode(uiContext);
    builderNode.build(wrapBuilder(insideScroll));
    this.scrollNode?.appendChild(builderNode.getFrameNode());
    return this.rootNode;
  }
}

@Entry
@Component
struct CrossLanguage {
  myNodeController: MyNodeController = new MyNodeController()
  @State attributeSetting: boolean = false;
  @State getCrossLanguageOptions: string = '{"attributeSetting": false}';

  build() {
    Scroll() {
      Column({ space: 15 }) {
        Column() {
          Scroll() {
            Column() {
              NodeContainer(this.myNodeController)
              Button("setCrossLanguageOptions").margin({ bottom: 15})
                .onClick(() => {
                  this.attributeSetting = !this.attributeSetting;
                  this.myNodeController.scrollNode?.setCrossLanguageOptions({
                    attributeSetting: this.attributeSetting
                  });
                  // 若attributeSetting为true，表示scrollNode支持通过非ArkTS语言进行属性设置，否则为不支持
                  this.getCrossLanguageOptions = JSON.stringify(this.myNodeController.scrollNode?.getCrossLanguageOptions());
                })
              Text("CrossLanguageOptions: " + this.getCrossLanguageOptions)
            }
          }.scrollBarColor(Color.Transparent)
        }
        .width('100%')
        .height(350)
        .backgroundColor(0xeeeeee)
        .id('Part_TS')
      }
      .width('100%')
    }.scrollBarColor(Color.Transparent)
  }
}
```

## 跨语言设置节点属性

获取节点后，若节点的跨语言配置设置为允许属性设置，ArkTS侧可利用getAttribute接口获取修改Native节点属性的对象，Native侧可利用[setAttribute](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口修改ArkTS节点属性。

以下示例创建了ArkTS的[Scroll](../harmonyos-references/js-apis-arkui-framenode.md#scroll12)类型节点，并在Native侧修改了Scroll的属性。

1. 在ArkTS侧创建组件类型为Scroll的命令式节点。新建CrossLanguage.ets页面文件，在页面创建时调用createCrossLanguageRoot方法通知Native侧创建跨语言示例组件，在页面销毁时调用destroyNativeRoot方法释放Native侧组件。此外，需要在entry/src/main/resources/base/profile/main\_pages.json中注册pages/CrossLanguage页面，并在主页面中添加跳转至该页面的路由。

   ```typescript
   import nativeNode from 'libentry.so';
   import { NodeController, UIContext, FrameNode, typeNode, BuilderNode, NodeContent } from '@kit.ArkUI';

   @Builder
   function insideScroll() {
     Column() {
       ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
         Text(item.toString())
           .width('75%')
           .height(50)
           .backgroundColor(0xFFFFFF)
           .borderRadius(15)
           .fontSize(30)
           .textAlign(TextAlign.Center)
           .margin({ top: 10 })
       }, (item: number) => item.toString())
     }
     .width('100%')
   }

   class MyNodeController extends NodeController {
     private uiContext: UIContext | null = null;
     private rootNode: FrameNode | null = null;
     public scrollNode: FrameNode | null = null;
     private scroller: Scroller = new Scroller();

     makeNode(uiContext: UIContext): FrameNode | null {
       this.uiContext = uiContext;
       this.rootNode = new FrameNode(uiContext);
       this.rootNode.commonAttribute.width('80%').height('50%').borderWidth(2).margin(15);
       const scroll = typeNode.createNode(uiContext, 'Scroll');
       scroll.initialize(this.scroller).id('scroll');
       this.scrollNode = scroll;
       this.rootNode.appendChild(this.scrollNode);
       const builderNode = new BuilderNode(uiContext);
       builderNode.build(wrapBuilder(insideScroll));
       this.scrollNode?.appendChild(builderNode.getFrameNode());
       return this.rootNode;
     }
   }

   @Entry
   @Component
   struct CrossLanguage {
     private myNodeController: MyNodeController = new MyNodeController();
     @State attributeSetting: boolean = false;
     @State getCrossLanguageOptions: string = '{"attributeSetting": false}';
     private rootSlot = new NodeContent();

     aboutToAppear(): void {
       // 传递NodeContent对象用于Native创建跨语言示例组件的挂载显示。
       nativeNode.createCrossLanguageRoot(this.rootSlot);
     }

     aboutToDisappear(): void {
       // 页面销毁时释放Native侧组件。
       nativeNode.destroyNativeRoot();
     }

     build() {
       Scroll() {
         Column({ space: 15 }) {
           Column() {
             Scroll() {
               Column() {
                 NodeContainer(this.myNodeController)
                 Button('setCrossLanguageOptions').margin({ bottom: 15})
                   .onClick(() => {
                     this.attributeSetting = !this.attributeSetting;
                     this.myNodeController.scrollNode?.setCrossLanguageOptions({
                       attributeSetting: this.attributeSetting
                     });
                     // 若attributeSetting为true，表示scrollNode支持通过非ArkTS语言进行属性设置，否则为不支持
                     this.getCrossLanguageOptions =
                       JSON.stringify(this.myNodeController.scrollNode?.getCrossLanguageOptions());
                   })
                 Text('CrossLanguageOptions: ' + this.getCrossLanguageOptions)
               }
             }.scrollBarColor(Color.Transparent)
           }
           .width('100%')
           .height(350)
           .backgroundColor(0xeeeeee)
           .id('Part_TS')

           Column() {
             ContentSlot(this.rootSlot)
           }
           .width(500)
           .height(400)
           .id('Part_C')
         }
         .width('100%')
       }.scrollBarColor(Color.Transparent)
     }
   }
   ```
2. 提供ArkTS侧引用Native桥接方法的接口声明与注册，使步骤1中通过import nativeNode from 'libentry.so'引用的createCrossLanguageRoot和destroyNativeRoot方法生效。

   其中，entry/src/main/cpp/types/libentry/oh-package.json5文件用于将libentry.so与接口声明文件Index.d.ts关联。

   ```json5
   {
     "name": "libentry.so",
     "types": "./Index.d.ts",
     "version": "1.0.0",
     "description": "Please describe the basic information."
   }
   ```

   接口声明。

   ```typescript
   // entry/src/main/cpp/types/libentry/Index.d.ts
   export const createNativeRoot: (content: Object) => void;
   export const createCrossLanguageRoot: (content: Object) => void;
   export const destroyNativeRoot: () => void;
   ```

   Native实现。

   ```
   // entry/src/main/cpp/napi_init.cpp
   #include "napi/native_api.h"
   #include "NativeEntry.h"

   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       // 绑定Native侧的创建组件和销毁组件。
       napi_property_descriptor desc[] = {
           {"createNativeRoot", nullptr,
            NativeModule::CreateNativeRoot, nullptr, nullptr,
            nullptr, napi_default, nullptr},
           {"createCrossLanguageRoot", nullptr,
            NativeModule::CreateCrossLanguageRoot, nullptr, nullptr,
            nullptr, napi_default, nullptr},
           {"destroyNativeRoot", nullptr,
            NativeModule::DestroyNativeRoot, nullptr, nullptr,
            nullptr, napi_default, nullptr}};
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
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
3. 本示例使用C++对NDK的C接口进行二次封装，需要提供获取NDK接口入口的封装接口NativeModule.h、组件树操作基类ArkUIBaseNode.h以及通用属性和事件的封装类ArkUINode.h。若已完成[接入ArkTS页面](ndk-access-the-arkts-page.md)中的Native侧配置，可直接复用对应文件。

   ```c
   // NativeModule.h
   // 提供获取ArkUI在Native侧模块的封装接口

   #ifndef MYAPPLICATION_NATIVEMODULE_H
   #define MYAPPLICATION_NATIVEMODULE_H

   #include <arkui/native_node.h>
   #include <cassert>

   #include <arkui/native_interface.h>

   namespace NativeModule {

   class NativeModuleInstance {
   public:
       static NativeModuleInstance *GetInstance()
       {
           static NativeModuleInstance instance;
           return &instance;
       }
       NativeModuleInstance()
       {
           OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, arkUINativeNodeApi_);
       }
       // 暴露给其他模块使用。
       ArkUI_NativeNodeAPI_1 *GetNativeNodeAPI() { return arkUINativeNodeApi_; }

   private:
       ArkUI_NativeNodeAPI_1 *arkUINativeNodeApi_ = nullptr;
   };

   } // namespace NativeModule

   #endif // MYAPPLICATION_NATIVEMODULE_H
   ```

   ```c
   // ArkUIBaseNode.h
   // 提供组件树操作的基类。
   #ifndef MYAPPLICATION_ARKUIBASENODE_H
   #define MYAPPLICATION_ARKUIBASENODE_H

   #include <arkui/native_type.h>
   #include <list>
   #include <memory>

   #include "NativeModule.h"

   namespace NativeModule {

   class ArkUIBaseNode {
   public:
       explicit ArkUIBaseNode(ArkUI_NodeHandle handle)
           : handle_(handle), nativeModule_(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()) {}

       virtual ~ArkUIBaseNode()
       {
           // 封装析构函数，实现子节点移除功能。
           if (!children_.empty()) {
               for (const auto& child : children_) {
                   nativeModule_->removeChild(handle_, child->GetHandle());
               }
               children_.clear();
           }
           // 封装析构函数，统一回收节点资源。
           nativeModule_->disposeNode(handle_);
       }

       void AddChild(const std::shared_ptr<ArkUIBaseNode> &child)
       {
           children_.emplace_back(child);
           OnAddChild(child);
       }

       void RemoveChild(const std::shared_ptr<ArkUIBaseNode> &child)
       {
           children_.remove(child);
           OnRemoveChild(child);
       }

       void InsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index)
       {
           if (index >= children_.size()) {
               AddChild(child);
           } else {
               auto iter = children_.begin();
               std::advance(iter, index);
               children_.insert(iter, child);
               OnInsertChild(child, index);
           }
       }

       ArkUI_NodeHandle GetHandle() const { return handle_; }

   protected:
       // 针对父容器子类需要重载下面的函数，实现组件挂载和卸载。
       virtual void OnAddChild(const std::shared_ptr<ArkUIBaseNode> &child) {}
       virtual void OnRemoveChild(const std::shared_ptr<ArkUIBaseNode> &child) {}
       virtual void OnInsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index) {}

       ArkUI_NodeHandle handle_;
       ArkUI_NativeNodeAPI_1 *nativeModule_ = nullptr;

   private:
       std::list<std::shared_ptr<ArkUIBaseNode>> children_;
   };
   } // namespace NativeModule

   #endif // MYAPPLICATION_ARKUIBASENODE_H
   ```

   ```c
   // ArkUINode.h
   // 提供通用属性和事件的封装。
   #ifndef MYAPPLICATION_ARKUINODE_H
   #define MYAPPLICATION_ARKUINODE_H

   #include "ArkUIBaseNode.h"
   #include "NativeModule.h"
   #include <arkui/native_node.h>
   #include <arkui/native_type.h>

   namespace NativeModule {

   class ArkUINode : public ArkUIBaseNode {
   public:
       explicit ArkUINode(ArkUI_NodeHandle handle) : ArkUIBaseNode(handle) {}

       ~ArkUINode() override {}
       
       void SetWidth(float width)
       {
           ArkUI_NumberValue value[] = {{.f32 = width}};
           ArkUI_AttributeItem item = {value, 1};
           nativeModule_->setAttribute(handle_, NODE_WIDTH, &item);
       }
       void SetPercentWidth(float percent)
       {
           ArkUI_NumberValue value[] = {{.f32 = percent}};
           ArkUI_AttributeItem item = {value, 1};
           nativeModule_->setAttribute(handle_, NODE_WIDTH_PERCENT, &item);
       }
       void SetHeight(float height)
       {
           ArkUI_NumberValue value[] = {{.f32 = height}};
           ArkUI_AttributeItem item = {value, 1};
           nativeModule_->setAttribute(handle_, NODE_HEIGHT, &item);
       }
       void SetPercentHeight(float percent)
       {
           ArkUI_NumberValue value[] = {{.f32 = percent}};
           ArkUI_AttributeItem item = {value, 1};
           nativeModule_->setAttribute(handle_, NODE_HEIGHT_PERCENT, &item);
       }
       void SetBackgroundColor(uint32_t color)
       {
           ArkUI_NumberValue value[] = {{.u32 = color}};
           ArkUI_AttributeItem item = {value, 1};
           nativeModule_->setAttribute(handle_, NODE_BACKGROUND_COLOR, &item);
       }

   protected:
       // 组件树操作的实现类对接。
       void OnAddChild(const std::shared_ptr<ArkUIBaseNode> &child) override
       {
           nativeModule_->addChild(handle_, child->GetHandle());
       }
       void OnRemoveChild(const std::shared_ptr<ArkUIBaseNode> &child) override
       {
           nativeModule_->removeChild(handle_, child->GetHandle());
       }
       void OnInsertChild(const std::shared_ptr<ArkUIBaseNode> &child, int32_t index) override
       {
           nativeModule_->insertChildAt(handle_, child->GetHandle(), index);
       }
   };
   } // namespace NativeModule

   #endif // MYAPPLICATION_ARKUINODE_H
   ```
4. 在NativeEntry.h中声明CreateCrossLanguageRoot等桥接方法，并管理Native组件的生命周期和内存。

   ```c
   // NativeEntry.h

   #ifndef MYAPPLICATION_NATIVEENTRY_H
   #define MYAPPLICATION_NATIVEENTRY_H

   #include <ArkUIBaseNode.h>
   #include <arkui/native_type.h>
   #include <js_native_api_types.h>

   namespace NativeModule {

   napi_value CreateNativeRoot(napi_env env, napi_callback_info info);

   napi_value CreateCrossLanguageRoot(napi_env env, napi_callback_info info);

   napi_value DestroyNativeRoot(napi_env env, napi_callback_info info);

   // 管理Native组件的生命周期和内存。
   class NativeEntry {
   public:
       static NativeEntry *GetInstance()
       {
           static NativeEntry nativeEntry;
           return &nativeEntry;
       }

       void SetContentHandle(ArkUI_NodeContentHandle handle)
       {
           handle_ = handle;
       }

       void SetRootNode(const std::shared_ptr<ArkUIBaseNode> &baseNode)
       {
           root_ = baseNode;
           // 添加Native组件到NodeContent上用于挂载显示。
           OH_ArkUI_NodeContent_AddNode(handle_, root_->GetHandle());
       }
       void DisposeRootNode()
       {
           // 从NodeContent上卸载组件并销毁Native组件。
           OH_ArkUI_NodeContent_RemoveNode(handle_, root_->GetHandle());
           root_.reset();
       }

   private:
       std::shared_ptr<ArkUIBaseNode> root_;
       ArkUI_NodeContentHandle handle_;
   };

   } // namespace NativeModule

   #endif  // MYAPPLICATION_NATIVEENTRY_H
   ```
5. 在NativeEntry.cpp中实现CreateCrossLanguageRoot方法，创建跨语言示例组件并挂载显示。其中CreateNativeRoot为[接入ArkTS页面](ndk-access-the-arkts-page.md)示例中挂载Native文本列表的方法。

   ```
   // NativeEntry.cpp

   #include <arkui/native_node_napi.h>
   #include <js_native_api.h>
   #include "NativeEntry.h"
   #include "CrossLanguageExample.h"
   #include "NormalTextListExample.h"

   namespace NativeModule {

   napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value args[1] = {nullptr};

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 获取NodeContent
       ArkUI_NodeContentHandle contentHandle;
       OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
       NativeEntry::GetInstance()->SetContentHandle(contentHandle);

       // 创建文本列表
       auto list = CreateTextListExample();

       // 保持Native侧对象到管理类中，维护生命周期。
       NativeEntry::GetInstance()->SetRootNode(list);
       return nullptr;
   }

   napi_value CreateCrossLanguageRoot(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value args[1] = {nullptr};

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 获取NodeContent
       ArkUI_NodeContentHandle contentHandle;
       OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
       NativeEntry::GetInstance()->SetContentHandle(contentHandle);

       // 创建跨语言属性设置示例
       auto node = CreateCrossLanguageExample();

       // 保持Native侧对象到管理类中，维护生命周期。
       NativeEntry::GetInstance()->SetRootNode(node);
       return nullptr;
   }

   napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   {
       // 从管理类中释放Native侧对象。
       NativeEntry::GetInstance()->DisposeRootNode();
       return nullptr;
   }
   } // namespace NativeModule
   ```
6. 新建CrossLanguageExample.h文件，在其中创建Native侧组件树，并通过OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById获取ArkTS侧创建的目标节点，设置其属性。

   ```c
   // CrossLanguageExample.h
   // 提供跨语言属性设置示例中Native侧组件的创建。

   #ifndef MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H
   #define MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H

   #include "ArkUINode.h"
   #include <hilog/log.h>
   #include <memory>

   namespace NativeModule {

   // 事件回调：在Native侧跨语言修改ArkTS侧创建的Scroll节点属性。
   void HandleCrossLanguageClick(ArkUI_NodeEvent *event)
   {
       auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

       if (OH_ArkUI_NodeEvent_GetTargetId(event) == 0) { // 修改滚动条颜色。
           ArkUI_NodeHandle node_ptr = nullptr;
           // 通过id获取ArkTS侧创建的节点。
           auto ret = OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("scroll", &node_ptr);
           if (ret != ARKUI_ERROR_CODE_NO_ERROR || node_ptr == nullptr) {
               OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample",
                   "OH_ArkUI_NodeUtils_GetAttachedNodeHandleById failed, error code: %{public}d", ret);
               return;
           }
           ArkUI_NumberValue scroll_color_value[] = {{.u32 = 0xff00ff00}};
           ArkUI_AttributeItem scroll_color_item = {scroll_color_value,
               sizeof(scroll_color_value) / sizeof(ArkUI_NumberValue)};
           // 若ArkTS侧未开启跨语言属性设置，此处设置失败并返回错误码。
           auto errCode = nodeAPI->setAttribute(node_ptr, NODE_SCROLL_BAR_COLOR, &scroll_color_item);
           if (errCode != ARKUI_ERROR_CODE_NO_ERROR) {
               OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample",
                   "crossLanguage setAttribute scroll bar color failed, error code: %{public}d", errCode);
           }
       }

       if (OH_ArkUI_NodeEvent_GetTargetId(event) == 1) { // 修改滚动条宽度。
           ArkUI_NodeHandle node_ptr = nullptr;
           auto ret = OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("scroll", &node_ptr);
           if (ret != ARKUI_ERROR_CODE_NO_ERROR || node_ptr == nullptr) {
               OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample",
                   "OH_ArkUI_NodeUtils_GetAttachedNodeHandleById failed, error code: %{public}d", ret);
               return;
           }
           ArkUI_NumberValue scroll_width_value[] = {{.f32 = 20}};
           ArkUI_AttributeItem scroll_width_item = {scroll_width_value,
               sizeof(scroll_width_value) / sizeof(ArkUI_NumberValue)};
           auto errCode = nodeAPI->setAttribute(node_ptr, NODE_SCROLL_BAR_WIDTH, &scroll_width_item);
           if (errCode != ARKUI_ERROR_CODE_NO_ERROR) {
               OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample",
                   "crossLanguage setAttribute scroll bar width failed, error code: %{public}d", errCode);
           }
       }
   }

   // 创建根节点Scroll。
   ArkUI_NodeHandle CreateScrollNode(ArkUI_NativeNodeAPI_1 *nodeAPI)
   {
       ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_SCROLL);
       ArkUI_NumberValue length_value[] = {{.f32 = 480}};
       ArkUI_AttributeItem length_item = {length_value, sizeof(length_value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(scroll, NODE_WIDTH, &length_item);
       ArkUI_NumberValue length_value1[] = {{.f32 = 650}};
       ArkUI_AttributeItem length_item1 = {length_value1, sizeof(length_value1) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(scroll, NODE_HEIGHT, &length_item1);
       ArkUI_AttributeItem scroll_id = {.string = "Scroll_CAPI"};
       nodeAPI->setAttribute(scroll, NODE_ID, &scroll_id);
       return scroll;
   }

   // 创建Column。
   ArkUI_NodeHandle CreateColumnNode(ArkUI_NativeNodeAPI_1 *nodeAPI)
   {
       ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
       ArkUI_NumberValue value[] = {{.f32 = 480}};
       ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(column, NODE_WIDTH, &item);
       ArkUI_NumberValue column_bc[] = {{.u32 = 0xFFF00BB}};
       ArkUI_AttributeItem column_item = {column_bc, 1};
       nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &column_item);
       ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
       nodeAPI->setAttribute(column, NODE_ID, &column_id);
       return column;
   }

   // 创建Text。
   ArkUI_NodeHandle CreateTextNode(ArkUI_NativeNodeAPI_1 *nodeAPI)
   {
       ArkUI_NodeHandle text0 = nodeAPI->createNode(ARKUI_NODE_TEXT);
       ArkUI_NumberValue text_width[] = {{.f32 = 300}};
       ArkUI_AttributeItem text_item0 = {text_width, sizeof(text_width) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text0, NODE_WIDTH, &text_item0);
       ArkUI_NumberValue text_height[] = {{.f32 = 50}};
       ArkUI_AttributeItem text_item1 = {text_height, sizeof(text_height) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text0, NODE_HEIGHT, &text_item1);
       ArkUI_AttributeItem text_item = {.string = "C设置TS创建的节点属性"};
       nodeAPI->setAttribute(text0, NODE_TEXT_CONTENT, &text_item);
       ArkUI_NumberValue margin[] = {{.f32 = 10}};
       ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text0, NODE_MARGIN, &item_margin);
       return text0;
   }

   // 创建Row。
   ArkUI_NodeHandle CreateRowNode(ArkUI_NativeNodeAPI_1 *nodeAPI)
   {
       ArkUI_NodeHandle row0 = nodeAPI->createNode(ARKUI_NODE_ROW);
       ArkUI_NumberValue width_value[] = {{.f32 = 330}};
       ArkUI_AttributeItem width_item = {width_value, sizeof(width_value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(row0, NODE_WIDTH, &width_item);
       ArkUI_NumberValue height_value[] = {{.f32 = 50}};
       ArkUI_AttributeItem height_item = {height_value, sizeof(height_value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(row0, NODE_HEIGHT, &height_item);
       ArkUI_NumberValue margin[] = {{.f32 = 10}};
       ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(row0, NODE_MARGIN, &item_margin);
       return row0;
   }

   // 创建Button，用于触发Native侧跨语言属性设置。
   void CreateButtonNodes(ArkUI_NativeNodeAPI_1 *nodeAPI, ArkUI_NodeHandle row0)
   {
       ArkUI_NumberValue btn_width[] = {{.f32 = 150}};
       ArkUI_AttributeItem btn_item0 = {btn_width, sizeof(btn_width) / sizeof(ArkUI_NumberValue)};
       ArkUI_NumberValue height_value[] = {{.f32 = 50}};
       ArkUI_AttributeItem height_item = {height_value, sizeof(height_value) / sizeof(ArkUI_NumberValue)};
       ArkUI_NumberValue margin[] = {{.f32 = 10}};
       ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};

       ArkUI_NodeHandle bt0 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
       nodeAPI->setAttribute(bt0, NODE_WIDTH, &btn_item0);
       nodeAPI->setAttribute(bt0, NODE_HEIGHT, &height_item);
       nodeAPI->setAttribute(bt0, NODE_MARGIN, &item_margin);
       ArkUI_AttributeItem bt0_item = {.string = "scrollBarColor"};
       nodeAPI->setAttribute(bt0, NODE_BUTTON_LABEL, &bt0_item);
       nodeAPI->registerNodeEvent(bt0, NODE_ON_CLICK, 0, nullptr);

       ArkUI_NodeHandle bt1 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
       nodeAPI->setAttribute(bt1, NODE_WIDTH, &btn_item0);
       nodeAPI->setAttribute(bt1, NODE_HEIGHT, &height_item);
       nodeAPI->setAttribute(bt1, NODE_MARGIN, &item_margin);
       ArkUI_AttributeItem bt1_item = {.string = "scrollBarWidth"};
       nodeAPI->setAttribute(bt1, NODE_BUTTON_LABEL, &bt1_item);
       nodeAPI->registerNodeEvent(bt1, NODE_ON_CLICK, 1, nullptr);

       nodeAPI->addChild(row0, bt0);
       nodeAPI->addChild(row0, bt1);
   }

   std::shared_ptr<ArkUIBaseNode> CreateCrossLanguageExample()
   {
       auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

       // 创建根节点Scroll。
       ArkUI_NodeHandle scroll = CreateScrollNode(nodeAPI);

       // 创建Column。
       ArkUI_NodeHandle column = CreateColumnNode(nodeAPI);

       // 创建Text。
       ArkUI_NodeHandle text0 = CreateTextNode(nodeAPI);

       // 创建Row。
       ArkUI_NodeHandle row0 = CreateRowNode(nodeAPI);

       // 创建Button，用于触发Native侧跨语言属性设置。
       CreateButtonNodes(nodeAPI, row0);

       // 注册事件回调，在Native侧跨语言修改ArkTS侧创建的Scroll节点属性。
       nodeAPI->registerNodeEventReceiver(HandleCrossLanguageClick);

       // 节点添加，构建组件树。
       nodeAPI->addChild(scroll, column);
       nodeAPI->addChild(column, text0);
       nodeAPI->addChild(column, row0);

       return std::make_shared<ArkUINode>(scroll);
   }
   } // namespace NativeModule

   #endif // MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H
   ```
7. 修改CMakeLists.txt，添加链接库。

   ```c
   # CMakeLists.txt
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(CAPI_DEMO)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()

   include_directories(${NATIVERENDER_ROOT_PATH}
                     ${NATIVERENDER_ROOT_PATH}/include)

   add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so hilog_ndk.z.so)
   ```
8. 运行程序，在示例主页面点击CrossLanguage按钮进入跨语言属性设置页面，在ArkTS侧点击setCrossLanguageOptions按钮，设置当前attributeSetting为true，在Native侧点击按钮，设置ArkTS侧Scroll组件滚动条的颜色和粗细属性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/i5p2KGz7T2KCJsXi2L0ZWw/zh-cn_image_0000002788306946.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004707Z&HW-CC-Expire=31536000000&HW-CC-Sign=421FC1C8E6E2B12C1217EA8693CF0C6F7263A8167989AEC5BF43C6D837CFFA3A)

## 支持跨语言设置属性的节点类型

仅以下节点类型支持跨语言设置节点属性。Native侧需要使用[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid)获取待修改属性的节点，不支持对[OH\_ArkUI\_GetNodeHandleFromNapiValue](../harmonyos-references/capi-native-node-napi-h.md#oh_arkui_getnodehandlefromnapivalue)获取的目标节点跨语言设置属性。

| ArkTS侧[TypedFrameNode](../harmonyos-references/js-apis-arkui-framenode.md#typedframenode12)类型 | Native侧[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)类型 | ArkTS属性获取接口 | ArkTS控制器获取/绑定接口 |
| --- | --- | --- | --- |
| [Button](../harmonyos-references/js-apis-arkui-framenode.md#button12) | ARKUI\_NODE\_BUTTON | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributebutton20) | NA |
| [Checkbox](../harmonyos-references/js-apis-arkui-framenode.md#checkbox18) | ARKUI\_NODE\_CHECKBOX | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributecheckbox20) | NA |
| [Radio](../harmonyos-references/js-apis-arkui-framenode.md#radio18) | ARKUI\_NODE\_RADIO | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeradio20) | NA |
| [Slider](../harmonyos-references/js-apis-arkui-framenode.md#slider18) | ARKUI\_NODE\_SLIDER | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeslider20) | NA |
| [Toggle](../harmonyos-references/js-apis-arkui-framenode.md#toggle18) | ARKUI\_NODE\_TOGGLE | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetoggle20) | NA |
| [Progress](../harmonyos-references/js-apis-arkui-framenode.md#progress12) | ARKUI\_NODE\_PROGRESS | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeprogress20) | NA |
| [LoadingProgress](../harmonyos-references/js-apis-arkui-framenode.md#loadingprogress12) | ARKUI\_NODE\_LOADING\_PROGRESS | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeloadingprogress20) | NA |
| [Image](../harmonyos-references/js-apis-arkui-framenode.md#image12) | ARKUI\_NODE\_IMAGE | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeimage20) | NA |
| [XComponent](../harmonyos-references/js-apis-arkui-framenode.md#xcomponent12) | ARKUI\_NODE\_XCOMPONENT | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributexcomponent20) | getController |
| [Column](../harmonyos-references/js-apis-arkui-framenode.md#column12) | ARKUI\_NODE\_COLUMN | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributecolumn20) | NA |
| [Row](../harmonyos-references/js-apis-arkui-framenode.md#row12) | ARKUI\_NODE\_ROW | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributerow20) | NA |
| [Stack](../harmonyos-references/js-apis-arkui-framenode.md#stack12) | ARKUI\_NODE\_STACK | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributestack20) | NA |
| [Flex](../harmonyos-references/js-apis-arkui-framenode.md#flex12) | ARKUI\_NODE\_FLEX | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeflex20) | NA |
| [RelativeContainer](../harmonyos-references/js-apis-arkui-framenode.md#relativecontainer12) | ARKUI\_NODE\_RELATIVE\_CONTAINER | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributerelativecontainer20) | NA |
| [Swiper](../harmonyos-references/js-apis-arkui-framenode.md#swiper12) | ARKUI\_NODE\_SWIPER | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeswiper20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerswiper20) |
| [Scroll](../harmonyos-references/js-apis-arkui-framenode.md#scroll12) | ARKUI\_NODE\_SCROLL | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributescroll15) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerscroll15) |
| [List](../harmonyos-references/js-apis-arkui-framenode.md#list12) | ARKUI\_NODE\_LIST | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributelist20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerlist20) |
| [ListItem](../harmonyos-references/js-apis-arkui-framenode.md#listitem12) | ARKUI\_NODE\_LIST\_ITEM | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributelistitem20) | NA |
| [ListItemGroup](../harmonyos-references/js-apis-arkui-framenode.md#listitemgroup12) | ARKUI\_NODE\_LIST\_ITEM\_GROUP | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributelistitemgroup20) | NA |
| [WaterFlow](../harmonyos-references/js-apis-arkui-framenode.md#waterflow12) | ARKUI\_NODE\_WATER\_FLOW | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributewaterflow20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerwaterflow20) |
| [FlowItem](../harmonyos-references/js-apis-arkui-framenode.md#flowitem12) | ARKUI\_NODE\_FLOW\_ITEM | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeflowitem20) | NA |
| [Grid](../harmonyos-references/js-apis-arkui-framenode.md#grid14) | ARKUI\_NODE\_GRID | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributegrid20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollergrid20) |
| [GridItem](../harmonyos-references/js-apis-arkui-framenode.md#griditem14) | ARKUI\_NODE\_GRID\_ITEM | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributegriditem20) | NA |
| [Text](../harmonyos-references/js-apis-arkui-framenode.md#text12) | ARKUI\_NODE\_TEXT | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetext20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollertext20) |
| [TextInput](../harmonyos-references/js-apis-arkui-framenode.md#textinput12) | ARKUI\_NODE\_TEXT\_INPUT | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetextinput20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollertextinput20) |
| [TextArea](../harmonyos-references/js-apis-arkui-framenode.md#textarea14) | ARKUI\_NODE\_TEXT\_AREA | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetextarea20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollertextarea20) |
