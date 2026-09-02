---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-29
title: 使用手机验证码登录帐号后，应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 使用手机验证码登录帐号后，应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9fdd296663898b5e9cc7412808cd2ee60efe9084514162a6fbb8626e4ce185e6
---

## 问题现象

使用手机验证码登录账号后，应用闪退，在平板横屏时出现，竖屏正常。

## 背景知识

* [JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)：Error是最基本的错误类型，其他的错误类型都继承自该类型。Error对象主要有两个重要属性message和name分别表示错误信息和错误名称。程序运行过程中抛出的异常一般都有具体的类型，Error类型一般都是开发人员自己抛出的异常。
* [150002 祖先节点无法获得焦点](../harmonyos-references/errorcode-focus.md#section150002-祖先节点无法获得焦点)：当前节点对应的祖先节点中存在无法获焦节点。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 问题定位

1. 查看faultlogger目录下的故障日志，故障原因是Error，错误码150002，异常信息是：This component has unfocusable ancestor，祖先节点无法获焦。

   ```screen
   Reason:Error
   Error name:Error
   Error message:This component has unfocusable ancestor.
   Error code:150002
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
      at requestFocus (obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/jsUIContext_ohos.js:978:1)
      at moveFocus (@abner/input_box|@abner/input_box|1.0.3|src/main/ets/components/InputBoxView.ts:624:1)
      at anonymous (@abner/input_box|@abner/input_box|1.0.3|src/main/ets/components/InputBoxView.ts:439:1)
   ```
2. 查看闪退之前的hilog日志，TextInput组件获焦失败，祖先组件NavDestination不可获焦。

   ```screen
   07-09 18:38:23.943  1444  1444 I C0391C/com.hx.example/AceFocus: [(100000:100000:scope)] TextInput/secure_fieldRequest focus sync by id
   07-09 18:38:23.944  1444  1444 I C0391C/com.hx.example/AceFocus: [(100000:100000:scope)] TextInput/secure_field RequestFocusImmediately isOnMainTree:1
   07-09 18:38:23.944  1444  1444 I C0391C/com.hx.example/AceFocus: [(100000:100000:scope)] Request focus by id on node: TextInput/381 return false, unfocusable node: NavDestination/215, focusable = 1, shown = 1, enabled = 0
   07-09 18:38:23.944  1444  1444 E C03900/com.hx.example/Ace: [<private>(<private>)] napi throw errCode <private> strMsg <private>
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler: [default] [Call:3600] occur exception need return
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler: [ecmascript] Pending exception before ExecutePendingJob called, in line:5568, exception details as follows:
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler: Error: This component has unfocusable ancestor.
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler: Cannot get SourceMap info, dump raw stack:
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler:     at requestFocus (obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/jsUIContext_ohos.js:978:1)
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler:     at moveFocus (@abner/input_box|@abner/input_box|1.0.3|src/main/ets/components/InputBoxView.ts:624:1)
   07-09 18:38:23.944  1444  1444 E C03F00/com.hx.example/ArkCompiler:     at anonymous (@abner/input_box|@abner/input_box|1.0.3|src/main/ets/components/InputBoxView.ts:439:1)
   ```
3. 在平板竖屏时，最后一个验证码输入框失去焦点后，正常跳转到主页。

   ```screen
   07-14 18:00:55.101   25150-25150   com.hx.example  I [(100000:100000:scope)] Focus view: NavBar/41 show
   07-14 18:00:55.101   25150-25150   com.hx.example  I [(100000:100000:scope)] Focus view: NavDestination/395 lost focus
   07-14 18:00:55.101   25150-25150   com.hx.example  I [(100000:100000:scope)] TextField 440 OnBlur
   07-14 18:00:55.101   25150-25150   com.hx.example  I [(100000:100000:scope)] transition start, disableAllAnimation: 0, animated: 1, isPopPage: 1, isDialog: 0
   07-14 18:00:55.101   25150-25150   com.hx.example  I [(100000:100000:scope)] AuthCode lifecycle change to onWillHide state.
   07-14 18:00:55.102   25150-25150   com.hx.example  I [(100000:100000:scope)] loginPage lifecycle change to onWillHide state.
   07-14 18:00:55.102   25150-25150   com.hx.example  I [(100000:100000:scope)] PageChange CloseKeyboard FrameNode notNeedSoftKeyboard.
   07-14 18:00:55.102   25150-25150   com.hx.example  I line: 379, function: Close,start.
   ```
4. 在平板横屏时，最后一个验证码输入框失去焦点后，触发了组件区域变化，导致应用重新将焦点设置到第一个输入框上，发生闪退。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/q4bcTVQcSPybWxqkl5yXPg/zh-cn_image_0000002658914201.png "点击放大")

   ```screen
   07-14 18:07:48.228   25150-25150   com.hx.example  I  [(100000:100000:scope)] TextField 653 OnBlur
   07-14 18:07:48.228   25150-25150   com.hx.example  I  [(100000:100000:scope)] transition start, disableAllAnimation: 0, animated: 1, isPopPage: 1, isDialog: 0
   07-14 18:07:48.228   25150-25150   com.hx.example  I  [(100000:100000:scope)] AuthCode lifecycle change to onWillHide state.
   07-14 18:07:48.229   25150-25150   com.hx.example  I  [(100000:100000:scope)] loginPage lifecycle change to onWillHide state.
   07-14 18:07:48.229   25150-25150   com.hx.example  I  [(100000:100000:scope)] PageChange CloseKeyboard FrameNode notNeedSoftKeyboard.
   // ...
   07-14 18:07:48.257   25150-25150   com.hx.example  I  [(-1:100000:singleton)] OccupiedAreaChange rect:Rect (0.00, 0.00) - [0.00 x 0.00] type: 0, positionY:1669.000000, height:94.900000, instanceId_ 100000
   // ...
   07-14 18:07:48.270   25150-25150   com.hx.example  I  [(100000:100000:scope)] Request focus immediately  sync by id. The node is TextInput/secure_field
   07-14 18:07:48.270   25150-25150   com.hx.example  I  [(100000:100000:scope)] TextInput/secure_field RequestFocusImmediately isOnMainTree:1
   07-14 18:07:48.270   25150-25150   com.hx.example  E  [<private>(<private>)] napi throw errCode <private> strMsg <private>
   07-14 18:07:48.270   25150-25150   com.hx.example  I  [(100000:100000:scope)] Request focus by id on node: TextInput/632 return false, unfocusable node: NavDestination/466, focusable = 1, shown = 1, enabled = 0
   07-14 18:07:48.270   25150-25150   com.hx.example  E  [default] [Call:3482] occur exception need return
   07-14 18:07:48.270   25150-25150   com.hx.example  E  [ecmascript] Pending exception before ExecutePendingJob called, in line:5346, exception details as follows:
   07-14 18:07:48.270   25150-25150   com.hx.example  E  Error: This component has unfocusable ancestor.
                                                   Cannot get SourceMap info, dump raw stack:
                                                         at requestFocus (../../../foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/jsUIContext.js:898:1)
                                                         at moveFocus (@abner/input_box|@abner/input_box|1.0.3|src/main/ets/components/InputBoxView.ts:624:1)
                                                         at anonymous (@abner/input_box|@abner/input_box|1.0.3|src/main/ets/components/InputBoxView.ts:439:1)
   ```
5. 对比竖屏横屏的日志可以发现，在横屏时会触发组件区域变化事件OccupiedAreaChange，随后应用会手动设置焦点。排查应用是否监听了组件区域变化事件，是否在[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)回调函数中手动设置了焦点。

## 分析结论

应用在手动设置焦点时，祖先节点不可获焦导致应用闪退。

## 修改建议

应用在首次组件区域变化时，手动设置焦点，之后当组件区域变化时，不再设置焦点。

```screen
@Entry
@Component
struct FocusPage {
  isFirst: boolean = true;

  build() {
    Column({ space: 15 }) {
      Text('控制仅在初次进入时获焦')
      TextInput()
        .id('testTextInput')
        .onAreaChange(() => {
          if (this.isFirst) {
            console.info('requestFocus on testTextInput');
            this.getUIContext().getFocusController().requestFocus('testTextInput');
            this.isFirst = false;
          }
        })
        .margin({
          right: 20,
          left: 20
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
