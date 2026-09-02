---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-33
title: 点击桌面应用卡片按钮，按钮状态变化响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 点击桌面应用卡片按钮，按钮状态变化响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c377e3582a1fd120ccad337d3d5cbae32b93c52bc1058a7c711ae9c50380a237
---

## 问题现象

点击桌面应用卡片按钮，按钮状态过了一段时间才变化（如"打开"切换到"关闭"或"关闭"切换到"打开"），响应慢。

## 背景知识

* [Form Kit](../harmonyos-guides/formkit-overview.md)：在桌面、锁屏等系统入口中可嵌入显示应用信息的开发框架，可以将应用内用户关注的重要信息显示在桌面卡片上，达到信息直观展示、一键直达的快捷体验效果，通常用于新闻资讯阅读、远程控制设备等场景。
* 点击桌面应用卡片按钮，按钮状态更新整体流程：桌面卡片收到点击事件处理后通知到应用，应用执行相应业务逻辑后调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口更新指定的卡片，会将卡片数据信息传输到卡片管理服务FMS，卡片管理服务会将卡片相关数据传递给卡片渲染服务FRS进行卡片组件渲染，更新卡片显示状态。相关日志关键字如下：

  | 日志关键字 | 描述 |
  | --- | --- |
  | Click accepted, tag: FormComponent | 卡片组件收到点击事件 |
  | OnActionEventHandle ,formId: 卡片ID值 | 桌面应用处理卡片交互事件 |
  | FormManagerService.\*?update formId 卡片ID值 | 卡片管理服务传递卡片相关数据给卡片渲染服务以更新卡片，由应用触发 |
  | FormRenderer: UpdateForm formId 卡片ID值 | 卡片渲染服务更新卡片 |

## 问题定位

1. 在日志中搜索Click accepted, tag: FormComponent|OnActionEventHandle ,formId:|FormManagerService.\*?update formId|FormRenderer: UpdateForm formId关键字，根据日志关键字的时间间隔确定各阶段耗时，从以下日志中可看到耗时主要集中在卡片交互事件处理至卡片管理服务更新卡片阶段，该部分涉及到应用业务处理流程，需要结合应用日志分析确认最终耗时较多的部分。

   ```txt
   06-07 10:23:45.866  4544  4544 I C03951/com.ohos.sceneboard/InputKeyFlow: [(100000:100000:scope)] Click accepted, tag: FormComponent
   06-07 10:23:45.870  4544  4589 I C03904/com.ohos.sceneboard/AceForm: [(-1:100000:singleton)] EventHandle - OnActionEventHandle ,formId: 1763614067
   06-07 10:23:49.022  1496  2389 I C01301/foundation/FormManagerService: [form_render_mgr.cpp(UpdateRenderingForm:116)]update formId:1763614067,3465
   06-07 10:23:49.092  6261 17557 I C039FF/com.ohos.formrenderservice/FormRenderer: UpdateForm formId 1763614067.
   ```
2. 通过应用包名确认应用进程号，然后在上述日志关键字中加入应用进程号来搜索日志关键字，排查应用日志，从以下日志中可看到桌面应用处理卡片交互事件十几毫秒之后，应用有相关日志打印，因此可知卡片交互事件传递到应用侧无较长的时延，而应用收到卡片交互事件到触发更新卡片数据时间间隔达到3s左右，耗时主要集中在应用侧，应用业务逻辑复杂，耗时较多，导致卡片按钮状态更新响应慢的问题。

   ```txt
   06-07 10:23:45.866  4544  4544 I C03951/com.ohos.sceneboard/InputKeyFlow: [(100000:100000:scope)] Click accepted, tag: FormComponent
   06-07 10:23:45.870  4544  4589 I C03904/com.ohos.sceneboard/AceForm: [(-1:100000:singleton)] EventHandle - OnActionEventHandle ,formId: 1763614067
   06-07 10:23:45.879 24607 24607 E C01332/com.hm.example/UIAbility: [js_ui_ability.cpp:1448]null remoteCallee_
   06-07 10:23:45.881 24607 24607 I C057C8/com.hm.example/napi_remoteObject: OnJsRemoteRequestCallBack 366: enter thread pool time:314682436703626
   06-07 10:23:49.016 24607 24607 I A03D00/com.hm.example/JSAPP: ... updateForm: 1763614067 ...
   06-07 10:23:49.022  1496  2389 I C01301/foundation/FormManagerService: [form_render_mgr.cpp(UpdateRenderingForm:116)]update formId:1763614067,3465
   06-07 10:23:49.092  6261 17557 I C039FF/com.ohos.formrenderservice/FormRenderer: UpdateForm formId 1763614067.
   ```

## 分析结论

应用接收到卡片交互事件处理时，业务逻辑复杂，耗时较多，更新卡片状态慢，导致按钮状态变化响应慢。

## 修改建议

优化耗时业务逻辑或在收到卡片交互事件时更新卡片状态提示加载中。

* 卡片FormExtensionAbility代码：

  ```ts
  import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
  import hilog from '@ohos.hilog';
  import { BusinessError } from '@ohos.base';
  import { taskpool } from '@kit.ArkTS';

  const DOMAIN = 0x0000;
  const TAG = 'testTag';

  // 循环打印模拟耗时任务
  @Concurrent
  async function timeConsumingTask() : Promise<number> {
    console.info('startTask');
    for (let i = 0; i < 100000; i++) {
      console.info(`number:${i}`);
    }
    return 1;
  }

  enum Status {
    Opened = 0,
    Closed = 1,
    Loading = 2
  }

  export default class EntryFormAbility extends FormExtensionAbility {
    status: Status = Status.Closed;

    onAddForm() {
      // Called to return a FormBindingData object.
      const formData = '';
      return formBindingData.createFormBindingData(formData);
    }

    onCastToNormalForm() {
      // Called when the form provider is notified that a temporary form is successfully
      // converted to a normal form.
    }

    onUpdateForm() {
      // Called to notify the form provider to update a specified form.
    }

    onFormEvent(formId: string, message: string) {
      // Called when a specified message event defined by the form provider is triggered.
      hilog.info(DOMAIN, TAG, 'onFormEvent %{public}s', message);

      let shortMessage: string = JSON.parse(message)['message'];
      if (shortMessage === 'change') {
        if (this.status === Status.Closed) { // 当前为已关闭状态
          // 切换成加载中
          this.updateTitle(formId, 'loading');
          this.status = Status.Loading;

          // 执行耗时任务模拟加载
          taskpool.execute(timeConsumingTask).then((result: Object) => {
            console.info(`result:${result as number}`);
            // 加载完成，设置状态为已打开
            this.updateTitle(formId, 'opened');
            this.status = Status.Opened;
          }).catch((error: BusinessError) => {
            console.error(`Failed to execute task: errCode is ${error.code}, errMessage is ${error.message}`);
          });
        } else if (this.status === Status.Opened) {
          // 设置状态为关闭
          this.updateTitle(formId, 'closed');
          this.status = Status.Closed;
        }
      }
    }

    onRemoveForm() {
      // Called to notify the form provider that a specified form has been destroyed.
    }

    onAcquireFormState() {
      // Called to return a {@link FormState} object.
      return formInfo.FormState.READY;
    }

    updateTitle(formId: string, title: string) {
      let createFormBindingDataParam: Record<string, string> = {
        'title': title
      };
      let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(createFormBindingDataParam);
      formProvider.updateForm(formId, formInfo).then(() => {
        hilog.info(DOMAIN, TAG, 'FormAbility updateForm success.');
      }).catch((error: BusinessError) => {
        hilog.info(DOMAIN, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
      });
    }
  }
  ```
* 卡片页面代码：

  ```ts
  let storageUpdateByMsg = new LocalStorage();

  @Entry(storageUpdateByMsg)
  @Component
  struct WidgetCard {
    /*
     * The title.
     */
    @LocalStorageProp('title') title: string = 'closed';
    /*
     * The action type.
     */
    readonly actionType: string = 'message';
    /*
     * The message.
     */
    readonly message: string = 'change';
    /*
     * The width percentage setting.
     */
    readonly fullWidthPercent: string = '100%';
    /*
     * The height percentage setting.
     */
    readonly fullHeightPercent: string = '100%';

    build() {
      Row() {
        Column() {
          Text(this.title)
            .fontSize($r('app.float.font_size'))
            .fontWeight(FontWeight.Medium)
            .fontColor($r('sys.color.font'))
        }
        .width(this.fullWidthPercent)
      }
      .height(this.fullHeightPercent)
      .backgroundColor($r('sys.color.comp_background_primary'))
      .onClick(() => {
        postCardAction(this, {
          action: this.actionType,
          params: {
            message: this.message
          }
        });
      })
    }
  }
  ```
