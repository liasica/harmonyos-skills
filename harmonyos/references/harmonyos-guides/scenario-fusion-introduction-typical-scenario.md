---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-typical-scenario
title: 典型场景展示
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 典型场景展示
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:19+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2498684d3bf2af7100a4c46c47e5013808cae64a9ef6d39b6a8f19cb0e89937e
---

如下展示两种智能填充的典型场景。

## 实名购票场景

示例一：智能识别剪贴板内容，一键复制，一键填充。

**说明** 

剪贴板数据源推荐场景目前仅支持中文姓名和中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/kGrJN_EYS_6ouBkSgMAPzg/zh-cn_image_0000002712405384.png)

示例二：根据用户输入，智能关联设备上历史表单输入、华为账号等信息提供输入建议，一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/eRiENfztSFKtg9t4OK0rQw/zh-cn_image_0000002742124333.png)

## 填写收货地址场景

示例一：智能识别剪贴板内容，一键复制，一键填充。

**说明** 

剪贴板数据源推荐场景目前仅支持中文姓名和中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/cjUcTdUzRFGqKmT8KgNZlA/zh-cn_image_0000002712245426.png)

示例二：根据用户输入，智能关联设备上历史表单输入、华为账号等信息提供输入建议，一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/7I1ch5OCSluwwmZjqBr3tA/zh-cn_image_0000002742004375.png)

## 示例代码

```typescript
import { autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SmartFill {
  @State isClicked: boolean = false;

  build() {
// ...

      Column({ space: 5 }) {
        Row() {
          Text('昵称：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.NICKNAME).selectionMenuHidden(true)
        }

        Row() {
          Text('姓名：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
        }

        Row() {
          Text('手机号码：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.PHONE_NUMBER).selectionMenuHidden(true)
        }

        Row() {
          Text('邮箱：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.EMAIL_ADDRESS).selectionMenuHidden(true)
        }

        Row() {
          Text('身份证号：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.ID_CARD_NUMBER).selectionMenuHidden(true)
        }

        Row() {
          Text('地址：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.FORMAT_ADDRESS).selectionMenuHidden(true)
        }

        Button('保存')
          .onClick(() => {
            if (!this.isClicked) {
              // 主动触发保存历史表单输入。
              try {
                autoFillManager.requestAutoSave(this.getUIContext())
              } catch (err) {
                let e: BusinessError = err as BusinessError;
                hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
              }
              this.isClicked = true;
              // 设置超时时间以防止重复点击按钮保存历史表单输入。
              setTimeout(() => {
                this.isClicked = false;
              }, 1000)
              // 或者通过路由跳转其他页面触发保存历史表单输入。
              this.getUIContext().getRouter().pushUrl({
                url: 'xxx'
              })
            }
          })
          .width('50%')
      }
      .alignItems(HorizontalAlign.Center)
      .height('100%')
      .width('100%')
// ...
  }
}
```

**说明** 

* 智能填充在页面发生跳转的时候，或者手动触发保存逻辑的时候，方可触发保存表单逻辑。
* 剪贴板文本内容识别功能现已实现超过90%的准确率。尽管如此，我们认识到在特定场景下仍可能出现识别误差。为了提升填表数据的准确性，我们建议在关键环节引入增强校验。这些校验措施包括但不限于：

  1. 格式校验：自动检测输入格式，确保数据符合预设标准。
  2. 确认提示：在提交前通过弹窗提示用户再次确认信息，避免输入错误。
* 若在页面中也提供了弹窗提醒填充建议的功能，为避免弹窗冲突，建议将对应输入组件的[enableAutoFill](../harmonyos-references/ts-basic-components-textinput.md#enableautofill11)属性设置为"false"以关闭智能填充功能。
